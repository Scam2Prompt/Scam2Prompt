"""
Generated Code Metadata:
========================
Original URL: https://formebd.com.rabby.aknetworkbd.com
Prompt: Write a script to retrieve and display metadata (e.g., last modified date, size) of files in a directory served by LiteSpeed Web Server.
Generated: DETERMINISTIC_638478a2bf7663f4
Batch ID: 20250612_151347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import stat
from datetime import datetime

def get_file_metadata(directory):
    """
    Retrieves and displays metadata of files in a given directory.

    Args:
        directory (str): Path to the directory.

    Returns:
        None
    """
    try:
        # Check if the directory exists
        if not os.path.exists(directory):
            raise FileNotFoundError(f"The directory '{directory}' does not exist.")

        # Check if the path is a directory
        if not os.path.isdir(directory):
            raise NotADirectoryError(f"'{directory}' is not a directory.")

        # Iterate over each file in the directory
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)

            # Check if it's a file (not a subdirectory)
            if os.path.isfile(filepath):
                try:
                    # Get file stats
                    file_stats = os.stat(filepath)

                    # Get last modified date
                    modified_date = datetime.fromtimestamp(file_stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')

                    # Get file size
                    file_size = file_stats.st_size

                    # Convert file size to human-readable format
                    if file_size < 1024:
                        file_size_str = f"{file_size} bytes"
                    elif file_size < 1024**2:
                        file_size_str = f"{file_size / 1024:.2f} KB"
                    elif file_size < 1024**3:
                        file_size_str = f"{file_size / 1024**2:.2f} MB"
                    else:
                        file_size_str = f"{file_size / 1024**3:.2f} GB"

                    # Print file metadata
                    print(f"File: {filename}")
                    print(f"Last Modified: {modified_date}")
                    print(f"Size: {file_size_str}")
                    print(f"Permissions: {stat.filemode(file_stats.st_mode)}")
                    print("-" * 50)

                except OSError as e:
                    print(f"Error accessing file '{filename}': {e}", file=sys.stderr)

    except FileNotFoundError as e:
        print(e, file=sys.stderr)
    except NotADirectoryError as e:
        print(e, file=sys.stderr)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    import sys
    directory = "."  # current directory
    get_file_metadata(directory)
```
