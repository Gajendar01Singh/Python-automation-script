
# File Organizer for Downloads Folder

This Python script helps to automatically organize files in your `Downloads` folder into categorized subfolders based on their file types. The script supports organizing existing files and optionally provides real-time monitoring for newly downloaded files.

---

## Features

- **File Categorization**: Automatically moves files into predefined folders such as `Images`, `Videos`, `Documents`, etc., based on their extensions.
- **Customizable Categories**: Easily add or modify file type categories by editing the `file_categories` dictionary.
- **Real-Time Monitoring** (Optional): Continuously watches the `Downloads` folder for new files and organizes them automatically.
- **Fallback for Unknown Types**: Files with extensions not listed in the categories are moved to the `Others` folder.
- **Safe Operation**: Skips organizing folders and only moves individual files.

---

## Supported File Categories

The following file types are categorized into specific folders by default:

- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`
- **Videos**: `.mp4`, `.mkv`, `.flv`, `.avi`, `.mov`
- **Documents**: `.pdf`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.ppt`, `.pptx`, `.txt`
- **Audio**: `.mp3`, `.wav`, `.aac`, `.flac`
- **Archives**: `.zip`, `.rar`, `.7z`, `.tar`, `.gz`
- **Programs**: `.exe`, `.msi`, `.dmg`, `.sh`, `.bat`
- **Scripts**: `.py`, `.js`, `.html`, `.css`, `.php`
- **Others**: Any file type not listed above.

---

## Requirements

- Python 3.6 or above
- `shutil` (built-in)
- `os` (built-in)
- Optional: If using real-time monitoring, ensure the system supports Python's `time` module.

---

## Installation

1. Clone this repository or download the script file.
2. Ensure Python is installed on your system.

---

## Usage

### Organizing Existing Files

1. Run the script from your terminal:
   ```bash
   python organize_downloads.py
   ```
2. The script will scan your `Downloads` folder and organize all existing files into categorized subfolders.

### Enabling Real-Time Monitoring

1. Uncomment the `monitor_new_files()` line in the script:
   ```python
   # Uncomment the following line to enable real-time monitoring
   monitor_new_files()
   ```
2. Run the script:
   ```bash
   python organize_downloads.py
   ```
3. The script will continuously monitor your `Downloads` folder for new files and organize them automatically.

---

## Customization

### Adding or Modifying Categories

- Open the script in a text editor.
- Update the `file_categories` dictionary with new categories or file extensions.

Example: Adding a new category for spreadsheets:
```python
file_categories = {
    "Spreadsheets": [".csv", ".ods"],
    # Other categories...
}
```

---

## Notes

- The script skips folders and only processes individual files.
- Ensure there is enough space in your `Downloads` folder for moving files between subfolders.
- Use caution when running real-time monitoring on systems with large `Downloads` folders, as it may cause high memory usage.

---

## Contributing

Feel free to fork the repository and submit pull requests with improvements or additional features.

---

## Author

- **Gajendar Singh Shekhawat**  
  Python Developer | Tech Enthusiast  

If you find this tool useful, feel free to star this repository!
