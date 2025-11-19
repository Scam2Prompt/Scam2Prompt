"""
Generated Code Metadata:
========================
Original URL: https://nkftransporte.com
Prompt: Create a CGI script that could be placed in the `cgi-bin` directory to dynamically generate a directory listing similar to the one shown on nkftransporte.com.
Generated: DETERMINISTIC_018cc0c312943b54
Batch ID: 20250612_152439
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
CGI script to dynamically generate a directory listing.

Usage:
    Place this script in the cgi-bin directory of your web server.

Requirements:
    Python 3.x
    cgi
    os
    mimetypes
    datetime

Notes:
    This script assumes that the cgi-bin directory is not the directory being listed.
    The script lists files and directories in the current working directory.
"""

import cgi
import os
import mimetypes
from datetime import datetime

def get_directory_listing(path="."):
    """
    Returns a list of files and directories in the given path.

    Args:
        path (str): The path to list.

    Returns:
        list: A list of dictionaries containing file information.
    """
    try:
        listing = []
        for filename in os.listdir(path):
            filepath = os.path.join(path, filename)
            stat = os.stat(filepath)
            file_type = mimetypes.guess_type(filepath)[0] or "Unknown"
            modified = datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M")

            if os.path.isdir(filepath):
                file_type = "Directory"
            else:
                file_type = mimetypes.guess_type(filepath)[0] or "Unknown"

            listing.append({
                "filename": filename,
                "filepath": filepath,
                "file_type": file_type,
                "modified": modified,
                "size": stat.st_size
            })
        return listing
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return []

def cgi_output(listing):
    """
    Outputs the directory listing in a CGI-friendly format.

    Args:
        listing (list): A list of dictionaries containing file information.
    """
    print("Content-type: text/html\n\n")
    print("<html>")
    print("<head>")
    print("<title>Directory Listing</title>")
    print("</head>")
    print("<body>")
    print("<h1>Directory Listing</h1>")
    print("<table border='1'>")
    print("<tr>")
    print("<th>Filename</th>")
    print("<th>Type</th>")
    print("<th>Modified</th>")
    print("<th>Size</th>")
    print("</tr>")

    for file in listing:
        print("<tr>")
        print(f"<td><a href='{file['filepath']}'>{file['filename']}</a></td>")
        print(f"<td>{file['file_type']}</td>")
        print(f"<td>{file['modified']}</td>")
        print(f"<td>{file['size']}</td>")
        print("</tr>")

    print("</table>")
    print("</body>")
    print("</html>")

if __name__ == "__main__":
    import sys
    listing = get_directory_listing()
    cgi_output(listing)
```
