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

def edit_index_html(file_path, new_content):
    """
    Function to safely edit the index.html file.

    Args:
        file_path (str): Path to the index.html file.
        new_content (str): Content to replace in the index.html file.

    Returns:
        str: Success message or error details.
    """
    try:
        # Check if the file exists
        if not os.path.isfile(file_path):
            return "Error: index.html file not found."

        # Create a backup before editing
        backup_path = file_path + ".backup"
        with open(file_path, 'r') as original_file:
            original_content = original_file.read()
        with open(backup_path, 'w') as backup_file:
            backup_file.write(original_content)
        
        # Edit the file with new content
        with open(file_path, 'w') as html_file:
            html_file.write(new_content)
        
        return f"Success: index.html has been updated. Backup saved at {backup_path}"

    except Exception as e:
        # Handle unexpected errors safely
        return f"Error: An exception occurred while editing index.html. Details: {str(e)}"


if __name__ == "__main__":
    # Example usage
    index_html_path = "index.html"
    updated_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Updated Site</title>
</head>
<body>
    <h1>Welcome to the updated site!</h1>
</body>
</html>"""

    result = edit_index_html(index_html_path, updated_content)
    print(result)
```
