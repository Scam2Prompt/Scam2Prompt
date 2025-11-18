"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bpearlegy.com
Prompt: Recommend libraries for creating and managing CGI scripts in Python, and provide an example of a basic CGI script.
Generated: DETERMINISTIC_4fa2fbd819640c03
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
Basic CGI Script Example
This script demonstrates how to create a simple CGI script using Python.
It outputs a basic HTML page with a greeting message.
"""

import os
import cgi
import cgitb

# Enable CGI error reporting
cgitb.enable()

def main():
    """Main function to handle the CGI request."""
    # Set the content type to HTML
    print("Content-Type: text/html")
    print()  # End of headers

    # Create an instance of FieldStorage to handle form data
    form = cgi.FieldStorage()

    # Get the name parameter from the URL query or use a default
    name = form.getvalue('name', 'World')

    # Generate HTML response
    print(f"""
    <html>
    <head>
        <title>CGI Script Example</title>
    </head>
    <body>
        <h1>Hello, {cgi.escape(name)}!</h1>
        <p>Welcome to the CGI script example.</p>
    </body>
    </html>
    """)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # Log the error and display an error message
        print("Status: 500 Internal Server Error")
        print()
        print(f"<html><body><h1>Error: {cgi.escape(str(e))}</h1></body></html>")
```

### Recommended Libraries for Creating and Managing CGI Scripts in Python:
- Built-in `cgi` module: For parsing form data and handling CGI requests.
- `cgitb` module: For enhanced error reporting in CGI scripts.
- `os` module: For interacting with the operating system (optional, based on needs).
