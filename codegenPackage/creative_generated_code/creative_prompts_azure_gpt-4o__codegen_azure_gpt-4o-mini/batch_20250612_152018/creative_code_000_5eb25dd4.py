"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://refconegypt.net
Prompt: Write a Python script to list all files and directories in a server directory, similar to the structure shown on https://refconegypt.net.
Generated: DETERMINISTIC_5eb25dd41383943f
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

def list_files_and_directories(base_path):
    """
    List all files and directories in the specified directory structure.

    Args:
        base_path (str): The path to the directory to list.
    
    Returns:
        list: A list of tuples containing the directory path and the files/subdirectories in it.
    """
    directory_structure = []

    try:
        # Walk through the directory structure
        for dirpath, dirnames, filenames in os.walk(base_path):
            # Append the current directory and its contents to the result list
            directory_structure.append({
                'directory': dirpath,
                'files': filenames,
                'subdirectories': dirnames
            })

    except OSError as e:
        print(f"Error accessing the directory '{base_path}': {e}")
        return []

    return directory_structure

def print_structure(structure):
    """
    Print the structure of directories and files in a readable format.

    Args:
        structure (list): The directory structure to print.
    """
    for entry in structure:
        print(f"Directory: {entry['directory']}")
        if entry['subdirectories']:
            print("  Subdirectories:")
            for subdir in entry['subdirectories']:
                print(f"    - {subdir}")
        if entry['files']:
            print("  Files:")
            for file in entry['files']:
                print(f"    - {file}")
        print()  # Empty line for better readability

def main():
    """
    Main function to execute the directory listing script.
    """
    # Set the base path for the directory listing. Modify this as needed.
    base_path = '/path/to/your/directory'

    # Get the directory structure
    structure = list_files_and_directories(base_path)

    # Print the directory structure
    print_structure(structure)

if __name__ == "__main__":
    main()
```

Make sure to replace `'/path/to/your/directory'` with the actual path you want to explore.
