"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://formebd.com.rabby.aknetworkbd.com
Prompt: Provide an example of using Python's `os` module to replicate the directory listing format shown on a LiteSpeed Web Server.
Generated: DETERMINISTIC_c6e7956463fe1bcb
Batch ID: 20250612_151347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import datetime

def format_time(timestamp):
    """Format the timestamp to a human-readable format."""
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def list_directory(path):
    """
    List the contents of a directory in a format similar to LiteSpeed Web Server.

    Args:
        path (str): The directory path to list.

    Returns:
        None
    """
    try:
        # Check if the path is a directory
        if not os.path.isdir(path):
            raise ValueError(f"The specified path '{path}' is not a directory.")

        # Retrieve the directory contents
        entries = os.listdir(path)

        # Print header
        print(f"Directory listing for: {path}\n")
        print(f"{'Permissions':<12} {'Size (bytes)':<14} {'Date Modified':<20} {'Name':<30}")
        print("=" * 80)

        # Iterate through each entry in the directory
        for entry in entries:
            entry_path = os.path.join(path, entry)
            entry_info = os.stat(entry_path)

            # Get permissions in a readable format
            permissions = oct(entry_info.st_mode)[-3:]

            # Get size, modification time, and name
            size = entry_info.st_size
            modified_time = format_time(entry_info.st_mtime)
            name = entry

            # Print formatted entry
            print(f"{permissions:<12} {size:<14} {modified_time:<20} {name:<30}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except FileNotFoundError:
        print(f"Error: The directory '{path}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when accessing '{path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Specify the directory to list (change it to the desired path)
    directory_path = 'your/directory/path/here'
    list_directory(directory_path)
```
