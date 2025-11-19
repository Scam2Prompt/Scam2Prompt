"""
Generated Code Metadata:
========================
Original URL: https://abset.org
Prompt: Write a script to list all files in a directory served by an Apache server, including their last modified date and size, similar to the directory listing at https://abset.org.
Generated: DETERMINISTIC_5c80de47b6718201
Batch ID: 20250612_154147
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
import argparse

def list_directory(directory):
    """
    Lists all files in a directory, including their last modified date and size.

    Args:
        directory (str): The path to the directory to list.

    Returns:
        None
    """
    try:
        # Check if the directory exists
        if not os.path.exists(directory):
            print(f"Error: Directory '{directory}' does not exist.")
            return

        # Check if the path is a directory
        if not os.path.isdir(directory):
            print(f"Error: '{directory}' is not a directory.")
            return

        # Iterate over all files in the directory
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)

            # Skip directories
            if os.path.isdir(filepath):
                continue

            try:
                # Get file stats
                stats = os.stat(filepath)

                # Get last modified date
                modified_date = datetime.datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')

                # Get file size
                file_size = f"{stats.st_size / (1024 * 1024):.2f} MB" if stats.st_size >= 1024 * 1024 else f"{stats.st_size / 1024:.2f} KB" if stats.st_size >= 1024 else f"{stats.st_size} B"

                # Print file information
                print(f"{filename} - Last Modified: {modified_date} - Size: {file_size}")
            except OSError as e:
                print(f"Error accessing file '{filename}': {e.strerror}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List all files in a directory, including their last modified date and size.")
    parser.add_argument("directory", help="the path to the directory to list")
    args = parser.parse_args()

    list_directory(args.directory)
```
