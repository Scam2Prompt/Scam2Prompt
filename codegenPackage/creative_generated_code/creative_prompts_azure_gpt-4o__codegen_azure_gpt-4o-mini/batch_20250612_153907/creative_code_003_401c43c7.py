"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://obyssey.xyz
Prompt: Create a step-by-step guide for initializing a web server using tools or methods discussed on obyssey.xyz.
Generated: DETERMINISTIC_401c43c786558c7b
Batch ID: 20250612_153907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from http.server import HTTPServer, SimpleHTTPRequestHandler
import logging
import socket

# Set up logging for the server
logging.basicConfig(level=logging.INFO)

class CustomHandler(SimpleHTTPRequestHandler):
    """
    Custom handler for processing HTTP requests.
    Inherits from SimpleHTTPRequestHandler to serve files.
    """

    def do_GET(self):
        """Handle GET requests."""
        logging.info(f"Received GET request for: {self.path}")
        super().do_GET()

    def send_error(self, code, message=None):
        """Override to log errors."""
        logging.error(f"Error {code}: {message}")
        super().send_error(code, message)

def run(server_class=HTTPServer, handler_class=CustomHandler, port=8000):
    """
    Initialize and run the web server.
    
    :param server_class: HTTP server class to use
    :param handler_class: Request handler class to use
    :param port: Port number to listen on
    """
    # Check if the port is within the valid range
    if port < 1 or port > 65535:
        logging.error("Invalid port number. Must be between 1 and 65535.")
        return

    server_address = ('', port)
    
    try:
        httpd = server_class(server_address, handler_class)
        logging.info(f'Serving on port {port}...')
        httpd.serve_forever()
    except OSError as e:
        logging.error(f"Failed to start server: {e}")
    except KeyboardInterrupt:
        logging.info("Server is shutting down.")
        httpd.server_close()

if __name__ == "__main__":
    # Initialize and start the web server
    PORT = 8000  # You can change the port number as needed
    run(port=PORT)
```
