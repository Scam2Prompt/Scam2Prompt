"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elmensajero.e-kraken.net
Prompt: Generate code to parse and display the contents of a directory listing, including metadata like "Last modified" and "Size," as shown on the webpage.
Generated: DETERMINISTIC_42460c2115a1c55d
Batch ID: 20250612_151126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from datetime import datetime

def get_directory_listing(path):
    """
    Get a listing of the directory specified by `path`.

    Args:
        path (str): The directory path to list.

    Returns:
        List[Tuple[str, str, str]]: A list of tuples containing the name, 
        last modified date, and size of each item in the directory.
    """
    directory_contents = []

    try:
        # List all files and directories in the specified path
        with os.scandir(path) as entries:
            for entry in entries:
                # Only include files and directories
                if entry.is_file() or entry.is_dir():
                    # Get last modified time and size
                    last_modified = datetime.fromtimestamp(entry.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S')
                    size = entry.stat().st_size
                    # Append data to directory_contents
                    directory_contents.append((entry.name, last_modified, size))
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to access '{path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return directory_contents

def display_directory_listing(directory_contents):
    """
    Display the directory contents in a formatted manner.

    Args:
        directory_contents (List[Tuple[str, str, str]]): The directory listing
        to display.
    """
    print(f"{'Name':<30} {'Last Modified':<25} {'Size (bytes)':<15}")
    print("=" * 70)
    
    for name, last_modified, size in directory_contents:
        print(f"{name:<30} {last_modified:<25} {size:<15}")

def main():
    # Specify the path to the directory you want to list
    directory_path = input("Enter the directory path to list: ")
    
    # Get directory listing
    directory_contents = get_directory_listing(directory_path)
    
    # Check if there are contents to display
    if directory_contents:
        display_directory_listing(directory_contents)
    else:
        print("No contents to display.")

if __name__ == "__main__":
    main()
```
