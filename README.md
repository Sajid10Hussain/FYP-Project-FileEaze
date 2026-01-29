# FileEaze – Final Year Project

FileEaze is a desktop-based file management system developed as a Final Year Project.
The primary goal of this project is to improve large file transfer and file organization
through intelligent, system-aware mechanisms.

---

## Core Innovation: Smart Copy

The **Smart Copy** feature is the main contribution of this project.

Unlike traditional file copy operations, Smart Copy dynamically adapts to limited
storage environments such as USB drives by:

- Detecting available free space on the destination device
- Automatically splitting large files into manageable chunks
- Allowing pause, resume, and cancel during transfer
- Supporting continuation using the same or a different storage device
- Maintaining transfer state to ensure data integrity
- Providing real-time progress feedback through a GUI

This makes Smart Copy suitable for scenarios where files are larger than the
available removable storage capacity.

---

## Additional Features: Smart Organization

FileEaze also includes intelligent file organization utilities:

- File type–based organization (Images, Documents, Videos, Music, etc.)
- File size–based organization
- Alphabetical sorting
- Extension-based organization
- File movement logging with undo functionality

These features help users automatically structure unorganized directories
with minimal manual effort.

---

## Feature Status

### Fully Implemented
- Smart Copy (core feature)
- Smart file organization:
  - File type–based
  - File size–based
  - Alphabetical
  - Extension-based
- File movement logging and undo support

### Partially Implemented / Incomplete
- Internet file downloader (intended for YouTube and other downloadable links)
- Settings module (UI partially completed, logic not finalized)

### Planned but Not Included in Final Build
- OCR-based text extraction from images  
- Duplicate file detection and removal module  

These features were planned during the design phase but could not be
integrated into the final build due to time and resource constraints.


---

## Future Enhancements
- Complete and stabilize the internet file downloader module
- Integrate OCR-based text extraction using a cross-platform setup
- Add duplicate file detection using hashing techniques
- Complete settings module with persistent configuration support



## Technologies Used
- Python
- PyQt5
- NumPy
- Matplotlib
- psutil

---

## Installation

1. Install Python 3.x
2. Install required dependencies:
