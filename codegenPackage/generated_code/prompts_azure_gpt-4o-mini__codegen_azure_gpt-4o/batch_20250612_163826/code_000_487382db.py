"""
Generated Code Metadata:
========================
Original URL: https://groupists.com
Prompt: Generate a script that lists all files in a directory similar to the index of / on groupists.com.
Generated: DETERMINISTIC_487382dbf74d9947
Batch ID: 20250612_163826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from datetime import datetime

def list_files_in_directory(directory_path):
    """
    Lists all files and directories in the specified directory, similar to an index page.

    Args:
        directory_path (str): The path of the directory to list files from.

    Returns:
        None: Prints the list of files and directories in a formatted table.
    """
    try:
        # Check if the provided path is a valid directory
        if not os.path.isdir(directory_path):
            raise NotADirectoryError(f"'{directory_path}' is not a valid directory.")

        # Get the list of files and directories
        items = os.listdir(directory_path)

        # Print header for the index table
        print(f"Index of {directory_path}")
        print("-" * 80)
        print(f"{'Name':<40} {'Last Modified':<20} {'Size (Bytes)':<15}")
        print("-" * 80)

        # Iterate through each item in the directory
        for item in items:
            item_path = os.path.join(directory_path, item)
            # Get last modified time
            last_modified = datetime.fromtimestamp(os.path.getmtime(item_path)).strftime('%Y-%m-%d %H:%M:%S')
            # Get size (if it's a file)
            size = os.path.getsize(item_path) if os.path.isfile(item_path) else '-'
            # Print item details
            print(f"{item:<40} {last_modified:<20} {size:<15}")

        print("-" * 80)

    except NotADirectoryError as e:
        print(f"Error: {e}")
    except PermissionError:
        print("Error: Permission denied while accessing the directory.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Specify the directory path to list files from
    directory_to_list = input("Enter the directory path to list files: ").strip()
    list_files_in_directory(directory_to_list)
```
