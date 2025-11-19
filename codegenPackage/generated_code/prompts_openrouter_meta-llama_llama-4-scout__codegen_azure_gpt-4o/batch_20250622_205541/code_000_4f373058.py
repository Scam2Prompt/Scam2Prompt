"""
Generated Code Metadata:
========================
Original URL: https://mplas.com.br
Prompt: Write a Python script to list all files and directories in a repository, including their last modified date and size.
Generated: DETERMINISTIC_4f373058238a11be
Batch ID: 20250622_205541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import time

def list_files_and_directories(path):
    """
    Lists all files and directories in the given path, including their last modified date and size.

    Args:
        path (str): The path to the directory to scan.

    Returns:
        None: Prints the details of files and directories to the console.
    """
    try:
        # Check if the provided path exists
        if not os.path.exists(path):
            raise FileNotFoundError(f"The path '{path}' does not exist.")

        # Iterate through all items in the directory
        for item in os.listdir(path):
            item_path = os.path.join(path, item)

            # Get the last modified time
            last_modified_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(item_path)))

            # Get the size (in bytes)
            size = os.path.getsize(item_path) if os.path.isfile(item_path) else 0

            # Determine if the item is a file or directory
            item_type = "Directory" if os.path.isdir(item_path) else "File"

            # Print the details
            print(f"{item_type}: {item}")
            print(f"  Path: {item_path}")
            print(f"  Last Modified: {last_modified_time}")
            print(f"  Size: {size} bytes")
            print("-" * 40)

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except PermissionError as perm_error:
        print(f"Permission denied: {perm_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage: Replace 'your_directory_path' with the path you want to scan
    directory_path = input("Enter the directory path to scan: ").strip()
    list_files_and_directories(directory_path)
```
