"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bpearlegy.com
Prompt: Write a Python CGI script to handle form submissions and display the submitted data on a webpage.
Generated: DETERMINISTIC_47bb6a01b78f0dff
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

import cgi
import cgitb

# Enable CGI error reporting
cgitb.enable()

# Set the content type of the response
print("Content-Type: text/html;charset=utf-8")
print()

# Function to generate the HTML response
def generate_html(form_data):
    """Generates an HTML response displaying the submitted form data."""
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Form Submission Result</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            h1 {{ color: #333; }}
            p {{ font-size: 1.1em; }}
        </style>
    </head>
    <body>
        <h1>Submitted Data</h1>
        <p><strong>Name:</strong> {form_data.get('name', [''])[0]}</p>
        <p><strong>Email:</strong> {form_data.get('email', [''])[0]}</p>
        <p><strong>Message:</strong> {form_data.get('message', [''])[0]}</p>
        <a href="form.html">Go back to the form</a>
    </body>
    </html>
    """
    return html

def main():
    """Main function to handle CGI form submission."""
    try:
        # Create a FieldStorage instance to handle form data
        form = cgi.FieldStorage()

        # Generate HTML with the form data
        response_html = generate_html(form)

        # Print the response HTML
        print(response_html)

    except Exception as e:
        # Print an error message if something goes wrong
        print("<h1>Error</h1>")
        print(f"<p>An error occurred: {str(e)}</p>")

if __name__ == "__main__":
    main()
```
