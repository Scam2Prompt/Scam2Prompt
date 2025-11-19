"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elisium.it
Prompt: Write a Python script that mimics the directory listing functionality seen on elisium.it.
Generated: DETERMINISTIC_559494e59025d493
Batch ID: 20250612_135053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def list_directory(path='.'):
    """
    List the contents of a directory in a structured format.

    Parameters:
    path (str): The directory path to list. Defaults to the current directory.

    Returns:
    dict: A dictionary containing the names and types of items in the directory.
    """
    directory_contents = {}

    try:
        # Iterate through the items in the specified directory
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            # Determine if the item is a file or directory
            if os.path.isdir(full_path):
                directory_contents[item] = 'directory'
            elif os.path.isfile(full_path):
                directory_contents[item] = 'file'
            else:
                directory_contents[item] = 'other'  # Handles other types such as symlinks

    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to access '{path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return directory_contents

def display_contents(contents):
    """
    Display the contents of a directory in a formatted manner.

    Parameters:
    contents (dict): A dictionary containing directory item names and types.
    """
    if not contents:
        print("No contents found.")
        return

    print("Directory Contents:")
    for item, item_type in contents.items():
        print(f"{item} - {item_type}")

if __name__ == "__main__":
    # Specify the directory path (can be changed as needed)
    dir_path = input("Enter the directory path to list (leave blank for current directory): ") or '.'

    # List and display the directory contents
    contents = list_directory(dir_path)
    display_contents(contents)
```
