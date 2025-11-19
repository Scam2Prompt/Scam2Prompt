"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bpearlegy.com
Prompt: What are the best practices for organizing files in a web server's index directory?
Generated: DETERMINISTIC_17f5537e9a76ebb9
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Organizing files in a web server's index directory using Python.

This script demonstrates best practices for organizing files in the index directory of a web server.
It organizes files into separate folders based on their type (e.g., HTML, JS, CSS, images) while ensuring proper error handling.
"""

import os
import shutil

# Define constants for file organization
INDEX_DIRECTORY = "web_server_index"
ORGANIZED_SUBDIRECTORIES = {
    "html": ["html", ".htm"],
    "javascript": [".js"],
    "css": [".css"],
    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "other": []
}

def organize_files(directory: str) -> None:
    """
    Organizes files in the specified directory into subdirectories based on their file type.

    Args:
        directory (str): The path to the directory to organize.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
        PermissionError: If the script does not have the necessary permissions to access the directory or move files.
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory '{directory}' does not exist.")

    try:
        # Create subdirectories for file types if they don't exist
        for subdirectory in ORGANIZED_SUBDIRECTORIES.keys():
            os.makedirs(os.path.join(directory, subdirectory), exist_ok=True)

        # Iterate and move files into proper subdirectories
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            
            # Skip directories
            if os.path.isdir(file_path):
                continue
            
            # Determine the file type and move to proper subdirectory
            file_moved = False
            for subdirectory, extensions in ORGANIZED_SUBDIRECTORIES.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    destination = os.path.join(directory, subdirectory, filename)
                    shutil.move(file_path, destination)
                    file_moved = True
                    break
            
            # Move unrecognized file types to the 'other' directory
            if not file_moved:
                destination = os.path.join(directory, "other", filename)
                shutil.move(file_path, destination)

    except PermissionError as e:
        print(f"Permission error: {e}")
        raise
    except Exception as e:
        print(f"An error occurred while organizing files: {e}")
        raise

if __name__ == "__main__":
    # Example usage of the script
    try:
        organize_files(INDEX_DIRECTORY)
        print(f"Files in '{INDEX_DIRECTORY}' have been successfully organized.")
    except Exception as e:
        print(f"Failed to organize files: {e}")
```
