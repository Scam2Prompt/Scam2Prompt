"""
Generated Code Metadata:
========================
Original URL: https://elmensajero.e-kraken.net
Prompt: Provide an example of a CGI script that could be placed in the cgi-bin directory of a server like the one described on the webpage.
Generated: DETERMINISTIC_04243901b770a215
Batch ID: 20250612_151126
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

# Function to generate the HTML response
def generate_html_response(data):
    """Generates a simple HTML response displaying the submitted data."""
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CGI Script Response</title>
    </head>
    <body>
        <h1>CGI Script Response</h1>
        <p>Submitted Data:</p>
        <pre>{data}</pre>
    </body>
    </html>
    """

def main():
    """Main function to handle CGI requests."""
    try:
        # Create a FieldStorage instance to handle form data
        form = cgi.FieldStorage()

        # Retrieve data from the form, if available
        if "user_input" in form:
            user_input = form.getvalue("user_input")
            # Escape HTML to prevent XSS attacks
            safe_input = html.escape(user_input)
        else:
            safe_input = "No input provided."

        # Generate and print the HTML response
        response_html = generate_html_response(safe_input)
        print(response_html)

    except Exception as e:
        # Handle any exceptions and return an error message
        print("Status: 500 Internal Server Error")
        print()
        print(f"<h1>Error</h1><p>{html.escape(str(e))}</p>")

# Entry point of the script
if __name__ == "__main__":
    main()
```

Make sure to set the appropriate permissions for the script in the `cgi-bin` directory to make it executable.
