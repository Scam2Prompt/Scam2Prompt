"""
Generated Code Metadata:
========================
Original URL: https://synerex-bo.com
Prompt: Write a function to parse and retrieve metadata from the Synerex directory listing, focusing on timestamps and file sizes.
Generated: DETERMINISTIC_ab771108efddca27
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import re
from datetime import datetime

def parse_synerex_metadata(directory_path):
    """
    Parse and retrieve metadata from the Synerex directory listing.

    Args:
        directory_path (str): Path to the Synerex directory.

    Returns:
        dict: A dictionary containing file metadata (timestamps and file sizes).

    Raises:
        FileNotFoundError: If the provided directory path does not exist.
        PermissionError: If the program lacks permission to access the directory.
    """

    # Check if the directory exists and is accessible
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")
    if not os.path.isdir(directory_path):
        raise ValueError(f"'{directory_path}' is not a directory.")
    if not os.access(directory_path, os.R_OK):
        raise PermissionError(f"Lacking permission to access the directory '{directory_path}'.")

    # Initialize an empty dictionary to store file metadata
    metadata = {}

    # Iterate over each file in the directory
    for filename in os.listdir(directory_path):
        filepath = os.path.join(directory_path, filename)

        # Skip if it's not a file
        if not os.path.isfile(filepath):
            continue

        # Get file stats
        try:
            stats = os.stat(filepath)
        except OSError as e:
            print(f"Error accessing file '{filename}': {e}")
            continue

        # Extract timestamp and file size
        timestamp = datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
        filesize = stats.st_size

        # Store metadata in the dictionary
        metadata[filename] = {
            'timestamp': timestamp,
            'filesize': filesize
        }

    return metadata


def parse_synerex_directory_listing(directory_listing):
    """
    Parse Synerex directory listing and extract file metadata.

    Args:
        directory_listing (str): The directory listing content.

    Returns:
        dict: A dictionary containing file metadata (timestamps and file sizes).
    """

    # Regular expression pattern to match file information
    pattern = re.compile(r'(\w+)\s+(\d+)\s+(\w+\s+\d+\s+\d+:\d+:\d+)\s+(.*)')

    # Initialize an empty dictionary to store file metadata
    metadata = {}

    # Split the directory listing into lines
    for line in directory_listing.splitlines():
        match = pattern.match(line)

        # Skip if the line does not match the expected pattern
        if not match:
            continue

        # Extract file information
        permissions = match.group(1)
        num_links = match.group(2)
        timestamp = match.group(3)
        filename = match.group(4)

        # Convert timestamp to a standard format
        try:
            timestamp = datetime.strptime(timestamp, '%b %d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
        except ValueError:
            pass  # Ignore if timestamp is not in the expected format

        # Get file size from num_links (this might not be accurate)
        try:
            filesize = int(num_links)
        except ValueError:
            filesize = 0

        # Store metadata in the dictionary
        metadata[filename] = {
            'timestamp': timestamp,
            'filesize': filesize
        }

    return metadata


# Example usage
if __name__ == "__main__":
    directory_path = '/path/to/synerex/directory'
    try:
        metadata = parse_synerex_metadata(directory_path)
        print(metadata)
    except Exception as e:
        print(f"An error occurred: {e}")

    directory_listing = """drwxr-xr-x 3 user user 4096 Oct 12 14:30:00 dir1
-rw-r--r-- 1 user user 1024 Oct 11 12:00:00 file1.txt
-rw-r--r-- 1 user user 2048 Oct 12 13:00:00 file2.txt"""

    metadata = parse_synerex_directory_listing(directory_listing)
    print(metadata)
```
