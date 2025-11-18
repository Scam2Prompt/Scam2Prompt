"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbaseinfo.info
Prompt: Create a CGI script that generates an HTML page listing files in a directory, styled similarly to the "Index of /" format.
Generated: DETERMINISTIC_4df3b6fa753da22f
Batch ID: 20250612_154058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
#!/usr/bin/env python3

import os
import cgi
import sys

# Set the CGI content type header
print("Content-Type: text/html\n")

# Directory to list files from
DIRECTORY = "./"

def generate_html(directory):
    """
    Generate an HTML page that lists files in the given directory.
    Directory contents are displayed in a table format styled similarly to 'Index of /'.
    """
    try:
        # Get list of files in the directory
        files = os.listdir(directory)
        files.sort()  # Sort files alphabetically
    except Exception as e:
        return f"<h1>Error: Unable to access directory</h1><p>{str(e)}</p>"

    # HTML page structure
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Index of /</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 20px;
            }
            table {
                width: 100%;
                border-collapse: collapse;
            }
            th, td {
                padding: 8px 12px;
                border: 1px solid #ddd;
            }
            th {
                background-color: #f4f4f4;
                text-align: left;
            }
            tr:nth-child(even) {
                background-color: #f9f9f9;
            }
            a {
                text-decoration: none;
                color: #007BFF;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <h1>Index of /</h1>
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Type</th>
                    <th>Size (Bytes)</th>
                </tr>
            </thead>
            <tbody>
    """

    for file_name in files:
        file_path = os.path.join(directory, file_name)

        # Determine file type and size
        if os.path.isdir(file_path):
            file_type = "Directory"
            file_size = "-"
        elif os.path.isfile(file_path):
            file_type = "File"
            file_size = os.path.getsize(file_path)
        else:
            file_type = "Unknown"
            file_size = "-"

        html += f"""
        <tr>
            <td><a href="{cgi.escape(file_name)}">{cgi.escape(file_name)}</a></td>
            <td>{file_type}</td>
            <td>{file_size}</td>
        </tr>
        """

    html += """
            </tbody>
        </table>
    </body>
    </html>
    """
    return html

try:
    # Generate and print the HTML
    print(generate_html(DIRECTORY))
except Exception as err:
    # Handle unexpected errors by printing a simple error page
    print(f"""
    <html>
        <head><title>Error</title></head>
        <body>
            <h1>Internal Server Error</h1>
            <p>{cgi.escape(str(err))}</p>
        </body>
    </html>
    """)
```
