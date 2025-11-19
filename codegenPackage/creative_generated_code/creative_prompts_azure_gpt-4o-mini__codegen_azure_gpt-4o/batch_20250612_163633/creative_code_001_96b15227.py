"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecataloguegoodies-pepsico.com
Prompt: Write a Python function that lists the contents of a directory similar to the index page of the eCatalog Goodies PepsiCo site.
Generated: DETERMINISTIC_96b15227832661a5
Batch ID: 20250612_163633
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

def list_directory_contents(directory_path):
    """
    Lists the contents of a directory, similar to an index page, displaying
    filenames, sizes, and modification dates.

    Args:
        directory_path (str): The path to the directory to list.

    Returns:
        list: A list of dictionaries containing file details.
    """
    try:
        # Validate the directory path
        if not os.path.isdir(directory_path):
            raise ValueError(f"The path '{directory_path}' is not a valid directory.")
        
        # Retrieve directory contents
        contents = os.listdir(directory_path)
        
        # Prepare a list to hold file information
        file_info_list = []

        for item in contents:
            item_path = os.path.join(directory_path, item)
            # Gather information about each file/directory
            file_info = {
                "name": item,  # File or directory name
                "is_directory": os.path.isdir(item_path),  # True if it's a directory
                "size": os.path.getsize(item_path) if os.path.isfile(item_path) else None,  # Size in bytes
                "last_modified": datetime.fromtimestamp(os.path.getmtime(item_path))  # Modification date
            }
            file_info_list.append(file_info)

        # Sort the list by name (case-insensitive)
        file_info_list.sort(key=lambda x: x["name"].lower())
        
        return file_info_list

    except Exception as e:
        # Handle any errors and print a user-friendly message
        print(f"Error listing directory contents: {e}")
        return []

# Example usage:
if __name__ == "__main__":
    directory_path = "./"  # Specify a directory here
    contents = list_directory_contents(directory_path)
    for item in contents:
        print(f"Name: {item['name']}, Is Directory: {item['is_directory']}, "
              f"Size: {item['size']} bytes, Last Modified: {item['last_modified']}")
```
