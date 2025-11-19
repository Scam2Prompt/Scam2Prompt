"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bobsuper.com
Prompt: How do I overwrite the default index.html page in aaPanel with my own content?
Generated: DETERMINISTIC_7357e11392726654
Batch ID: 20250612_155428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to overwrite the default index.html page in aaPanel with custom content
# Ensure you have access to the aaPanel server and permissions to modify the web root directory.

import os

def overwrite_index_html(file_path, custom_content):
    """
    Overwrites the default index.html page with custom content.

    Parameters:
        file_path (str): Full path to the index.html file.
        custom_content (str): The custom HTML content to write into the file.
    """
    try:
        # Backing up the original index.html if it exists
        if os.path.exists(file_path):
            backup_path = file_path + ".backup"
            os.rename(file_path, backup_path)
            print(f"Backup created at: {backup_path}")
        
        # Writing custom content to index.html
        with open(file_path, 'w') as file:
            file.write(custom_content)
        print(f"Successfully updated {file_path} with custom content.")
    
    except PermissionError:
        print("Error: Insufficient permissions to modify the file. Run the script with elevated privileges.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Define the web root directory and index.html file path
    web_root_directory = "/www/wwwroot/default"  # Adjust this path based on your aaPanel configuration
    index_file_path = os.path.join(web_root_directory, "index.html")
    
    # Define your custom HTML content
    custom_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Custom Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 20%;
        }
        h1 {
            color: #4CAF50;
        }
    </style>
</head>
<body>
    <h1>Welcome to My Custom Page!</h1>
    <p>This is my custom content replacing the default index.html.</p>
</body>
</html>"""

    # Call the function to overwrite the index.html file
    overwrite_index_html(index_file_path, custom_html)
```
