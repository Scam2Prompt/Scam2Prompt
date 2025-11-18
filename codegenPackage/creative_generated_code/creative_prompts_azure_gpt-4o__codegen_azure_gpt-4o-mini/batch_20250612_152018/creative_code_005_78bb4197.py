"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://refconegypt.net
Prompt: Provide an example of using the `os` module in Python to replicate the directory listing format shown on https://refconegypt.net, including last modified dates and file sizes.
Generated: DETERMINISTIC_78bb4197b03a9ee2
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import time

def get_directory_listing(directory_path):
    """
    Returns a formatted list of files and directories in the specified directory.
    Each entry includes the name, last modified date, and size.

    :param directory_path: Path to the directory to list
    :return: List of formatted strings with file details
    """
    # Check if the provided path is a directory
    if not os.path.isdir(directory_path):
        raise ValueError(f"The provided path '{directory_path}' is not a valid directory.")

    # List to hold formatted entries
    directory_listing = []

    # Iterate through each item in the directory
    for entry in os.listdir(directory_path):
        # Get full path of the entry
        full_path = os.path.join(directory_path, entry)

        # Get the last modified time and convert it to a readable format
        last_modified_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(full_path)))

        # Get the size of the entry in bytes
        size = os.path.getsize(full_path)

        # Append formatted string to the listing
        directory_listing.append(f"{entry}\t{last_modified_time}\t{size} bytes")

    return directory_listing

def print_directory_listing(directory_path):
    """
    Prints the directory listing to the console.

    :param directory_path: Path to the directory to list
    """
    try:
        # Get the directory listing
        directory_listing = get_directory_listing(directory_path)

        # Print header
        print(f"Directory listing for: {directory_path}\n")
        print(f"{'Name':<30} {'Last Modified':<20} {'Size':<10}")
        print("=" * 60)

        # Print each entry
        for entry in directory_listing:
            print(entry)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Specify the directory to list
    directory_to_list = '.'  # Change this to the desired directory

    # Print the directory listing
    print_directory_listing(directory_to_list)
```
