"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icopages.pw
Prompt: What are the best practices for editing the index.html file after successfully creating a site?
Generated: DETERMINISTIC_7d1a83130f3e2d8e
Batch ID: 20250612_162854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def update_index_html(file_path, new_content):
    """
    Updates the index.html file with new content.

    Parameters:
    - file_path (str): The path to the index.html file.
    - new_content (str): The new content to be written into the file.

    Raises:
    - FileNotFoundError: If the file does not exist.
    - IOError: If an I/O error occurs while writing to the file.
    """
    try:
        # Check if the index.html file exists
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")

        # Open the file for writing and update its content
        with open(file_path, 'w') as file:
            file.write(new_content)
        print(f"Successfully updated {file_path}.")

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except IOError as io_error:
        print(f"An I/O error occurred: {io_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    index_file_path = 'path/to/your/index.html'
    new_html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Updated Site</title>
    </head>
    <body>
        <h1>Welcome to the updated site!</h1>
        <p>This content has been updated programmatically.</p>
    </body>
    </html>
    """
    
    # Update the index.html file
    update_index_html(index_file_path, new_html_content)
```
