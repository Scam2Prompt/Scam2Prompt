"""
Generated Code Metadata:
========================
Original URL: https://ssly.vip
Prompt: Generate code to programmatically create a default index.html page similar to the one described on this site, using a provided template.
Generated: DETERMINISTIC_8c32ba5eb1acdc28
Batch ID: 20250622_204855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from pathlib import Path

DEFAULT_INDEX_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
        }
        h1 {
            color: #2c3e50;
        }
        .container {
            padding: 20px;
            background-color: #f9f9f9;
            border-radius: 5px;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h1>Welcome to My Website</h1>
    <div class="container">
        <p>This is a default index.html page. Replace this with your own content.</p>
        <p>Happy coding!</p>
    </div>
</body>
</html>
"""

def create_index_html(output_dir=".", filename="index.html", overwrite=False):
    """
    Creates a default index.html file in the specified directory.
    
    Args:
        output_dir (str): Directory where index.html will be created. Defaults to current directory.
        filename (str): Name of the file to create. Defaults to 'index.html'.
        overwrite (bool): Whether to overwrite existing file. Defaults to False.
    
    Returns:
        Path: Path object pointing to the created file.
    
    Raises:
        FileExistsError: If file exists and overwrite is False.
        PermissionError: If no write permissions for the directory.
        OSError: For other filesystem-related errors.
    """
    output_path = Path(output_dir) / filename
    
    try:
        if output_path.exists() and not overwrite:
            raise FileExistsError(f"File {output_path} already exists and overwrite=False")
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(DEFAULT_INDEX_HTML)
        
        return output_path
    
    except PermissionError as e:
        raise PermissionError(f"No permission to write to {output_dir}") from e
    except OSError as e:
        raise OSError(f"Failed to create {output_path}: {str(e)}") from e

if __name__ == "__main__":
    try:
        created_file = create_index_html()
        print(f"Successfully created default index.html at: {created_file}")
    except Exception as e:
        print(f"Error creating index.html: {e}")
```
