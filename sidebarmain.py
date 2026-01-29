import sys
import psutil
from math import *
from org import *
import numpy as np
import math
from matplotlib.patches import Patch
from PyQt5.QtGui import QDesktopServices
import matplotlib.pyplot as plt
from PyQt5.QtGui import QPixmap
from collections import Counter
from PyQt5.QtCore import Qt, QUrl, QThread, pyqtSignal, QMutex, QWaitCondition, QStandardPaths
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QDialog, QApplication, QWidget, QStackedWidget, QMainWindow,QVBoxLayout, QLabel, QLineEdit, QPushButton
from sidebar2resources import *
from smartCopy import *


class mainscreen(QMainWindow):
    
    def __init__(self):
        super(mainscreen, self).__init__()
        loadUi('sidebarfe2.ui', self)
        self.file_path = None
        self.usb_drive = None

        self.status_file = 0
        self.icons_widget.hide()
        self.stackedWidget.setCurrentIndex(0)
        self.homebtn2.setChecked(True)
        self.searchbtn.clicked.connect(self.on_search_btn_clicked)
        #self.searchbtn.clicked.connect(self.on_stackedWidget_currentChanged)
        self.homebtn1.clicked.connect(self.on_home_btn_1_toggled)
        self.homebtn2.clicked.connect(self.on_home_btn_2_toggled)
        self.sobtn1.clicked.connect(self.on_smtorg_btn_1_toggled)
        self.sobtn2.clicked.connect(self.on_smtorg_btn_2_toggled)
        self.downbtn1.clicked.connect(self.on_downloader_btn_1_toggled)
        self.downbtn2.clicked.connect(self.on_downloader_btn_2_toggled)
        #-------------------------------------------------------------------
        self.copybtn1.clicked.connect(self.on_smartCopy_btn_1_toggled)
        self.copybtn2.clicked.connect(self.on_smartCopy_btn_2_toggled)
        self.selectSmtFileBtn.clicked.connect(self.select_file)
        self.selectSmtDestBtn.clicked.connect(self.select_destination)
        self.smtStartBtn.clicked.connect(self.start_smt)









        #=====================================================================
        self.dupbtn1.clicked.connect(self.on_dupFinder_btn_1_toggled)
        self.dupbtn2.clicked.connect(self.on_dupFinder_btn_2_toggled)
        self.tebtn1.clicked.connect(self.on_txtExtractor_btn_1_toggled)
        self.tebtn2.clicked.connect(self.on_txtExtractor_btn_2_toggled)
        self.setbtn1.clicked.connect(self.on_settings_btn_1_toggled)
        self.setbtn2.clicked.connect(self.on_settings_btn_2_toggled)

        self.sobtn3.clicked.connect(self.on_smtorg_btn_1_toggled)
        #------------------------------------------------------------------
        self.downbtn3.clicked.connect(self.on_downloader_btn_1_toggled)
        # Find the URL input field by object name
        self.urlInput = self.findChild(QtWidgets.QLineEdit, "url")
        self.save_path = self.findChild(QtWidgets.QComboBox, "save_path")
        if self.save_path is None:
            print("Error: save_path not found in UI file.")
        else:
            # Fetch the default download path dynamically
            default_download_path = QStandardPaths.writableLocation(QStandardPaths.DownloadLocation)
            self.save_path.addItem(default_download_path)
            self.save_path.addItem("Choose a folder...") 
            self.save_path.currentIndexChanged.connect(self.on_save_path_changed)
        
        self.download_dialog = None
        self.download_btn.clicked.connect(self.main_download_btn_clicked)




        #-------------------------------------------------------------------
        self.copybtn3.clicked.connect(self.on_smartCopy_btn_1_toggled)
        self.dupbtn3.clicked.connect(self.on_dupFinder_btn_1_toggled)
        self.tebtn3.clicked.connect(self.on_txtExtractor_btn_1_toggled)
        self.addFolderBtn.clicked.connect(self.onAddFolderBtnClick)
        
        self.fExtBtn.clicked.connect(self.onFExtOrgBtnClick)
        self.fTypeBtn.clicked.connect(self.onFTypeOrgBtnClick)
        self.fSizeBtn.clicked.connect(self.onFSizeOrgBtnClick)
        self.alphaSortBtn.clicked.connect(self.onAlphaSortBtnClick)
        self.customOrgBtn.clicked.connect(self.onCustomOrgClick)

        # self.selectSmtFileBtn.clicked.connect(self.select_file)
        # self.selectSmtDestBtn.clicked.connect(self.select_destination)
        # self.smtStartBtn.clicked.connect(self.start_smt)

    







    def on_search_btn_clicked(self):
        self.stackedWidget.setCurrentIndex(1)
        search_text = self.searchInput.text().strip()
        if search_text:
          self.label_10.setText(search_text)


        ## Change QPushButton Checkable status when stackedWidget index changed
    #def on_stackedWidget_currentChanged(self, index):
       # btn_list = self.icons_widget.findChildren(QPushButton) \
       #             + self.full_menuwidget.findChildren(QPushButton)
        
        #for btn in btn_list:
           # if index in [1]:
           #     btn.setAutoExclusive(False)
            #    btn.setChecked(False)
            #else:
            #    btn.setAutoExclusive(True)



        ## functions for changing menu page
    def on_home_btn_1_toggled(self):
        self.stackedWidget.setCurrentIndex(0)
    
    def on_home_btn_2_toggled(self):
        self.stackedWidget.setCurrentIndex(0)

    def on_smtorg_btn_1_toggled(self):
        self.stackedWidget.setCurrentIndex(2)

    def on_smtorg_btn_2_toggled(self):
        self.stackedWidget.setCurrentIndex(2)

    def on_downloader_btn_1_toggled(self):
        self.stackedWidget.setCurrentIndex(4)

    def on_downloader_btn_2_toggled(self):
        self.stackedWidget.setCurrentIndex(4)

    def on_smartCopy_btn_1_toggled(self):
        self.stackedWidget.setCurrentIndex(5)

    def on_smartCopy_btn_2_toggled(self):
        self.stackedWidget.setCurrentIndex(5)

    def on_dupFinder_btn_1_toggled(self):
        self.stackedWidget.setCurrentIndex(7)

    def on_dupFinder_btn_2_toggled(self):
        self.stackedWidget.setCurrentIndex(7)

    def on_txtExtractor_btn_1_toggled(self):
        self.stackedWidget.setCurrentIndex(6)

    def on_txtExtractor_btn_2_toggled(self):
        self.stackedWidget.setCurrentIndex(6)

    def on_settings_btn_1_toggled(self):
        self.stackedWidget.setCurrentIndex(3)

    def on_settings_btn_2_toggled(self):
        self.stackedWidget.setCurrentIndex(3)
    
    # global folder_name
    # folder_name=r'C:\Users\Sajid\Downloads'
    

    def onAddFolderBtnClick(self):
        global folder_name
        # folder_name=r'C:\Downloads'
        folder_name = QFileDialog.getExistingDirectory(self, 'Open Folder', r'Downloads')
        name=folder_name.split('/')
        self.folderNameLabel.setText(name[-1])
        self.generate_pie_chart()

    
    def generate_pie_chart(self):
    # Define categories
        categories = {
            'Images': ['.jpeg', '.jpg', '.png', '.gif', '.bmp', '.tiff', '.svg'],
            'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.xls', '.xlsx', '.ppt', '.pptx'],
            'Videos': ['.mp4', '.avi', '.mov', '.mkv', '.mpg', '.wmv', '.flv', '.webm'],
            'Music': ['.mp3', '.wav', '.ogg', '.flac', '.aac', '.wma', '.m4a']
        }

        # Get file types and counts
        file_types = []
        for root, dirs, files in os.walk(folder_name):
            for file in files:
                extension = os.path.splitext(file)[1].lower()
                file_types.append(extension)

        # Categorize file types into provided categories
        categorized_counts = Counter()
        for category, extensions in categories.items():
            for extension in extensions:
                categorized_counts[category] += file_types.count(extension)

        # Categorize remaining file types as "Others"
        other_count = sum(categorized_counts.values())
        categorized_counts['Others'] = len(file_types) - other_count

        # Remove empty categories
        categorized_counts = {category: count for category, count in categorized_counts.items() if count > 0}

        # Plotting the pie chart
        labels = list(categorized_counts.keys())
        sizes = list(categorized_counts.values())
        colors = plt.cm.tab20c.colors  # Using a predefined color map
        fig, ax = plt.subplots()
        wedges, _ = ax.pie(sizes, startangle=100, colors=colors, wedgeprops={'edgecolor': 'black'})

        # Add legend with labels on the right side
        legend_elements = [Patch(facecolor=color, edgecolor='black', label=label) for color, label in zip(colors, labels)]
        ax.legend(handles=legend_elements, loc='center left', bbox_to_anchor=(1, 0.5), frameon=False)

        # Set the background of the plot to be transparent
        fig.patch.set_alpha(0)

        # Save the plot as an image
        chart_image_path = "pie_chart.png"
        plt.savefig(chart_image_path, transparent=True)

        # Close the plot to free up resources
        plt.close()

        # Clear the existing image in the label
        self.graphLabel.clear()

        # Display the pie chart image in the label
        pixmap = QPixmap(chart_image_path)
        self.graphLabel.setPixmap(pixmap)


   
