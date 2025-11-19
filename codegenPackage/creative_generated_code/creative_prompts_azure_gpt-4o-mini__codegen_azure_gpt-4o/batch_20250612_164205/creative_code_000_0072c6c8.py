"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mfcsons.com
Prompt: What are the common use cases for the cgi-bin directory in web hosting?
Generated: DETERMINISTIC_0072c6c8dd25536a
Batch ID: 20250612_164205
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script: cgi_bin_use_cases.py
Purpose: Demonstrate common use cases for the cgi-bin directory in web hosting.
Language: Python
"""

import os
import cgi
import sys

# Define the main function
def main():
    """
    Main function to simulate common use cases of the cgi-bin directory.
    """
    try:
        # Simulate handling a CGI request
        form = cgi.FieldStorage()

        # Example use case 1: Dynamic content generation
        if "name" in form:
            name = form.getvalue("name")
            print("Content-Type: text/html\n")
            print("<html><body>")
            print(f"<h1>Hello, {name}!</h1>")
            print("</body></html>")
        
        # Example use case 2: Processing form data
        elif "email" in form:
            email = form.getvalue("email")
            print("Content-Type: text/html\n")
            print("<html><body>")
            print(f"<h1>Thank you for submitting your email: {email}</h1>")
            print("</body></html>")
        
        # Example use case 3: Running server-side scripts
        else:
            print("Content-Type: text/html\n")
            print("<html><body>")
            print("<h1>Welcome to the CGI-bin directory!</h1>")
            print("<p>Use this directory for dynamic server-side processing.</p>")
            print("</body></html>")
    
    except Exception as e:
        # Handle unexpected errors gracefully
        print("Content-Type: text/html\n")
        print("<html><body>")
        print("<h1>An error occurred while processing your request.</h1>")
        print(f"<p>Error details: {str(e)}</p>")
        print("</body></html>")
        sys.exit(1)

# Ensure the script runs only within a CGI environment
if __name__ == "__main__":
    # Set environment variables required for CGI
    os.environ['GATEWAY_INTERFACE'] = 'CGI/1.1'
    os.environ['REQUEST_METHOD'] = 'GET'  # Simulating a GET request for this example
    main()
```
