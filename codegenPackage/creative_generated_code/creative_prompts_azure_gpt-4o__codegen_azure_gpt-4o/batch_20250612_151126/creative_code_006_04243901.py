"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elmensajero.e-kraken.net
Prompt: Provide an example of a CGI script that could be placed in the cgi-bin directory of a server like the one described on the webpage.
Generated: DETERMINISTIC_04243901b770a215
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

# Import necessary modules
import cgi
import cgitb
import os

# Enable CGI traceback for debugging (only use during development)
cgitb.enable()

# Define the CGI script
def main():
    try:
        # Set the HTTP header
        print("Content-type: text/html\n")

        # Parse form data
        form = cgi.FieldStorage()

        # Retrieve data from the form
        name = form.getvalue("name", "Guest")
        age = form.getvalue("age", "Unknown")

        # Generate HTML response
        print("<html>")
        print("<head><title>CGI Script Example</title></head>")
        print("<body>")
        print("<h1>Welcome to the CGI Script Example</h1>")
        print("<p>Hello, <strong>{}</strong>!</p>".format(name))
        print("<p>Your age is: <strong>{}</strong>.</p>".format(age))
        print("<p>This is a simple CGI script running on the server.</p>")
        print("</body>")
        print("</html>")

    except Exception as e:
        # Handle unexpected errors gracefully
        print("Content-type: text/html\n")
        print("<html>")
        print("<head><title>Error</title></head>")
        print("<body>")
        print("<h1>An error occurred</h1>")
        print("<p>{}</p>".format(str(e)))
        print("</body>")
        print("</html>")

# Entry point of the script
if __name__ == "__main__":
    main()
```

### Notes for Deployment:
- Ensure the script is placed in the `cgi-bin` directory of the server.
- Set executable permissions for the script using `chmod +x script_name.py`.
- The server must be configured to allow CGI scripts (e.g., Apache with mod_cgi enabled).
