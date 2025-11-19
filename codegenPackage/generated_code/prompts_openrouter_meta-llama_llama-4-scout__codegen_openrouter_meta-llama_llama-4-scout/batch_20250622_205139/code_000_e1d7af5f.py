"""
Generated Code Metadata:
========================
Original URL: https://elisium.it
Prompt: Write a Python script to generate a directory listing, including the last modified date and file size, similar to the one found on https://elisium.it.
Generated: DETERMINISTIC_e1d7af5f74f8f755
Batch ID: 20250622_205139
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

def get_directory_listing(directory):
    """
    Generate a directory listing, including the last modified date and file size.

    Args:
        directory (str): The path to the directory to list.

    Returns:
        list: A list of dictionaries containing the file information.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory '{directory}' does not exist.")

    listing = []
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(filepath))
            file_size = os.path.getsize(filepath)
            listing.append({
                'filename': filename,
                'modified_date': modified_date.strftime('%Y-%m-%d %H:%M:%S'),
                'file_size': file_size,
                'file_size_human': human_readable_size(file_size)
            })
    return listing

def human_readable_size(size):
    """
    Convert a file size in bytes to a human-readable format.

    Args:
        size (int): The file size in bytes.

    Returns:
        str: The file size in a human-readable format.
    """
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(size) < 1024.0:
            return f"{size:3.1f} {unit}B"
        size /= 1024.0
    return f"{size:.1f} YB"

def print_directory_listing(listing):
    """
    Print a directory listing in a formatted manner.

    Args:
        listing (list): A list of dictionaries containing the file information.
    """
    print(f"{'Filename':^50} | {'Last Modified':^20} | {'Size':^10}")
    print("-" * 90)
    for file in listing:
        print(f"{file['filename']:^50} | {file['modified_date']:^20} | {file['file_size_human']:^10}")

def main():
    directory = "."  # default to current directory
    try:
        listing = get_directory_listing(directory)
        print_directory_listing(listing)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    import sys
    main()
```
