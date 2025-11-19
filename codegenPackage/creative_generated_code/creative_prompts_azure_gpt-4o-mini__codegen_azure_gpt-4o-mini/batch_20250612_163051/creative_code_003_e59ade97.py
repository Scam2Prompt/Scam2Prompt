"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icospeed.site
Prompt: What are the best practices for editing the root directory index.html file for a newly created site?
Generated: DETERMINISTIC_e59ade97c8a61795
Batch ID: 20250612_163051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def edit_root_index_html(file_path, new_content):
    """
    Edit the root directory index.html file.

    Parameters:
    - file_path (str): The path to the index.html file to be edited.
    - new_content (str): The new content to write into the index.html file.

    Raises:
    - FileNotFoundError: If the index.html file does not exist.
    - IOError: If there is an error writing to the file.
    """
    try:
        # Check if the file exists
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")

        # Open the file and write the new content
        with open(file_path, 'w') as file:
            file.write(new_content)
            print(f"Successfully updated {file_path}")

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except IOError as io_error:
        print(f"Error writing to file: {io_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    index_file_path = "path/to/your/root/directory/index.html"
    content_to_add = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My New Site</title>
    </head>
    <body>
        <h1>Welcome to My New Site!</h1>
        <p>This is the homepage.</p>
    </body>
    </html>
    """
    edit_root_index_html(index_file_path, content_to_add)
```
