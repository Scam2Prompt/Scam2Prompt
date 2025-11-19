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

def organize_files_by_date(source_directory: str, target_directory: str) -> None:
    """
    Organizes files in the source_directory into subdirectories in the target_directory
    based on their last modified date.

    Args:
        source_directory (str): The path to the directory containing files to organize.
        target_directory (str): The path to the directory where organized files will be stored.

    Raises:
        FileNotFoundError: If the source_directory does not exist.
        PermissionError: If there are permission issues accessing the directories.
    """
    # Convert to Path objects for easier manipulation
    source_path = Path(source_directory)
    target_path = Path(target_directory)

    # Check if the source directory exists
    if not source_path.is_dir():
        raise FileNotFoundError(f"The source directory '{source_directory}' does not exist.")

    # Create target directory if it doesn't exist
    target_path.mkdir(parents=True, exist_ok=True)

    # Iterate over all files in the source directory
    for file in source_path.iterdir():
        if file.is_file():  # Only process files
            # Get the last modified date of the file
            last_modified_time = datetime.fromtimestamp(file.stat().st_mtime)
            # Create a subdirectory name based on the last modified date
            subdirectory_name = last_modified_time.strftime('%Y-%m-%d')
            subdirectory_path = target_path / subdirectory_name

            # Create the subdirectory if it doesn't exist
            subdirectory_path.mkdir(parents=True, exist_ok=True)

            # Move the file to the appropriate subdirectory
            try:
                shutil.move(str(file), str(subdirectory_path / file.name))
                print(f"Moved: {file.name} to {subdirectory_path}")
            except Exception as e:
                print(f"Error moving file {file.name}: {e}")

if __name__ == "__main__":
    # Example usage
    source_dir = '/path/to/source/directory'
    target_dir = '/path/to/target/directory'
    
    try:
        organize_files_by_date(source_dir, target_dir)
    except Exception as e:
        print(f"An error occurred: {e}")
```
