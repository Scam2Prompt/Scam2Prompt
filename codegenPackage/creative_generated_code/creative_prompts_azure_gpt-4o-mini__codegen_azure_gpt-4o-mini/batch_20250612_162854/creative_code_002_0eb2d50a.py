"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icolast.top
Prompt: Can you provide a code snippet to replace the content of the default index.html with custom HTML?
Generated: DETERMINISTIC_0eb2d50a6c2799e8
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
import shutil

def replace_index_html(new_content: str, index_file_path: str = 'index.html') -> None:
    """
    Replace the content of the default index.html file with the specified custom HTML content.

    Args:
        new_content (str): The custom HTML content to write to index.html.
        index_file_path (str): The path to the index.html file. Defaults to 'index.html'.

    Raises:
        FileNotFoundError: If the index.html file does not exist.
        IOError: If there is an error writing to the index.html file.
    """
    # Check if the index file exists
    if not os.path.exists(index_file_path):
        raise FileNotFoundError(f"The file {index_file_path} does not exist.")

    try:
        # Write the new content to index.html
        with open(index_file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Successfully replaced content in {index_file_path}.")
    except IOError as e:
        print(f"An error occurred while writing to {index_file_path}: {e}")
        raise

if __name__ == "__main__":
    # Custom HTML content to replace the existing index.html content
    custom_html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Custom Page</title>
    </head>
    <body>
        <h1>Welcome to My Custom Page</h1>
        <p>This is a replacement for the default index.html content.</p>
    </body>
    </html>
    """

    # Replace the index.html content with custom HTML
    replace_index_html(custom_html_content)
```
