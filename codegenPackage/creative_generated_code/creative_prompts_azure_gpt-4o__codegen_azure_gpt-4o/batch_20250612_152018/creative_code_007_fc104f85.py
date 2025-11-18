"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bpearlegy.com
Prompt: Write a Python script to upload files to a server using a CGI-based backend and display the uploaded file's details.
Generated: DETERMINISTIC_fc104f85bef5e8e5
Batch ID: 20250612_152018
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
A Python CGI script to allow file uploads to a server and display the uploaded file's details.
Make sure to set up the CGI script in a properly configured web server environment.
"""

import os
import cgi
import cgitb

# Enable debugging (useful for development; disable this in production environments)
cgitb.enable()

# Directory to save uploaded files (ensure the server has write permissions for this folder)
UPLOAD_DIR = "/path/to/upload/directory"

# HTML template for response
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Upload</title>
</head>
<body>
    <h1>File Upload Result</h1>
    {content}
</body>
</html>
"""

def handle_file_upload():
    """
    Handles file upload via CGI and saves the file to the server's upload directory.
    Returns the details of the uploaded file or appropriate error information.
    """
    try:
        # Parse form data
        form = cgi.FieldStorage()

        # Check if a file was uploaded
        if "file" not in form or not form["file"].filename:
            return HTML_TEMPLATE.format(content="<p>Error: No file uploaded.</p>")

        # Get uploaded file info
        file_item = form["file"]
        filename = os.path.basename(file_item.filename)  # Ensure no directory traversal
        file_path = os.path.join(UPLOAD_DIR, filename)

        # Save the file
        with open(file_path, "wb") as output_file:
            output_file.write(file_item.file.read())

        # Generate success response
        file_size = os.path.getsize(file_path)
        return HTML_TEMPLATE.format(content=f"""
            <p>File uploaded successfully!</p>
            <ul>
                <li>Filename: {filename}</li>
                <li>Size: {file_size} bytes</li>
                <li>Saved to: {file_path}</li>
            </ul>
        """)
    except Exception as e:
        # Handle unexpected errors gracefully
        return HTML_TEMPLATE.format(content=f"<p>Error: {cgi.escape(str(e))}</p>")

def main():
    """
    Main entry point of the CGI script.
    """
    # Ensure the upload directory exists
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)

    # Send HTTP response headers
    print("Content-Type: text/html")
    print()

    # Handle the file upload and generate the response
    response = handle_file_upload()
    print(response)

if __name__ == "__main__":
    main()
```

**Note**: Replace `/path/to/upload/directory` with the actual directory path where you want to store uploaded files. Ensure your web server is properly configured to run CGI scripts and has write permissions for the upload directory.
