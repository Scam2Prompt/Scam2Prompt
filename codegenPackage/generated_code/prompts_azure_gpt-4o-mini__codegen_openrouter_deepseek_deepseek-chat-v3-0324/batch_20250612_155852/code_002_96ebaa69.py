"""
Generated Code Metadata:
========================
Original URL: https://bryantroll.com
Prompt: Write a script that lists all files in a specified directory and outputs their last modified date and size.
Generated: DETERMINISTIC_96ebaa6984330e73
Batch ID: 20250612_155852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import time
from datetime import datetime

def list_files_with_metadata(directory):
    """
    Lists all files in the specified directory along with their last modified date and size.
    
    Args:
        directory (str): Path to the directory to scan.
    
    Returns:
        list: A list of dictionaries containing file metadata.
    """
    if not os.path.isdir(directory):
        raise ValueError(f"Directory does not exist: {directory}")
    
    files_metadata = []
    
    for entry in os.listdir(directory):
        full_path = os.path.join(directory, entry)
        
        if os.path.isfile(full_path):
            stat_info = os.stat(full_path)
            
            file_metadata = {
                'filename': entry,
                'last_modified': datetime.fromtimestamp(stat_info.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
                'size_bytes': stat_info.st_size,
                'size_human_readable': _convert_size(stat_info.st_size)
            }
            
            files_metadata.append(file_metadata)
    
    return files_metadata

def _convert_size(size_bytes):
    """
    Converts file size in bytes to human-readable format.
    
    Args:
        size_bytes (int): File size in bytes.
    
    Returns:
        str: Human-readable file size.
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} PB"

def print_files_metadata(files_metadata):
    """
    Prints file metadata in a formatted table.
    
    Args:
        files_metadata (list): List of file metadata dictionaries.
    """
    if not files_metadata:
        print("No files found in the directory.")
        return
    
    print("\nFiles in directory:")
    print("{:<40} {:<25} {:<15} {:<15}".format(
        "Filename", "Last Modified", "Size (Bytes)", "Size (Human)"))
    print("-" * 95)
    
    for file in files_metadata:
        print("{:<40} {:<25} {:<15} {:<15}".format(
            file['filename'],
            file['last_modified'],
            file['size_bytes'],
            file['size_human_readable']
        ))

if __name__ == "__main__":
    try:
        directory = input("Enter directory path: ").strip()
        files_metadata = list_files_with_metadata(directory)
        print_files_metadata(files_metadata)
    except Exception as e:
        print(f"Error: {str(e)}")
```
