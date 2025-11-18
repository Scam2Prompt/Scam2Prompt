"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defluo.hr
Prompt: Write a Python CGI script that can be deployed in a "cgi-bin/" directory to handle form submissions and return a custom HTML response.
Generated: DETERMINISTIC_816a78d7078bb32e
Batch ID: 20250612_151659
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

# Enable CGI error reporting
cgitb.enable()

# Content-Type header for HTML response
print("Content-Type: text/html\n")

# Function to handle form submissions
def handle_form_submission():
    # Create a FieldStorage instance to parse form data
    form = cgi.FieldStorage()

    # Check if the form was submitted
    if "name" not in form or "message" not in form:
        print("<html><body>")
        print("<h1>Error: Form submission is incomplete.</h1>")
        print("</body></html>")
        return

    # Safely retrieve and sanitize form inputs
    name = html.escape(form.getvalue("name"))
    message = html.escape(form.getvalue("message"))

    # Create a custom HTML response
    print("<html><body>")
    print("<h1>Thank You for Your Submission!</h1>")
    print(f"<p><strong>Name:</strong> {name}</p>")
    print(f"<p><strong>Message:</strong> {message}</p>")
    print("</body></html>")

# Call the function to handle the form submission
if __name__ == "__main__":
    handle_form_submission()
```
