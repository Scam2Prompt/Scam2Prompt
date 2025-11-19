"""
Generated Code Metadata:
========================
Original URL: https://defluo.hr
Prompt: Generate a Python script that interacts with the cgi-bin directory on a web server.
Generated: DETERMINISTIC_bcc2010393931cb6
Batch ID: 20250612_135839
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3

import cgi
import os
import sys
import logging

# Set up logging for error tracking
logging.basicConfig(filename='cgi_script.log', level=logging.ERROR)

def main():
    try:
        # Set the content type for the response
        print("Content-Type: text/html")    # HTML is following
        print()                              # Blank line required to end headers

        # Parse the form data
        form = cgi.FieldStorage()

        # Get the action from the form data
        action = form.getvalue('action', 'default')

        # Handle different actions
        if action == 'list_files':
            list_files()
        elif action == 'upload_file':
            upload_file(form)
        else:
            print("<h1>Invalid action specified.</h1>")

    except Exception as e:
        logging.error("An error occurred: %s", e)
        print("<h1>An error occurred while processing your request.</h1>")

def list_files():
    """List files in the cgi-bin directory."""
    cgi_bin_path = os.path.dirname(os.path.abspath(__file__))
    try:
        files = os.listdir(cgi_bin_path)
        print("<h1>Files in cgi-bin:</h1>")
        print("<ul>")
        for file in files:
            print(f"<li>{file}</li>")
        print("</ul>")
    except OSError as e:
        logging.error("Failed to list files: %s", e)
        print("<h1>Failed to list files.</h1>")

def upload_file(form):
    """Handle file upload from the form."""
    if 'file' not in form:
        print("<h1>No file uploaded.</h1>")
        return

    file_item = form['file']
    
    # Check if the file was uploaded
    if file_item.filename:
        # Define the path to save the uploaded file
        upload_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_item.filename)
        
        try:
            # Save the uploaded file
            with open(upload_path, 'wb') as f:
                f.write(file_item.file.read())
            print(f"<h1>File '{file_item.filename}' uploaded successfully.</h1>")
        except Exception as e:
            logging.error("Failed to upload file: %s", e)
            print("<h1>Failed to upload file.</h1>")
    else:
        print("<h1>No file was uploaded.</h1>")

if __name__ == "__main__":
    main()
```

Make sure to set the appropriate permissions for this script to be executable on your web server and ensure that the web server is configured to allow CGI scripts to run.
