"""
Generated Code Metadata:
========================
Original URL: https://ottbangla.store
Prompt: Generate a code snippet to retrieve the last modified date and file size of a list of files, similar to the information displayed on ottbangla.store.
Generated: DETERMINISTIC_365f99d698da51ba
Batch ID: 20250622_211656
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

def get_file_info(file_paths):
    """
    Retrieves the last modified date and file size of a list of files.

    Args:
        file_paths (list): A list of file paths.

    Returns:
        dict: A dictionary where the keys are the file paths and the values are dictionaries containing the last modified date and file size.

    Raises:
        FileNotFoundError: If a file in the list does not exist.
        OSError: If there is an operating system error while trying to access a file.
    """
    file_info = {}
    for file_path in file_paths:
        try:
            # Get the last modified date and file size
            modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
            file_size = os.path.getsize(file_path)

            # Store the file information in a dictionary
            file_info[file_path] = {
                'last_modified': modified_date,
                'file_size': file_size
            }
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except OSError as e:
            print(f"Error: Unable to access file '{file_path}': {e}")
    return file_info

def main():
    # Example usage
    file_paths = ['example1.txt', 'example2.txt', 'example3.txt']
    file_info = get_file_info(file_paths)

    # Print the file information
    for file_path, info in file_info.items():
        if info:
            print(f"File: {file_path}")
            print(f"Last Modified: {info['last_modified']}")
            print(f"File Size: {info['file_size']} bytes")
            print("------------------------")

if __name__ == "__main__":
    main()
```
