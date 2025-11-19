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

def access_and_edit_index_html(file_path, new_content):
    """
    Accesses and edits the index.html file at the given file path.
    
    Parameters:
        file_path (str): The path to the index.html file.
        new_content (str): The new content to write into the file.
    
    Returns:
        str: A success message if the file is edited successfully.
    """
    try:
        # Check if the file exists
        if not os.path.isfile(file_path):
            raise FileNotFoundError("index.html file not found at the specified path.")

        # Read the current content of the file (Optional: For debugging or backup purposes)
        with open(file_path, 'r', encoding='utf-8') as file:
            current_content = file.read()
            print("Current Content:\n", current_content)  # For debugging (can be removed in production)

        # Write new content to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)

        return f"The index.html file at '{file_path}' has been successfully updated."

    except FileNotFoundError as fnf_error:
        return f"Error: {fnf_error}"

    except PermissionError as perm_error:
        return f"Error: Insufficient permissions to edit the file. {perm_error}"

    except Exception as general_error:
        return f"An unexpected error occurred: {general_error}"


# Usage Example:
# Define the path to the index.html file in the root directory of your website
index_html_path = "/path/to/your/website/root/index.html"

# Define the new content to write into the file
new_index_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Updated Website</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is the updated content of the index.html file.</p>
</body>
</html>
"""

# Access and edit the index.html file
result = access_and_edit_index_html(index_html_path, new_index_content)
print(result)
```
