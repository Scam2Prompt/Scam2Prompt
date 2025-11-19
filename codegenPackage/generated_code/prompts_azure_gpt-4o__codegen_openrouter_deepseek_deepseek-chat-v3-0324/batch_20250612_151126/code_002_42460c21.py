"""
Generated Code Metadata:
========================
Original URL: https://elmensajero.e-kraken.net
Prompt: Generate code to parse and display the contents of a directory listing, including metadata like "Last modified" and "Size," as shown on the webpage.
Generated: DETERMINISTIC_42460c2115a1c55d
Batch ID: 20250612_151126
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
from pathlib import Path

def get_directory_listing(directory_path: str) -> List[Dict[str, str]]:
    """
    Get a list of files and directories with their metadata.
    
    Args:
        directory_path: Path to the directory to list.
    
    Returns:
        List of dictionaries containing file/directory metadata.
    """
    try:
        path = Path(directory_path)
        if not path.exists():
            raise FileNotFoundError(f"Directory not found: {directory_path}")
        if not path.is_dir():
            raise NotADirectoryError(f"Path is not a directory: {directory_path}")

        entries = []
        for entry in path.iterdir():
            stat = entry.stat()
            entries.append({
                'name': entry.name,
                'type': 'directory' if entry.is_dir() else 'file',
                'size': stat.st_size,
                'last_modified': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stat.st_mtime)),
                'path': str(entry.absolute())
            })
        
        return sorted(entries, key=lambda x: x['name'].lower())
    
    except Exception as e:
        raise Exception(f"Error reading directory: {str(e)}")

def display_directory_listing(entries: List[Dict[str, str]]) -> None:
    """
    Display directory listing in a formatted table.
    
    Args:
        entries: List of file/directory metadata dictionaries.
    """
    if not entries:
        print("Directory is empty.")
        return
    
    # Calculate column widths
    name_width = max(len(entry['name']) for entry in entries) + 2
    type_width = 10
    size_width = 10
    mod_width = 20
    
    # Print header
    print(f"{'Name':<{name_width}} {'Type':<{type_width}} {'Size':>{size_width}} {'Last Modified':<{mod_width}}")
    print("-" * (name_width + type_width + size_width + mod_width + 3))
    
    # Print entries
    for entry in entries:
        size = f"{entry['size']:,}" if entry['type'] == 'file' else '-'
        print(f"{entry['name']:<{name_width}} "
              f"{entry['type']:<{type_width}} "
              f"{size:>{size_width}} "
              f"{entry['last_modified']:<{mod_width}}")

if __name__ == "__main__":
    try:
        directory = input("Enter directory path: ").strip()
        entries = get_directory_listing(directory)
        display_directory_listing(entries)
    except Exception as e:
        print(f"Error: {str(e)}")
```
