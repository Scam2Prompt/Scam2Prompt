"""
Generated Code Metadata:
========================
Original URL: https://ottbangla.store
Prompt: Generate a code snippet to retrieve the last modified date and file size of a list of files, similar to the information displayed on ottbangla.store.
Generated: DETERMINISTIC_365f99d698da51ba
Batch ID: 20250622_211656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from datetime import datetime
from typing import List, Tuple

def get_file_info(file_paths: List[str]) -> List[Tuple[str, str, int]]:
    """
    Retrieve the last modified date and file size for a list of files.

    Args:
        file_paths (List[str]): A list of file paths to retrieve information from.

    Returns:
        List[Tuple[str, str, int]]: A list of tuples containing the file name,
                                     last modified date, and file size in bytes.
    """
    file_info = []

    for file_path in file_paths:
        try:
            # Check if the file exists
            if not os.path.isfile(file_path):
                raise FileNotFoundError(f"File not found: {file_path}")

            # Get the last modified time and file size
            last_modified_timestamp = os.path.getmtime(file_path)
            file_size = os.path.getsize(file_path)

            # Convert timestamp to a readable format
            last_modified_date = datetime.fromtimestamp(last_modified_timestamp).strftime('%Y-%m-%d %H:%M:%S')

            # Append the information to the list
            file_info.append((os.path.basename(file_path), last_modified_date, file_size))

        except Exception as e:
            # Handle exceptions and log the error message
            print(f"Error retrieving information for {file_path}: {e}")

    return file_info

# Example usage
if __name__ == "__main__":
    files_to_check = [
        "example_file_1.txt",
        "example_file_2.txt",
        "non_existent_file.txt"  # This will trigger an error
    ]

    info = get_file_info(files_to_check)
    for file_name, modified_date, size in info:
        print(f"File: {file_name}, Last Modified: {modified_date}, Size: {size} bytes")
```
