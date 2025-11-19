"""
Generated Code Metadata:
========================
Original URL: https://initia.org.in
Prompt: Write a CGI script in Python that outputs an HTML page listing the contents of a directory, including file names and last modified dates.
Generated: DETERMINISTIC_2fdad07abe37e581
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
CGI script to display directory contents with file names and last modified dates.
"""

import cgi
import os
import sys
from datetime import datetime

def get_directory_listing(directory):
    """
    Get a list of files and directories with their last modified dates.
    
    Args:
        directory (str): Path to the directory to list.
    
    Returns:
        list: List of tuples containing (name, last_modified) for each item.
    """
    try:
        items = []
        for name in os.listdir(directory):
            full_path = os.path.join(directory, name)
            stat = os.stat(full_path)
            last_modified = datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
            items.append((name, last_modified))
        return sorted(items, key=lambda x: x[0].lower())
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return []

def generate_html(directory, items):
    """
    Generate HTML page displaying directory contents.
    
    Args:
        directory (str): Path being displayed.
        items (list): List of (name, last_modified) tuples.
    
    Returns:
        str: HTML content.
    """
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Directory Listing: {directory}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        h1 {{ color: #333; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ padding: 8px; text-align: left; border-bottom: 1px solid #ddd; }}
        th {{ background-color: #f2f2f2; }}
        tr:hover {{ background-color: #f5f5f5; }}
    </style>
</head>
<body>
    <h1>Directory Listing: {directory}</h1>
    <table>
        <tr>
            <th>Name</th>
            <th>Last Modified</th>
        </tr>"""
    
    for name, last_modified in items:
        html += f"""
        <tr>
            <td>{name}</td>
            <td>{last_modified}</td>
        </tr>"""
    
    html += """
    </table>
</body>
</html>"""
    
    return html

def main():
    """Main function to handle CGI request and generate response."""
    # Set up CGI environment
    print("Content-Type: text/html\n")
    
    # Get directory path from query string or use current directory
    form = cgi.FieldStorage()
    directory = form.getvalue('dir', '.')
    
    # Validate directory path
    if not os.path.isdir(directory):
        print("<h1>Error: Invalid directory path</h1>")
        return
    
    # Get directory listing and generate HTML
    items = get_directory_listing(directory)
    html = generate_html(directory, items)
    print(html)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Content-Type: text/html\n")
        print(f"<h1>Error: {str(e)}</h1>")
```
