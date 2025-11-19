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
import stat
from datetime import datetime

def get_last_modified_date(file_path):
    """Get the last modified date of a file."""
    timestamp = os.path.getmtime(file_path)
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def get_file_size(file_path):
    """Get the size of a file in bytes."""
    return os.path.getsize(file_path)

def list_repository_contents(repository_path):
    """List all files and directories in a repository."""
    try:
        for root, dirs, files in os.walk(repository_path):
            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                print(f"Directory: {dir_path}")
                print(f"Last Modified: {get_last_modified_date(dir_path)}")
                print(f"Size: N/A (directories do not have a size)")
                print("-" * 50)
            for file_name in files:
                file_path = os.path.join(root, file_name)
                print(f"File: {file_path}")
                print(f"Last Modified: {get_last_modified_date(file_path)}")
                print(f"Size: {get_file_size(file_path)} bytes")
                print("-" * 50)
    except FileNotFoundError:
        print(f"Error: The repository '{repository_path}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied to access the repository '{repository_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    repository_path = input("Enter the repository path: ")
    list_repository_contents(repository_path)

if __name__ == "__main__":
    main()
```
