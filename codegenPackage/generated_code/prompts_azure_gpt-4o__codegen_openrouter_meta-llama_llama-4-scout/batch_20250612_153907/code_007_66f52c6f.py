"""
Generated Code Metadata:
========================
Original URL: https://consejodigitalmx.com
Prompt: Recommend a library or tool for analyzing directory structures like the one shown in `Index of /`, and demonstrate its usage in a code snippet.
Generated: DETERMINISTIC_66f52c6ff72109db
Batch ID: 20250612_153907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import pathlib
from typing import Dict, List

def analyze_directory_structure(directory_path: str) -> Dict[str, List[str]]:
    """
    Analyzes a directory structure and returns a dictionary representing the structure.

    Args:
    directory_path (str): The path to the directory to analyze.

    Returns:
    Dict[str, List[str]]: A dictionary representing the directory structure.
    """

    # Initialize an empty dictionary to store the directory structure
    directory_structure = {}

    try:
        # Iterate over each item in the directory
        for item in os.listdir(directory_path):
            # Construct the full path to the item
            item_path = os.path.join(directory_path, item)

            # Check if the item is a file or directory
            if os.path.isfile(item_path):
                # If it's a file, add it to the dictionary with a 'file' type
                directory_structure.setdefault('files', []).append(item)
            elif os.path.isdir(item_path):
                # If it's a directory, recursively analyze its structure
                subdirectory_structure = analyze_directory_structure(item_path)
                directory_structure[item] = subdirectory_structure

    except FileNotFoundError:
        print(f"Error: Directory '{directory_path}' not found.")
    except PermissionError:
        print(f"Error: Permission denied for directory '{directory_path}'.")

    return directory_structure


def print_directory_structure(directory_structure: Dict[str, List[str]], indent: int = 0) -> None:
    """
    Prints a directory structure in a human-readable format.

    Args:
    directory_structure (Dict[str, List[str]]): The directory structure to print.
    indent (int): The indentation level (default is 0).
    """

    for key, value in directory_structure.items():
        if isinstance(value, dict):
            print('  ' * indent + str(key) + '/')
            print_directory_structure(value, indent + 1)
        else:
            for item in value:
                print('  ' * indent + item)


def main() -> None:
    directory_path = '/path/to/directory'
    directory_structure = analyze_directory_structure(directory_path)
    print_directory_structure(directory_structure)


if __name__ == "__main__":
    main()
```
