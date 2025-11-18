"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synerex-bo.com
Prompt: Write a function to parse and retrieve metadata from the Synerex directory listing, focusing on timestamps and file sizes.
Generated: DETERMINISTIC_ab771108efddca27
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from datetime import datetime

def parse_synerex_directory(directory_path):
    """
    Parses the Synerex directory listing and retrieves metadata for files, including timestamps and file sizes.

    Args:
        directory_path (str): Path to the directory to be parsed.

    Returns:
        list[dict]: A list of dictionaries containing metadata for each file.
                    Each dictionary contains:
                        - 'file_name': Name of the file
                        - 'file_size': Size of the file in bytes
                        - 'last_modified': Last modified timestamp of the file (datetime object)

    Raises:
        ValueError: If the directory_path does not exist or is not a directory.
    """
    try:
        # Check if the directory exists and is actually a directory
        if not os.path.exists(directory_path):
            raise ValueError(f"Directory path does not exist: {directory_path}")
        if not os.path.isdir(directory_path):
            raise ValueError(f"Provided path is not a directory: {directory_path}")

        # Initialize an empty list to store file metadata
        file_metadata_list = []

        # Iterate over all files in the directory
        for entry in os.scandir(directory_path):
            if entry.is_file():  # Process only files, skip directories
                # Retrieve file metadata
                file_name = entry.name
                file_size = entry.stat().st_size  # File size in bytes
                last_modified = datetime.fromtimestamp(entry.stat().st_mtime)  # Last modified timestamp

                # Append metadata to the list
                file_metadata_list.append({
                    'file_name': file_name,
                    'file_size': file_size,
                    'last_modified': last_modified
                })

        return file_metadata_list

    except Exception as e:
        # Catch any unexpected errors and log them appropriately
        print(f"An error occurred while parsing the directory: {e}")
        raise

# Example usage:
# directory_metadata = parse_synerex_directory("/path/to/synerex/directory")
# for file_meta in directory_metadata:
#     print(file_meta)
```
