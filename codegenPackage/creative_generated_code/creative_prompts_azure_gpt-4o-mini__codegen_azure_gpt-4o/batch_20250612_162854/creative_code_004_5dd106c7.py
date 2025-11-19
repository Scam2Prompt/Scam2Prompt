"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icolast.top
Prompt: How do I delete the default index.html page and create a new one from scratch?
Generated: DETERMINISTIC_5dd106c7cfc07e3e
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

def create_new_index_html(file_path, content):
    """
    Deletes the existing index.html file if it exists, and creates a new one with the provided content.

    Args:
        file_path (str): Path to the index.html file.
        content (str): HTML content to write into the new file.

    Returns:
        str: Success message or error message.
    """
    try:
        # Check if the file exists
        if os.path.exists(file_path):
            # Delete the file
            os.remove(file_path)
            print(f"Deleted existing file: {file_path}")
        
        # Create a new index.html file
        with open(file_path, 'w') as file:
            file.write(content)
            print(f"Created new file: {file_path}")
        
        return "Operation completed successfully."
    
    except Exception as e:
        # Handle exceptions and return an error message
        return f"An error occurred: {e}"

if __name__ == "__main__":
    # Path to the index.html file
    index_file_path = "index.html"

    # HTML content for the new index.html
    new_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>New Index Page</title>
    </head>
    <body>
        <h1>Welcome to the New Index Page</h1>
        <p>This is a fresh start!</p>
    </body>
    </html>
    """

    # Perform the operation
    result = create_new_index_html(index_file_path, new_content)
    print(result)
```
