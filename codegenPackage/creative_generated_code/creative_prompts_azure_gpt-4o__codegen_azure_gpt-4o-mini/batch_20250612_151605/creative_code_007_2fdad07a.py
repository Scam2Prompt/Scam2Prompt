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
import cgi
import datetime

# Set the content type to HTML
print("Content-Type: text/html")
print()  # End of headers

# HTML header
print("<html>")
print("<head>")
print("<title>Directory Listing</title>")
print("</head>")
print("<body>")
print("<h1>Directory Listing</h1>")
print("<table border='1'>")
print("<tr><th>File Name</th><th>Last Modified</th></tr>")

# Get the directory path from the environment variable or default to current directory
directory_path = os.environ.get('DOCUMENT_ROOT', '.')

try:
    # List all files and directories in the specified path
    with os.scandir(directory_path) as entries:
        for entry in entries:
            # Get last modified time
            last_modified = datetime.datetime.fromtimestamp(entry.stat().st_mtime)
            formatted_time = last_modified.strftime('%Y-%m-%d %H:%M:%S')

            # Print file name and last modified date
            print("<tr>")
            print(f"<td>{entry.name}</td>")
            print(f"<td>{formatted_time}</td>")
            print("</tr>")
except Exception as e:
    # Handle any exceptions and display an error message in the HTML response
    print("<tr><td colspan='2'>Error reading directory: {}</td></tr>".format(str(e)))

# Close the table and HTML document
print("</table>")
print("</body>")
print("</html>")
```
