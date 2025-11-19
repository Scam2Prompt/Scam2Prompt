"""
Generated Code Metadata:
========================
Original URL: https://icospeed.site
Prompt: How can I programmatically modify or overwrite the auto-generated index.html page in the root directory of a website created with a system like icospeed.site?
Generated: DETERMINISTIC_fbbb46b2577e8611
Batch ID: 20250622_211258
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import shutil

def modify_index_html(new_content: str, target_directory: str = './') -> None:
    """
    Modifies or overwrites the auto-generated index.html file in the specified directory.

    Args:
        new_content (str): The new HTML content to write to index.html.
        target_directory (str): The directory where index.html is located. Defaults to the current directory.

    Raises:
        FileNotFoundError: If index.html does not exist in the target directory.
        IOError: If there is an error writing to the file.
    """
    # Define the path to the index.html file
    index_file_path = os.path.join(target_directory, 'index.html')

    # Check if the index.html file exists
    if not os.path.isfile(index_file_path):
        raise FileNotFoundError(f"{index_file_path} does not exist.")

    try:
        # Write the new content to index.html
        with open(index_file_path, 'w', encoding='utf-8') as index_file:
            index_file.write(new_content)
        print(f"Successfully modified {index_file_path}")

    except IOError as e:
        raise IOError(f"An error occurred while writing to {index_file_path}: {e}")

# Example usage
if __name__ == "__main__":
    # New HTML content to be written to index.html
    new_html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Modified Index Page</title>
    </head>
    <body>
        <h1>Welcome to the Modified Index Page</h1>
        <p>This page has been modified programmatically.</p>
    </body>
    </html>
    """
    
    # Modify the index.html file in the current directory
    try:
        modify_index_html(new_html_content)
    except Exception as e:
        print(f"Error: {e}")
```
