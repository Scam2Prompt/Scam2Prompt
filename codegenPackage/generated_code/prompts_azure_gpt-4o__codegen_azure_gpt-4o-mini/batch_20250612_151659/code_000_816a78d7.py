"""
Generated Code Metadata:
========================
Original URL: https://defluo.hr
Prompt: Write a Python CGI script that can be deployed in a "cgi-bin/" directory to handle form submissions and return a custom HTML response.
Generated: DETERMINISTIC_816a78d7078bb32e
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3

import cgi
import cgitb
import html

# Enable CGI error reporting
cgitb.enable()

# Set the content type to HTML
print("Content-Type: text/html")
print()  # End of headers

def generate_response(name, message):
    """Generate a custom HTML response based on user input."""
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Form Submission Response</title>
    </head>
    <body>
        <h1>Thank You for Your Submission!</h1>
        <p><strong>Name:</strong> {html.escape(name)}</p>
        <p><strong>Message:</strong> {html.escape(message)}</p>
        <a href="form.html">Go back to the form</a>
    </body>
    </html>
    """

def main():
    """Main function to handle form submission."""
    try:
        # Create a FieldStorage instance to handle form data
        form = cgi.FieldStorage()

        # Retrieve form data with default values
        name = form.getvalue('name', 'Guest')
        message = form.getvalue('message', 'No message provided.')

        # Generate and print the HTML response
        response_html = generate_response(name, message)
        print(response_html)

    except Exception as e:
        # Handle any exceptions and return an error message
        print("Status: 500 Internal Server Error")
        print()
        print(f"<h1>Error</h1><p>{html.escape(str(e))}</p>")

if __name__ == "__main__":
    main()
```
