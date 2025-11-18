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

import cgi
import cgitb
import html

# Enable error reporting for debugging
cgitb.enable()

# Set the content type of the response to HTML
print("Content-Type: text/html")
print()  # End of headers

# Function to generate HTML response
def generate_html_response(user_input):
    # Escape user input to prevent XSS attacks
    safe_input = html.escape(user_input)
    return f"""
    <html>
    <head>
        <title>CGI Script Response</title>
    </head>
    <body>
        <h1>CGI Script Output</h1>
        <p>You entered: {safe_input}</p>
    </body>
    </html>
    """

try:
    # Create a FieldStorage instance to hold the form data
    form = cgi.FieldStorage()

    # Get the user input from the form (default to empty string if not provided)
    user_input = form.getvalue("input", "")

    # Generate the HTML response
    html_response = generate_html_response(user_input)

    # Print the HTML response
    print(html_response)

except Exception as e:
    # Handle exceptions and return an error message to the user
    print("Status: 500 Internal Server Error")
    print()
    print("<html><body><h1>Error</h1>")
    print("<p>There was an error processing your request.</p>")
    print(f"<p>Error details: {html.escape(str(e))}</p>")
    print("</body></html>")
```

Make sure to give this script appropriate permissions to be executed in the `cgi-bin` directory, for example, by running `chmod 755 your_script.py`.
