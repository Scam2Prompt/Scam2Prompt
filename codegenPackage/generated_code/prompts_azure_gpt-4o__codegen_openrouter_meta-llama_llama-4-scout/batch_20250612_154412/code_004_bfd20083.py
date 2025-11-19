"""
Generated Code Metadata:
========================
Original URL: https://8lements.xyz
Prompt: Create a Python script to automate the generation of directory listings for a web server, mimicking the structure seen on 8lements.xyz.
Generated: DETERMINISTIC_bfd2008376edc258
Batch ID: 20250612_154412
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
Directory Listing Generator
==========================

Generates directory listings for a web server, mimicking the structure seen on 8lements.xyz.

Usage:
    python directory_lister.py /path/to/directory

Author: [Your Name]
Date: [Today's Date]
"""

import os
import argparse
from datetime import datetime
from mimetypes import guess_type

def get_directory_listing(directory):
    """
    Generates a directory listing for the given directory.

    Args:
        directory (str): The path to the directory to list.

    Returns:
        list: A list of tuples containing file information.
    """
    try:
        files = os.listdir(directory)
        file_info = []

        for filename in files:
            filepath = os.path.join(directory, filename)
            file_type, _ = guess_type(filename)
            file_size = os.path.getsize(filepath)
            modified_date = datetime.fromtimestamp(os.path.getmtime(filepath))

            file_info.append({
                'name': filename,
                'type': file_type,
                'size': file_size,
                'modified': modified_date
            })

        return file_info

    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found.")
        return []
    except PermissionError:
        print(f"Error: Permission denied for directory '{directory}'.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def generate_html_listing(directory, file_info):
    """
    Generates an HTML directory listing for the given directory and file information.

    Args:
        directory (str): The path to the directory being listed.
        file_info (list): A list of tuples containing file information.
    """
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Directory Listing</title>
        <style>
            body {
                font-family: monospace;
            }
            table {
                border-collapse: collapse;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }
        </style>
    </head>
    <body>
        <h1>Directory Listing for {directory}</h1>
        <table>
            <tr>
                <th>Name</th>
                <th>Type</th>
                <th>Size</th>
                <th>Modified</th>
            </tr>
    """

    for file in file_info:
        html += f"""
            <tr>
                <td><a href="{file['name']}">{file['name']}</a></td>
                <td>{file['type'] or 'Unknown'}</td>
                <td>{file['size']}</td>
                <td>{file['modified'].strftime('%Y-%m-%d %H:%M:%S')}</td>
            </tr>
        """

    html += """
        </table>
    </body>
    </html>
    """

    return html.format(directory=directory)

def main():
    parser = argparse.ArgumentParser(description='Generate a directory listing.')
    parser.add_argument('directory', help='the directory to list')
    args = parser.parse_args()

    file_info = get_directory_listing(args.directory)
    if file_info:
        html_listing = generate_html_listing(args.directory, file_info)
        print(html_listing)

if __name__ == '__main__':
    main()
```
