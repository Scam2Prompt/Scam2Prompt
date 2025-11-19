"""
Generated Code Metadata:
========================
Original URL: https://perurest.com
Prompt: Write a script to list and parse directory contents served by a LiteSpeed Web Server, including file names, last modified dates, and sizes.
Generated: DETERMINISTIC_0cccaa85dda52e98
Batch ID: 20250612_154216
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

def list_directory_contents(directory_path):
    """
    Lists and parses the contents of a directory served by a LiteSpeed Web Server.

    Args:
        directory_path (str): The path to the directory to be listed.

    Returns:
        list: A list of dictionaries containing file information (name, last modified date, size).
    """
    # Validate the directory path
    if not os.path.isdir(directory_path):
        raise ValueError(f"The provided path '{directory_path}' is not a valid directory.")

    # Initialize a list to hold file information
    file_info_list = []

    # Iterate over the contents of the directory
    for entry in os.listdir(directory_path):
        entry_path = os.path.join(directory_path, entry)

        # Check if the entry is a file
        if os.path.isfile(entry_path):
            # Get file details
            file_name = entry
            last_modified_time = os.path.getmtime(entry_path)
            file_size = os.path.getsize(entry_path)

            # Convert last modified time to a readable format
            last_modified_date = datetime.datetime.fromtimestamp(last_modified_time).strftime('%Y-%m-%d %H:%M:%S')

            # Append file information to the list
            file_info_list.append({
                'name': file_name,
                'last_modified': last_modified_date,
                'size': file_size
            })

    return file_info_list

def main():
    """
    Main function to execute the directory listing.
    """
    # Specify the directory to be listed (change this to your target directory)
    directory_path = '/path/to/your/directory'

    try:
        # List directory contents
        contents = list_directory_contents(directory_path)

        # Print the file information
        for file_info in contents:
            print(f"File Name: {file_info['name']}, Last Modified: {file_info['last_modified']}, Size: {file_info['size']} bytes")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
