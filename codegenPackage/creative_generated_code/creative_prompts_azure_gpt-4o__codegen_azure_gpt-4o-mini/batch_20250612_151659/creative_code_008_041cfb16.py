"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defluo.hr
Prompt: Write a guide for debugging CGI scripts located in the "cgi-bin/" directory of a web server.
Generated: DETERMINISTIC_041cfb162a299639
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# cgi_debugger.py

import os
import cgi
import logging

# Configure logging for debugging
logging.basicConfig(filename='cgi_debugger.log', level=logging.DEBUG)

def print_form_data(form):
    """Prints the form data received from the CGI request."""
    logging.info("Received form data:")
    for field in form:
        value = form.getvalue(field)
        logging.info(f"{field}: {value}")

def main():
    """Main function to handle CGI requests and debug CGI scripts."""
    try:
        # Create instance of FieldStorage to handle form data
        form = cgi.FieldStorage()

        # Log the request method
        logging.info(f"Request method: {os.environ.get('REQUEST_METHOD')}")

        # Print out the form data for debugging
        print_form_data(form)

        # Generate HTTP response
        print("Content-Type: text/html;charset=utf-8")
        print()  # Blank line required between headers and content
        print("<html><head><title>CGI Debugger</title></head>")
        print("<body><h1>CGI Debugger Output</h1>")
        print("<p>Check the logs for detailed form data.</p>")
        print("</body></html>")

    except Exception as e:
        # Log the exception with traceback for debugging
        logging.error("An error occurred while processing the CGI request.", exc_info=True)
        print("Content-Type: text/html;charset=utf-8")
        print()  # Blank line required between headers and content
        print("<html><head><title>Error</title></head>")
        print("<body><h1>An Error Occurred</h1>")
        print(f"<p>{str(e)}</p>")
        print("</body></html>")

if __name__ == "__main__":
    main()
```
