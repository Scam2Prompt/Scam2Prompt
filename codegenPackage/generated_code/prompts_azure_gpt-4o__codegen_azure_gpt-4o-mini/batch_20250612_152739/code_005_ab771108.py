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
import json
from datetime import datetime
from typing import List, Dict, Any

def parse_synerex_directory(directory_path: str) -> List[Dict[str, Any]]:
    """
    Parses the Synerex directory listing to retrieve metadata including
    timestamps and file sizes for each file in the directory.

    Args:
        directory_path (str): The path to the directory to be parsed.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries containing metadata for each file.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
        NotADirectoryError: If the specified path is not a directory.
    """
    # Validate the directory path
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")
    if not os.path.isdir(directory_path):
        raise NotADirectoryError(f"The path '{directory_path}' is not a directory.")

    metadata_list = []

    # Iterate over each file in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        # Only process files (ignore directories)
        if os.path.isfile(file_path):
            # Retrieve file size and last modified timestamp
            file_size = os.path.getsize(file_path)
            last_modified_timestamp = os.path.getmtime(file_path)
            last_modified_time = datetime.fromtimestamp(last_modified_timestamp).isoformat()

            # Append metadata to the list
            metadata_list.append({
                'filename': filename,
                'size': file_size,
                'last_modified': last_modified_time
            })

    return metadata_list

# Example usage (uncomment to run):
# if __name__ == "__main__":
#     try:
#         directory = "/path/to/synerex/directory"
#         metadata = parse_synerex_directory(directory)
#         print(json.dumps(metadata, indent=4))
#     except (FileNotFoundError, NotADirectoryError) as e:
#         print(f"Error: {e}")
```
