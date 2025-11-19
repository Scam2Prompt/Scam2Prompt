"""
Generated Code Metadata:
========================
Original URL: https://initia.org.in
Prompt: Generate a Python script to list all files in a directory, similar to the structure shown on https://initia.org.in.
Generated: DETERMINISTIC_b75be257f9f59b21
Batch ID: 20250612_151605
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
from typing import List, Dict, Optional
import json
import argparse

def get_file_info(directory: str) -> List[Dict[str, Optional[str]]]:
    """
    Get information about all files in a directory.
    
    Args:
        directory: Path to the directory to scan.
    
    Returns:
        List of dictionaries containing file information (name, path, size, type).
    """
    file_list = []
    try:
        for entry in os.scandir(directory):
            file_info = {
                'name': entry.name,
                'path': entry.path,
                'size': entry.stat().st_size if entry.is_file() else None,
                'type': 'file' if entry.is_file() else 'directory'
            }
            file_list.append(file_info)
    except PermissionError:
        print(f"Permission denied: {directory}")
    except FileNotFoundError:
        print(f"Directory not found: {directory}")
    except Exception as e:
        print(f"Error scanning directory {directory}: {str(e)}")
    
    return file_list

def format_output(file_list: List[Dict[str, Optional[str]]], output_format: str = 'text') -> str:
    """
    Format the file list output based on the requested format.
    
    Args:
        file_list: List of file information dictionaries.
        output_format: Desired output format ('text', 'json').
    
    Returns:
        Formatted output string.
    """
    if output_format == 'json':
        return json.dumps(file_list, indent=2)
    else:
        output = []
        for file_info in file_list:
            output.append(
                f"{file_info['type'].upper().ljust(10)} {file_info['size'] or '':<10} {file_info['name']}"
            )
        return '\n'.join(output)

def main():
    parser = argparse.ArgumentParser(description='List files in a directory.')
    parser.add_argument('directory', help='Directory to list files from')
    parser.add_argument('--format', choices=['text', 'json'], default='text',
                       help='Output format (text or json)')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.directory):
        print(f"Error: Directory '{args.directory}' does not exist.")
        return
    
    file_list = get_file_info(args.directory)
    print(format_output(file_list, args.format))

if __name__ == '__main__':
    main()
```
