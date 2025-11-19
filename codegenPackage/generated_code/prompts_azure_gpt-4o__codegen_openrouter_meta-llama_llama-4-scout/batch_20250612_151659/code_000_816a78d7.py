"""
Generated Code Metadata:
========================
Original URL: https://defluo.hr
Prompt: Write a Python CGI script that can be deployed in a "cgi-bin/" directory to handle form submissions and return a custom HTML response.
Generated: DETERMINISTIC_816a78d7078bb32e
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3

"""
CGI Script to handle form submissions and return a custom HTML response.

Usage:
    Deploy this script in a "cgi-bin/" directory and submit a form with 
    'name' and 'email' fields to see a custom response.

Author: [Your Name]
Date: [Today's Date]
"""

import cgi
import os

def get_form_data():
    """
    Retrieves form data from the CGI environment.

    Returns:
        dict: A dictionary containing the form data.
    """
    form = cgi.FieldStorage()
    return {key: form[key].value for key in form}

def validate_form_data(data):
    """
    Validates the form data.

    Args:
        data (dict): The form data.

    Returns:
        bool: True if the data is valid, False otherwise.
    """
    required_fields = ['name', 'email']
    return all(field in data for field in required_fields)

def generate_html_response(data):
    """
    Generates a custom HTML response.

    Args:
        data (dict): The form data.

    Returns:
        str: The HTML response.
    """
    html = """
    <html>
        <head>
            <title>Form Submission Response</title>
        </head>
        <body>
            <h1>Thank you for submitting the form!</h1>
            <p>Name: {name}</p>
            <p>Email: {email}</p>
        </body>
    </html>
    """
    return html.format(name=data['name'], email=data['email'])

def main():
    try:
        # Get the form data
        data = get_form_data()

        # Validate the form data
        if not validate_form_data(data):
            raise ValueError("Invalid form data")

        # Generate the HTML response
        html_response = generate_html_response(data)

        # Print the HTML response
        print("Content-Type: text/html")
        print()
        print(html_response)

    except Exception as e:
        # Handle any exceptions
        print("Content-Type: text/plain")
        print()
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
