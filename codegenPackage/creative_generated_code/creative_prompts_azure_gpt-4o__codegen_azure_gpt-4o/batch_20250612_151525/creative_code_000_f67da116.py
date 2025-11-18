"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ouatvs.com
Prompt: Write a Python script to parse and list the contents of a directory, including file names, last modified dates, and sizes, similar to the format shown on a LiteSpeed Web Server directory listing.
Generated: DETERMINISTIC_f67da116d488864e
Batch ID: 20250612_151525
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
import sys

def list_directory_contents(directory_path):
    """
    Lists the contents of the specified directory, including file names,
    last modified dates, and sizes, in a format similar to a LiteSpeed Web Server listing.

    Parameters:
        directory_path (str): Path to the directory to be listed.

    Returns:
        None: Prints the directory contents to the console.
    """
    try:
        # Check if the given path is a valid directory
        if not os.path.isdir(directory_path):
            raise NotADirectoryError(f"'{directory_path}' is not a valid directory.")

        # Print header similar to LiteSpeed Web Server listing
        print(f"Listing contents of: {directory_path}\n")
        print("{:<40} {:<20} {:<10}".format("Name", "Last Modified", "Size (bytes)"))
        print("-" * 70)

        # Iterate over each item in the directory
        for item in os.listdir(directory_path):
            item_path = os.path.join(directory_path, item)

            # Get file details
            last_modified = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(item_path)))
            size = os.path.getsize(item_path) if os.path.isfile(item_path) else '-'

            # Print details in a formatted manner
            print("{:<40} {:<20} {:<10}".format(item, last_modified, size))

    except NotADirectoryError as e:
        print(f"Error: {e}")
    except PermissionError:
        print(f"Error: Permission denied to access '{directory_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Ensure the script is called with a directory path argument
    if len(sys.argv) != 2:
        print("Usage: python list_directory.py <directory_path>")
        sys.exit(1)

    # Get directory path from command line arguments
    directory_path = sys.argv[1]

    # List directory contents
    list_directory_contents(directory_path)
```
