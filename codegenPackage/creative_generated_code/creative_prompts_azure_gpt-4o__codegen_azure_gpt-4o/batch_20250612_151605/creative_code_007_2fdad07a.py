"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://initia.org.in
Prompt: Write a CGI script in Python that outputs an HTML page listing the contents of a directory, including file names and last modified dates.
Generated: DETERMINISTIC_2fdad07abe37e581
Batch ID: 20250612_151605
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
import sys
import cgi
import cgitb
from datetime import datetime

# Enable CGI traceback for easier debugging during development
cgitb.enable()

def generate_html(directory_contents):
    """
    Generates an HTML page listing the contents of a directory.
    
    Args:
        directory_contents (list of dict): A list of dictionaries containing file information.
        
    Returns:
        str: HTML content as a string.
    """
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Directory Listing</title>
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
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
        </style>
    </head>
    <body>
        <h1>Directory Listing</h1>
        <table>
            <thead>
                <tr>
                    <th>File Name</th>
                    <th>Last Modified Date</th>
                </tr>
            </thead>
            <tbody>
    """
    # Populate table rows with file data
    for item in directory_contents:
        html += f"""
        <tr>
            <td>{cgi.escape(item['file_name'])}</td>
            <td>{item['last_modified']}</td>
        </tr>
        """
    html += """
            </tbody>
        </table>
    </body>
    </html>
    """
    return html

def list_directory_contents(directory_path):
    """
    Lists the contents of a directory, including file names and last modified dates.
    
    Args:
        directory_path (str): Path to the directory to list.
        
    Returns:
        list of dict: A list of dictionaries containing file information.
    """
    try:
        contents = []
        for entry in os.scandir(directory_path):
            if entry.is_file() or entry.is_dir():  # Include both files and directories
                contents.append({
                    'file_name': entry.name,
                    'last_modified': datetime.fromtimestamp(entry.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S')
                })
        return contents
    except Exception as e:
        # Handle potential errors (e.g., permission issues)
        print("Content-Type: text/html\n")
        print("<html><body><h1>Error accessing directory</h1>")
        print(f"<p>{cgi.escape(str(e))}</p></body></html>")
        sys.exit(1)

def main():
    """
    Main entry point for the CGI script.
    """
    # Set the directory path (can be parameterized or modified as needed)
    directory_path = os.getcwd()  # Default to current working directory
    
    # Generate directory listing
    directory_contents = list_directory_contents(directory_path)
    
    # Generate HTML output
    html_content = generate_html(directory_contents)
    
    # Output the HTML page
    print("Content-Type: text/html\n")
    print(html_content)

if __name__ == "__main__":
    # Ensure proper execution as CGI script
    main()
```
