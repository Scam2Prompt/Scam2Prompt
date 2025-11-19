"""
Generated Code Metadata:
========================
Original URL: https://mfcsons.com
Prompt: What are the common use cases for the cgi-bin directory in web hosting?
Generated: DETERMINISTIC_0072c6c8dd25536a
Batch ID: 20250612_164205
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to demonstrate common use cases for the cgi-bin directory in web hosting.

This script is a simple CGI program written in Python. It showcases:
1. Dynamic content generation
2. Form handling
3. Interaction with server-side resources

To use this script, place it in the cgi-bin directory of your web server and ensure
the server is configured to execute CGI scripts.
"""

import os
import cgi
import cgitb

# Enable CGI traceback for debugging (only use in development, disable in production)
cgitb.enable()

def main():
    try:
        # Print HTTP headers
        print("Content-Type: text/html")
        print()  # Blank line to separate headers from content

        # Generate dynamic HTML content
        print("<html>")
        print("<head><title>CGI-bin Use Case Example</title></head>")
        print("<body>")
        print("<h1>Welcome to the CGI-bin Use Case Example</h1>")

        # Example 1: Display server environment variables
        print("<h2>Server Environment Variables</h2>")
        print("<ul>")
        for key, value in os.environ.items():
            print(f"<li><b>{key}:</b> {value}</li>")
        print("</ul>")

        # Example 2: Handle form submission
        print("<h2>Form Submission Example</h2>")
        print("""
        <form method="post" action="">
            <label for="name">Enter your name:</label>
            <input type="text" id="name" name="name">
            <input type="submit" value="Submit">
        </form>
        """)

        # Parse form data
        form = cgi.FieldStorage()
        if "name" in form:
            name = form.getvalue("name")
            print(f"<p>Hello, <b>{name}</b>! Thank you for submitting the form.</p>")

        print("</body>")
        print("</html>")

    except Exception as e:
        # Handle errors gracefully
        print("Content-Type: text/html")
        print()
        print("<html>")
        print("<head><title>Error</title></head>")
        print("<body>")
        print("<h1>An error occurred</h1>")
        print(f"<p>{str(e)}</p>")
        print("</body>")
        print("</html>")

# Entry point for the CGI script
if __name__ == "__main__":
    main()
```
