"""
Generated Code Metadata:
========================
Original URL: https://mfcsons.com
Prompt: What are the common use cases for the cgi-bin directory in web hosting?
Generated: DETERMINISTIC_0072c6c8dd25536a
Batch ID: 20250612_164205
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Common CGI-Bin Use Cases in Web Hosting

```python
#!/usr/bin/env python3
"""
This script demonstrates common use cases for the cgi-bin directory in web hosting.
It includes examples of form processing, dynamic content generation, and server-side scripting.
"""

import cgi
import cgitb
import json
from http import cookies
import os
import sys

# Enable detailed error reporting for debugging
cgitb.enable()

# Set content type header
print("Content-Type: text/html\n")

def handle_form_submission():
    """Process form data submitted via POST"""
    try:
        form = cgi.FieldStorage()
        
        # Get form values with error handling
        name = form.getvalue('name', 'Not provided')
        email = form.getvalue('email', 'Not provided')
        
        # Process the data (e.g., save to database, send email)
        # This is a simulation - in production you'd have proper storage
        result = f"Received submission: Name={name}, Email={email}"
        
        # Return response
        print(f"""
        <html>
        <head><title>Form Submission Result</title></head>
        <body>
            <h1>Thank You!</h1>
            <p>{result}</p>
        </body>
        </html>
        """)
    except Exception as e:
        print(f"<p>Error processing form: {str(e)}</p>")

def generate_dynamic_content():
    """Generate dynamic HTML content"""
    try:
        # Example of dynamic content generation
        import datetime
        now = datetime.datetime.now()
        
        print(f"""
        <html>
        <head><title>Dynamic Content</title></head>
        <body>
            <h1>Current Server Time</h1>
            <p>The server time is: {now.strftime('%Y-%m-%d %H:%M:%S')}</p>
        </body>
        </html>
        """)
    except Exception as e:
        print(f"<p>Error generating content: {str(e)}</p>")

def handle_cookie_operations():
    """Demonstrate cookie handling"""
    try:
        # Create cookie
        cookie = cookies.SimpleCookie()
        cookie['visits'] = 1
        
        # Check for existing cookie
        if 'HTTP_COOKIE' in os.environ:
            cookie.load(os.environ['HTTP_COOKIE'])
            if 'visits' in cookie:
                cookie['visits'] = int(cookie['visits'].value) + 1
        
        # Print headers first
        print(cookie.output())
        print("Content-Type: text/html\n")
        
        print(f"""
        <html>
        <head><title>Cookie Example</title></head>
        <body>
            <h1>Cookie Demo</h1>
            <p>You've visited this page {cookie['visits'].value} times.</p>
        </body>
        </html>
        """)
    except Exception as e:
        print(f"<p>Error handling cookies: {str(e)}</p>")

def process_ajax_request():
    """Handle AJAX/JSON requests"""
    try:
        # Get JSON data from POST body
        if os.environ.get('CONTENT_TYPE') == 'application/json':
            data = json.load(sys.stdin)
            
            # Process the data
            response = {
                'status': 'success',
                'message': f"Received: {data.get('input', 'No input')}",
                'processed': True
            }
            
            # Return JSON response
            print("Content-Type: application/json\n")
            print(json.dumps(response))
            return True
    except Exception as e:
        print("Content-Type: application/json\n")
        print(json.dumps({'status': 'error', 'message': str(e)}))
        return True
    return False

def main():
    """Main entry point for the CGI script"""
    try:
        # Check if this is an AJAX request
        if process_ajax_request():
            return
            
        # Check for form submission
        if os.environ.get('REQUEST_METHOD') == 'POST':
            handle_form_submission()
            return
            
        # Check for cookie demo request
        if 'show_cookies' in os.environ.get('QUERY_STRING', ''):
            handle_cookie_operations()
            return
            
        # Default case - generate dynamic content
        generate_dynamic_content()
        
    except Exception as e:
        print(f"<h1>Error</h1><p>{str(e)}</p>")

if __name__ == '__main__':
    main()
```
