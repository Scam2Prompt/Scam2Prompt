"""
Generated Code Metadata:
========================
Original URL: https://elmensajero.e-kraken.net
Prompt: Generate code to parse and display the contents of a directory listing, including metadata like "Last modified" and "Size," as shown on the webpage.
Generated: DETERMINISTIC_42460c2115a1c55d
Batch ID: 20250612_151126
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

def get_directory_listing(path):
    """
    Get a listing of the directory at the specified path, including file metadata.

    Args:
        path (str): The path to the directory to list.

    Returns:
        list: A list of dictionaries containing file metadata.
    """
    try:
        # List to hold file metadata
        directory_contents = []

        # Iterate over the items in the directory
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            # Get file metadata
            file_info = {
                'name': item,
                'size': os.path.getsize(item_path),
                'last_modified': datetime.datetime.fromtimestamp(os.path.getmtime(item_path))
            }
            directory_contents.append(file_info)

        return directory_contents

    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
        return []
    except PermissionError:
        print(f"Error: Permission denied to access '{path}'.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def display_directory_listing(directory_contents):
    """
    Display the directory listing in a formatted manner.

    Args:
        directory_contents (list): A list of dictionaries containing file metadata.
    """
    if not directory_contents:
        print("No files to display.")
        return

    print(f"{'Name':<30} {'Size (bytes)':<15} {'Last Modified':<25}")
    print("=" * 70)

    for file_info in directory_contents:
        print(f"{file_info['name']:<30} {file_info['size']:<15} {file_info['last_modified']:<25}")

def main():
    """
    Main function to execute the directory listing and display.
    """
    # Specify the directory path (change this to the desired directory)
    directory_path = './'  # Current directory

    # Get the directory listing
    directory_contents = get_directory_listing(directory_path)

    # Display the directory listing
    display_directory_listing(directory_contents)

if __name__ == "__main__":
    main()
```
