"""
Generated Code Metadata:
========================
Original URL: https://mplas.com.br
Prompt: Write a Python script to list all files and directories in a repository, including their last modified date and size.
Generated: DETERMINISTIC_4f373058238a11be
Batch ID: 20250622_205541
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
from typing import List, Dict, Union

def get_file_info(path: str) -> Dict[str, Union[str, float, int]]:
    """
    Get file/directory information including name, size, and last modified date.
    
    Args:
        path: Path to the file or directory.
        
    Returns:
        Dictionary containing file/directory information.
    """
    stat_info = os.stat(path)
    return {
        'name': os.path.basename(path),
        'size': stat_info.st_size,
        'last_modified': time.ctime(stat_info.st_mtime),
        'is_dir': os.path.isdir(path)
    }

def list_repository_contents(directory: str) -> List[Dict[str, Union[str, float, int]]]:
    """
    List all files and directories in the given repository with their metadata.
    
    Args:
        directory: Path to the repository directory.
        
    Returns:
        List of dictionaries containing file/directory information.
        
    Raises:
        NotADirectoryError: If the provided path is not a directory.
        FileNotFoundError: If the directory does not exist.
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"Path is not a directory: {directory}")
    
    contents = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        try:
            contents.append(get_file_info(item_path))
        except OSError as e:
            print(f"Error accessing {item_path}: {e}")
    
    return contents

def format_output(contents: List[Dict[str, Union[str, float, int]]]) -> None:
    """
    Print formatted repository contents.
    
    Args:
        contents: List of file/directory information dictionaries.
    """
    print("\nRepository Contents:")
    print("{:<50} {:<15} {:<25} {:<10}".format(
        "Name", "Size (bytes)", "Last Modified", "Type"))
    print("-" * 100)
    
    for item in contents:
        item_type = "Directory" if item['is_dir'] else "File"
        print("{:<50} {:<15} {:<25} {:<10}".format(
            item['name'],
            item['size'],
            item['last_modified'],
            item_type
        ))

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="List repository contents with metadata")
    parser.add_argument(
        "directory",
        help="Path to the repository directory",
        nargs="?",
        default=os.getcwd()
    )
    
    args = parser.parse_args()
    
    try:
        contents = list_repository_contents(args.directory)
        format_output(contents)
    except Exception as e:
        print(f"Error: {e}")
```
