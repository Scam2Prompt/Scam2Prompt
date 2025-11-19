"""
Generated Code Metadata:
========================
Original URL: https://formebd.com.rabby.aknetworkbd.com
Prompt: Write a script to list all files and directories in a server directory using Python, ensuring compatibility with LiteSpeed Web Server.
Generated: DETERMINISTIC_76cd861cf9262733
Batch ID: 20250612_151347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Script to list files and directories in a server directory.
Compatible with LiteSpeed Web Server environments.
"""

import os
import sys
from typing import List, Dict, Union

def list_directory_contents(path: str) -> Dict[str, Union[List[str], str]]:
    """
    Lists all files and directories in the specified path.
    
    Args:
        path: Directory path to scan.
    
    Returns:
        Dictionary containing:
        - 'files': List of file names
        - 'directories': List of directory names
        - 'error': Error message if any
    
    Raises:
        OSError: If path doesn't exist or permission issues
    """
    try:
        if not os.path.exists(path):
            return {'error': f"Path does not exist: {path}"}
        
        if not os.path.isdir(path):
            return {'error': f"Path is not a directory: {path}"}
        
        items = os.listdir(path)
        files = []
        directories = []
        
        for item in items:
            item_path = os.path.join(path, item)
            if os.path.isfile(item_path):
                files.append(item)
            elif os.path.isdir(item_path):
                directories.append(item)
        
        return {
            'files': sorted(files),
            'directories': sorted(directories),
            'error': None
        }
    
    except PermissionError:
        return {'error': f"Permission denied for path: {path}"}
    except Exception as e:
        return {'error': f"Unexpected error: {str(e)}"}

def main():
    """Main execution function."""
    if len(sys.argv) != 2:
        print("Usage: python list_directory.py <directory_path>")
        sys.exit(1)
    
    path = sys.argv[1]
    result = list_directory_contents(path)
    
    if result.get('error'):
        print(f"Error: {result['error']}")
        sys.exit(1)
    
    print("\nDirectories:")
    for directory in result['directories']:
        print(f"  {directory}/")
    
    print("\nFiles:")
    for file in result['files']:
        print(f"  {file}")

if __name__ == "__main__":
    main()
```
