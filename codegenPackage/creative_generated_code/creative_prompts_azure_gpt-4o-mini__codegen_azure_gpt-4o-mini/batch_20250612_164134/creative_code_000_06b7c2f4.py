"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eigenlayer.magpiey.xyz
Prompt: Generate a code snippet to set up a web server that displays a custom default page instead of the standard "no website at this address" message.
Generated: DETERMINISTIC_06b7c2f42488ecc5
Batch ID: 20250612_164134
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class CustomHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests."""
        self.send_response(200)  # Send HTTP status code 200 (OK)
        self.send_header('Content-type', 'text/html')  # Set content type to HTML
        self.end_headers()  # End the headers

        # Custom HTML content for the default page
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Welcome to My Custom Server</title>
        </head>
        <body>
            <h1>Welcome to My Custom Web Server!</h1>
            <p>This is a custom default page instead of a standard error message.</p>
        </body>
        </html>
        """
        self.wfile.write(bytes(html_content, 'utf-8'))  # Write HTML content to response

    def log_message(self, format, *args):
        """Override log_message to customize the logging output."""
        print("%s - - [%s] %s\n" % (self.address_string(), self.log_date_time_string(), format % args))

def run(server_class=HTTPServer, handler_class=CustomHTTPRequestHandler, port=8080):
    """Run the web server on the specified port."""
    server_address = ('', port)  # Listen on all interfaces
    httpd = server_class(server_address, handler_class)

    try:
        print(f'Starting server on port {port}...')
        httpd.serve_forever()  # Start the server
    except KeyboardInterrupt:
        print('Server is shutting down...')
    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        httpd.server_close()  # Ensure the server closes properly

if __name__ == "__main__":
    run()  # Execute the server
```