#File Organization based on the extensions of the files.            
    def onFExtOrgBtnClick(self):
        try:
            fileExtOrg(folder_name)
            
            # Open the folder in the default file manager
            QDesktopServices.openUrl(QUrl.fromLocalFile(folder_name))
            
            # Show a message box indicating successful organization and asking for confirmation
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Question)
            msgBox.setText("Files organized successfully!")
            msgBox.setInformativeText("Do you want to keep the changes or undo?")
            msgBox.setWindowTitle("Success")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            
            # Set default button to No
            msgBox.setDefaultButton(QMessageBox.No)
            
            # Execute the message box and handle user response
            response = msgBox.exec_()
            
            # Handle user's choice
            if response == QMessageBox.Yes:
                # User wants to keep changes
                # Perform any action needed here
                print("Changes kept.")
                os.remove(folder_name+'\\'+'log_file_movement.txt')
            else:
                undo_fileExtOrg(folder_name)
                print('changes reverted!')
        except: QMessageBox.warning(self,'warning', 'Please select any folder first!')




# Organization based on the file type.
    def onFTypeOrgBtnClick(self):
        try:
            fileTypeOrg(folder_name)
            
            # Open the folder in the default file manager
            QDesktopServices.openUrl(QUrl.fromLocalFile(folder_name))
            
            # Show a message box indicating successful organization and asking for confirmation
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Question)
            msgBox.setText("Files organized successfully!")
            msgBox.setInformativeText("Do you want to keep the changes or undo?")
            msgBox.setWindowTitle("Success")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            
            # Set default button to No
            msgBox.setDefaultButton(QMessageBox.No)
            
            # Execute the message box and handle user response
            response = msgBox.exec_()
            
            # Handle user's choice
            if response == QMessageBox.Yes:
                # User wants to keep changes
                # Perform any action needed here
                print("Changes kept.")
                os.remove(folder_name+'\\'+'log_file_movement.txt')
            else:
                undo_fileExtOrg(folder_name)
                print('changes reverted!')
        except: QMessageBox.warning(self,'warning', 'Please select any folder first!')


    def onFSizeOrgBtnClick(self):
        try:
            if folder_name:
                pass
            # Create the size ranges dialog
            ranges_dialog = SizeRangesDialog()

            # Get the size ranges after dialog is closed
            result = ranges_dialog.exec_()

            # Check if dialog was accepted (OK button clicked)
            if result == QDialog.Accepted:
                size_ranges = ranges_dialog.size_ranges

                # Call fileTypeOrg with the folder name and size ranges
                fileSizeOrg(folder_name, size_ranges)

                # Open the folder in the default file manager
                QDesktopServices.openUrl(QUrl.fromLocalFile(folder_name))

                # Show a message box indicating successful organization and asking for confirmation
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Question)
                msgBox.setText("Files organized successfully!")
                msgBox.setInformativeText("Do you want to keep the changes or undo?")
                msgBox.setWindowTitle("Success")
                msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

                # Set default button to No
                msgBox.setDefaultButton(QMessageBox.No)

                # Execute the message box and handle user response
                response = msgBox.exec_()

                # Handle user's choice
                if response == QMessageBox.Yes:
                    # User wants to keep changes
                    # Perform any action needed here
                    print("Changes kept.")
                    os.remove(os.path.join(folder_name, 'log_file_movement.txt'))
                else:
                    # User wants to undo changes
                    undo_fileExtOrg(folder_name)
                    print('Changes reverted!')
        except: QMessageBox.warning(self,'warning', 'Please select any folder first!')





    def onAlphaSortBtnClick(self):
        try:
            alphaSort(folder_name)
            
            # Open the folder in the default file manager
            QDesktopServices.openUrl(QUrl.fromLocalFile(folder_name))
            
            # Show a message box indicating successful organization and asking for confirmation
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Question)
            msgBox.setText("Files organized successfully!")
            msgBox.setInformativeText("Do you want to keep the changes or undo?")
            msgBox.setWindowTitle("Success")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            
            # Set default button to No
            msgBox.setDefaultButton(QMessageBox.No)
            
            # Execute the message box and handle user response
            response = msgBox.exec_()
            
            # Handle user's choice
            if response == QMessageBox.Yes:
                # User wants to keep changes
                # Perform any action needed here
                print("Changes kept.")
                os.remove(folder_name+'\\'+'log_file_movement.txt')
            else:
                undo_fileExtOrg(folder_name)
                print('changes reverted!')
        except: QMessageBox.warning(self,'warning', 'Please select any folder first!')


    def onCustomOrgClick(self):
        try:
            if folder_name:
                pass
            self.custom=customOrganizer(folder_name)
            self.custom.exec_()
        except: QMessageBox.warning(self,'warning', 'Please select any folder first!')
