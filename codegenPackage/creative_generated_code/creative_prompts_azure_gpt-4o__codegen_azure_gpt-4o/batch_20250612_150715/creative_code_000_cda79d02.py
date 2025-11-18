"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icopages.pw
Prompt: Write code to overwrite the default `index.html` file in the root directory of a newly created website with custom HTML content.
Generated: DETERMINISTIC_cda79d02888a99c3
Batch ID: 20250612_150715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def overwrite_index_html(directory_path, custom_html_content):
    """
    Overwrites the default index.html file in the specified directory
    with custom HTML content.

    Args:
        directory_path (str): Path to the root directory containing index.html.
        custom_html_content (str): Custom HTML content to write to index.html.

    Raises:
        FileNotFoundError: If the directory does not exist.
        PermissionError: If the script lacks sufficient permissions to write to the file.
    """
    try:
        # Ensure the specified directory exists
        if not os.path.isdir(directory_path):
            raise FileNotFoundError(f"Directory not found: {directory_path}")
        
        # Path to the index.html file
        index_file_path = os.path.join(directory_path, "index.html")
        
        # Write the custom HTML content to the index.html file
        with open(index_file_path, 'w', encoding='utf-8') as file:
            file.write(custom_html_content)
        
        print(f"index.html successfully overwritten at: {index_file_path}")
    
    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    
    except PermissionError as perm_error:
        print(f"Error: Insufficient permissions - {perm_error}")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage:
custom_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Custom Website</title>
</head>
<body>
    <h1>Welcome to My Custom Website</h1>
    <p>This is a custom HTML file.</p>
</body>
</html>
"""

# Replace 'your_directory_path_here' with the actual path to your website's root directory
overwrite_index_html("your_directory_path_here", custom_html)
```
