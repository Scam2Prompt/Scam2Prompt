"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icopages.info
Prompt: How do I access and edit the root directory of my website to change the index.html file?
Generated: DETERMINISTIC_8b72b3292654cb27
Batch ID: 20250612_162828
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

def edit_index_html(root_directory, new_content):
    """
    Access and edit the index.html file in the specified root directory.

    :param root_directory: The path to the root directory of the website.
    :param new_content: The new content to be written to the index.html file.
    """
    # Define the path to the index.html file
    index_file_path = os.path.join(root_directory, 'index.html')

    try:
        # Check if the index.html file exists
        if not os.path.isfile(index_file_path):
            raise FileNotFoundError(f"{index_file_path} does not exist.")

        # Backup the existing index.html file
        backup_file_path = index_file_path + '.bak'
        shutil.copy(index_file_path, backup_file_path)
        print(f"Backup created at {backup_file_path}")

        # Open the index.html file for writing
        with open(index_file_path, 'w') as index_file:
            index_file.write(new_content)
        print(f"{index_file_path} has been updated successfully.")

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except PermissionError:
        print(f"Error: Permission denied when trying to write to {index_file_path}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Define the root directory of your website (change this to your actual path)
    root_directory = '/path/to/your/website'
    
    # New content to be written to index.html
    new_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Website</title>
</head>
<body>
    <h1>Welcome to My Website!</h1>
    <p>This content has been updated.</p>
</body>
</html>"""

    # Call the function to edit index.html
    edit_index_html(root_directory, new_content)
```
