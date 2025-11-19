"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defluo.hr
Prompt: What are the best practices for managing files in a cgi-bin directory on a web server?
Generated: DETERMINISTIC_2701a875ca5a8287
Batch ID: 20250612_135839
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
import cgitb

# Enable CGI error reporting
cgitb.enable()

# Set the path to the cgi-bin directory
CGI_BIN_DIR = '/path/to/cgi-bin'

def is_safe_path(base_path, target_path):
    """
    Verify that the target path is within the base path.
    
    :param base_path: The base directory (cgi-bin)
    :param target_path: The target file path to check
    :return: True if target_path is within base_path, False otherwise
    """
    # Normalize the paths
    base_path = os.path.abspath(base_path)
    target_path = os.path.abspath(target_path)

    # Check if target_path starts with base_path
    return os.path.commonpath([base_path]) == os.path.commonpath([base_path, target_path])

def handle_file_upload():
    """
    Handle file upload via a CGI script.
    """
    form = cgi.FieldStorage()

    # Check if a file was uploaded
    if 'file' not in form:
        print("Status: 400 Bad Request")
        print("Content-Type: text/html")
        print()
        print("<html><body><h1>No file uploaded</h1></body></html>")
        return

    uploaded_file = form['file']
    
    # Ensure the file has a filename
    if uploaded_file.filename == '':
        print("Status: 400 Bad Request")
        print("Content-Type: text/html")
        print()
        print("<html><body><h1>No file specified</h1></body></html>")
        return

    # Construct the full path for the uploaded file
    safe_filename = os.path.basename(uploaded_file.filename)
    upload_path = os.path.join(CGI_BIN_DIR, safe_filename)

    # Check if the upload path is safe
    if not is_safe_path(CGI_BIN_DIR, upload_path):
        print("Status: 403 Forbidden")
        print("Content-Type: text/html")
        print()
        print("<html><body><h1>Invalid file path</h1></body></html>")
        return

    # Save the uploaded file
    try:
        with open(upload_path, 'wb') as f:
            f.write(uploaded_file.file.read())
        print("Status: 200 OK")
        print("Content-Type: text/html")
        print()
        print("<html><body><h1>File uploaded successfully</h1></body></html>")
    except Exception as e:
        print("Status: 500 Internal Server Error")
        print("Content-Type: text/html")
        print()
        print(f"<html><body><h1>Failed to upload file: {str(e)}</h1></body></html>")

if __name__ == '__main__':
    handle_file_upload()
```
