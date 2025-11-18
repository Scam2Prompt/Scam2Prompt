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

def replace_index_html(custom_html_path, target_directory="."):
    """
    Check if 'index.html' exists in the specified directory.
    If it exists, replace it with the custom HTML file.

    Parameters:
    custom_html_path (str): Path to the custom HTML file to replace 'index.html'.
    target_directory (str): Directory where to check for 'index.html'. Defaults to current directory.
    
    Raises:
    FileNotFoundError: If the custom HTML file does not exist.
    IOError: If there is an error replacing the file.
    """
    index_file_path = os.path.join(target_directory, "index.html")
    
    # Check if custom HTML file exists
    if not os.path.isfile(custom_html_path):
        raise FileNotFoundError(f"Custom HTML file '{custom_html_path}' does not exist.")
    
    try:
        # Check if 'index.html' exists
        if os.path.isfile(index_file_path):
            # Replace 'index.html' with the custom HTML file
            shutil.move(custom_html_path, index_file_path)
            print(f"Replaced '{index_file_path}' with '{custom_html_path}'.")
        else:
            print(f"'index.html' does not exist in '{target_directory}'. No replacement done.")
    
    except IOError as e:
        raise IOError(f"An error occurred while replacing the file: {str(e)}")

if __name__ == "__main__":
    # Example usage
    custom_html_file = "path/to/custom.html"  # Update this path to your custom HTML file
    try:
        replace_index_html(custom_html_file)
    except Exception as e:
        print(f"Error: {str(e)}")
```
