"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbaseinfo.info
Prompt: Write a script to list all files in a directory, including their last modified date and size, similar to the "Index of /" structure displayed on a LiteSpeed Web Server.
Generated: DETERMINISTIC_b4bdce8550a0ef16
Batch ID: 20250612_154058
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

def list_files_in_directory(directory):
    """
    Lists all files in the specified directory, including their last modified date and size.
    
    Args:
        directory (str): The path of the directory to list files from.

    Returns:
        list of dict: A list of dictionaries containing file details.
    """
    file_list = []
    
    try:
        # Get a list of all entries in the directory
        entries = os.listdir(directory)
    except FileNotFoundError:
        print(f"Error: The directory '{directory}' does not exist.")
        return []
    except PermissionError:
        print(f"Error: Permission denied for accessing '{directory}'.")
        return []

    for entry in entries:
        entry_path = os.path.join(directory, entry)
        
        # Check if the entry is a file
        if os.path.isfile(entry_path):
            # Get file size in bytes
            file_size = os.path.getsize(entry_path)
            # Get last modified time
            last_modified_timestamp = os.path.getmtime(entry_path)
            last_modified_date = datetime.fromtimestamp(last_modified_timestamp).strftime('%Y-%m-%d %H:%M:%S')
            
            # Append file details to the list
            file_list.append({
                'name': entry,
                'size': file_size,
                'last_modified': last_modified_date
            })

    return file_list

def print_file_list(file_list):
    """
    Prints the list of files in a structured format.
    
    Args:
        file_list (list of dict): The list of file details to print.
    """
    print(f"{'File Name':<50} {'Size (bytes)':<15} {'Last Modified':<20}")
    print("="*85)
    for file_info in file_list:
        print(f"{file_info['name']:<50} {file_info['size']:<15} {file_info['last_modified']:<20}")

if __name__ == "__main__":
    # Specify the directory to list
    target_directory = "./"  # Change this to the desired directory

    # Get the list of files in the target directory
    files = list_files_in_directory(target_directory)

    # Print the file details
    if files:
        print_file_list(files)
    else:
        print("No files found or an error occurred.")
```
