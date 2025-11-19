"""
Generated Code Metadata:
========================
Original URL: https://formebd.com.rabby.aknetworkbd.com
Prompt: Provide an example of using Python's `os` module to replicate the directory listing format shown on a LiteSpeed Web Server.
Generated: DETERMINISTIC_c6e7956463fe1bcb
Batch ID: 20250612_151347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import datetime

def format_size(size):
    """Convert a file size in bytes to a human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} PB"

def format_time(timestamp):
    """Format the timestamp into a human-readable string."""
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def list_directory(path):
    """List the contents of a directory in a format similar to LiteSpeed Web Server."""
    try:
        # Get the list of entries in the directory
        entries = os.listdir(path)
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
        return
    except PermissionError:
        print(f"Error: Permission denied to access '{path}'.")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    # Print the header
    print(f"{'Name':<30} {'Size':<10} {'Last Modified':<20}")
    print("=" * 60)

    # Iterate through the entries and print their details
    for entry in entries:
        entry_path = os.path.join(path, entry)
        try:
            # Get the size and last modified time
            size = os.path.getsize(entry_path)
            last_modified = os.path.getmtime(entry_path)

            # Format and print the entry details
            print(f"{entry:<30} {format_size(size):<10} {format_time(last_modified):<20}")
        except Exception as e:
            print(f"Error retrieving information for '{entry}': {e}")

if __name__ == "__main__":
    # Specify the directory to list
    directory_to_list = '.'  # Current directory
    list_directory(directory_to_list)
```
