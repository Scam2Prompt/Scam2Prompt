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

### HTML Form (save as `form.html`)
```html
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
        <br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

---

### Python CGI Script (save as `process_form.py`)
```python
#!/usr/bin/env python3

import cgi
import cgitb

# Enable debugging for CGI scripts
cgitb.enable()

def main():
    try:
        # Parse form data
        form = cgi.FieldStorage()
        name = form.getfirst("name", "").strip()
        email = form.getfirst("email", "").strip()

        # Output HTTP headers
        print("Content-Type: text/html")  # Response is HTML
        print()  # End of headers

        # Validate form data
        if not name or not email:
            print("<html><body>")
            print("<h1>Error: Missing form data</h1>")
            print("<p>Please ensure both Name and Email fields are filled out.</p>")
            print("</body></html>")
            return

        # Output the response
        print("<html><body>")
        print("<h1>Form Submission Successful</h1>")
        print(f"<p>Name: {name}</p>")
        print(f"<p>Email: {email}</p>")
        print("</body></html>")

    except Exception as e:
        # Handle unexpected errors gracefully
        print("Content-Type: text/html")
        print()
        print("<html><body>")
        print("<h1>Error: An unexpected error occurred</h1>")
        print(f"<p>{cgi.escape(str(e))}</p>")
        print("</body></html>")

# Entry point for the CGI script
if __name__ == "__main__":
    main()
```

---

### Notes:
1. Make sure the CGI script (`process_form.py`) is placed in the `/cgi-bin/` directory or configured directory on your web server.
2. Ensure the script has executable permissions (`chmod +x process_form.py`).
3. The server must be properly configured to execute CGI scripts.
