"""
Generated Code Metadata:
========================
Original URL: https://infrastructure.bincom.net
Prompt: Write code to programmatically list and parse the contents of a directory from a server, similar to the structure shown at https://infrastructure.bincom.net.
Generated: DETERMINISTIC_12f662ac002a668d
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Directory Lister and Parser**
=====================================

**Python Implementation**
------------------------

```python
import os
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def list_directory_contents(directory_path):
    """
    Lists the contents of a directory.

    Args:
        directory_path (str): The path to the directory.

    Returns:
        list: A list of directory contents.

    Raises:
        FileNotFoundError: If the directory does not exist.
        NotADirectoryError: If the path is not a directory.
    """
    try:
        # Check if the directory exists
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")

        # Check if the path is a directory
        if not os.path.isdir(directory_path):
            raise NotADirectoryError(f"The path '{directory_path}' is not a directory.")

        # List the directory contents
        contents = os.listdir(directory_path)
        return contents

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return []

def parse_directory_contents(directory_path):
    """
    Parses the contents of a directory.

    Args:
        directory_path (str): The path to the directory.

    Returns:
        dict: A dictionary containing the directory contents.

    Raises:
        FileNotFoundError: If the directory does not exist.
        NotADirectoryError: If the path is not a directory.
    """
    try:
        contents = list_directory_contents(directory_path)
        parsed_contents = {}

        # Iterate over the directory contents
        for item in contents:
            item_path = os.path.join(directory_path, item)

            # Check if the item is a file or directory
            if os.path.isfile(item_path):
                parsed_contents[item] = {"type": "file", "size": os.path.getsize(item_path)}
            elif os.path.isdir(item_path):
                parsed_contents[item] = {"type": "directory"}

        return parsed_contents

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return {}

if __name__ == "__main__":
    directory_path = "/path/to/directory"  # Replace with the desired directory path
    contents = list_directory_contents(directory_path)
    parsed_contents = parse_directory_contents(directory_path)

    print("Directory Contents:")
    for item in contents:
        print(item)

    print("\nParsed Directory Contents:")
    import json
    print(json.dumps(parsed_contents, indent=4))
```

**Example Use Case:**

Replace `"/path/to/directory"` with the desired directory path and run the script. The script will list and parse the contents of the directory, printing the results to the console.

**Notes:**

* Make sure to replace `"/path/to/directory"` with the actual directory path you want to list and parse.
* The `list_directory_contents` function returns a list of directory contents, while the `parse_directory_contents` function returns a dictionary containing the parsed directory contents.
* The script uses the `os` module for interacting with the file system and the `logging` module for error handling and logging.
* The script follows best practices for Python development, including proper error handling, documentation, and code organization.
