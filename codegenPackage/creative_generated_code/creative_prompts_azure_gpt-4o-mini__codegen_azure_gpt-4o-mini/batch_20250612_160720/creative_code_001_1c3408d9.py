"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bpearlegy.com
Prompt: Can you provide a code snippet for creating a CGI script in Python?
Generated: DETERMINISTIC_1c3408d917b3496f
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

# Enable CGI error reporting
cgitb.enable()

# Set the content type to HTML
print("Content-Type: text/html;charset=utf-8")
print()  # End of headers

# Function to generate HTML response
def generate_html_response(title, message):
    """Generate a simple HTML response."""
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            h1 {{ color: #333; }}
        </style>
    </head>
    <body>
        <h1>{title}</h1>
        <p>{message}</p>
    </body>
    </html>
    """
    return html

# Main function to handle the CGI script
def main():
    """Main function to process CGI input and generate an HTML response."""
    try:
        # Get form data
        form = cgi.FieldStorage()
        name = form.getvalue('name', 'World')  # Default to 'World' if no name is provided

        # Prepare the response message
        message = f"Hello, {name}!"  # Greet the user
        response_html = generate_html_response("CGI Script Response", message)

        # Print the HTML response
        print(response_html)

    except Exception as e:
        # Handle any unexpected errors
        print("Content-Type: text/plain;charset=utf-8\n")
        print(f"An error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
```
