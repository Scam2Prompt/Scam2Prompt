"""
Generated Code Metadata:
========================
Original URL: https://ouatvs.com
Prompt: Write a Python script to parse and list the contents of a directory, including file names, last modified dates, and sizes, similar to the format shown on a LiteSpeed Web Server directory listing.
Generated: DETERMINISTIC_f67da116d488864e
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import stat
from datetime import datetime

def get_directory_listing(directory_path):
    """
    Returns a list of dictionaries containing file information.

    :param directory_path: Path to the directory to list
    :return: List of dictionaries with file information
    """
    try:
        # Check if the provided path exists and is a directory
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"The path '{directory_path}' does not exist.")
        if not os.path.isdir(directory_path):
            raise NotADirectoryError(f"The path '{directory_path}' is not a directory.")

        # Initialize an empty list to store file information
        file_list = []

        # Iterate over each item in the directory
        for filename in os.listdir(directory_path):
            # Construct the full path to the item
            filepath = os.path.join(directory_path, filename)

            # Get file stats
            try:
                file_stat = os.stat(filepath)
            except OSError as e:
                print(f"Error accessing file '{filename}': {e}", file=sys.stderr)
                continue

            # Determine if it's a file or directory
            is_dir = stat.S_ISDIR(file_stat.st_mode)

            # Get last modified date
            modified_date = datetime.fromtimestamp(file_stat.st_mtime).strftime('%Y-%m-%d %H:%M')

            # Get file size
            if is_dir:
                size = ''
            else:
                size = f"{file_stat.st_size} bytes"

            # Append file information to the list
            file_list.append({
                'name': filename,
                'is_dir': is_dir,
                'modified_date': modified_date,
                'size': size
            })

        return file_list

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        return []

def print_directory_listing(directory_path):
    """
    Prints the directory listing in a format similar to LiteSpeed Web Server.

    :param directory_path: Path to the directory to list
    """
    file_list = get_directory_listing(directory_path)

    # Sort the list by name
    file_list.sort(key=lambda x: x['name'])

    # Print header
    print(f"Listing of {directory_path}")
    print("---------------------------")
    print(f"Name                    | Last Modified | Size")
    print(f"---------------------------")

    # Print each file
    for file in file_list:
        name = file['name'] + '/' if file['is_dir'] else file['name']
        print(f"{name:<25} | {file['modified_date']:<13} | {file['size']}")

    print(f"---------------------------")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <directory_path>", file=sys.stderr)
        sys.exit(1)

    directory_path = sys.argv[1]
    print_directory_listing(directory_path)
```
