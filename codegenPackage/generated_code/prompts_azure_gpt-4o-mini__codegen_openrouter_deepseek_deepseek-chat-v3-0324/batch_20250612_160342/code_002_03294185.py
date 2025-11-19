"""
Generated Code Metadata:
========================
Original URL: https://fixedfiloat.com
Prompt: Write a Python function to retrieve and display directory contents, inspired by the structure seen on fixedfiloat.com.
Generated: DETERMINISTIC_0329418532469793
Batch ID: 20250612_160342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from typing import List, Dict, Optional
import stat
from datetime import datetime

def get_directory_contents(path: str = '.') -> List[Dict[str, Optional[str]]]:
    """
    Retrieves and returns the contents of a directory in a structured format.
    
    Args:
        path (str): Path to the directory. Defaults to current directory.
        
    Returns:
        List[Dict[str, Optional[str]]]: List of dictionaries containing file/directory info.
        
    Raises:
        FileNotFoundError: If the specified path does not exist.
        NotADirectoryError: If the specified path is not a directory.
        PermissionError: If permission to access the directory is denied.
    """
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Path '{path}' does not exist")
            
        if not os.path.isdir(path):
            raise NotADirectoryError(f"Path '{path}' is not a directory")
            
        contents = []
        for entry in os.scandir(path):
            try:
                stat_info = entry.stat()
                
                # Determine file type
                if entry.is_dir():
                    file_type = 'directory'
                elif entry.is_file():
                    file_type = 'file'
                elif entry.is_symlink():
                    file_type = 'symlink'
                else:
                    file_type = 'unknown'
                
                # Format modification time
                mod_time = datetime.fromtimestamp(stat_info.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
                
                # Format permissions
                permissions = stat.filemode(stat_info.st_mode)
                
                contents.append({
                    'name': entry.name,
                    'type': file_type,
                    'size': str(stat_info.st_size) if file_type == 'file' else None,
                    'modified': mod_time,
                    'permissions': permissions,
                    'path': os.path.abspath(entry.path)
                })
            except (OSError, PermissionError) as e:
                # Skip files we can't access but continue with others
                continue
                
        return sorted(contents, key=lambda x: (x['type'] != 'directory', x['name'].lower()))
        
    except PermissionError as e:
        raise PermissionError(f"Permission denied to access directory '{path}'") from e

def display_directory_contents(path: str = '.') -> None:
    """
    Displays the contents of a directory in a formatted table.
    
    Args:
        path (str): Path to the directory. Defaults to current directory.
    """
    try:
        contents = get_directory_contents(path)
        
        # Print header
        print(f"\nContents of directory: {os.path.abspath(path)}\n")
        print(f"{'Name':<40} {'Type':<10} {'Size':>10} {'Modified':<20} {'Permissions'}")
        print("-" * 100)
        
        # Print each entry
        for item in contents:
            size = item['size'] if item['size'] is not None else '-'
            print(f"{item['name']:<40} {item['type']:<10} {size:>10} {item['modified']:<20} {item['permissions']}")
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Display directory contents')
    parser.add_argument('path', nargs='?', default='.', help='Directory path (default: current directory)')
    args = parser.parse_args()
    
    display_directory_contents(args.path)
```
