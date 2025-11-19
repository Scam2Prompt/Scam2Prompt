"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://refconegypt.net
Prompt: How can I create a script for the cgi-bin directory as referenced on refconegypt.net?
Generated: DETERMINISTIC_b468f643d28f71f3
Batch ID: 20250612_160720
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
CGI Script for the cgi-bin directory.
This script demonstrates creating a basic CGI application to handle HTTP requests.

Usage:
Place this script in the `cgi-bin` directory and ensure it has executable permissions.
Access it via a browser or HTTP client through the server running on refconegypt.net.

Best Practices:
1. Ensure proper file permissions (chmod +x script_name.py).
2. Validate and sanitize user input to prevent security vulnerabilities.
3. Implement comprehensive error handling to handle unexpected issues gracefully.
"""

import os
import cgi
import cgitb

# Enable CGI traceback for debugging (should be disabled in production for security)
cgitb.enable()

def main():
    """
    Main function that handles incoming CGI requests.
    """
    try:
        # Set HTTP headers
        print("Content-Type: text/html")  # HTML content
        print("")  # Blank line to separate headers from the content

        # Parse CGI form data
        form = cgi.FieldStorage()

        # Extract data from the form
        name = form.getvalue("name", "Guest")  # Default to 'Guest' if no 'name' provided
        age = form.getvalue("age", "unknown")  # Default to 'unknown' if no 'age' provided

        # Generate response
        print("<html>")
        print("<head><title>CGI Script Response</title></head>")
        print("<body>")
        print("<h1>Welcome to the CGI Script!</h1>")
        print(f"<p>Hello, {name}! Your age is {age}.</p>")
        print("</body>")
        print("</html>")
    
    except Exception as e:
        # Handle any unexpected errors
        print("Content-Type: text/html")
        print("")
        print("<html>")
        print("<head><title>Error</title></head>")
        print("<body>")
        print("<h1>An error occurred!</h1>")
        print(f"<p>Error details: {str(e)}</p>")
        print("</body>")
        print("</html>")

# Ensure the script runs only when accessed as a CGI application
if __name__ == "__main__":
    main()
```
