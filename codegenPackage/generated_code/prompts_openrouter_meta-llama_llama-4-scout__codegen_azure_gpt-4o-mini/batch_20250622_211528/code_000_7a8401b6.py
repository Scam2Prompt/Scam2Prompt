"""
Generated Code Metadata:
========================
Original URL: https://bryantroll.com
Prompt: "Write a Python script to list all files and directories in a given path, including their last modified date and size."
Generated: DETERMINISTIC_7a8401b6bb75379c
Batch ID: 20250622_211528
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import datetime

def list_files_and_directories(path):
    """
    List all files and directories in the given path, including their last modified date and size.

    Args:
        path (str): The directory path to list files and directories from.

    Returns:
        list: A list of tuples containing the name, last modified date, and size of each file/directory.
    """
    try:
        # Check if the provided path is a valid directory
        if not os.path.isdir(path):
            raise ValueError(f"The provided path '{path}' is not a valid directory.")

        # List to hold the details of files and directories
        file_details = []

        # Iterate through the directory
        for entry in os.listdir(path):
            entry_path = os.path.join(path, entry)
            # Get the last modified time and size
            last_modified_time = os.path.getmtime(entry_path)
            size = os.path.getsize(entry_path) if os.path.isfile(entry_path) else None
            
            # Convert last modified time to a readable format
            last_modified_date = datetime.datetime.fromtimestamp(last_modified_time).strftime('%Y-%m-%d %H:%M:%S')
            
            # Append the details to the list
            file_details.append((entry, last_modified_date, size))

        return file_details

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def main():
    # Define the path to list files and directories
    path = input("Enter the directory path to list files and directories: ")
    
    # Get the file and directory details
    details = list_files_and_directories(path)
    
    # Print the details
    if details:
        print(f"{'Name':<30} {'Last Modified':<20} {'Size (bytes)':<15}")
        print("=" * 65)
        for name, modified_date, size in details:
            print(f"{name:<30} {modified_date:<20} {size if size is not None else 'N/A':<15}")

if __name__ == "__main__":
    main()
```
