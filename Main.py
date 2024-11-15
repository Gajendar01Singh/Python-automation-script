import os
import shutil

# Define the file type categories and their corresponding folders
file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov"],
    "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Programs": [".exe", ".msi", ".dmg", ".sh", ".bat"],
    "Scripts": [".py", ".js", ".html", ".css", ".php"],
    "Others": []
}

# Get the Downloads folder path
downloads_folder = os.path.expanduser("~/Downloads")

# Function to organize files


def organize_files(folder_path):
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        # Skip if item is a folder
        if os.path.isdir(item_path):
            continue

        # Get the file extension
        file_ext = os.path.splitext(item)[1].lower()

        # Find the category for the file
        target_folder = None
        for category, extensions in file_categories.items():
            if file_ext in extensions:
                target_folder = category
                break
        if not target_folder:
            target_folder = "Others"  # Default category for unlisted types

        # Create the target folder if it doesn't exist
        target_folder_path = os.path.join(folder_path, target_folder)
        os.makedirs(target_folder_path, exist_ok=True)

        # Move the file to the target folder
        shutil.move(item_path, os.path.join(target_folder_path, item))

# Watch for new downloads (optional)


def monitor_new_files():
    import time
    seen_files = set(os.listdir(downloads_folder))
    while True:
        time.sleep(5)  # Check every 5 seconds
        current_files = set(os.listdir(downloads_folder))
        new_files = current_files - seen_files
        if new_files:
            for new_file in new_files:
                organize_files(downloads_folder)
        seen_files = current_files


if __name__ == "__main__":
    print("Organizing existing files in the Downloads folder...")
    organize_files(downloads_folder)
    print("Organizing completed.")

    # Uncomment the following line to enable real-time monitoring
monitor_new_files()
