"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ouatvs.com
Prompt: Write a Python script to parse and list the contents of a directory, including file names, last modified dates, and sizes, similar to the format shown on a LiteSpeed Web Server directory listing.
Generated: DETERMINISTIC_f67da116d488864e
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import datetime

def list_directory_contents(directory_path):
    """
    Lists the contents of the specified directory, including file names,
    last modified dates, and sizes.

    Args:
        directory_path (str): The path of the directory to list.

    Returns:
        list: A list of tuples, each containing the file name, last modified date,
              and size of the file.
    """
    try:
        # Check if the provided path is a directory
        if not os.path.isdir(directory_path):
            raise ValueError(f"The path '{directory_path}' is not a valid directory.")

        # Prepare a list to hold directory contents
        directory_contents = []

        # Iterate over the items in the directory
        for item in os.listdir(directory_path):
            item_path = os.path.join(directory_path, item)

            # Get file statistics
            file_stats = os.stat(item_path)
            
            # Get last modified date
            last_modified = datetime.datetime.fromtimestamp(file_stats.st_mtime)
            # Get file size in bytes
            file_size = file_stats.st_size
            
            # Append a tuple of (file name, last modified date, size) to the list
            directory_contents.append((item, last_modified, file_size))

        return directory_contents

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def main():
    # Specify the directory path
    directory_path = input("Enter the directory path to list: ")

    # Get the directory contents
    contents = list_directory_contents(directory_path)

    # Print the formatted directory contents
    if contents:
        print(f"{'File Name':<30} {'Last Modified':<25} {'Size (bytes)':<15}")
        print("=" * 70)
        for file_name, last_modified, size in contents:
            print(f"{file_name:<30} {last_modified:<25} {size:<15}")

if __name__ == "__main__":
    main()
```
