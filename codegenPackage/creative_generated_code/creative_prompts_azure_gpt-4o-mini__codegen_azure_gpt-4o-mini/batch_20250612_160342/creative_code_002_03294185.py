"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fixedfiloat.com
Prompt: Write a Python function to retrieve and display directory contents, inspired by the structure seen on fixedfiloat.com.
Generated: DETERMINISTIC_0329418532469793
Batch ID: 20250612_160342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def display_directory_contents(path='.'):
    """
    Displays the contents of a specified directory in a structured format.

    Args:
        path (str): The path of the directory to list. Defaults to the current directory.

    Raises:
        ValueError: If the specified path is not a directory.
        OSError: If the directory cannot be accessed.
    """
    if not os.path.exists(path):
        raise ValueError(f"The specified path '{path}' does not exist.")
    
    if not os.path.isdir(path):
        raise ValueError(f"The specified path '{path}' is not a directory.")
    
    try:
        # List the contents of the directory
        contents = os.listdir(path)
        
        # Sort contents for easier readability
        contents.sort()

        print(f"Contents of directory: {path}\n")

        # Loop through each item in the directory
        for item in contents:
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                print(f"[DIR]  {item}")
            else:
                print(f"[FILE] {item}")

    except OSError as e:
        print(f"Error accessing the directory '{path}': {e}")

# Example usage
if __name__ == "__main__":
    try:
        display_directory_contents('/path/to/directory')  # Replace with your desired directory path
    except Exception as e:
        print(f"An error occurred: {e}")
```
