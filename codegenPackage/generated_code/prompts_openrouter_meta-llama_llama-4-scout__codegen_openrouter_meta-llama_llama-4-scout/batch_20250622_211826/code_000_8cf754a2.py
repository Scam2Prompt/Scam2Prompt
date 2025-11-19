"""
Generated Code Metadata:
========================
Original URL: https://spadaro.id.au
Prompt: "Write a Python script to generate a directory listing with last modified date and file size, similar to the one found on spadaro.id.au."
Generated: DETERMINISTIC_8cf754a2dcfabd56
Batch ID: 20250622_211826
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
    Generate a directory listing with last modified date and file size.

    Args:
        directory (str): The path to the directory to list.

    Returns:
        list: A list of dictionaries containing file information.

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
                'modified_date': modified_date,
                'file_size': file_size
            })
    return listing

def print_directory_listing(listing):
    """
    Print the directory listing in a human-readable format.

    Args:
        listing (list): A list of dictionaries containing file information.
    """
    print(f"{'Filename':^50} | {'Last Modified':^20} | {'File Size':^10}")
    print("-" * 85)
    for file_info in listing:
        filename = file_info['filename']
        modified_date = file_info['modified_date'].strftime('%Y-%m-%d %H:%M')
        file_size = f"{file_info['file_size'] / 1024:.2f} KB" if file_info['file_size'] < 1024 * 1024 else f"{file_info['file_size'] / (1024 * 1024):.2f} MB"
        print(f"{filename:^50} | {modified_date:^20} | {file_size:^10}")

def main():
    directory = '.'  # default to current directory
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
