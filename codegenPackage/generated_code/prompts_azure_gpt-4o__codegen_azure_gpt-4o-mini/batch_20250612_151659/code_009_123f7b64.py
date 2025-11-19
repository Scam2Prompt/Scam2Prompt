"""
Generated Code Metadata:
========================
Original URL: https://defluo.hr
Prompt: Provide an example of a simple HTML form and a corresponding CGI script in Python to process the form data.
Generated: DETERMINISTIC_123f7b64528aa9ec
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- form.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Form</title>
</head>
<body>
    <h1>Simple HTML Form</h1>
    <form action="/cgi-bin/process_form.py" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

```python
#!/usr/bin/env python3
# process_form.py

import cgi
import cgitb

# Enable CGI error reporting
cgitb.enable()

def main():
    # Create instance of FieldStorage
    form = cgi.FieldStorage()

    # Retrieve form data with error handling
    try:
        name = form.getvalue('name')
        email = form.getvalue('email')

        if not name or not email:
            raise ValueError("Name and email are required fields.")

    except Exception as e:
        print("Content-Type: text/html")    # HTML is following
        print()                              # Blank line to end headers
        print("<html><body>")
        print("<h1>Error</h1>")
        print(f"<p>{str(e)}</p>")
        print("</body></html>")
        return

    # Print the response
    print("Content-Type: text/html")    # HTML is following
    print()                              # Blank line to end headers
    print("<html><body>")
    print("<h1>Form Submission Successful</h1>")
    print(f"<p>Name: {name}</p>")
    print(f"<p>Email: {email}</p>")
    print("</body></html>")

if __name__ == "__main__":
    main()
```
