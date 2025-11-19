"""
Generated Code Metadata:
========================
Original URL: https://ottbangla.store
Prompt: Write a script to list the files in a directory index, similar to the one shown on ottbangla.store.
Generated: DETERMINISTIC_4f2070b5e51a0d02
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
from pathlib import Path
from datetime import datetime

def list_directory_contents(directory_path):
    """
    Lists files and directories in the specified path, similar to a directory index.
    
    Args:
        directory_path (str): Path to the directory to list contents of.
    
    Returns:
        list: A list of dictionaries containing file/directory details.
              Each dictionary contains keys: name, type, size, modified_time.
    
    Raises:
        FileNotFoundError: If the specified directory does not exist.
        PermissionError: If the user does not have permission to access the directory.
    """
    try:
        path = Path(directory_path)
        
        # Verify the directory exists
        if not path.exists():
            raise FileNotFoundError(f"Directory not found: {directory_path}")
        
        # Verify it's a directory
        if not path.is_dir():
            raise NotADirectoryError(f"Path is not a directory: {directory_path}")
        
        contents = []
        
        for item in path.iterdir():
            try:
                # Get file stats
                stat = item.stat()
                
                # Determine if it's a file or directory
                item_type = 'file' if item.is_file() else 'directory'
                
                # Format size (in bytes for files, empty for directories)
                size = stat.st_size if item.is_file() else 0
                
                # Format modified time
                modified_time = datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
                
                contents.append({
                    'name': item.name,
                    'type': item_type,
                    'size': size,
                    'modified_time': modified_time
                })
            except PermissionError:
                # Skip files/directories we don't have permission to access
                continue
        
        # Sort by name (case-insensitive)
        contents.sort(key=lambda x: x['name'].lower())
        
        return contents
    
    except Exception as e:
        raise e

def print_directory_listing(contents):
    """
    Prints the directory listing in a formatted table.
    
    Args:
        contents (list): List of file/directory dictionaries from list_directory_contents()
    """
    if not contents:
        print("Directory is empty.")
        return
    
    # Print header
    print(f"{'Name':<50} {'Type':<10} {'Size':>10} {'Modified':<20}")
    print("-" * 90)
    
    # Print each item
    for item in contents:
        size_str = f"{item['size']} bytes" if item['type'] == 'file' else ''
        print(f"{item['name']:<50} {item['type']:<10} {size_str:>10} {item['modified_time']:<20}")

if __name__ == "__main__":
    import sys
    
    try:
        # Get directory path from command line or use current directory
        directory = sys.argv[1] if len(sys.argv) > 1 else '.'
        
        # Get directory contents
        contents = list_directory_contents(directory)
        
        # Print formatted output
        print_directory_listing(contents)
    
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except PermissionError as e:
        print(f"Error: Permission denied - {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)
```
