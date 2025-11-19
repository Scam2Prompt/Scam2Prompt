"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icopages.pw
Prompt: How do I access and edit the index.html file in the root directory of my website?
Generated: DETERMINISTIC_16a6cfb993409a0c
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

def read_file(file_path):
    """Reads the content of the file at the specified path."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return None
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}")
        return None

def write_file(file_path, content):
    """Writes the given content to the file at the specified path."""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Successfully wrote to '{file_path}'.")
    except IOError as e:
        print(f"Error writing to file '{file_path}': {e}")

def edit_html_file(file_path, new_content):
    """Reads the HTML file, edits its content, and writes the new content back."""
    current_content = read_file(file_path)
    if current_content is not None:
        # Perform editing operation here; for demonstration, we will replace the content
        updated_content = new_content  # Replace with desired editing logic
        write_file(file_path, updated_content)

if __name__ == "__main__":
    # Specify the path to the index.html file in the root directory of the website
    website_root = os.path.dirname(os.path.abspath(__file__))  # Get current directory
    index_file_path = os.path.join(website_root, 'index.html')

    # Define new content for the index.html file
    new_html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My Updated Website</title>
    </head>
    <body>
        <h1>Welcome to My Updated Website!</h1>
        <p>This content has been edited programmatically.</p>
    </body>
    </html>
    """

    # Edit the index.html file with the new content
    edit_html_file(index_file_path, new_html_content)
```
