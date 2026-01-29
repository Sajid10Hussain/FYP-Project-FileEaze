from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QApplication, QDialog
from PyQt5.uic import loadUi
import sys
import os
import shutil
from math import ceil
import psutil
from PyQt5.QtWidgets import QApplication, QMessageBox, QFileDialog, QPushButton
class FileSplitter(QDialog):
    def __init__(self, file_path, usb_drive, status_file):
        super().__init__()
        loadUi("smtcopyprogress.ui", self)
        self.setWindowTitle("Smart Copy")
        self.file_path = file_path
        self.usb_drive = usb_drive
        self.status_file = status_file
        self.progressBar.setValue(0)
        
        # State variables for pause and cancel
        self.paused = False
        self.canceled = False
        
        # Connect buttons to their functions
        self.pauseButton.clicked.connect(self.toggle_pause)
        self.cancelButton.clicked.connect(self.cancel_transfer)
        
        self.show()

    def toggle_pause(self):
        self.paused = not self.paused
        if self.paused:
            self.pauseButton.setText("Resume")
        else:
            self.pauseButton.setText("Pause")

    def cancel_transfer(self):
        self.canceled = True



    def split_and_transfer(self):
        try:
            file_size = os.path.getsize(self.file_path)
            self.progressText.append(f"Total file size: {file_size / (1024 * 1024):.2f} MB")
            QApplication.processEvents()

            chunk_number = self.status_file
            compSoFar = 0
            with open(self.file_path, 'rb') as f:
                while compSoFar < file_size:
                    if self.canceled:
                        self.progressText.append("Transfer canceled.")
                        QMessageBox.information(self, "Canceled", "File transfer has been canceled.")
                        break

                    while self.paused:
                        QApplication.processEvents()

                    free_space = get_free_space(self.usb_drive)
                    self.progressText.append(f"Free space on USB drive: {free_space / (1024 * 1024):.2f} MB")
                    QApplication.processEvents()

                    chunk_size = free_space - (150 * 1024 * 1024)
                    if chunk_size <= 0:
                        QMessageBox.critical(self, "Not Enough Space", "Not enough space on the USB drive. Please free up some space and try again.")
                        break

                    chunk_size = min(chunk_size, file_size - compSoFar)
                    f.seek(compSoFar)
                    remaining_size = file_size - compSoFar
                    read_size = min(chunk_size, remaining_size)

                    if read_size <= 0:
                        self.progressText.append("Invalid read size calculated. Please select another USB drive.")
                        changeUsb = QFileDialog.getExistingDirectory(self, "Select Destination", options=QFileDialog.ShowDirsOnly)
                        if not changeUsb:
                            QMessageBox.warning(self, "Warning", "No USB selected. Operation will be canceled.")
                            self.canceled = True
                            return
                        self.usb_drive = changeUsb
                        self.progressText.append(f"Selected new USB: {self.usb_drive}")
                        continue

                    chunk_file_name = os.path.join(self.usb_drive, f'{os.path.basename(self.file_path)}.part{chunk_number}')

                    with open(chunk_file_name, 'wb') as chunk_file:
                        bytes_written = 0
                        while bytes_written < read_size:
                            if self.canceled:
                                self.progressText.append("Transfer canceled.")
                                QMessageBox.information(self, "Canceled", "File transfer has been canceled.")
                                return
                            while self.paused:
                                QApplication.processEvents()

                            chunk_data = f.read(min(4096, read_size - bytes_written))
                            if not chunk_data:
                                break

                            chunk_file.write(chunk_data)
                            bytes_written += len(chunk_data)

                            self.smtCopyLabel.setText(f"Processing chunk {chunk_number}, bytes written: {bytes_written / (1024 * 1024):.2f} MB")
                            self.progressBar.setValue(int(ceil((compSoFar + bytes_written) / file_size * 100)))
                            QApplication.processEvents()

                    chunk_number += 1
                    self.status_file = chunk_number

                    transferred_size = compSoFar + bytes_written
                    compSoFar += bytes_written
                    progress = min(transferred_size / file_size * 100, 100)
                    self.progressText.append(f'Transferred {transferred_size / (1024 * 1024):.2f} MB of {file_size / (1024 * 1024):.2f} MB ({progress:.2f}%)')
                    self.progressBar.setValue(int(ceil(progress)))
                    QApplication.processEvents()

                    if transferred_size == file_size:
                        self.progressText.append('Entire File is successfully copied!!')
                        QMessageBox.information(self, 'Transfer Complete', 'Entire File is successfully copied!!')
                        source_file = 'Combiner.exe'
                        shutil.copy2(source_file, self.usb_drive)
                        break
                    else:
                        msg_box = QMessageBox(self)
                        msg_box.setWindowTitle('Action Required')
                        msg_box.setText("Please transfer the contents from the USB drive to the destination PC and then press Continue or select a different Storage device to copy the next part into.")
                        
                        # Creating and styling the buttons
                        continue_button = QPushButton('Continue')
                        select_other_button = QPushButton('Select Other Device')
                        button_style = """
                        QPushButton{
                            border-radius: 8px;
                            font: 9pt "MS Shell Dlg 2";
                            color: rgb(255, 255, 255);
                            padding: 5px 10px;
                            background-color: rgb(49, 58, 70);
                        }
                        QPushButton:hover{
                            background-color: rgb(85, 170, 255);
                            color: rgb(255, 255, 255);
                        }
                        """
                        continue_button.setStyleSheet(button_style)
                        select_other_button.setStyleSheet(button_style)
                        
                        msg_box.addButton(continue_button, QMessageBox.YesRole)
                        msg_box.addButton(select_other_button, QMessageBox.NoRole)
                        response = msg_box.exec_()

                        if response == 0:
                            while True:
                                try:
                                    space = get_free_space(self.usb_drive)
                                    if space == 150 * 1024 * 1024:
                                        QMessageBox.information(self, 'Action Required', "Please free the USB and then press Continue to continue.")
                                        space = get_free_space(self.usb_drive)
                                        continue
                                except:
                                    if not os.path.exists(self.usb_drive):
                                        QMessageBox.information(self, 'Action Required', "Please insert the same USB and then press Continue.")
                                        continue
                                break
                        else:
                            changeUsb = QFileDialog.getExistingDirectory(self, "Select Destination", options=QFileDialog.ShowDirsOnly)
                            if not changeUsb:
                                QMessageBox.warning(self, "Warning", "No USB selected. Operation will be canceled.")
                                self.canceled = True
                                return
                            self.usb_drive = changeUsb
                            self.progressText.append(f"Selected new USB: {self.usb_drive}")
                            continue

                    for i in range(chunk_number):
                        chunk_file_name = os.path.join(self.usb_drive, f'{os.path.basename(self.file_path)}.part{i}')
                        if os.path.exists(chunk_file_name):
                            os.remove(chunk_file_name)
        except Exception as e:
            print(f"Error: {e}")
            QMessageBox.critical(self, "Error", str(e))



