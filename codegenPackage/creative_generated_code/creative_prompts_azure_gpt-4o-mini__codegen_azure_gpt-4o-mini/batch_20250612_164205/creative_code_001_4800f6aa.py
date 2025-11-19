"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mfcsons.com
Prompt: Can you provide a code snippet for setting up a CGI script in the cgi-bin directory?
Generated: DETERMINISTIC_4800f6aaaf1ad4aa
Batch ID: 20250612_164205
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
import cgitb
import os

# Enable CGI error reporting
cgitb.enable()

# Set the content type to text/html
print("Content-Type: text/html")
print()  # End of headers

def main():
    """Main function to handle CGI requests."""
    try:
        # Parse form data received from a client
        form = cgi.FieldStorage()

        # Get the value of an input field named 'name'
        name = form.getvalue('name', 'World')  # Default to 'World' if not provided

        # HTML response
        print("<html>")
        print("<head>")
        print("<title>CGI Script Response</title>")
        print("</head>")
        print("<body>")
        print(f"<h1>Hello, {name}!</h1>")
        print("<p>This is a simple CGI script.</p>")
        print("</body>")
        print("</html>")
    
    except Exception as e:
        # Handle exceptions and output error message
        print("<html>")
        print("<head>")
        print("<title>Error</title>")
        print("</head>")
        print("<body>")
        print("<h1>Error occurred</h1>")
        print(f"<p>{str(e)}</p>")
        print("</body>")
        print("</html>")

if __name__ == "__main__":
    main()
```

Make sure to set the correct permissions for the script to be executable in the `cgi-bin` directory. You can do this by running:
```bash
chmod 755 your_script_name.py
```
