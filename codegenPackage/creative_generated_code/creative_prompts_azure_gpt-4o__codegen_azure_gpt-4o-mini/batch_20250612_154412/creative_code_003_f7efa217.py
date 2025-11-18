"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://8lements.xyz
Prompt: Write a script to monitor and log requests to a LiteSpeed Web Server running on port 443.
Generated: DETERMINISTIC_f7efa21751706416
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import socket
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

# Configure logging
logging.basicConfig(
    filename='server_requests.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class RequestHandler(BaseHTTPRequestHandler):
    """Handles HTTP requests and logs them."""

    def do_GET(self):
        """Handle GET requests."""
        self.log_request()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Request logged successfully.')

    def log_request(self):
        """Log the details of the incoming request."""
        client_ip, _ = self.client_address
        logging.info(f'GET request from {client_ip} for {self.path}')

    def log_error(self, format, *args):
        """Override to log errors."""
        logging.error(format % args)

def run(server_class=HTTPServer, port=443):
    """Starts the HTTP server to monitor requests."""
    server_address = ('', port)
    httpd = server_class(server_address, RequestHandler)
    try:
        logging.info(f'Server starting on port {port}...')
        httpd.serve_forever()
    except KeyboardInterrupt:
        logging.info('Server stopping.')
        httpd.server_close()
    except Exception as e:
        logging.error(f'An error occurred: {e}')
        httpd.server_close()

if __name__ == '__main__':
    run()
```
