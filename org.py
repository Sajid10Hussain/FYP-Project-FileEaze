import os
import shutil
import time
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QListWidget, QMessageBox, QFileDialog, QComboBox, QScrollArea
)
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QFont, QDesktopServices







# def fileTypeOrg(source_folder):
#     categories = {
#     'Images': ['.jpeg', '.jpg', '.png', '.gif', '.bmp', '.tiff', '.svg'],
#     'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.xls', '.xlsx', '.ppt', '.pptx'],
#     'Videos': ['.mp4', '.avi', '.mov', '.mkv', '.mpg', '.wmv', '.flv', '.webm'],
#     'Music': ['.mp3', '.wav', '.ogg', '.flac', '.aac', '.wma', '.m4a'],
#     'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z', '.bz2'],
#     'Programming Files': ['.py', '.java', '.cpp', '.c', '.h', '.cs', '.html', '.css', '.js', '.php', '.rb',
#                           '.pl', '.sh', '.swift', '.go', '.rs', '.lua', '.ts', '.dart', '.kt', '.scala', 
#                           '.asm', '.json', '.xml', '.yaml', '.ini', '.bat', '.cmd', '.sql', '.asm', '.asmx',
#                           '.aspx', '.coffee', '.jsx', '.ts', '.tsx', '.vue', '.ejs', '.scss', '.less', '.jsx',
#                           '.pug', '.yml', '.groovy', '.feature', '.d', '.dll', '.exe', '.jar', '.war', '.ear',
#                           '.apk', '.ipa', '.msi', '.deb', '.rpm', '.dmg', '.iso', '.img', '.tar.gz', '.tar.bz2',
#                           '.tar.xz', '.whl', '.egg', '.rpm', '.sh', '.bat', '.cmd', '.ps1', '.bash', '.fish',
#                           '.zsh', '.pl', '.awk', '.sed', '.r', '.rmd', '.ipynb', '.pyc', '.class', '.obj',
#                           '.so', '.lib', '.a', '.pdb', '.dmp', '.dSYM'],
#     'Others': []  # Default folder for other file types
# }

#     files=os.listdir(source_folder)
#     #for category in categories:
#       #  folder=os.path.join(source_folder, category)
#        # if not os.path.exists(folder):
#         #    os.mkdir(folder)
#     for file in files:
#         ext=os.path.splitext(file)[1].lower()
#         #print(ext)
#         extValues = [value for key, value in categories.items()]
#         print(extValues)
#         if any(ext in sublist for sublist in extValues) and file!='log_file_movement.txt':
#             for type, ex in categories.items():
#                 if ex==ext:
#                     folder=os.path.join(source_folder, type)
#                     if not os.path.exists(folder):
#                         os.mkdir(folder)
#                         shutil.move(os.path.join(source_folder, file), os.path.join(folder, file))
#                         try:
#                             log_file_movement(source_folder, folder)      
#                         except:
#                             print(f"unknown error encountered!")
#                     else:
#                         shutil.move(os.path.join(source_folder, file), os.path.join(folder, file))
#                         try:
#                             log_file_movement(source_folder, folder)      
#                         except:
#                             print(f"unknown error encountered!")

#         # else:
#         #     shutil.move(os.path.join(source_folder, file), os.path.join(source_folder,'Others', file))
#     print('Work Done! FIles Moved!')







def fileTypeOrg(source_folder):
    categories = {
        'Images': ['.jpeg', '.jpg', '.png', '.gif', '.bmp', '.tiff', '.svg'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.xls', '.xlsx', '.ppt', '.pptx'],
        'Videos': ['.mp4', '.avi', '.mov', '.mkv', '.mpg', '.wmv', '.flv', '.webm'],
        'Music': ['.mp3', '.wav', '.ogg', '.flac', '.aac', '.wma', '.m4a'],
        'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z', '.bz2'],
        'Programming Files': ['.py', '.java', '.cpp', '.c', '.h', '.cs', '.html', '.css', '.js', '.php', '.rb',
                              '.pl', '.sh', '.swift', '.go', '.rs', '.lua', '.ts', '.dart', '.kt', '.scala',
                              '.asm', '.json', '.xml', '.yaml', '.ini', '.bat', '.cmd', '.sql', '.asm', '.asmx',
                              '.aspx', '.coffee', '.jsx', '.ts', '.tsx', '.vue', '.ejs', '.scss', '.less', '.jsx',
                              '.pug', '.yml', '.groovy', '.feature', '.d', '.dll', '.exe', '.jar', '.war', '.ear',
                              '.apk', '.ipa', '.msi', '.deb', '.rpm', '.dmg', '.iso', '.img', '.tar.gz', '.tar.bz2',
                              '.tar.xz', '.whl', '.egg', '.rpm', '.sh', '.bat', '.cmd', '.ps1', '.bash', '.fish',
                              '.zsh', '.pl', '.awk', '.sed', '.r', '.rmd', '.ipynb', '.pyc', '.class', '.obj',
                              '.so', '.lib', '.a', '.pdb', '.dmp', '.dSYM'],
        'Others': []  # Default folder for other file types
    }

    files = os.listdir(source_folder)

    for file in files:
        ext = os.path.splitext(file)[1].lower()
        moved = False

        for category, extensions in categories.items():
            if ext in extensions:
                folder = os.path.join(source_folder, category)
                if not os.path.exists(folder):
                    os.mkdir(folder)
                shutil.move(os.path.join(source_folder, file), os.path.join(folder, file))
                try:
                    log_file_movement(source_folder, folder)
                except Exception as e:
                    print(f"Error encountered while moving file: {e}")
                moved = True
                break

        if not moved:
            other_folder = os.path.join(source_folder, 'Others')
            if not os.path.exists(other_folder):
                os.mkdir(other_folder)
            shutil.move(os.path.join(source_folder, file), os.path.join(other_folder, file))

    print('Work Done! Files Moved!')





