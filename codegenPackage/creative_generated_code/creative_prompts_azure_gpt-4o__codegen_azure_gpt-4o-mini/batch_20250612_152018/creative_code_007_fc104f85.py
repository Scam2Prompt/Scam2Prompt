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

import cgi
import os
import sys

# Set the upload directory
UPLOAD_DIR = '/path/to/upload/directory'

def save_uploaded_file(form_field):
    """Save the uploaded file to the specified upload directory."""
    try:
        # Ensure the upload directory exists
        os.makedirs(UPLOAD_DIR, exist_ok=True)

        # Get the uploaded file details
        uploaded_file = form_field['file']
        file_name = uploaded_file.filename

        # Path where the file will be saved
        file_path = os.path.join(UPLOAD_DIR, file_name)

        # Open the destination file in binary write mode
        with open(file_path, 'wb') as output_file:
            # Read and write the uploaded file content in chunks
            while True:
                chunk = uploaded_file.file.read(1024)  # Read in 1KB chunks
                if not chunk:
                    break
                output_file.write(chunk)

        return file_name, file_path

    except Exception as e:
        print("Content-Type: text/html")
        print()
        print("<html><body>")
        print(f"<h1>Error: {str(e)}</h1>")
        print("</body></html>")
        sys.exit(1)

def generate_response(file_name, file_path):
    """Generate the HTML response to display uploaded file details."""
    print("Content-Type: text/html")
    print()
    print("<html><body>")
    print("<h1>File Uploaded Successfully!</h1>")
    print(f"<p>File Name: {file_name}</p>")
    print(f"<p>File Path: {file_path}</p>")
    print("</body></html>")

def main():
    """Main function to handle the file upload."""
    # Parse the form data
    form = cgi.FieldStorage()
    
    # Check if the file field is present
    if 'file' not in form:
        print("Content-Type: text/html")
        print()
        print("<html><body>")
        print("<h1>Error: No file uploaded.</h1>")
        print("</body></html>")
        return

    # Save the uploaded file and get its details
    file_name, file_path = save_uploaded_file(form)
    
    # Generate the response to show the file details
    generate_response(file_name, file_path)

if __name__ == "__main__":
    main()
```

**Note:** Make sure to replace `'/path/to/upload/directory'` with the actual path where you want to store the uploaded files. Additionally, ensure that the server has the proper permissions to write to the specified directory.
