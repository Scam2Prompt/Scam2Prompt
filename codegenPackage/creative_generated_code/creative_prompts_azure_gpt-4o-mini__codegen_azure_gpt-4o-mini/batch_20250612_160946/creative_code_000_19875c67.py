"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magpiexyz.click
Prompt: Generate a code snippet for setting up a web server that displays a custom default page when no website is hosted at a specific address.
Generated: DETERMINISTIC_19875c6784bb90f3
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

# Custom request handler class
class CustomRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        """Handle GET requests."""
        self.send_response(200)  # Send a 200 OK response
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Custom default page content
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Default Page</title>
        </head>
        <body>
            <h1>Welcome to My Custom Default Page!</h1>
            <p>This is a placeholder for when no specific site is hosted.</p>
        </body>
        </html>
        """
        self.wfile.write(html_content.encode('utf-8'))  # Write content to the response

    def log_message(self, format, *args):
        """Override to customize logging format."""
        logging.info("%s - - [%s] %s", self.client_address[0], self.log_date_time_string(), format % args)

def run(server_class=HTTPServer, handler_class=CustomRequestHandler, port=8080):
    """Run the HTTP server."""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.basicConfig(level=logging.INFO)  # Set up logging
    try:
        logging.info(f'Starting server on port {port}...')
        httpd.serve_forever()  # Start the server
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        httpd.server_close()  # Ensure the server is closed safely
        logging.info('Server stopped.')

if __name__ == "__main__":
    run()  # Execute the run function
```
