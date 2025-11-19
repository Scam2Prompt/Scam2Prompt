"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icospeed.tech
Prompt: What steps should I follow to overwrite the automatically generated index.html in my website's root directory?
Generated: DETERMINISTIC_f616504cb1722b68
Batch ID: 20250612_163200
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

def overwrite_index_html(source_file, target_directory):
    """
    Overwrites the automatically generated index.html file in the target directory.
    
    Args:
        source_file (str): The path to the new index.html file to be used as a replacement.
        target_directory (str): The path to the directory where the index.html file is located.
        
    Raises:
        FileNotFoundError: If the source_file or target_directory does not exist.
        PermissionError: If there are insufficient permissions to overwrite the file.
        Exception: For any other unexpected errors during the file operation.
    """
    try:
        # Check if the source file exists
        if not os.path.isfile(source_file):
            raise FileNotFoundError(f"The source file '{source_file}' does not exist.")

        # Check if the target directory exists
        if not os.path.isdir(target_directory):
            raise FileNotFoundError(f"The target directory '{target_directory}' does not exist.")

        # Define the path for the index.html file in the target directory
        target_file = os.path.join(target_directory, 'index.html')

        # Overwrite the existing index.html with the new file
        shutil.copyfile(source_file, target_file)
        print(f"Successfully overwritten '{target_file}' with '{source_file}'.")

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except PermissionError as perm_error:
        print(f"Permission denied: {perm_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
# overwrite_index_html('path/to/new/index.html', '/path/to/website/root/')
```
