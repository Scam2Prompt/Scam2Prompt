"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartd.org.ls
Prompt: Write a script to programmatically list all files and directories in a server directory, similar to the structure shown at https://smartd.org.ls.
Generated: DETERMINISTIC_8e87ec81120ba9e6
Batch ID: 20250612_151853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def list_files_and_directories(path):
    """
    Recursively lists all files and directories in the given path.

    Args:
        path (str): The starting directory path.

    Returns:
        dict: A nested dictionary representing the file and directory structure.
    """
    try:
        structure = {}
        for entry in os.scandir(path):
            if entry.is_dir():
                # If the entry is a directory, recursively call the function
                structure[entry.name] = list_files_and_directories(entry.path)
            else:
                # If the entry is a file, add it to the structure
                structure[entry.name] = None
        return structure
    except FileNotFoundError as e:
        print(f"Error: The directory '{path}' was not found.")
        return {}
    except PermissionError as e:
        print(f"Error: Permission denied to access '{path}'.")
        return {}

def print_structure(structure, indent=0):
    """
    Prints the file and directory structure in a readable format.

    Args:
        structure (dict): The file and directory structure.
        indent (int): The current indentation level (used for recursive formatting).
    """
    for name, content in structure.items():
        print("  " * indent + f"- {name}")
        if isinstance(content, dict):
            # If the content is a dictionary, recursively print its contents
            print_structure(content, indent + 1)

if __name__ == "__main__":
    # Define the directory path you want to list
    directory_path = "/path/to/server/directory"  # Change this to the target path
    
    print("Listing files and directories:")
    # Get the structure of the directory
    dir_structure = list_files_and_directories(directory_path)
    
    # Print the directory structure
    print_structure(dir_structure)
```

### Usage:
1. Replace `/path/to/server/directory` in the code with the actual directory path you want to list.
2. Run the script. It will recursively list all files and subdirectories in a readable format.
