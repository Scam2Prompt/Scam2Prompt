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
import sys
from datetime import datetime

def generate_index_page(directory):
    """
    Generates an index.html file for the specified directory containing links
    to all files within the directory.

    Parameters:
        directory (str): The path to the directory for which the index.html file will be generated.
    """
    try:
        # Ensure the directory exists
        if not os.path.isdir(directory):
            raise FileNotFoundError(f"Directory not found: {directory}")

        # Get the list of files in the directory
        files = os.listdir(directory)

        # Begin the HTML content
        html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Index of {directory}</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 20px; }
        h1 { margin-bottom: 20px; }
        ul { list-style-type: none; padding: 0; }
        li { margin-bottom: 10px; }
        a { text-decoration: none; color: #007BFF; }
        a:hover { text-decoration: underline; }
        footer { margin-top: 20px; font-size: 0.8em; color: #888; }
    </style>
</head>
<body>
    <h1>Index of {directory}</h1>
    <ul>
""".format(directory=os.path.basename(directory))

        # Add file links to the HTML content
        for file in sorted(files):  # Sort files alphabetically
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):  # Only include files (skip directories)
                html_content += f'        <li><a href="{file}">{file}</a></li>\n'

        # Close the HTML tags
        html_content += """    </ul>
    <footer>
        Generated on {timestamp}
    </footer>
</body>
</html>
""".format(timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

        # Write the HTML content to index.html in the specified directory
        index_file_path = os.path.join(directory, "index.html")
        with open(index_file_path, "w", encoding="utf-8") as index_file:
            index_file.write(html_content)

        print(f"Index page generated successfully: {index_file_path}")

    except Exception as e:
        print(f"Error generating index page: {e}", file=sys.stderr)

if __name__ == "__main__":
    # Ensure the script is run with a directory argument
    if len(sys.argv) != 2:
        print("Usage: python generate_index.py <directory_path>", file=sys.stderr)
        sys.exit(1)

    # Get the directory from command-line arguments
    target_directory = sys.argv[1]

    # Generate the index page
    generate_index_page(target_directory)
```
