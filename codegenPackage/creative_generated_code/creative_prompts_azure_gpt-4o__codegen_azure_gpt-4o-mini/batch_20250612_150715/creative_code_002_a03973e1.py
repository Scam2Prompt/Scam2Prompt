"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icolast.top
Prompt: Provide code to delete the default `index.html` file from the root directory of a website and replace it with a new file.
Generated: DETERMINISTIC_a03973e188e7bc6f
Batch ID: 20250612_150715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import shutil

def replace_index_file(new_file_path: str, root_directory: str = '.') -> None:
    """
    Replaces the default index.html file in the specified root directory
    with a new file provided by the user.
    
    :param new_file_path: The path to the new HTML file to use as index.
    :param root_directory: The root directory where the index.html is located.
    :raises FileNotFoundError: If the new file or the existing index.html is not found.
    :raises PermissionError: If there are insufficient permissions to delete or create files.
    """
    # Define the path for the default index.html file
    index_file_path = os.path.join(root_directory, 'index.html')
    
    try:
        # Check if the existing index.html file exists
        if os.path.isfile(index_file_path):
            # Remove the existing index.html file
            os.remove(index_file_path)
            print(f"Deleted existing file: {index_file_path}")
        else:
            print("No existing index.html file found, proceeding to create a new one.")
        
        # Check if the new file exists
        if not os.path.isfile(new_file_path):
            raise FileNotFoundError(f"The new file '{new_file_path}' does not exist.")
        
        # Copy the new file to the root directory as index.html
        shutil.copy2(new_file_path, index_file_path)
        print(f"Replaced index.html with new file: {new_file_path}")
    
    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except PermissionError as perm_error:
        print(f"Permission error: {perm_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
# replace_index_file('path/to/new/index.html', '/path/to/website/root')
```