#----------------------------------------------------------------------------------------------------------------------
    #Youtube Downloader area
    def main_download_btn_clicked(self):
        try:
            url = self.urlInput.text().strip()
            if not url:
                QMessageBox.warning(self, "Warning", "Please enter a URL.")
                return
            format_quality_dialog = FormatQualityDialog()
            format_quality_dialog.accepted.connect(lambda format_selected, quality_selected: self.start_download_dialog(url, format_selected, quality_selected))
            format_quality_dialog.exec_()
        except Exception as e:
            print(f"Exception occurred in main_download_btn_clicked: {e}")

    def on_save_path_changed(self, index):
        try:
            if self.save_path.currentText() == "Choose a folder...":
                options = QFileDialog.Options()
                options |= QFileDialog.ShowDirsOnly
                folder = QFileDialog.getExistingDirectory(self, "Select Download Folder", "", options)
                if folder:
                    if self.save_path.count() > 1 and self.save_path.itemText(1) == "Choose a folder...":
                        self.save_path.removeItem(1)
                    self.save_path.addItem(folder)
                    self.save_path.setCurrentText(folder)
                else:
                    self.save_path.setCurrentIndex(0)  
        except Exception as e:
            print(f"Exception occurred in on_save_path_changed: {e}")

    def start_download_dialog(self, url, format_selected, quality_selected):
        try:
            save_path = self.save_path.currentText()
            print(f"URL: {url}, Save Path: {save_path}")
            self.download_dialog = DownloadDialog()
            self.download_dialog.show()
            self.download_dialog.start_download(url, save_path, format_selected, quality_selected)
            print("Clicked")
        except Exception as e:
            print(f"Exception occurred in start_download_dialog: {e}")

