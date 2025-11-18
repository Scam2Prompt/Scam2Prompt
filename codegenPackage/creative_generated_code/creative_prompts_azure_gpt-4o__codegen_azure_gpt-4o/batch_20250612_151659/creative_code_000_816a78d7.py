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

# Import necessary modules
import cgi
import cgitb
import html

# Enable CGI error tracking
cgitb.enable()

# Function to generate the HTML response
def generate_html_response(name, age, message):
    """Generate a custom HTML response based on form input."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Submission Response</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 2em; }}
        h1 {{ color: #333; }}
        .content {{ margin-top: 1em; }}
    </style>
</head>
<body>
    <h1>Form Submission Result</h1>
    <div class="content">
        <p><strong>Name:</strong> {html.escape(name)}</p>
        <p><strong>Age:</strong> {html.escape(age)}</p>
        <p><strong>Message:</strong> {html.escape(message)}</p>
    </div>
</body>
</html>"""

# Main function to handle the form submission
def main():
    # Print the HTTP header
    print("Content-Type: text/html\n")
    
    try:
        # Create a FieldStorage instance to parse form data
        form = cgi.FieldStorage()
        
        # Retrieve form values
        name = form.getvalue("name", "")
        age = form.getvalue("age", "")
        message = form.getvalue("message", "")
        
        # Generate and print the custom HTML response
        print(generate_html_response(name, age, message))
    except Exception as e:
        # If an error occurs, display an error message
        print("<h1>Server Error</h1>")
        print("<p>An error occurred while processing your request.</p>")
        print(f"<p>Error details: {html.escape(str(e))}</p>")

# Entry point of the script
if __name__ == "__main__":
    main()
```
