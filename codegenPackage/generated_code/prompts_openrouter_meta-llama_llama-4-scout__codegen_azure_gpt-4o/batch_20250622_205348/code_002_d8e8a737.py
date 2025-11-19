"""
Generated Code Metadata:
========================
Original URL: https://defluo.hr
Prompt: "Write a Python script to automate the process of organizing files on a server based on their last modified date."
Generated: DETERMINISTIC_d8e8a73763e8404d
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import shutil
from datetime import datetime
from pathlib import Path

def organize_files_by_date(source_directory, destination_directory):
    """
    Organizes files in the source directory into subdirectories in the destination directory
    based on their last modified date.

    Args:
        source_directory (str): Path to the directory containing files to organize.
        destination_directory (str): Path to the directory where organized files will be stored.

    Raises:
        FileNotFoundError: If the source directory does not exist.
        PermissionError: If there are insufficient permissions to access or modify files.
    """
    # Ensure source directory exists
    if not os.path.exists(source_directory):
        raise FileNotFoundError(f"Source directory '{source_directory}' does not exist.")

    # Create destination directory if it doesn't exist
    os.makedirs(destination_directory, exist_ok=True)

    # Iterate through all files in the source directory
    for item in os.listdir(source_directory):
        item_path = os.path.join(source_directory, item)

        # Skip directories, only process files
        if not os.path.isfile(item_path):
            continue

        try:
            # Get the last modified date of the file
            last_modified_timestamp = os.path.getmtime(item_path)
            last_modified_date = datetime.fromtimestamp(last_modified_timestamp).strftime('%Y-%m-%d')

            # Create a subdirectory in the destination directory based on the date
            date_directory = os.path.join(destination_directory, last_modified_date)
            os.makedirs(date_directory, exist_ok=True)

            # Move the file to the appropriate subdirectory
            shutil.move(item_path, os.path.join(date_directory, item))
        except PermissionError:
            print(f"Permission denied while accessing '{item_path}'. Skipping...")
        except Exception as e:
            print(f"An error occurred while processing '{item_path}': {e}")

if __name__ == "__main__":
    # Example usage
    source_dir = "/path/to/source/directory"
    destination_dir = "/path/to/destination/directory"

    try:
        organize_files_by_date(source_dir, destination_dir)
        print("Files have been successfully organized.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
