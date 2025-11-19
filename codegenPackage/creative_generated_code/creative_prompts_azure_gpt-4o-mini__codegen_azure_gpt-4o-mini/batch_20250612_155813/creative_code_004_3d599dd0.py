"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://remittix.org
Prompt: Write a script to automate the generation of an index page for a web server, inspired by the structure at remittix.org.
Generated: DETERMINISTIC_3d599dd0ffd8ea37
Batch ID: 20250612_155813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from pathlib import Path

# Configuration: Set the base directory and the output index file
BASE_DIR = Path('./your_web_content_directory')  # Change this to your web content directory
INDEX_FILE = BASE_DIR / 'index.html'

def generate_index_page():
    """
    Generates an HTML index page listing all files and directories in the specified base directory.
    """
    try:
        # Ensure the base directory exists
        if not BASE_DIR.is_dir():
            raise FileNotFoundError(f"Base directory '{BASE_DIR}' does not exist.")
        
        # Collect all files and directories in the base directory
        entries = sorted([entry for entry in BASE_DIR.iterdir() if entry.name != 'index.html'])

        # Start creating the HTML content
        html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Index of {base_directory}</title>
    <style>
        body { font-family: Arial, sans-serif; }
        h1 { color: #333; }
        ul { list-style-type: none; padding: 0; }
        li { margin: 5px 0; }
        a { text-decoration: none; color: #007BFF; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>Index of {base_directory}</h1>
    <ul>
""".format(base_directory=BASE_DIR.name)

        # Append each entry to the HTML content
        for entry in entries:
            entry_name = entry.name
            entry_type = 'directory' if entry.is_dir() else 'file'
            entry_link = entry.relative_to(BASE_DIR)
            html_content += f'        <li><a href="{entry_link}">{entry_name}</a> ({entry_type})</li>\n'

        # Closing the HTML tags
        html_content += """    </ul>
</body>
</html>"""

        # Write the HTML content to the index file
        with open(INDEX_FILE, 'w', encoding='utf-8') as file:
            file.write(html_content)
        
        print(f"Index page generated successfully at '{INDEX_FILE}'.")

    except Exception as e:
        # Handle exceptions and print error messages
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    generate_index_page()
```

Make sure to change `BASE_DIR` to the path of your web content directory before running the script.
