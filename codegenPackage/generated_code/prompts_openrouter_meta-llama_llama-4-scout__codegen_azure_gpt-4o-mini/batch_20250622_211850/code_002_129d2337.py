"""
Generated Code Metadata:
========================
Original URL: https://www.flare-networks.xyz
Prompt: Write a script to list the files in a directory, similar to the directory listing shown for the Flare Networks server.
Generated: DETERMINISTIC_129d23374a90697e
Batch ID: 20250622_211850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os

def list_files_in_directory(directory_path):
    """
    Lists all files and directories in the specified directory.

    Args:
        directory_path (str): The path of the directory to list files from.

    Returns:
        list: A list of files and directories in the specified directory.

    Raises:
        ValueError: If the provided path is not a directory.
        FileNotFoundError: If the directory does not exist.
    """
    # Check if the provided path exists
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")
    
    # Check if the provided path is a directory
    if not os.path.isdir(directory_path):
        raise ValueError(f"The path '{directory_path}' is not a directory.")

    # List to hold the names of files and directories
    files_and_dirs = []

    # Iterate through the directory and collect file and directory names
    for entry in os.listdir(directory_path):
        full_path = os.path.join(directory_path, entry)
        if os.path.isfile(full_path):
            files_and_dirs.append(f"File: {entry}")
        elif os.path.isdir(full_path):
            files_and_dirs.append(f"Directory: {entry}")

    return files_and_dirs

def main():
    """
    Main function to execute the script.
    """
    # Specify the directory to list
    directory_to_list = input("Enter the directory path to list files: ")

    try:
        # Get the list of files and directories
        items = list_files_in_directory(directory_to_list)
        print("\nContents of the directory:")
        for item in items:
            print(item)
    except (ValueError, FileNotFoundError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
