"""
Generated Code Metadata:
========================
Original URL: https://ouatvs.com
Prompt: Write a Python script to parse and list the contents of a directory, including file names, last modified dates, and sizes, similar to the format shown on a LiteSpeed Web Server directory listing.
Generated: DETERMINISTIC_f67da116d488864e
Batch ID: 20250612_151525
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
    Lists the contents of the specified directory, including file names,
    last modified dates, and sizes.

    Args:
        directory_path (str): The path to the directory to be listed.

    Returns:
        list: A list of dictionaries containing file information.
    """
    # Check if the provided path is a directory
    if not os.path.isdir(directory_path):
        raise ValueError(f"The path '{directory_path}' is not a valid directory.")

    contents = []

    # Iterate over the items in the directory
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)

        # Get file information
        try:
            file_info = {
                'name': item,
                'last_modified': datetime.datetime.fromtimestamp(os.path.getmtime(item_path)),
                'size': os.path.getsize(item_path)
            }
            contents.append(file_info)
        except Exception as e:
            print(f"Error retrieving information for '{item}': {e}")

    return contents

def format_directory_listing(contents):
    """
    Formats the directory contents into a human-readable string.

    Args:
        contents (list): A list of dictionaries containing file information.

    Returns:
        str: A formatted string of the directory listing.
    """
    output = "Directory Listing:\n"
    output += "{:<30} {:<25} {:<10}\n".format("File Name", "Last Modified", "Size (bytes)")
    output += "-" * 65 + "\n"

    for item in contents:
        output += "{:<30} {:<25} {:<10}\n".format(
            item['name'],
            item['last_modified'].strftime('%Y-%m-%d %H:%M:%S'),
            item['size']
        )

    return output

def main():
    """
    Main function to execute the directory listing script.
    """
    directory_path = input("Enter the directory path to list: ")

    try:
        contents = list_directory_contents(directory_path)
        formatted_listing = format_directory_listing(contents)
        print(formatted_listing)
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
