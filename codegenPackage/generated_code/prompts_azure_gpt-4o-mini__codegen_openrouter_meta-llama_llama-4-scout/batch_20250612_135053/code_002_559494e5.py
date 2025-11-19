"""
Generated Code Metadata:
========================
Original URL: https://elisium.it
Prompt: Write a Python script that mimics the directory listing functionality seen on elisium.it.
Generated: DETERMINISTIC_559494e59025d493
Batch ID: 20250612_135053
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
import mimetypes
import argparse

def get_directory_listing(path):
    """
    Returns a list of files and directories in the given path.

    Args:
        path (str): The path to list.

    Returns:
        list: A list of dictionaries containing file information.
    """
    try:
        files = os.listdir(path)
    except FileNotFoundError:
        print(f"Error: '{path}' not found.")
        return []
    except PermissionError:
        print(f"Error: Permission denied for '{path}'.")
        return []

    file_list = []
    for filename in files:
        filepath = os.path.join(path, filename)
        file_stat = os.stat(filepath)

        file_info = {
            'name': filename,
            'size': file_stat.st_size,
            'modified': datetime.datetime.fromtimestamp(file_stat.st_mtime).strftime('%b %d %H:%M'),
            'type': get_file_type(filename)
        }
        file_list.append(file_info)

    return file_list

def get_file_type(filename):
    """
    Returns the MIME type of the given file.

    Args:
        filename (str): The filename.

    Returns:
        str: The MIME type.
    """
    return mimetypes.guess_type(filename)[0] or 'Unknown'

def print_directory_listing(path):
    """
    Prints the directory listing in a human-readable format.

    Args:
        path (str): The path to list.
    """
    file_list = get_directory_listing(path)

    if not file_list:
        return

    print(f"Directory listing for {path}:")
    print("--------------------------------")
    print(f"{'Name':^50} | {'Size':^10} | {'Modified':^20} | {'Type':^20}")
    print("--------------------------------")
    for file_info in file_list:
        print(f"{file_info['name']:^50} | {file_info['size']:^10,} | {file_info['modified']:^20} | {file_info['type']:^20}")
    print("--------------------------------")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Directory listing script')
    parser.add_argument('path', help='the path to list')
    args = parser.parse_args()

    print_directory_listing(args.path)
```
