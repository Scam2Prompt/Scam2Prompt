"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synerex-bo.com
Prompt: Generate a Python script to list all files in a directory, similar to the index structure found on synerex-bo.com.
Generated: DETERMINISTIC_6e44ffd2af690028
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from datetime import datetime

def list_files_in_directory(directory_path):
    """
    Lists all files and directories in the specified directory path.

    Args:
        directory_path (str): The path of the directory to list files from.

    Returns:
        list: A list of dictionaries containing file information.
    """
    try:
        # Validate that the directory exists
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")
        
        # Validate that the path is indeed a directory
        if not os.path.isdir(directory_path):
            raise NotADirectoryError(f"The path '{directory_path}' is not a directory.")
        
        file_list = []
        
        # Iterate over all entries in the directory
        for entry in os.scandir(directory_path):
            file_info = {
                "name": entry.name,  # File or directory name
                "type": "Directory" if entry.is_dir() else "File",  # Type: File or Directory
                "size": os.path.getsize(entry.path) if entry.is_file() else None,  # File size (None for directories)
                "last_modified": datetime.fromtimestamp(entry.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S')  # Last modified timestamp
            }
            file_list.append(file_info)
        
        return file_list

    except Exception as e:
        # Catch any exception and print an error message
        print(f"Error: {e}")
        return []

def display_file_list(file_list):
    """
    Displays the list of files and directories in a formatted manner.

    Args:
        file_list (list): A list of dictionaries containing file information.
    """
    print(f"{'Name':<40} {'Type':<10} {'Size (bytes)':<15} {'Last Modified':<20}")
    print('-' * 85)
    for file_info in file_list:
        size = file_info["size"] if file_info["size"] is not None else "-"
        print(f"{file_info['name']:<40} {file_info['type']:<10} {size:<15} {file_info['last_modified']:<20}")

if __name__ == "__main__":
    # Specify the directory path
    directory_path = input("Enter the path of the directory to list files: ").strip()
    
    # Get the list of files and directories
    file_list = list_files_in_directory(directory_path)
    
    # Display the files if the list is not empty
    if file_list:
        display_file_list(file_list)
    else:
        print("No files or directories found.")
```

This script is production-ready, adheres to best practices, includes error handling, and is well-commented for clarity. It lists all files and directories within a specified directory, displays their details in a structured format, and handles common errors like invalid paths.
