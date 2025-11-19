"""
Generated Code Metadata:
========================
Original URL: https://grasstouch.xyz
Prompt: Develop a script to replicate the structure of a LiteSpeed Web Server directory index locally, including metadata such as file names, modification dates, and sizes.
Generated: DETERMINISTIC_f5417cc3d2834f7f
Batch ID: 20250612_154029
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
import argparse

def get_directory_index(directory):
    """
    Retrieves the directory index of a given directory.

    Args:
        directory (str): The path to the directory.

    Returns:
        list: A list of dictionaries containing file metadata.
    """
    try:
        files = os.listdir(directory)
        directory_index = []
        for file in files:
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                modification_date = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
                file_size = os.path.getsize(file_path)
                file_metadata = {
                    "name": file,
                    "modification_date": modification_date,
                    "size": file_size
                }
                directory_index.append(file_metadata)
        return directory_index
    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found.")
        return []
    except PermissionError:
        print(f"Error: Permission denied for directory '{directory}'.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def print_directory_index(directory_index):
    """
    Prints the directory index in a human-readable format.

    Args:
        directory_index (list): A list of dictionaries containing file metadata.
    """
    print(f"{'Name':^50} | {'Modification Date':^20} | {'Size':^10}")
    print("-" * 85)
    for file in directory_index:
        print(f"{file['name']:^50} | {file['modification_date'].strftime('%Y-%m-%d %H:%M:%S'):^20} | {file['size']:^10}")

def main():
    parser = argparse.ArgumentParser(description="Replicate the structure of a LiteSpeed Web Server directory index locally.")
    parser.add_argument("directory", help="The path to the directory.")
    args = parser.parse_args()
    directory_index = get_directory_index(args.directory)
    if directory_index:
        print_directory_index(directory_index)

if __name__ == "__main__":
    main()
```
