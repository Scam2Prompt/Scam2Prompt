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

import cgi
import cgitb
import os

# Enable error reporting for debugging purposes
cgitb.enable()

# Set the content type for the response to be HTML
print("Content-Type: text/html")    # HTML is following
print()                              # End of headers

def main():
    """
    Main function to handle the CGI request.
    Processes form data and generates an HTML response.
    """
    try:
        # Create an instance of FieldStorage to handle incoming data
        form = cgi.FieldStorage()

        # Retrieve form data; if not found, use default values
        name = form.getvalue('name', 'Guest')
        age = form.getvalue('age', 'unknown')

        # Generate the HTML response
        print("<html>")
        print("<head><title>CGI Script Response</title></head>")
        print("<body>")
        print("<h1>Hello, {}!</h1>".format(name))
        print("<p>Your age is: {}</p>".format(age))
        print("</body>")
        print("</html>")
        
    except Exception as e:
        # Handle exceptions and print error message in HTML format
        print("<html>")
        print("<head><title>Error</title></head>")
        print("<body>")
        print("<h1>Error occurred</h1>")
        print("<p>{}</p>".format(str(e)))
        print("</body>")
        print("</html>")

# Execute the main function
if __name__ == "__main__":
    main()
```

Make sure to set the appropriate permissions for this script to be executable in your `cgi-bin` directory, and configure your web server correctly to support CGI.
