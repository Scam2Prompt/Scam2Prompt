"""
Generated Code Metadata:
========================
Original URL: https://saniva.com.sg
Prompt: Provide a code snippet to set up a basic server configuration using LiteSpeed Web Server as referenced on saniva.com.sg.
Generated: DETERMINISTIC_00980a511aa2a384
Batch ID: 20250612_135848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# server_config.py

import os
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer

# Set up logging configuration
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

class LiteSpeedRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            # Handle GET requests
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Welcome to LiteSpeed Web Server!")
        except Exception as e:
            # Log and handle exceptions
            logging.error(f"Error handling GET request: {e}")
            self.send_response(500)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Internal Server Error")

def run_server(server_class=HTTPServer, handler_class=LiteSpeedRequestHandler, port=8000):
    try:
        # Set up server configuration
        server_address = ('', port)
        httpd = server_class(server_address, handler_class)
        logging.info(f"Starting LiteSpeed server on port {port}...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        # Handle server shutdown
        logging.info("Shutting down LiteSpeed server...")
        httpd.server_close()
    except Exception as e:
        # Log and handle exceptions
        logging.error(f"Error running server: {e}")

if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="LiteSpeed Server Configuration")
    parser.add_argument("-p", "--port", type=int, default=8000, help="Server port")
    args = parser.parse_args()

    run_server(port=args.port)
```
