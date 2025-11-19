"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elmensajero.e-kraken.net
Prompt: How can I use Python to interact with the cgi-bin directory on the e-Kraken web server?
Generated: DETERMINISTIC_5741222c2acccb8a
Batch ID: 20250612_140024
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

# Set the content type to HTML
print("Content-Type: text/html")
print()  # End of headers

def main():
    """
    Main function to handle CGI interaction with e-Kraken web server's cgi-bin directory.
    """

    # CGI form handling
    form = cgi.FieldStorage()

    # Check for specific input, e.g., a file name to read
    filename = form.getvalue('filename')

    if filename:
        # Sanitize the filename to prevent directory traversal
        if not is_safe_filename(filename):
            print("<h1>Error: Invalid filename</h1>")
            return
        
        # Construct the full path to the file
        file_path = os.path.join('cgi-bin', filename)

        try:
            # Check if the file exists and read its contents
            if os.path.isfile(file_path):
                with open(file_path, 'r') as file:
                    file_content = file.read()
                    print("<h1>File Content:</h1>")
                    print("<pre>{}</pre>".format(cgi.escape(file_content)))  # Escape HTML
            else:
                print("<h1>Error: File does not exist</h1>")
        except Exception as e:
            print("<h1>Error: Could not read file</h1>")
            print("<p>{}</p>".format(str(e)))

def is_safe_filename(filename):
    """
    Check if the filename is safe to use.
    
    :param filename: The filename to check.
    :return: True if the filename is safe, False otherwise.
    """
    # Allow only alphanumeric filenames and underscores
    return all(c.isalnum() or c == '_' for c in filename)

if __name__ == "__main__":
    main()
```

Make sure to set executable permissions for this script and place it in the appropriate `cgi-bin` directory on your e-Kraken web server.
