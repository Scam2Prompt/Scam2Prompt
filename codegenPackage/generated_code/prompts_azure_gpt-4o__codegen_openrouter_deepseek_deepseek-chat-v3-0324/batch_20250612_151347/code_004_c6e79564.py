"""
Generated Code Metadata:
========================
Original URL: https://formebd.com.rabby.aknetworkbd.com
Prompt: Provide an example of using Python's `os` module to replicate the directory listing format shown on a LiteSpeed Web Server.
Generated: DETERMINISTIC_c6e7956463fe1bcb
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
import time
from datetime import datetime

def format_size(size):
    """Format file size in human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:3.1f} {unit}"
        size /= 1024.0
    return f"{size:.1f} PB"

def format_date(timestamp):
    """Format timestamp into LiteSpeed-like date format."""
    dt = datetime.fromtimestamp(timestamp)
    return dt.strftime("%d-%b-%Y %H:%M")

def list_directory_litespeed_style(path='.'):
    """List directory contents in LiteSpeed Web Server format."""
    try:
        entries = os.listdir(path)
        entries.sort(key=lambda x: x.lower())
        
        print(f"Index of {os.path.abspath(path)}")
        print("----------------------------------------")
        print("Mode         Last Modified         Size  Name")
        print("----------------------------------------")
        
        for entry in entries:
            full_path = os.path.join(path, entry)
            stat = os.stat(full_path)
            
            mode = oct(stat.st_mode)[-3:]
            size = format_size(stat.st_size)
            modified = format_date(stat.st_mtime)
            
            if os.path.isdir(full_path):
                entry += "/"
                size = "-"
            
            print(f"{mode:<12} {modified:<20} {size:<6} {entry}")
            
    except PermissionError:
        print("Error: Permission denied")
    except FileNotFoundError:
        print(f"Error: Directory '{path}' not found")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    list_directory_litespeed_style(path)
```
