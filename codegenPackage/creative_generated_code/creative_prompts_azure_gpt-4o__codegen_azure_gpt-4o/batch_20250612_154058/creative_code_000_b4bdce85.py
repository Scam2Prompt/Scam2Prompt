"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbaseinfo.info
Prompt: Write a script to list all files in a directory, including their last modified date and size, similar to the "Index of /" structure displayed on a LiteSpeed Web Server.
Generated: DETERMINISTIC_b4bdce8550a0ef16
Batch ID: 20250612_154058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import sys
from datetime import datetime

def list_directory_contents(directory_path):
    """
    Lists all files and directories in the given directory with their
    last modified date and size.
    
    Args:
        directory_path (str): The path to the directory.

    Returns:
        None
    """
    try:
        # Check if the provided path is a valid directory
        if not os.path.exists(directory_path):
            print(f"Error: The directory '{directory_path}' does not exist.")
            return
        if not os.path.isdir(directory_path):
            print(f"Error: The path '{directory_path}' is not a directory.")
            return

        print(f"Index of {directory_path}\n")
        print(f"{'Name':<40} {'Last Modified':<25} {'Size (bytes)':<15}")
        print("-" * 80)

        # Iterate through each file/directory in the given directory
        for entry in os.scandir(directory_path):
            # Get name, last modified date, and size
            name = entry.name
            last_modified = datetime.fromtimestamp(entry.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S')
            size = entry.stat().st_size if entry.is_file() else '-'

            # Print formatted information
            print(f"{name:<40} {last_modified:<25} {size:<15}")

    except PermissionError:
        print(f"Error: Insufficient permissions to access '{directory_path}'.")
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")

if __name__ == "__main__":
    # Ensure the user provides a directory path as an argument
    if len(sys.argv) != 2:
        print("Usage: python list_directory.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        list_directory_contents(directory_path)
```
