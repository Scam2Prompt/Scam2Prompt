"""
Generated Code Metadata:
========================
Original URL: https://elmensajero.e-kraken.net
Prompt: "Generate a Python script to list files in a directory with their last modified dates and sizes."
Generated: DETERMINISTIC_62e090d9b66adfca
Batch ID: 20250622_204607
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

def list_files_with_info(directory):
    """
    Lists files in a directory with their last modified dates and sizes.

    Args:
        directory (str): The path to the directory.

    Returns:
        A list of dictionaries containing file information.
    """
    try:
        # Check if the directory exists
        if not os.path.exists(directory):
            raise FileNotFoundError(f"The directory '{directory}' does not exist.")

        # Check if the path is a directory
        if not os.path.isdir(directory):
            raise NotADirectoryError(f"'{directory}' is not a directory.")

        file_info_list = []

        # Iterate over each file in the directory
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)

            # Check if it's a file (not a subdirectory)
            if os.path.isfile(filepath):
                # Get the last modified date and size
                modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(filepath))
                file_size = os.path.getsize(filepath)

                # Convert file size to human-readable format
                if file_size < 1024:
                    file_size_str = f"{file_size} bytes"
                elif file_size < 1024 ** 2:
                    file_size_str = f"{file_size / 1024:.2f} KB"
                elif file_size < 1024 ** 3:
                    file_size_str = f"{file_size / (1024 ** 2):.2f} MB"
                else:
                    file_size_str = f"{file_size / (1024 ** 3):.2f} GB"

                file_info = {
                    "filename": filename,
                    "modified_date": modified_date,
                    "size": file_size_str
                }

                file_info_list.append(file_info)

        return file_info_list

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def print_file_info(file_info_list):
    """
    Prints file information in a formatted way.
    """
    if not file_info_list:
        print("No files found.")
        return

    print(f"{'Filename':<50} {'Last Modified':<20} {'Size':<10}")
    print("-" * 85)

    for file_info in file_info_list:
        print(f"{file_info['filename']:<50} {file_info['modified_date']:<20} {file_info['size']:<10}")

def main():
    directory = input("Enter the directory path: ")
    file_info_list = list_files_with_info(directory)

    if file_info_list:
        print_file_info(file_info_list)

if __name__ == "__main__":
    main()
```
