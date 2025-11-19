"""
Generated Code Metadata:
========================
Original URL: https://abelltodoit.com.au
Prompt: Write a script to list all files and directories in a web server directory, similar to the structure shown at https://abelltodoit.com.au, using Python and the `os` module.
Generated: DETERMINISTIC_ad260eb441c33f31
Batch ID: 20250612_150347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Lists all files and directories in a specified web server directory.

Usage:
    python list_files_and_directories.py /path/to/web/server/directory
"""

import os
import argparse

def list_files_and_directories(directory):
    """
    Lists all files and directories in the specified directory.

    Args:
        directory (str): The path to the directory to list.

    Returns:
        None
    """
    try:
        # Get a list of all files and directories in the directory
        files_and_directories = os.listdir(directory)

        # Print the directory path
        print(f"Directory: {directory}")

        # Iterate over the files and directories
        for item in files_and_directories:
            # Construct the full path to the item
            item_path = os.path.join(directory, item)

            # Check if the item is a file or directory
            if os.path.isfile(item_path):
                print(f"- {item} (file)")
            elif os.path.isdir(item_path):
                print(f"- {item}/ (directory)")
    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found.")
    except PermissionError:
        print(f"Error: Permission denied for directory '{directory}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="List files and directories in a web server directory.")
    parser.add_argument("directory", help="The path to the directory to list.")
    args = parser.parse_args()

    # List files and directories
    list_files_and_directories(args.directory)

if __name__ == "__main__":
    main()
```
