"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bpearlegy.com
Prompt: What are the common uses of the cgi-bin directory in web development?
Generated: DETERMINISTIC_d172fb3eb7f3b5f6
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
CGI Script Example: This script demonstrates a common use of the cgi-bin directory
in web development by processing form data and returning a simple HTML response.
"""

import os
import cgi
import cgitb

# Enable CGI error reporting
cgitb.enable()

# Define the content type for the HTTP response
print("Content-Type: text/html")  # HTTP header
print()  # Blank line required after the header

def main():
    """Main function to handle CGI form submission."""
    try:
        # Create a FieldStorage instance to handle form data
        form = cgi.FieldStorage()

        # Get value from the form, with a default if not provided
        name = form.getvalue("name", "World")

        # Generate a simple HTML response
        print("<html>")
        print("<head>")
        print("<title>CGI Example</title>")
        print("</head>")
        print("<body>")
        print(f"<h1>Hello, {name}!</h1>")
        print("<p>This CGI script demonstrates form handling.</p>")
        print("</body>")
        print("</html>")
    
    except Exception as e:
        # Handle unexpected errors
        print("<html>")
        print("<head>")
        print("<title>Error</title>")
        print("</head>")
        print("<body>")
        print("<h1>An error occurred</h1>")
        print(f"<p>{str(e)}</p>")
        print("</body>")
        print("</html>")

if __name__ == "__main__":
    # Execute the main function
    main()
```

### Usage Instructions
- Save this script in the `cgi-bin` directory on your web server.
- Ensure that the script is executable (`chmod +x script_name.py`).
- Access the script through a web browser to see the output.
- You can create an HTML form that targets this script to test form submission.
