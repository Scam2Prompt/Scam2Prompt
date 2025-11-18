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

# Import necessary modules
import cgi
import cgitb

# Enable CGI traceback for debugging
cgitb.enable()

def main():
    # Set the HTTP header for the response
    print("Content-Type: text/html\n")

    # Create a form object to parse submitted data
    form = cgi.FieldStorage()

    # Extract data from the form (default to empty string if the field is missing)
    name = form.getvalue("name", "")
    email = form.getvalue("email", "")
    message = form.getvalue("message", "")

    # Generate HTML content to display the submitted data
    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Form Submission</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 20px;
            }
            .container {
                max-width: 600px;
                margin: auto;
                padding: 20px;
                border: 1px solid #ccc;
                border-radius: 5px;
                background-color: #f9f9f9;
            }
            h1 {
                text-align: center;
            }
            p {
                font-size: 1.1em;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Form Submission</h1>
    """)

    # Display the submitted data
    if name or email or message:
        print(f"<p><strong>Name:</strong> {escape_html(name)}</p>")
        print(f"<p><strong>Email:</strong> {escape_html(email)}</p>")
        print(f"<p><strong>Message:</strong> {escape_html(message)}</p>")
    else:
        print("<p>No data was submitted.</p>")

    print("""
        </div>
    </body>
    </html>
    """)

def escape_html(text):
    """
    Escape special HTML characters for safe display on the webpage.
    """
    import html
    return html.escape(text)

# Entry point for the script
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # Display a generic error message in case of unexpected errors
        print("Content-Type: text/html\n")
        print("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Error</title>
        </head>
        <body>
            <h1>An error occurred</h1>
            <p>Please try again later.</p>
        </body>
        </html>
        """)
```

To test this script:
1. Save it as `form_handler.py` in your CGI-enabled web server's appropriate directory (e.g., `/var/www/cgi-bin`).
2. Make sure it has executable permissions (`chmod +x form_handler.py`).
3. Create an HTML form that submits data to this script (e.g., `<form action="/cgi-bin/form_handler.py" method="post">`).
