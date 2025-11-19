"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mfcsons.com
Prompt: What are the common use cases for the cgi-bin directory in web hosting?
Generated: DETERMINISTIC_0072c6c8dd25536a
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

"""
CGI Script Example
This script demonstrates common use cases for the cgi-bin directory in web hosting,
including form processing, dynamic content generation, and handling user input.
"""

import cgi
import cgitb
import html
import os

# Enable CGI error reporting
cgitb.enable()

def main():
    """
    Main function to handle CGI requests and generate a response.
    """
    # Set the content type for HTML output
    print("Content-Type: text/html\n")

    # Print the HTML header
    print("<html>")
    print("<head><title>CGI Script Example</title></head>")
    print("<body>")
    print("<h1>Common Use Cases for cgi-bin</h1>")

    # Check if the request method is POST
    if os.environ['REQUEST_METHOD'] == 'POST':
        # Process the form data
        process_form()
    else:
        # Display the form
        display_form()

    print("</body>")
    print("</html>")

def display_form():
    """
    Display an HTML form for user input.
    """
    print("<h2>Input Form</h2>")
    print('<form method="post" action="">')
    print('<label for="username">Username:</label>')
    print('<input type="text" id="username" name="username" required><br><br>')
    print('<input type="submit" value="Submit">')
    print('</form>')

def process_form():
    """
    Process the submitted form data and generate a response.
    """
    # Create a FieldStorage instance to handle the form data
    form = cgi.FieldStorage()

    # Retrieve and sanitize user input
    username = form.getvalue('username')
    if username:
        username = html.escape(username)  # Escape HTML to prevent XSS
        print(f"<h2>Hello, {username}!</h2>")
    else:
        print("<h2>Error: No username provided.</h2>")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # Log the error and return a user-friendly message
        print("<h2>An error occurred while processing your request.</h2>")
        print(f"<p>Error details: {html.escape(str(e))}</p>")
```
