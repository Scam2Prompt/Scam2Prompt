"""
Generated Code Metadata:
========================
Original URL: https://interrpay.com
Prompt: Create a basic web server configuration file using a popular library or framework.
Generated: DETERMINISTIC_6e3bf52538271cf8
Batch ID: 20250622_204841
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RequestHandler(BaseHTTPRequestHandler):
    """Handles incoming HTTP requests."""

    def do_GET(self):
        """Handles GET requests."""
        logging.info(f"Received GET request for: {self.path}")
        
        # Set response status code
        self.send_response(200)
        # Set response headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Write response content
        self.wfile.write(b"<html><body><h1>Hello, World!</h1></body></html>")
        logging.info("Response sent successfully.")

    def log_message(self, format, *args):
        """Override to prevent default logging to stderr."""
        logging.info(format % args)

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    """Starts the HTTP server."""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    
    try:
        logging.info(f"Starting server on port {port}...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        logging.info("Server is shutting down.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        httpd.server_close()
        logging.info("Server closed.")

if __name__ == "__main__":
    run()
```
