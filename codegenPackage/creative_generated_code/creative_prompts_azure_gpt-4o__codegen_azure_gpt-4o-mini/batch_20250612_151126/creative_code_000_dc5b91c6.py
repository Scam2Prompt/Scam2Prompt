"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elmensajero.e-kraken.net
Prompt: Write a Python script to interact with a CGI-bin directory on a server, using the structure described in the webpage.
Generated: DETERMINISTIC_dc5b91c6ab7051da
Batch ID: 20250612_151126
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

def main():
    """Main function to handle CGI requests and interact with a CGI-bin directory."""
    
    # Set the response content type
    print("Content-Type: text/html")
    print()  # End of headers

    try:
        # Parse the form data received from the client
        form = cgi.FieldStorage()

        # Example of fetching a parameter from the form
        action = form.getvalue('action', 'default')
        
        # Process based on the action parameter
        if action == "list_files":
            list_files()
        elif action == "upload_file":
            upload_file(form)
        else:
            print("<h1>Welcome to the CGI-bin Directory</h1>")
            print("<p>Use 'action=list_files' to list files or 'action=upload_file' to upload a file.</p>")

    except Exception as e:
        # Handle any unexpected errors
        print("<h1>Error occurred</h1>")
        print(f"<p>{str(e)}</p>")

def list_files():
    """List files in the CGI-bin directory."""
    
    # Define the directory for the CGI-bin
    cgi_bin_dir = '/path/to/cgi-bin'

    try:
        # Fetch the list of files in the specified directory
        files = os.listdir(cgi_bin_dir)

        print("<h2>Files in CGI-bin:</h2>")
        print("<ul>")
        for file in files:
            print(f"<li>{file}</li>")
        print("</ul>")
        
    except FileNotFoundError:
        print("<h1>Error: CGI-bin directory not found!</h1>")
    except PermissionError:
        print("<h1>Error: Permission denied while accessing the CGI-bin directory!</h1>")
    except Exception as e:
        print(f"<h1>An unexpected error occurred:</h1><p>{str(e)}</p>")

def upload_file(form):
    """Handle file uploads to the CGI-bin directory."""
    
    # Define the directory for uploading files
    cgi_bin_dir = '/path/to/cgi-bin'
    
    if 'file' not in form:
        print("<h1>Error: No file part in the request!</h1>")
        return

    file_item = form['file']
    
    if file_item.filename:
        filepath = os.path.join(cgi_bin_dir, os.path.basename(file_item.filename))
        
        try:
            # Open the file in binary write mode and save it
            with open(filepath, 'wb') as f:
                f.write(file_item.file.read())
            print(f"<h1>File '{file_item.filename}' uploaded successfully!</h1>")
        except Exception as e:
            print(f"<h1>Upload failed:</h1><p>{str(e)}</p>")
    else:
        print("<h1>Error: No file selected for upload!</h1>")

if __name__ == '__main__':
    main()
```
