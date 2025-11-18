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
import json
from datetime import datetime
from typing import List, Dict

def parse_synerex_directory(directory_path: str) -> List[Dict[str, str]]:
    """
    Parses the Synerex directory listing to retrieve metadata including timestamps and file sizes.

    Args:
        directory_path (str): The path to the directory to parse.

    Returns:
        List[Dict[str, str]]: A list of dictionaries containing metadata for each file.
    
    Raises:
        ValueError: If the provided directory path does not exist or is not a directory.
    """
    # Validate the provided directory path
    if not os.path.exists(directory_path):
        raise ValueError(f"The provided path does not exist: {directory_path}")
    if not os.path.isdir(directory_path):
        raise ValueError(f"The provided path is not a directory: {directory_path}")

    metadata_list = []

    # Iterate through each item in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        
        # Only process files (skip directories)
        if os.path.isfile(file_path):
            # Get the file size in bytes
            file_size = os.path.getsize(file_path)
            # Get the last modified timestamp
            timestamp = os.path.getmtime(file_path)
            # Convert timestamp to a readable format
            readable_time = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")

            # Append metadata to the list
            metadata_list.append({
                'filename': filename,
                'size_bytes': file_size,
                'last_modified': readable_time
            })

    return metadata_list

# Example usage (uncomment to test it in an environment with a valid directory)
# if __name__ == "__main__":
#     directory = "/path/to/synerex/directory"
#     try:
#         metadata = parse_synerex_directory(directory)
#         print(json.dumps(metadata, indent=2))
#     except ValueError as ve:
#         print(f"Error: {ve}")
```
