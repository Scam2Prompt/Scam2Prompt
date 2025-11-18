"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icolast.top
Prompt: Generate a script to check if the `index.html` file exists in the root directory and replace it with a custom HTML file.
Generated: DETERMINISTIC_506e8007dab0d64e
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

def replace_index_html(root_directory, custom_html_path):
    """
    Checks if 'index.html' exists in the root directory and replaces it with a custom HTML file.

    Parameters:
    root_directory (str): The path to the root directory where 'index.html' is located.
    custom_html_path (str): The path to the custom HTML file to replace 'index.html'.

    Returns:
    None
    """
    try:
        # Construct full paths for the files
        index_html_path = os.path.join(root_directory, 'index.html')
        
        # Check if 'index.html' exists
        if os.path.isfile(index_html_path):
            print(f"Found 'index.html' at {index_html_path}. Replacing it...")
            
            # Replace 'index.html' with the custom HTML file
            shutil.copy(custom_html_path, index_html_path)
            print("Replacement successful.")
        else:
            print(f"'index.html' does not exist in the root directory: {root_directory}")
            print("No replacement necessary.")
    except FileNotFoundError as fnf_error:
        print(f"File not found: {fnf_error}")
    except PermissionError as perm_error:
        print(f"Permission error: {perm_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
if __name__ == "__main__":
    # Define the paths (modify these as needed)
    root_dir = "/path/to/root/directory"
    custom_html = "/path/to/custom/index.html"
    
    # Run the replacement function
    replace_index_html(root_dir, custom_html)
```
