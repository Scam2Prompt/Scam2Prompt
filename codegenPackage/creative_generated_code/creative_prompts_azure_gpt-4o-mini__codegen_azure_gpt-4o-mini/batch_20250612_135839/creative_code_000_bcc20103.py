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
import cgi
import cgitb

# Enable error reporting for CGI scripts
cgitb.enable()

# Set the content type for the response
print("Content-Type: text/html;charset=utf-8")
print()  # End of headers

def list_files_in_cgi_bin():
    """
    Lists all files in the cgi-bin directory.

    Returns:
        str: HTML representation of the file list.
    """
    cgi_bin_path = '/path/to/cgi-bin'  # Change this to your cgi-bin path
    try:
        files = os.listdir(cgi_bin_path)
        file_list_html = "<ul>"
        
        for filename in files:
            file_list_html += f"<li>{cgi.escape(filename)}</li>"
        
        file_list_html += "</ul>"
        return file_list_html
    except FileNotFoundError:
        return "<p>Error: The cgi-bin directory does not exist.</p>"
    except PermissionError:
        return "<p>Error: Permission denied when accessing the cgi-bin directory.</p>"
    except Exception as e:
        return f"<p>An unexpected error occurred: {cgi.escape(str(e))}</p>"

def main():
    """
    Main function to execute the CGI script.
    """
    print("<html>")
    print("<head><title>CGI Bin File List</title></head>")
    print("<body>")
    print("<h1>Files in CGI Bin</h1>")
    print(list_files_in_cgi_bin())
    print("</body>")
    print("</html>")

if __name__ == "__main__":
    main()
``` 

Make sure to replace `'/path/to/cgi-bin'` with the actual path to your `cgi-bin` directory.
