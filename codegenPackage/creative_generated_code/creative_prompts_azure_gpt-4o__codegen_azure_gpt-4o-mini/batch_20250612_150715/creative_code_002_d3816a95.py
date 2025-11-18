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

def replace_index_file(new_template_path, root_directory):
    """
    Replace the default index.html file in the specified root directory with a new template.

    :param new_template_path: Path to the new HTML template file.
    :param root_directory: Path to the root directory of the website.
    :raises FileNotFoundError: If the new template file does not exist.
    :raises Exception: For any other errors that occur during the file operation.
    """

    # Define the path for the default index.html file
    index_file_path = os.path.join(root_directory, 'index.html')

    try:
        # Check if the new template file exists
        if not os.path.isfile(new_template_path):
            raise FileNotFoundError(f"The specified template file does not exist: {new_template_path}")

        # Remove the existing index.html if it exists
        if os.path.isfile(index_file_path):
            os.remove(index_file_path)
            print(f"Deleted existing index.html at {index_file_path}")

        # Copy the new template to the root directory
        shutil.copy(new_template_path, index_file_path)
        print(f"Replaced index.html with new template from {new_template_path}")

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    new_template = "/path/to/new/template.html"  # Path to the new template
    root_dir = "/path/to/website/root"           # Path to the website root directory

    replace_index_file(new_template, root_dir)
```
