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

def list_files_in_directory(directory):
    """
    List all files in the specified directory along with their last modified dates and sizes.

    Args:
        directory (str): The path to the directory to list files from.

    Returns:
        list: A list of tuples containing file name, last modified date, and size in bytes.
    """
    # Check if the provided directory exists
    if not os.path.isdir(directory):
        raise ValueError(f"The provided path '{directory}' is not a valid directory.")

    file_info_list = []

    # Iterate over all items in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Check if the item is a file
        if os.path.isfile(file_path):
            # Get the last modified time and size of the file
            last_modified_time = os.path.getmtime(file_path)
            file_size = os.path.getsize(file_path)

            # Convert last modified time to a readable format
            last_modified_date = datetime.datetime.fromtimestamp(last_modified_time).strftime('%Y-%m-%d %H:%M:%S')

            # Append the file information to the list
            file_info_list.append((filename, last_modified_date, file_size))

    return file_info_list

def main():
    # Specify the directory to list files from
    directory = input("Enter the directory path: ")

    try:
        # Get the list of files with their details
        files = list_files_in_directory(directory)

        # Print the file details
        print(f"{'Filename':<30} {'Last Modified':<20} {'Size (bytes)':<15}")
        print("=" * 65)
        for filename, last_modified, size in files:
            print(f"{filename:<30} {last_modified:<20} {size:<15}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
