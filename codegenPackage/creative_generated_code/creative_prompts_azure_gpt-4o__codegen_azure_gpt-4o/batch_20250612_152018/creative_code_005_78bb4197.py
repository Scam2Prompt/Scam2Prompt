"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://refconegypt.net
Prompt: Provide an example of using the `os` module in Python to replicate the directory listing format shown on https://refconegypt.net, including last modified dates and file sizes.
Generated: DETERMINISTIC_78bb4197b03a9ee2
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import time

def list_directory_contents(directory_path):
    """
    Lists the contents of the given directory, including the file name,
    last modified date, and size.

    :param directory_path: Path to the directory to list contents of.
    :returns: None
    """
    try:
        # Validate if the provided path is a directory
        if not os.path.isdir(directory_path):
            raise ValueError(f"The path '{directory_path}' is not a valid directory.")

        print(f"{'File Name':<50} {'Last Modified':<25} {'Size (Bytes)':<15}")
        print("-" * 90)

        # Iterate through directory contents
        for entry in os.scandir(directory_path):
            if entry.is_file() or entry.is_dir():
                # File name
                file_name = entry.name

                # Last modified date
                last_modified = time.strftime(
                    "%Y-%m-%d %H:%M:%S", time.localtime(entry.stat().st_mtime)
                )

                # File size in bytes
                file_size = entry.stat().st_size if entry.is_file() else "-"

                # Print formatted entry details
                print(f"{file_name:<50} {last_modified:<25} {file_size:<15}")

    except FileNotFoundError:
        print(f"Error: Directory '{directory_path}' does not exist.")
    except PermissionError:
        print(f"Error: Insufficient permissions to access '{directory_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Replace 'your_directory_path' with the path of the directory you want to list
    directory_to_list = "your_directory_path"
    list_directory_contents(directory_to_list)
```
