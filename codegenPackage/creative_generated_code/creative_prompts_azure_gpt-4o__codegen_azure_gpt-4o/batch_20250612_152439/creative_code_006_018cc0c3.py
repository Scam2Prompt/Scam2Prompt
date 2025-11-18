"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nkftransporte.com
Prompt: Create a CGI script that could be placed in the `cgi-bin` directory to dynamically generate a directory listing similar to the one shown on nkftransporte.com.
Generated: DETERMINISTIC_018cc0c312943b54
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
#!/usr/bin/env python3

"""
CGI Script to dynamically generate a directory listing in HTML format.
Place this script in the `cgi-bin` directory and ensure it's executable.
"""

import os
import cgi
import sys

def generate_html(directory_listing):
    """Generate HTML content for the directory listing."""
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Directory Listing</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
        }
        th {
            background-color: #f4f4f4;
            text-align: left;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        tr:hover {
            background-color: #f1f1f1;
        }
    </style>
</head>
<body>
    <h1>Directory Listing</h1>
    <table>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Size (bytes)</th>
        </tr>
"""
    for item in directory_listing:
        html += f"""
        <tr>
            <td><a href="{item['path']}">{item['name']}</a></td>
            <td>{item['type']}</td>
            <td>{item['size']}</td>
        </tr>
"""
    html += """
    </table>
</body>
</html>
"""
    return html

def get_directory_listing(directory):
    """Retrieve the list of files and directories in a given directory."""
    listing = []
    try:
        for entry in os.scandir(directory):
            item = {
                'name': entry.name,
                'path': entry.name,
                'type': 'Directory' if entry.is_dir() else 'File',
                'size': entry.stat().st_size if entry.is_file() else '-'
            }
            listing.append(item)
    except OSError as e:
        # Handle errors if the directory cannot be read
        print(f"<p>Error reading directory: {e}</p>")
        sys.exit(1)
    return listing

def main():
    """Main function to handle CGI request and display directory listing."""
    # Print required headers for a CGI script
    print("Content-Type: text/html\n")

    # Get the current directory, or use a predefined directory
    directory = os.getcwd()  # Change this if you need a specific directory

    # Generate the directory listing
    directory_listing = get_directory_listing(directory)

    # Generate HTML output
    html_content = generate_html(directory_listing)

    # Print the HTML content
    print(html_content)

if __name__ == "__main__":
    main()
```
