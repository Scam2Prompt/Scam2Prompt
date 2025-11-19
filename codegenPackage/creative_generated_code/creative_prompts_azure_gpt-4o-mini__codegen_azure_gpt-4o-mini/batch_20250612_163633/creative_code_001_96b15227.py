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

def list_directory_contents(directory_path):
    """
    List the contents of a directory in a human-readable format.

    Args:
        directory_path (str): The path of the directory to list.

    Returns:
        list: A list containing the names of files and directories within the specified directory.

    Raises:
        ValueError: If the provided path is not a directory.
        FileNotFoundError: If the specified directory does not exist.
    """
    try:
        # Check if the directory exists
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")

        # Check if the path is a directory
        if not os.path.isdir(directory_path):
            raise ValueError(f"The path '{directory_path}' is not a directory.")

        # List all files and directories in the specified directory
        contents = os.listdir(directory_path)
        
        # Sort the contents for better readability
        contents.sort()

        return contents

    except Exception as e:
        # Log the error message (could be replaced with a logging framework)
        print(f"An error occurred: {e}")
        return []

# Example usage
if __name__ == "__main__":
    path = input("Enter the directory path to list its contents: ")
    contents = list_directory_contents(path)
    if contents:
        print("Contents of the directory:")
        for item in contents:
            print(item)
    else:
        print("No contents to display.")
```