def fileSizeOrg(source_folder, size_ranges):
    files = os.listdir(source_folder)

    for file in files:
        file_path = os.path.join(source_folder, file)
        size = os.path.getsize(file_path)

        for size_category, size_range in size_ranges.items():
            if size_range[0] <= size < size_range[1]:
                folder = os.path.join(source_folder, size_category)
                if not os.path.exists(folder):
                    os.mkdir(folder)
                shutil.move(file_path, os.path.join(folder, file))
                log_file_movement(source_folder, folder)
                break

    print('Work Done! Files Moved!')



# def fileSizeOrg(source_folder, size_ranges):
#     files = os.listdir(source_folder)

#     for file in files:
#         file_path = os.path.join(source_folder, file)
#         size = os.path.getsize(file_path)

#         for size_category, size_range in size_ranges.items():
#             if size_range[0] <= size < size_range[1]:
#                 folder = os.path.join(source_folder, size_category)
#                 if not os.path.exists(folder):
#                     os.mkdir(folder)
#                 shutil.move(file_path, os.path.join(folder, file))
#                 log_file_movement(source_folder, folder, file)
#                 break

#     print('Work Done! Files Moved!')

















































































def log_file_movement(source_folder, destination_folder):
    log_file_path=source_folder+'\\'+'log_file_movement.txt'
    #time=datetime.now()
    log_entry=f"{destination_folder}\n"
    with open(log_file_path, 'a') as f:
        f.write(log_entry)
    f.close()
    
    
    
def undo_fileExtOrg(destination_folder):
    log_file_path=destination_folder+'\\'+'log_file_movement.txt'
    try:
        with open(log_file_path, 'r') as f:
            for i in f:
                i=i.strip('\n')
                print(i)
                source_folder=i
                if os.path.exists(source_folder):
                    files=os.listdir(source_folder)
                    for file in files:
                        shutil.move(os.path.join(source_folder, file), os.path.join(destination_folder, file))
                        print(f'{file}File moved back to original location')
                    if not os.listdir(source_folder):
                        os.rmdir(source_folder)
                        print("Folder deleted successfully.")

        f.close()
    except FileNotFoundError:
        print(f"File '{log_file_path}' not found.")
        
    try:
        os.remove(log_file_path)
        print("Reset Done! Log File Removed")
    except FileNotFoundError:
        print(f"File '{log_file_path}' not found.")
    except Exception as e:
        print(f"Error while deleting the file: {e}")




def fileExtOrg(source_folder):
    categories=['.mkv','.mp4','.avi','.webm','.pdf','.docx','.txt','.csv','.jpg','.png','.gif','.jpeg','.vtt','.py','doc','.mp3','.mov','.wav','.ogg','.zip', '.rar', '.tar', '.gz']
    files=os.listdir(source_folder)
    #for category in categories:
      #  folder=os.path.join(source_folder, category)
       # if not os.path.exists(folder):
        #    os.mkdir(folder)
    for file in files:
        ext=os.path.splitext(file)[1].lower()
        #print(ext)
        if ext in categories and file!='log_file_movement.txt':
            folder=os.path.join(source_folder, ext)
            if not os.path.exists(folder):
                os.mkdir(folder)
                shutil.move(os.path.join(source_folder, file), os.path.join(folder, file))
                try:
                     log_file_movement(source_folder, folder)      
                except:
                     print(f"unknown error encountered!")
            else:
                shutil.move(os.path.join(source_folder, file), os.path.join(folder, file))
                try:
                    log_file_movement(source_folder, folder)      
                except:
                    print(f"unknown error encountered!")
    print('Work Done! FIles Moved!')






#alphabetical order organization.
def alphaSort(source_folder):
    files = os.listdir(source_folder)
    
    for file in files:
        if file != 'log_file_movement.txt':
            first_letter = file[0].lower()
            folder = os.path.join(source_folder, first_letter)
            
            if not os.path.exists(folder):
                os.mkdir(folder)
                
            shutil.move(os.path.join(source_folder, file), os.path.join(folder, file))
            
            try:
                log_file_movement(source_folder, folder)      
            except Exception as e:
                print(f"Error encountered: {e}")
    
    print('Work Done! Files Moved!')


