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
import sys
from datetime import datetime

def list_files_in_directory(directory):
    """
    Lists all files in the specified directory along with their last modified date and size.

    Args:
        directory (str): The path to the directory to list files from.

    Raises:
        ValueError: If the provided directory path is not valid.
        OSError: If there is an error accessing the directory.
    """
    # Check if the provided directory path is valid
    if not os.path.isdir(directory):
        raise ValueError(f"The provided path '{directory}' is not a valid directory.")

    try:
        # List all files in the directory
        print(f"Files in directory: {directory}\n")
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)

            # Check if the path is a file
            if os.path.isfile(file_path):
                # Get last modified time and size
                last_modified_time = os.path.getmtime(file_path)
                file_size = os.path.getsize(file_path)

                # Convert last modified time to a readable format
                last_modified_date = datetime.fromtimestamp(last_modified_time).strftime('%Y-%m-%d %H:%M:%S')

                # Output the file details
                print(f"File: {filename}")
                print(f"  Last Modified: {last_modified_date}")
                print(f"  Size: {file_size} bytes\n")

    except OSError as e:
        print(f"Error accessing the directory: {e}")

if __name__ == "__main__":
    # Check if a directory path was provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python list_files.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]

    try:
        list_files_in_directory(directory_path)
    except ValueError as ve:
        print(ve)
        sys.exit(1)
```
