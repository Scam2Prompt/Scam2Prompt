"""
Generated Code Metadata:
========================
Original URL: https://stelax.io
Prompt: Write a script that retrieves and displays directory contents, inspired by the index structure of stelax.io.
Generated: DETERMINISTIC_d2be1b0c66b3f8a0
Batch ID: 20250612_162728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import argparse
from datetime import datetime

def get_directory_contents(path):
    """
    Retrieves and displays directory contents.

    Args:
        path (str): The path to the directory.

    Returns:
        dict: A dictionary containing the directory contents.
    """
    try:
        # Check if the path exists and is a directory
        if not os.path.exists(path) or not os.path.isdir(path):
            raise FileNotFoundError(f"The path '{path}' does not exist or is not a directory.")

        # Initialize an empty dictionary to store directory contents
        contents = {
            "files": [],
            "directories": [],
            "metadata": {
                "path": path,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        }

        # Iterate over each item in the directory
        for item in os.listdir(path):
            item_path = os.path.join(path, item)

            # Check if the item is a file
            if os.path.isfile(item_path):
                contents["files"].append({
                    "name": item,
                    "size": os.path.getsize(item_path),
                    "modified": datetime.fromtimestamp(os.path.getmtime(item_path)).strftime("%Y-%m-%d %H:%M:%S")
                })
            # Check if the item is a directory
            elif os.path.isdir(item_path):
                contents["directories"].append({
                    "name": item,
                    "modified": datetime.fromtimestamp(os.path.getmtime(item_path)).strftime("%Y-%m-%d %H:%M:%S")
                })

        return contents

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def print_directory_contents(contents):
    """
    Prints the directory contents in a formatted manner.

    Args:
        contents (dict): A dictionary containing the directory contents.
    """
    if contents is not None:
        print(f"Directory: {contents['metadata']['path']}")
        print(f"Timestamp: {contents['metadata']['timestamp']}\n")

        print("Files:")
        for file in contents["files"]:
            print(f"- {file['name']} (Size: {file['size']} bytes, Modified: {file['modified']})")

        print("\nDirectories:")
        for directory in contents["directories"]:
            print(f"- {directory['name']} (Modified: {directory['modified']})")


def main():
    parser = argparse.ArgumentParser(description="Retrieve and display directory contents.")
    parser.add_argument("path", help="The path to the directory.")
    args = parser.parse_args()

    contents = get_directory_contents(args.path)
    print_directory_contents(contents)


if __name__ == "__main__":
    main()
```
