"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bpearlegy.com
Prompt: What are the common uses of the cgi-bin directory in web development?
Generated: DETERMINISTIC_d172fb3eb7f3b5f6
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

"""
cgi-bin Example Script

This script demonstrates the common uses of a cgi-bin directory in web development.
CGI scripts are used to handle user input, perform server-side processing, and generate dynamic responses.
"""

import cgi
import cgitb
import os

# Enable debugging to log errors (for development purposes; disable in production)
cgitb.enable()

# Function to handle environment variables
def print_environment_variables():
    """
    Prints all environment variables available to the CGI script.
    Useful for debugging and observing server settings.
    """
    print("<h2>Environment Variables</h2>")
    print("<ul>")
    for key, value in os.environ.items():
        print(f"<li><b>{key}</b>: {value}</li>")
    print("</ul>")

# Function to handle form submission
def process_form():
    """
    Processes data submitted via an HTML form using CGI.
    """
    print("<h2>Submitted Form Data</h2>")
    form = cgi.FieldStorage()
    
    if not form.keys():
        print("<p>No data received from the form.</p>")
        return

    print("<ul>")
    for key in form.keys():
        value = form.getvalue(key)
        print(f"<li><b>{key}</b>: {value}</li>")
    print("</ul>")

# Main function
def main():
    """
    Entry point for the CGI script.
    Generates an HTML response based on user input and server-side processing.
    """
    # Print HTTP headers (required for all CGI scripts)
    print("Content-Type: text/html")
    print()  # Blank line to separate headers from the body

    # Start of HTML document
    print("<!DOCTYPE html>")
    print("<html lang='en'>")
    print("<head>")
    print("<meta charset='UTF-8'>")
    print("<meta name='viewport' content='width=device-width, initial-scale=1.0'>")
    print("<title>CGI-bin Script Example</title>")
    print("</head>")
    print("<body>")
    print("<h1>Welcome to the CGI-bin Example</h1>")
    
    # Display submitted form data
    process_form()

    # Display environment variables
    print_environment_variables()
    
    print("</body>")
    print("</html>")

# Entry point of the script
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # Handle unexpected errors and provide feedback
        print("Content-Type: text/html")
        print()
        print("<h1>Error</h1>")
        print(f"<p>An unexpected error occurred: {e}</p>")
```

Place this script in your `cgi-bin` directory and ensure that the server is properly configured to execute it. This script demonstrates the use of `cgi-bin` for processing form submissions and inspecting environment variables.
