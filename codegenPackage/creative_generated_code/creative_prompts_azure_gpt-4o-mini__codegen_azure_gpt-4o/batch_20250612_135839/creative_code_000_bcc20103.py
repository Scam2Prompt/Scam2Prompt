"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defluo.hr
Prompt: Generate a Python script that interacts with the cgi-bin directory on a web server.
Generated: DETERMINISTIC_bcc2010393931cb6
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
import sys
import cgi
import cgitb

# Enable detailed error reporting for debugging (disable in production by removing or commenting out this line)
cgitb.enable()

# Set the content header for the response
print("Content-Type: text/html\n")

# Function to list files in the cgi-bin directory
def list_cgi_bin_files():
    try:
        # Get the path to the cgi-bin directory relative to the script's execution directory
        cgi_bin_path = os.path.join(os.getcwd(), "cgi-bin")
        
        # Ensure the cgi-bin directory exists
        if not os.path.exists(cgi_bin_path):
            raise FileNotFoundError("The cgi-bin directory does not exist.")

        # List all files in the cgi-bin directory
        files = os.listdir(cgi_bin_path)

        # Filter only regular files
        files = [f for f in files if os.path.isfile(os.path.join(cgi_bin_path, f))]

        return files
    except Exception as e:
        # Handle errors and return an error message
        return f"Error accessing cgi-bin directory: {str(e)}"

# Main function to handle the CGI request
def main():
    try:
        # Parse CGI input using cgi.FieldStorage
        form = cgi.FieldStorage()

        # Retrieve any parameters passed via the form
        action = form.getvalue('action', None)

        # If action is list, list files in the cgi-bin directory
        if action == "list":
            files = list_cgi_bin_files()
            if isinstance(files, str):  # Error occurred
                print(f"<h1>Error</h1><p>{files}</p>")
            else:
                print("<h1>Files in cgi-bin Directory</h1>")
                print("<ul>")
                for file in files:
                    print(f"<li>{file}</li>")
                print("</ul>")
        else:
            # Default response for invalid or missing action parameter
            print("<h1>Welcome to CGI-bin Interface</h1>")
            print("<p>Use the 'action=list' parameter to list files in the cgi-bin directory.</p>")
    except Exception as e:
        # Catch any unexpected exceptions and display an error message
        print("<h1>Internal Server Error</h1>")
        print(f"<p>{str(e)}</p>")

# Entry point for the script
if __name__ == "__main__":
    main()
```
