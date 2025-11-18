"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbiotico.org
Prompt: Write a Python script to parse and extract file names, last modified dates, and sizes from a directory listing similar to the one at https://symbiotico.org.
Generated: DETERMINISTIC_6a7f3ffc23f8d372
Batch ID: 20250612_152006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import sys
from datetime import datetime


def parse_directory(directory_path):
    """
    Parse a directory and extract details of files including name, last modified date, and size.

    Args:
        directory_path (str): Path to the directory to be parsed.

    Returns:
        list: A list of dictionaries containing file details.
    """
    file_details = []

    try:
        # Get the list of files and directories in the specified path
        entries = os.listdir(directory_path)
    except FileNotFoundError:
        print(f"Error: Directory '{directory_path}' not found.", file=sys.stderr)
        return []
    except PermissionError:
        print(f"Error: Permission denied to access '{directory_path}'.", file=sys.stderr)
        return []

    for entry in entries:
        entry_path = os.path.join(directory_path, entry)

        # Process only files, skip directories
        if os.path.isfile(entry_path):
            try:
                # Extract file details
                file_name = entry
                file_size = os.path.getsize(entry_path)  # File size in bytes
                last_modified_timestamp = os.path.getmtime(entry_path)  # Last modified timestamp
                last_modified_date = datetime.fromtimestamp(last_modified_timestamp).strftime('%Y-%m-%d %H:%M:%S')

                # Append file details to the list
                file_details.append({
                    "name": file_name,
                    "last_modified": last_modified_date,
                    "size_bytes": file_size
                })
            except OSError as e:
                print(f"Error reading file '{entry_path}': {e}", file=sys.stderr)

    return file_details


if __name__ == "__main__":
    # Specify the directory to parse (modify as needed)
    directory_to_parse = input("Enter the path of the directory to parse: ").strip()

    # Parse the directory and extract file details
    files = parse_directory(directory_to_parse)

    # Display the extracted file details
    if files:
        print("\nFile Details:")
        for file in files:
            print(f"Name: {file['name']}, Last Modified: {file['last_modified']}, Size: {file['size_bytes']} bytes")
    else:
        print("\nNo files found or an error occurred.")
```
