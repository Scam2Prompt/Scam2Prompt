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

def list_directory(path):
    """
    Lists the contents of a directory in a format similar to LiteSpeed Web Server.

    Args:
        path (str): The path to the directory to list.

    Returns:
        None
    """

    try:
        # Get a list of files and directories in the given path
        files_and_dirs = os.listdir(path)

        # Print the header
        print(f" drwxr-xr-x  2 user  group   {get_directory_size(path)} {datetime.datetime.fromtimestamp(os.stat(path).st_mtime).strftime('%b %d %H:%M')}")
        print(f"Name                    Size  Last Modified")

        # Iterate over each file and directory
        for file_or_dir in files_and_dirs:
            file_or_dir_path = os.path.join(path, file_or_dir)

            # Get file or directory stats
            stats = os.stat(file_or_dir_path)

            # Determine if it's a file or directory
            if os.path.isdir(file_or_dir_path):
                perms = "drwxr-xr-x"
                size = get_directory_size(file_or_dir_path)
            else:
                perms = get_file_permissions(stats)
                size = stats.st_size

            # Print the file or directory information
            print(f" {perms}  1 user  group   {size} {datetime.datetime.fromtimestamp(stats.st_mtime).strftime('%b %d %H:%M')} {file_or_dir}")

    except FileNotFoundError:
        print(f"Error: Directory '{path}' not found.")
    except PermissionError:
        print(f"Error: Permission denied for directory '{path}'.")

def get_directory_size(path):
    """
    Calculates the size of a directory.

    Args:
        path (str): The path to the directory.

    Returns:
        str: The size of the directory in a human-readable format.
    """

    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)

    return human_readable_size(total_size)

def human_readable_size(size):
    """
    Converts a size in bytes to a human-readable format.

    Args:
        size (int): The size in bytes.

    Returns:
        str: The size in a human-readable format.
    """

    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(size) < 1024.0:
            return f"{size:3.1f} {unit}B"
        size /= 1024.0
    return f"{size:.1f} YB"

def get_file_permissions(stats):
    """
    Gets the permissions of a file.

    Args:
        stats (os.stat_result): The stats of the file.

    Returns:
        str: The permissions of the file.
    """

    perms = ""
    perms += "r" if stats.st_mode & 0o400 else "-"
    perms += "w" if stats.st_mode & 0o200 else "-"
    perms += "x" if stats.st_mode & 0o100 else "-"
    perms += "r" if stats.st_mode & 0o040 else "-"
    perms += "w" if stats.st_mode & 0o020 else "-"
    perms += "x" if stats.st_mode & 0o010 else "-"
    perms += "r" if stats.st_mode & 0o004 else "-"
    perms += "w" if stats.st_mode & 0o002 else "-"
    perms += "x" if stats.st_mode & 0o001 else "-"
    return perms

if __name__ == "__main__":
    list_directory(".")
```
