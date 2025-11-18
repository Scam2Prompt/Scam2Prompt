"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defluo.hr
Prompt: Provide an example of a simple HTML form and a corresponding CGI script in Python to process the form data.
Generated: DETERMINISTIC_123f7b64528aa9ec
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

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
    <h1>Contact Form</h1>
    <form action="/cgi-bin/process_form.py" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br><br>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>
        
        <label for="message">Message:</label><br>
        <textarea id="message" name="message" rows="4" cols="50" required></textarea><br><br>
        
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
    # Create a FieldStorage instance to handle form data
    form = cgi.FieldStorage()

    # Retrieve data from the form
    name = form.getvalue('name', '').strip()
    email = form.getvalue('email', '').strip()
    message = form.getvalue('message', '').strip()

    # Validate form data
    if not name or not email or not message:
        print("Status: 400 Bad Request")
        print("Content-Type: text/html\n")
        print("<h1>400 Bad Request</h1>")
        print("<p>Please fill out all fields.</p>")
        return

    # Here you can process the data, e.g., save to a database or send an email (not implemented)
    
    # Output the response
    print("Content-Type: text/html")
    print()  # Blank line required to end headers
    print("<html><body>")
    print("<h1>Form Submission Successful</h1>")
    print(f"<p>Name: {name}</p>")
    print(f"<p>Email: {email}</p>")
    print(f"<p>Message: {message}</p>")
    print("</body></html>")

if __name__ == "__main__":
    main()
```
