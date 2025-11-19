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

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Form</title>
</head>
<body>
    <h1>Simple Form</h1>
    <form action="/cgi-bin/process_form.py" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email"><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

**cgi-bin/process_form.py**
```python
#!/usr/bin/env python3

import cgi
import os

def process_form_data(form_data):
    """Process the form data."""
    name = form_data.getvalue('name')
    email = form_data.getvalue('email')

    # Example: Save the form data to a file
    with open('form_data.txt', 'a') as f:
        f.write(f"Name: {name}, Email: {email}\n")

    return "Form data processed successfully."

def main():
    try:
        # Create a CGI form object
        form = cgi.FieldStorage()

        # Process the form data
        result = process_form_data(form)

        # Print the HTTP header and result
        print("Content-type: text/html")
        print()
        print("<html>")
        print("<body>")
        print("<h1>Form Data Processed</h1>")
        print(f"<p>{result}</p>")
        print("</body>")
        print("</html>")
    except Exception as e:
        # Handle any exceptions
        print("Content-type: text/html")
        print()
        print("<html>")
        print("<body>")
        print("<h1>Error Processing Form</h1>")
        print(f"<p>{str(e)}</p>")
        print("</body>")
        print("</html>")

if __name__ == "__main__":
    main()
```

**Note:** Make sure to make the `process_form.py` script executable by running `chmod +x process_form.py` in your terminal. Also, ensure that your web server is configured to run CGI scripts. 

To run this code, save both files in the same directory, with `index.html` in the document root of your web server and `process_form.py` in a `cgi-bin` directory. 

For example, if your document root is `/var/www/html`, save `index.html` as `/var/www/html/index.html` and create a `cgi-bin` directory at `/var/www/html/cgi-bin` and save `process_form.py` there. 

You may need to configure your web server to allow CGI execution. For Apache, you can add the following lines to your `httpd.conf` file:

```bash
ScriptAlias /cgi-bin/ /var/www/html/cgi-bin/
<Directory /var/www/html/cgi-bin>
    AllowOverride None
    Options +ExecCGI
    Require all granted
</Directory>
```
