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
import sys
import os

# Enable detailed error reporting for debugging (disable in production)
cgitb.enable()

# Set the content type to HTML
print("Content-Type: text/html\n")

# HTML template
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CGI Script Example</title>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; }}
        h1 {{ color: #333; }}
        .form-group {{ margin-bottom: 15px; }}
        .error {{ color: red; }}
    </style>
</head>
<body>
    <h1>CGI Form Example</h1>
    <form method="post" action="">
        <div class="form-group">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
        </div>
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
        </div>
        <div class="form-group">
            <input type="submit" value="Submit">
        </div>
    </form>
    {response}
</body>
</html>
"""

def main():
    form = cgi.FieldStorage()
    response = ""

    try:
        # Process form submission
        if form.getvalue("name") and form.getvalue("email"):
            name = form.getvalue("name")
            email = form.getvalue("email")
            
            # Basic validation
            if not name.strip() or not email.strip():
                response = "<p class='error'>Please fill in all fields.</p>"
            else:
                response = f"""
                <div class="result">
                    <h2>Thank You!</h2>
                    <p>Name: {cgi.escape(name)}</p>
                    <p>Email: {cgi.escape(email)}</p>
                </div>
                """
    except Exception as e:
        response = f"<p class='error'>An error occurred: {cgi.escape(str(e))}</p>"

    print(HTML_TEMPLATE.format(response=response))

if __name__ == "__main__":
    main()
```
