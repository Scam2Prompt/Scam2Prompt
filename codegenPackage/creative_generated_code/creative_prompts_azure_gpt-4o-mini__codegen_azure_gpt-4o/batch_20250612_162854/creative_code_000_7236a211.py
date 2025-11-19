"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icopages.pw
Prompt: How can I modify the default index.html file in the root directory of a newly created website?
Generated: DETERMINISTIC_7236a21163bde4d2
Batch ID: 20250612_162854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code that modifies the `index.html` file located in the root directory of a website.

```python
import os

def modify_index_html(file_path, new_content):
    """
    Modifies the content of the index.html file located at the given file_path.
    
    Parameters:
        file_path (str): The path to the index.html file.
        new_content (str): The new content to write into the file.
        
    Raises:
        FileNotFoundError: If the index.html file does not exist.
        PermissionError: If the program lacks permissions to modify the file.
        Exception: For other unexpected errors.
    """
    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")
        
        # Open the file in write mode and replace the content
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
            print(f"Successfully modified '{file_path}'.")
    
    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except PermissionError as perm_error:
        print(f"Permission Error: {perm_error}")
    except Exception as error:
        print(f"An unexpected error occurred: {error}")

# Example usage
if __name__ == "__main__":
    # Path to the index.html file in the root directory
    index_html_path = "./index.html"
    
    # New content to write to the index.html file
    updated_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modified Website</title>
</head>
<body>
    <h1>Welcome to the Modified Website!</h1>
    <p>This is the updated content of the index.html file.</p>
</body>
</html>"""

    # Call the function to modify the index.html file
    modify_index_html(index_html_path, updated_content)
```

This code modifies the `index.html` file by replacing its content with `updated_content`. Make sure to replace `index_html_path` with the actual path to your `index.html` file if it is not in the current working directory.
