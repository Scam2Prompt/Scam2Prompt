"""
Generated Code Metadata:
========================
Original URL: https://coinbaseinfo.info
Prompt: Write a script to list all files in a directory, including their last modified date and size, similar to the "Index of /" structure displayed on a LiteSpeed Web Server.
Generated: DETERMINISTIC_b4bdce8550a0ef16
Batch ID: 20250612_154058
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
from datetime import datetime
from pathlib import Path

def format_size(size_bytes):
    """Convert file size to human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} PB"

def format_date(timestamp):
    """Convert timestamp to formatted date string."""
    return datetime.fromtimestamp(timestamp).strftime('%d-%b-%Y %H:%M')

def list_directory(directory_path):
    """List all files and directories with their metadata."""
    try:
        path = Path(directory_path)
        if not path.exists():
            raise FileNotFoundError(f"Directory not found: {directory_path}")
        
        if not path.is_dir():
            raise NotADirectoryError(f"Path is not a directory: {directory_path}")

        items = []
        for item in path.iterdir():
            stat = item.stat()
            is_dir = item.is_dir()
            name = item.name + ('/' if is_dir else '')
            size = 0 if is_dir else stat.st_size
            modified = stat.st_mtime
            
            items.append({
                'name': name,
                'size': size,
                'modified': modified,
                'is_dir': is_dir
            })

        # Sort directories first, then by name
        items.sort(key=lambda x: (not x['is_dir'], x['name'].lower()))

        # Generate output similar to LiteSpeed's "Index of /"
        print(f"Index of {directory_path}")
        print("-" * 80)
        print(f"{'Name':<50} {'Last Modified':<25} {'Size':>15}")
        print("-" * 80)
        
        for item in items:
            print(f"{item['name']:<50} {format_date(item['modified']):<25} "
                  f"{format_size(item['size']) if not item['is_dir'] else '-':>15}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python directory_lister.py <directory_path>")
        sys.exit(1)
    
    list_directory(sys.argv[1])
```
