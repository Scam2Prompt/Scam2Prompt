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
import sys
from datetime import datetime

def list_files_and_directories(path):
    """
    Lists all files and directories in the given path, including their last modified date and size.

    Args:
        path (str): The directory path to scan.

    Returns:
        None: Prints the details of files and directories to the console.
    """
    try:
        # Check if the provided path exists
        if not os.path.exists(path):
            print(f"Error: The path '{path}' does not exist.")
            return

        # Iterate through the items in the directory
        for item in os.listdir(path):
            item_path = os.path.join(path, item)

            # Get the last modified date
            last_modified = datetime.fromtimestamp(os.path.getmtime(item_path)).strftime('%Y-%m-%d %H:%M:%S')

            # Get the size (in bytes)
            size = os.path.getsize(item_path) if os.path.isfile(item_path) else 0

            # Determine if the item is a file or directory
            item_type = "File" if os.path.isfile(item_path) else "Directory"

            # Print the details
            print(f"{item_type}: {item}")
            print(f"  Path: {item_path}")
            print(f"  Last Modified: {last_modified}")
            print(f"  Size: {size} bytes")
            print("-" * 40)

    except PermissionError:
        print("Error: Permission denied while accessing the path.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Ensure the script is run with a valid path argument
    if len(sys.argv) != 2:
        print("Usage: python list_files_and_directories.py <path>")
        sys.exit(1)

    # Get the path from the command-line arguments
    directory_path = sys.argv[1]

    # Call the function to list files and directories
    list_files_and_directories(directory_path)
```