#---------------------------------------------------------------------
# Smart copy portion


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
            QMessageBox.warning(self, 'Warning','Smart copy is not needed here, just go and do the normal copy becuase there is enough space on destination drive to accomodate the whole file!')
            return
        splitter = FileSplitter(self.file_path, self.usb_drive, self.status_file)
        splitter.split_and_transfer()

 








#File Size Organization

class SizeRangesDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Size Ranges")

        # Load the UI file
        loadUi("fileSizeOrg.ui", self)

        # Connect apply button to submit_ranges method
        self.applyBtn.clicked.connect(self.submit_ranges)

    def submit_ranges(self):
        small_range_mb = self.small_input.value()
        medium_range_mb = self.medium_input.value()
        large_range_mb = self.large_input.value()

        # Convert megabytes to bytes
        small_range_bytes = small_range_mb * 1024 * 1024
        medium_range_bytes = medium_range_mb * 1024 * 1024
        large_range_bytes = large_range_mb * 1024 * 1024

        self.size_ranges = {
            'Small': (0, small_range_bytes),  # 0 bytes to small_range bytes
            'Medium': (small_range_bytes, medium_range_bytes),  # small_range bytes to medium_range bytes
            'Large': (medium_range_bytes, large_range_bytes),  # medium_range bytes to large_range bytes
            'X-Large': (large_range_bytes, float('inf'))  # large_range bytes and above
        }

        self.accept()

