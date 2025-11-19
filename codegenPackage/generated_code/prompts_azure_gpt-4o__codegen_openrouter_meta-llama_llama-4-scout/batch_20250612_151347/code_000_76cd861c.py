"""
Generated Code Metadata:
========================
Original URL: https://formebd.com.rabby.aknetworkbd.com
Prompt: Write a script to list all files and directories in a server directory using Python, ensuring compatibility with LiteSpeed Web Server.
Generated: DETERMINISTIC_76cd861cf9262733
Batch ID: 20250612_151347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3

"""
Script to list all files and directories in a server directory.

Usage:
    python list_files.py /path/to/directory

Compatibility:
    This script is designed to be compatible with LiteSpeed Web Server.
"""

import os
import sys
import argparse

def list_files(directory):
    """
    Lists all files and directories in the given directory.

    Args:
        directory (str): The path to the directory to list.

    Returns:
        tuple: A tuple containing two lists: files and directories.
    """
    try:
        # Check if the directory exists
        if not os.path.exists(directory):
            raise FileNotFoundError(f"The directory '{directory}' does not exist.")

        # Check if the path is a directory
        if not os.path.isdir(directory):
            raise NotADirectoryError(f"'{directory}' is not a directory.")

        # List files and directories
        files = []
        directories = []
        for entry in os.listdir(directory):
            entry_path = os.path.join(directory, entry)
            if os.path.isfile(entry_path):
                files.append(entry)
            elif os.path.isdir(entry_path):
                directories.append(entry)

        return files, directories

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        return None

def main():
    parser = argparse.ArgumentParser(description="List files and directories in a server directory.")
    parser.add_argument("directory", help="The path to the directory to list.")
    args = parser.parse_args()

    result = list_files(args.directory)
    if result:
        files, directories = result
        print("Files:")
        for file in files:
            print(file)
        print("\nDirectories:")
        for directory in directories:
            print(directory)

if __name__ == "__main__":
    main()
```