class mainscreen(QMainWindow):
    def __init__(self):
        super(mainscreen, self).__init__()
        loadUi('sidebarfe2.ui', self)
        self.file_path = None
        self.usb_drive = None

        self.status_file = 0
        self.selectSmtFileBtn.clicked.connect(self.select_file)
        self.selectSmtDestBtn.clicked.connect(self.select_destination)
        self.smtStartBtn.clicked.connect(self.start_smt)

    def select_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        self.file_path, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*)", options=options)
        self.smtFileEdit.setText(str(self.file_path))
        return self.file_path

    def select_destination(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly
        self.usb_drive = QFileDialog.getExistingDirectory(self, "Select Destination", options=options)
        self.smtDestEdit.setText(str(self.usb_drive))
        return self.usb_drive

    def start_smt(self):
        if not self.file_path or not self.usb_drive:
            QMessageBox.warning(self, 'Warning', 'Please select both file and destination.')
            return
        file_size = os.path.getsize(self.file_path)
        if file_size < get_free_space(self.usb_drive):
            QMessageBox.warning(self, 'Warning','Smart copy is not needed here, just go and do the normal copy because there is enough space on destination drive to accommodate the whole file!')
            return
        splitter = FileSplitter(self.file_path, self.usb_drive, self.status_file)
        splitter.split_and_transfer()

def get_free_space(drive):
    """Get the free space of the given drive in bytes."""
    usage = psutil.disk_usage(drive)
    return usage.free

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainscreen()
    window.show()
    sys.exit(app.exec_())