#------------------------------------------------------------------------------------------------
#custom organization
class customOrganizer(QDialog):
    def __init__(self, folder):
        super().__init__()
        self.folderName=folder
        self.folder_assignments = {}
        self.initUI()

    def initUI(self):
        self.setWindowTitle('File Organizer')
        self.setGeometry(100, 100, 600, 400)

        # Folder Widgets
        self.label_folder_name = QLabel('Folder Name:')
        self.input_folder_name = QLineEdit()
        self.btn_add_folder = QPushButton('Add Folder')
        self.btn_remove_folder = QPushButton('Remove Folder')

        # Extension Widgets
        self.label_extension = QLabel('File Extension:')
        self.combo_extension = QComboBox()
        self.populate_extensions()
        self.btn_assign_extension = QPushButton('Assign Extension')
        self.btn_remove_extension = QPushButton('Remove Extension')

        self.list_folders = QListWidget()
        self.list_extensions = QListWidget()

        # Make folders and extensions lists scrollable
        self.scroll_folders = QScrollArea()
        self.scroll_folders.setWidgetResizable(True)
        self.scroll_folders.setWidget(self.list_folders)

        self.scroll_extensions = QScrollArea()
        self.scroll_extensions.setWidgetResizable(True)
        self.scroll_extensions.setWidget(self.list_extensions)

        self.btn_save_settings = QPushButton('Save Settings')
        self.btn_load_settings = QPushButton('Load Settings')
        self.btn_apply_organization = QPushButton('Apply Organization')

        # Layouts
        layout_main = QVBoxLayout()

        layout_folder_input = QHBoxLayout()
        layout_folder_input.addWidget(self.label_folder_name)
        layout_folder_input.addWidget(self.input_folder_name)
        layout_folder_input.addWidget(self.btn_add_folder)
        layout_folder_input.addWidget(self.btn_remove_folder)

        layout_extension_input = QHBoxLayout()
        layout_extension_input.addWidget(self.label_extension)
        layout_extension_input.addWidget(self.combo_extension)
        layout_extension_input.addWidget(self.btn_assign_extension)
        layout_extension_input.addWidget(self.btn_remove_extension)

        layout_folders = QVBoxLayout()
        layout_folders.addLayout(layout_folder_input)
        layout_folders.addWidget(QLabel('Folders:'))
        layout_folders.addWidget(self.scroll_folders)

        layout_extensions = QVBoxLayout()
        layout_extensions.addLayout(layout_extension_input)
        layout_extensions.addWidget(QLabel('Extensions:'))
        layout_extensions.addWidget(self.scroll_extensions)

        layout_buttons = QHBoxLayout()
        layout_buttons.addWidget(self.btn_save_settings)
        layout_buttons.addWidget(self.btn_load_settings)
        layout_buttons.addWidget(self.btn_apply_organization)

        layout_main.addLayout(layout_folders)
        layout_main.addLayout(layout_extensions)
        layout_main.addLayout(layout_buttons)

        self.setLayout(layout_main)

        # Button connections
        self.btn_add_folder.clicked.connect(self.add_folder)
        self.btn_remove_folder.clicked.connect(self.remove_folder)
        self.btn_assign_extension.clicked.connect(self.assign_extension)
        self.btn_remove_extension.clicked.connect(self.remove_extension)
        self.btn_save_settings.clicked.connect(self.save_settings)
        self.btn_load_settings.clicked.connect(self.load_settings)
        self.btn_apply_organization.clicked.connect(self.apply_organization)

        # Apply styles
        self.setStyleSheet("""
        QPushButton {
            border-radius: 5px;
            font: 9pt "MS Shell Dlg 2";
            color: rgb(255, 255, 255);
            background-color: rgb(49, 58, 70);
            padding: 5px 10px;
        }
        QPushButton:hover {
            background-color: rgb(85, 170, 255);
            color: rgb(255, 255, 255);
        }
        QLineEdit {
            font: 10pt "MS Shell Dlg 2";
            padding: 5px;
        }
        QLabel {
            font: 10pt "MS Shell Dlg 2";
        }
        QComboBox {
            font: 10pt "MS Shell Dlg 2";
            padding: 5px;
        }
        QListWidget {
            font: 10pt "MS Shell Dlg 2";
            padding: 5px;
        }
        """)

        self.input_folder_name.setFont(QFont("MS Shell Dlg 2", 10))
        self.combo_extension.setFont(QFont("MS Shell Dlg 2", 10))
        self.list_folders.setFont(QFont("MS Shell Dlg 2", 10))
        self.list_extensions.setFont(QFont("MS Shell Dlg 2", 10))

    def populate_extensions(self):
        # Add popular file extensions
        popular_extensions = [
            "jpg - JPEG image",
            "png - PNG image",
            "gif - GIF image",
            "txt - Text file",
            "pdf - PDF document",
            "doc - Word document",
            "docx - Word document",
            "xls - Excel spreadsheet",
            "xlsx - Excel spreadsheet",
            "ppt - PowerPoint presentation",
            "pptx - PowerPoint presentation",
            "mp3 - MP3 audio",
            "wav - WAV audio",
            "mp4 - MP4 video",
            "avi - AVI video",
            "mkv - MKV video"
        ]
        self.combo_extension.addItems(popular_extensions)

    def add_folder(self):
        folder_name = self.input_folder_name.text().strip()
        if folder_name:
            if folder_name not in self.folder_assignments:
                self.folder_assignments[folder_name] = set()
                self.list_folders.addItem(folder_name)
                self.input_folder_name.clear()
            else:
                self.show_message('Folder already exists', 'Please enter a unique folder name.')
        else:
            self.show_message('Invalid folder name', 'Please enter a folder name.')

    def remove_folder(self):
        folder_item = self.list_folders.currentItem()
        if folder_item:
            folder_name = folder_item.text()
            del self.folder_assignments[folder_name]
            self.list_folders.takeItem(self.list_folders.row(folder_item))
            self.update_extension_list()

    def assign_extension(self):
        folder_item = self.list_folders.currentItem()
        if folder_item:
            folder_name = folder_item.text()
            extension = self.combo_extension.currentText().split(" - ")[0]
            if extension:
                if not self.is_extension_assigned(extension):
                    self.folder_assignments[folder_name].add(extension)
                    self.update_extension_list()
                else:
                    self.show_message('Extension already assigned', 'This extension is already assigned to another folder.')
            else:
                self.show_message('Invalid extension', 'Please select a file extension.')
        else:
            self.show_message('No folder selected', 'Please select a folder to assign an extension.')

    def remove_extension(self):
        extension_item = self.list_extensions.currentItem()
        if extension_item:
            extension_text = extension_item.text()
            folder_name, extension = extension_text.split(": ")
            self.folder_assignments[folder_name].remove(extension)
            self.update_extension_list()

    def is_extension_assigned(self, extension):
        for extensions in self.folder_assignments.values():
            if extension in extensions:
                return True
        return False

    def update_extension_list(self):
        self.list_extensions.clear()
        for folder, extensions in self.folder_assignments.items():
            for extension in extensions:
                self.list_extensions.addItem(f"{folder}: {extension}")

    def save_settings(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        default_path = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
        initial_path = os.path.join(default_path, 'File Eaze')

        if not os.path.exists(initial_path):
            os.makedirs(initial_path)

        file, _ = QFileDialog.getSaveFileName(self, "Save Settings", initial_path, "Text Files (*.txt);;All Files (*)", options=options)
        if file:
            if not file.endswith('.txt'):
                file += '.txt'
            with open(file, 'w') as f:
                for folder, extensions in self.folder_assignments.items():
                    f.write(f"{folder}:{','.join(extensions)}\n")
            self.show_message('Settings Saved', 'Settings have been saved successfully.')


    def load_settings(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        default_path = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
        initial_path = os.path.join(default_path, 'File Eaze')

        file, _ = QFileDialog.getOpenFileName(self, "Load Settings", initial_path, "Text Files (*.txt);;All Files (*)", options=options)
        if file:
            self.folder_assignments.clear()
            with open(file, 'r') as f:
                for line in f:
                    folder, extensions = line.strip().split(':')
                    self.folder_assignments[folder] = set(extensions.split(','))
            self.update_folder_list()
            self.update_extension_list()


    def update_folder_list(self):
        self.list_folders.clear()
        for folder in self.folder_assignments.keys():
            self.list_folders.addItem(folder)

    def apply_organization(self):
        folder_path = self.folderName
        if folder_path:
            for folder, extensions in self.folder_assignments.items():
                target_folder = os.path.join(folder_path, folder)
                for extension in extensions:
                    for filename in os.listdir(folder_path):
                        if filename.endswith(f".{extension}"):
                            if not os.path.exists(target_folder):
                                os.makedirs(target_folder)
                                shutil.move(os.path.join(folder_path, filename), os.path.join(target_folder, filename))
                                try:
                                    log_file_movement(folder_path, target_folder)      
                                except:
                                    print(f"unknown error encountered!")
                            else:
                                shutil.move(os.path.join(folder_path, filename), os.path.join(target_folder, filename))
                                try:
                                    log_file_movement(folder_path, target_folder)      
                                except:
                                    print(f"unknown error encountered!")
                            
            #self.show_message('Organization Applied', 'Files have been organized successfully.')
            QDesktopServices.openUrl(QUrl.fromLocalFile(folder_path))
            
            # Show a message box indicating successful organization and asking for confirmation
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Question)
            msgBox.setText("Files organized successfully!")
            msgBox.setInformativeText("Do you want to keep the changes or undo?")
            msgBox.setWindowTitle("Success")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            
            # Set default button to No
            msgBox.setDefaultButton(QMessageBox.No)
            
            # Execute the message box and handle user response
            response = msgBox.exec_()
            
            # Handle user's choice
            if response == QMessageBox.Yes:
                # User wants to keep changes
                # Perform any action needed here
                print("Changes kept.")
                os.remove(folder_path+'\\'+'log_file_movement.txt')
            else:
                undo_fileExtOrg(folder_path)
                print('changes reverted!')

    def show_message(self, title, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()



#Youtube Downloader Part
from download_func import *

class FormatQualityDialog(QDialog):
    accepted = pyqtSignal(str, str)

    def __init__(self):
        super(FormatQualityDialog, self).__init__()
        loadUi('Format-Quality.ui', self)
        print('Format-Quality.ui loaded')
        self.setWindowTitle("Select Format and Quality")
        self.format_comboBox.addItems(['Video', 'Audio'])
        self.format_comboBox.currentIndexChanged.connect(self.update_quality_options)
        self.update_quality_options()
        self.Start_btn.clicked.connect(self.on_select_clicked)
    
    def update_quality_options(self):
        format_selected = self.format_comboBox.currentText()
        self.quality_comboBox.clear()
        if format_selected == 'Video':
            self.quality_comboBox.addItems(['360p', '720p', '1080p'])
        elif format_selected == 'Audio':
            self.quality_comboBox.addItems(['128kbps', '256kbps', '320kbps'])

    def on_select_clicked(self):
        format_selected = self.format_comboBox.currentText()
        quality_selected = self.quality_comboBox.currentText()
        self.accepted.emit(format_selected, quality_selected)
        self.accept()  

class DownloadDialog(QDialog):
    def __init__(self):
        super(DownloadDialog, self).__init__()
        loadUi('ytb-downloader.ui', self)
        print('ytb-downloader.ui loaded')
        self.setWindowTitle("Youtube Downloader")
        self.download_thread = None
        self.paused = False
        self.Pause_Resume_btn.clicked.connect(self.toggle_pause_resume)
        self.Cancel_btn.clicked.connect(self.cancel_download)

    def on_format_quality_accepted(self, format_selected, quality_selected):
        url = self.url_line_edit.text()  
        save_path = self.save_path_line_edit.text() 
        print(f"Starting download with URL: {url}, Save Path: {save_path}, Format: {format_selected}, Quality: {quality_selected}")
        self.start_download(url, save_path, format_selected, quality_selected)

    def start_download(self, url, save_path, format_selected, quality_selected):
        self.download_thread = DownloadThread(url, save_path, format_selected, quality_selected)
        self.download_thread.progress_update.connect(self.update_progress)
        self.download_thread.alert.connect(self.show_alert)
        self.download_thread.size_update.connect(self.update_size)
        self.download_thread.speed_update.connect(self.update_speed)
        self.download_thread.time_update.connect(self.update_time)
        self.download_thread.status_update.connect(self.update_status)
        self.download_thread.error_signal.connect(lambda error_message: self.show_alert(error_message))
        self.error_occurred = False
        self.download_thread.start()

    def toggle_pause_resume(self):
        if self.paused:
            self.download_thread.resume()
            self.paused = False
            self.Pause_Resume_btn.setText("Pause")
            self.update_status("Resumed")
            print("Resuming download")
        else:
            self.download_thread.pause()
            self.paused = True
            self.Pause_Resume_btn.setText("Resume")
            self.update_status("Paused")
            print("Pausing download")

    def update_time(self, time_taken):
        self.time_label.setText(f"Time Taken: {time_taken:.2f} seconds")

    def cancel_download(self):
        self.download_thread.cancel()
        self.update_status("Canceled")
        print("Canceling download")

    def update_progress(self, progress):
        self.progressBar.setValue(progress)

    def update_size(self, size):
        kb_size = size / 1024.0
        mb_size = kb_size / 1024.0
        gb_size = mb_size / 1024.0
        if gb_size >= 1:
            self.size_label.setText(f"Size: {gb_size:.2f} GB")
        elif mb_size >= 1:
            self.size_label.setText(f"Size: {mb_size:.2f} MB")
        else:
            self.size_label.setText(f"Size: {kb_size:.2f} KB")

    def update_speed(self, speed):
        kb_speed = speed / 1024.0
        mb_speed = kb_speed / 1024.0
        if mb_speed >= 1:
            self.speed_label.setText(f"Speed: {mb_speed:.2f} MB/s")
        else:
            self.speed_label.setText(f"Speed: {kb_speed:.2f} KB/s")

    def update_status(self, status):
        self.status_label.setText(f"Status: {status}")

    def show_alert(self, error_message=None):
        if error_message:
            QMessageBox.critical(self, "Download Failed", error_message)
            self.update_status("Failed")
        else:
            QMessageBox.information(self, "Download Completed", "The download has been completed.")
            self.update_status("Completed")

    def show_dialog(self):
        print("Showing dialog")
        self.show()

class DownloadThread(QThread):
    progress_update = pyqtSignal(int)
    alert = pyqtSignal()
    size_update = pyqtSignal(int)
    speed_update = pyqtSignal(float)
    time_update = pyqtSignal(float)
    status_update = pyqtSignal(str)
    error_signal = pyqtSignal(str)

    def __init__(self, url, save_path, format_selected, quality_selected):
        super().__init__()
        self.url = url
        self.save_path = save_path
        self.format_selected = format_selected
        self.quality_selected = quality_selected
        self.downloading = True
        self.paused = False
        self.mutex = QMutex()
        self.wait_condition = QWaitCondition()

    def run(self):
        try:
            self.status_update.emit("Starting download")
            downloader(self.url, self.save_path, self.format_selected, self.quality_selected,
                       self.progress_update.emit,
                       self.alert.emit,
                       self.size_update.emit,
                       self.speed_update.emit,
                       self.update_time_callback,
                       self.is_paused,
                       self.is_canceled,
                       self.status_update.emit,
                       self.error_signal.emit)
        except Exception as e:
            print(f"Error during download: {e}")

    def update_time_callback(self, elapsed_time):
        self.time_update.emit(elapsed_time)

    def pause(self):
        self.mutex.lock()
        self.paused = True
        self.mutex.unlock()

    def resume(self):
        self.mutex.lock()
        self.paused = False
        self.wait_condition.wakeAll()
        self.mutex.unlock()

    def cancel(self):
        self.downloading = False
        self.resume()

    def is_paused(self):
        self.mutex.lock()
        paused = self.paused
        if paused:
            self.wait_condition.wait(self.mutex)
        self.mutex.unlock()
        return paused

    def is_canceled(self):
        return not self.downloading























app= QApplication(sys.argv)
welcome=mainscreen()
widget= QStackedWidget()
widget.addWidget(welcome)
# widget.setFixedHeight(800)
# widget.setFixedWidth(1200)
widget.show()
try:
    sys.exit(app.exec())
except:
    print('exiting')