"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://initia.org.in
Prompt: Generate a Python script to list all files in a directory, similar to the structure shown on https://initia.org.in.
Generated: DETERMINISTIC_b75be257f9f59b21
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def list_files_in_directory(directory_path):
    """
    List all files in the specified directory, including subdirectories.

    Args:
        directory_path (str): The path to the directory to list files from.

    Returns:
        list: A list of file paths found in the directory and subdirectories.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
        PermissionError: If permission is denied to access the directory or its contents.
    """
    files_list = []

    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")

    if not os.path.isdir(directory_path):
        raise NotADirectoryError(f"The path '{directory_path}' is not a directory.")

    try:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                # Create the full path to the file
                full_path = os.path.join(root, file)
                files_list.append(full_path)

    except PermissionError as e:
        raise PermissionError(f"Permission denied while accessing '{directory_path}': {str(e)}")

    return files_list

def main():
    # Specify the directory to list files from
    directory_to_list = input("Enter the directory path to list files: ")

    try:
        files = list_files_in_directory(directory_to_list)
        if files:
            print("Files found:")
            for file in files:
                print(file)
        else:
            print("No files found in the specified directory.")
    except (FileNotFoundError, NotADirectoryError, PermissionError) as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
