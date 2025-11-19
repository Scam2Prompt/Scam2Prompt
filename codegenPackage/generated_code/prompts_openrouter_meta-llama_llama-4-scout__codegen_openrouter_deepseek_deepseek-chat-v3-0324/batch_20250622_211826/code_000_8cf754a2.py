"""
Generated Code Metadata:
========================
Original URL: https://spadaro.id.au
Prompt: "Write a Python script to generate a directory listing with last modified date and file size, similar to the one found on spadaro.id.au."
Generated: DETERMINISTIC_8cf754a2dcfabd56
Batch ID: 20250622_211826
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
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} PB"

def generate_directory_listing(directory_path, output_file=None):
    """
    Generate a directory listing with last modified date and file size.
    
    Args:
        directory_path (str): Path to the directory to list
        output_file (str, optional): File to write the output to. Defaults to None (prints to console).
    """
    try:
        path = Path(directory_path)
        if not path.is_dir():
            raise NotADirectoryError(f"{directory_path} is not a valid directory")
        
        entries = []
        for entry in path.iterdir():
            stat = entry.stat()
            modified_time = datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M')
            size = format_size(stat.st_size) if entry.is_file() else "-"
            name = entry.name + "/" if entry.is_dir() else entry.name
            entries.append((modified_time, size, name))
        
        # Sort directories first, then files, both alphabetically
        entries.sort(key=lambda x: (not x[2].endswith('/'), x[2].lower()))
        
        # Generate the output
        output = []
        output.append(f"Directory listing for {path.resolve()}\n")
        output.append("Last Modified      Size     Name")
        output.append("------------------ -------- --------------------")
        
        for modified_time, size, name in entries:
            output.append(f"{modified_time}  {size:8}  {name}")
        
        result = '\n'.join(output)
        
        if output_file:
            try:
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(result)
                print(f"Directory listing saved to {output_file}")
            except IOError as e:
                print(f"Error writing to file: {e}")
        else:
            print(result)
            
    except Exception as e:
        print(f"Error generating directory listing: {e}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate a directory listing with last modified dates and file sizes.')
    parser.add_argument('directory', help='Directory to list')
    parser.add_argument('-o', '--output', help='Output file path (optional)')
    
    args = parser.parse_args()
    
    generate_directory_listing(args.directory, args.output)
```
