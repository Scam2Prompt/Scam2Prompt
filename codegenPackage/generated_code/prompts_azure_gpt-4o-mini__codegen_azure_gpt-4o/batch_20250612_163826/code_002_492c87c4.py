"""
Generated Code Metadata:
========================
Original URL: https://groupists.com
Prompt: How can I implement a CGI script to manage file listings in a directory structure as seen on groupists.com?
Generated: DETERMINISTIC_492c87c49d6d2c61
Batch ID: 20250612_163826
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
CGI Script to manage file listings in a directory structure.
This script lists files and directories in a specified path and displays them in an HTML format.
"""

import os
import cgi
import cgitb

# Enable CGI traceback for debugging
cgitb.enable()

# HTML template for the response
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Directory Listing</title>
    <style>
        body {{ font-family: Arial, sans-serif; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; }}
        th {{ background-color: #f4f4f4; }}
        a {{ text-decoration: none; color: blue; }}
    </style>
</head>
<body>
    <h1>Directory Listing</h1>
    <p>Path: {path}</p>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Type</th>
                <th>Size (Bytes)</th>
            </tr>
        </thead>
        <tbody>
            {rows}
        </tbody>
    </table>
</body>
</html>
"""

def generate_file_listing(path):
    """
    Generate HTML rows for files and directories in the given path.

    Args:
        path (str): The directory path to list.

    Returns:
        str: HTML rows for the files and directories.
    """
    rows = []
    try:
        # List all files and directories in the specified path
        for entry in os.scandir(path):
            name = entry.name
            if entry.is_file():
                file_type = "File"
                size = entry.stat().st_size
            elif entry.is_dir():
                file_type = "Directory"
                size = "-"
            else:
                file_type = "Other"
                size = "-"
            
            # Create a row for the current entry
            rows.append(f"<tr><td><a href='{name}'>{name}</a></td><td>{file_type}</td><td>{size}</td></tr>")
    except Exception as e:
        # Handle errors gracefully
        rows.append(f"<tr><td colspan='3'>Error: {str(e)}</td></tr>")
    return "\n".join(rows)

def main():
    """
    Main function to handle the CGI request and generate the response.
    """
    # Parse CGI parameters
    form = cgi.FieldStorage()
    path = form.getvalue("path", ".")  # Default to current directory if no path is provided

    # Validate the path
    if not os.path.exists(path):
        print("Content-Type: text/html\n")
        print("<h1>Error: Path does not exist</h1>")
        return

    # Generate the file listing
    rows = generate_file_listing(path)

    # Generate the final HTML response
    html_content = HTML_TEMPLATE.format(path=path, rows=rows)

    # Output the response
    print("Content-Type: text/html\n")
    print(html_content)

if __name__ == "__main__":
    main()
```
