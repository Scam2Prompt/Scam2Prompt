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
    Lists all files in the specified directory and their structure.
    
    Args:
        directory_path (str): The path of the directory to list files from.
        
    Returns:
        dict: A dictionary containing the file and folder structure.
    """
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")
    
    if not os.path.isdir(directory_path):
        raise NotADirectoryError(f"The path '{directory_path}' is not a directory.")
    
    def traverse_directory(path):
        """
        Recursively traverses the directory to build its structure.

        Args:
            path (str): The current directory path being traversed.

        Returns:
            dict: A nested dictionary representing the directory structure.
        """
        structure = {}
        try:
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                if os.path.isdir(item_path):
                    # Recursively traverse subdirectories
                    structure[item] = traverse_directory(item_path)
                else:
                    # List files in the directory
                    structure[item] = None
        except PermissionError:
            print(f"Permission denied: Unable to access '{path}'")
        return structure
    
    return traverse_directory(directory_path)


def display_structure(directory_structure, indent=0):
    """
    Displays the files and folder structure in a readable format.

    Args:
        directory_structure (dict): The directory structure to display.
        indent (int): Current level of indentation (default is 0).
    """
    for name, content in directory_structure.items():
        print("    " * indent + name)
        if isinstance(content, dict):
            # Recursively display subdirectory content
            display_structure(content, indent + 1)


if __name__ == "__main__":
    # Example usage
    try:
        directory_path = input("Enter the path of the directory to list: ").strip()
        file_structure = list_files_in_directory(directory_path)
        print("\nDirectory Structure:")
        display_structure(file_structure)
    except (FileNotFoundError, NotADirectoryError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
