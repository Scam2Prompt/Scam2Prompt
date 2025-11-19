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
import time
from typing import List, Dict

def get_file_metadata(file_paths: List[str]) -> List[Dict[str, str]]:
    """
    Retrieves the last modified date and file size for a list of files.

    Args:
        file_paths: List of file paths to retrieve metadata for.

    Returns:
        A list of dictionaries containing 'file_path', 'last_modified', and 'file_size' for each file.
        Returns an empty list if no valid files are provided.

    Raises:
        TypeError: If file_paths is not a list.
    """
    if not isinstance(file_paths, list):
        raise TypeError("file_paths must be a list of strings")

    file_metadata = []

    for file_path in file_paths:
        try:
            # Get file stats
            file_stat = os.stat(file_path)
            
            # Convert last modified timestamp to readable format
            last_modified = time.strftime(
                '%Y-%m-%d %H:%M:%S',
                time.localtime(file_stat.st_mtime)
            )
            
            # Convert file size to KB with 2 decimal places
            file_size_kb = round(file_stat.st_size / 1024, 2)
            
            file_metadata.append({
                'file_path': file_path,
                'last_modified': last_modified,
                'file_size': f"{file_size_kb} KB"
            })
            
        except (OSError, FileNotFoundError) as e:
            # Skip files that don't exist or can't be accessed
            continue
        except Exception as e:
            # Log unexpected errors but continue processing other files
            print(f"Unexpected error processing {file_path}: {str(e)}")
            continue

    return file_metadata

# Example usage:
if __name__ == "__main__":
    files = ["example.txt", "nonexistent_file.txt", "another_file.jpg"]
    metadata = get_file_metadata(files)
    
    for item in metadata:
        print(f"File: {item['file_path']}")
        print(f"Last Modified: {item['last_modified']}")
        print(f"Size: {item['file_size']}")
        print("-" * 40)
```
