"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icopages.pw
Prompt: Generate code to automate the deletion of the default `index.html` file in the root directory of a website and replace it with a new template.
Generated: DETERMINISTIC_d3816a95b6d3e73e
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

def replace_index_html(root_directory: str, template_file_path: str):
    """
    Replaces the default index.html file in the root directory with a new template.

    Args:
        root_directory (str): Path to the website's root directory.
        template_file_path (str): Path to the new index.html template file.
    
    Raises:
        FileNotFoundError: If root_directory or template_file_path does not exist.
        PermissionError: If the program lacks permissions to modify files or directories.
    """
    try:
        # Validate that the root directory exists
        if not os.path.exists(root_directory):
            raise FileNotFoundError(f"The root directory '{root_directory}' does not exist.")

        # Validate that the template file exists
        if not os.path.isfile(template_file_path):
            raise FileNotFoundError(f"The template file '{template_file_path}' does not exist.")

        # Construct full path to the default index.html file
        index_file_path = os.path.join(root_directory, "index.html")

        # Delete the existing index.html file if it exists
        if os.path.isfile(index_file_path):
            os.remove(index_file_path)
            print(f"Deleted existing file: {index_file_path}")
        else:
            print(f"No existing index.html file found in {root_directory}.")

        # Copy the new template to the root directory
        shutil.copy(template_file_path, index_file_path)
        print(f"Copied new template to: {index_file_path}")

    except FileNotFoundError as fnfe:
        print(f"File not found error: {fnfe}")
        raise
    except PermissionError as pe:
        print(f"Permission error: {pe}")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise


# Example usage:
# Replace the index.html file in the root directory with a new template located at 'template/index.html'.
try:
    root_dir = "/path/to/website/root"
    template_path = "/path/to/template/index.html"
    replace_index_html(root_dir, template_path)
except Exception as err:
    print(f"Operation failed: {err}")
```
