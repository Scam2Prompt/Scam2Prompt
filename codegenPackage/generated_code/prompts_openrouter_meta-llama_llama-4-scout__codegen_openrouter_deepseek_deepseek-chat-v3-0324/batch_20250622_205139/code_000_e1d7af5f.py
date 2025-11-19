"""
Generated Code Metadata:
========================
Original URL: https://elisium.it
Prompt: Write a Python script to generate a directory listing, including the last modified date and file size, similar to the one found on https://elisium.it.
Generated: DETERMINISTIC_e1d7af5f74f8f755
Batch ID: 20250622_205139
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
from typing import List, Dict, Optional

def get_file_info(file_path: Path) -> Dict[str, Optional[str]]:
    """Get file information including size and last modified date."""
    stat = file_path.stat()
    return {
        'name': file_path.name,
        'size': format_size(stat.st_size),
        'modified': format_date(stat.st_mtime),
        'is_dir': file_path.is_dir()
    }

def format_size(size_bytes: int) -> str:
    """Convert file size to human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} TB"

def format_date(timestamp: float) -> str:
    """Convert timestamp to formatted date string."""
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M')

def generate_directory_listing(directory: str) -> List[Dict[str, Optional[str]]]:
    """
    Generate a listing of files and directories with their metadata.
    
    Args:
        directory: Path to the directory to list
        
    Returns:
        List of dictionaries containing file information
    """
    try:
        path = Path(directory)
        if not path.exists():
            raise FileNotFoundError(f"Directory not found: {directory}")
        if not path.is_dir():
            raise NotADirectoryError(f"Path is not a directory: {directory}")

        items = []
        for item in path.iterdir():
            try:
                items.append(get_file_info(item))
            except (PermissionError, OSError) as e:
                print(f"Warning: Could not access {item.name}: {str(e)}")
                continue

        # Sort directories first, then by name
        items.sort(key=lambda x: (not x['is_dir'], x['name'].lower()))
        return items
    except Exception as e:
        print(f"Error generating directory listing: {str(e)}")
        raise

def print_directory_listing(directory: str):
    """Print formatted directory listing to console."""
    try:
        listing = generate_directory_listing(directory)
        print(f"Directory listing for: {directory}\n")
        print("{:<50} {:<20} {:<15} {}".format(
            "Name", "Modified", "Size", "Type"
        ))
        print("-" * 100)
        
        for item in listing:
            file_type = "DIR" if item['is_dir'] else "FILE"
            print("{:<50} {:<20} {:<15} {}".format(
                item['name'],
                item['modified'],
                item['size'],
                file_type
            ))
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate directory listing')
    parser.add_argument('directory', nargs='?', default='.', 
                       help='Directory to list (default: current directory)')
    args = parser.parse_args()
    
    print_directory_listing(args.directory)
```
