"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grasstouch.xyz
Prompt: Write a script to list all files and directories from a LiteSpeed Web Server directory index, similar to the structure shown at https://grasstouch.xyz.
Generated: DETERMINISTIC_68ed50b329b39e12
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def list_files_and_directories(start_path):
    """
    List all files and directories from the specified path in a structured format.

    Args:
        start_path (str): The directory path to start the listing.

    Returns:
        list: A list of tuples where each tuple contains the directory name and a list of its files.
    """
    directory_structure = []

    # Verify that the given start_path exists and is a directory
    if not os.path.exists(start_path):
        raise FileNotFoundError(f"The path '{start_path}' does not exist.")
    if not os.path.isdir(start_path):
        raise NotADirectoryError(f"The path '{start_path}' is not a directory.")

    # Walk through the directory and subdirectories
    for root, dirs, files in os.walk(start_path):
        # Store current directory and its files
        current_dir = os.path.relpath(root, start_path)  # Get relative path
        directory_structure.append((current_dir, files))
    
    return directory_structure

def print_directory_structure(directory_structure):
    """
    Print the directory structure in a readable format.

    Args:
        directory_structure (list): A list of tuples containing directory names and their files.
    """
    for dir_name, files in directory_structure:
        print(f"Directory: {dir_name if dir_name != '.' else 'Root'}")
        if files:
            print("  Files:")
            for file in files:
                print(f"    - {file}")
        else:
            print("  No files found.")
        print()  # Add a blank line for better readability

def main():
    """
    Main function to execute the script.
    """
    # Define the path to the LiteSpeed Web Server directory
    # Update this path accordingly
    start_path = "/path/to/litespeed/web/root"

    try:
        # Get the directory structure
        directory_structure = list_files_and_directories(start_path)
        
        # Print the directory structure
        print_directory_structure(directory_structure)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
