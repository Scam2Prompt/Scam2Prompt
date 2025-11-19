"""
Generated Code Metadata:
========================
Original URL: https://suigate.xyz
Prompt: Provide an example of how to use a specific web server software or framework to display a custom success message.
Generated: DETERMINISTIC_26d57c4889c5d59d
Batch ID: 20250622_211343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import the required libraries
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)

class SuccessHandler(BaseHTTPRequestHandler):
    """
    Custom request handler to display a success message.
    """

    def do_GET(self):
        """
        Handle GET requests and return a custom success message.
        """
        try:
            # Define the custom success message
            success_message = "Operation successful!"

            # Set the HTTP status code and headers
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            # Render the HTML response with the success message
            html_response = f"""
            <html>
                <body>
                    <h1>{success_message}</h1>
                </body>
            </html>
            """
            self.wfile.write(html_response.encode())
        except Exception as e:
            # Log any exceptions and return a 500 error response
            logging.error(f"Error handling request: {e}")
            self.send_response(500)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Internal Server Error")

def run_server(server_class=HTTPServer, handler_class=SuccessHandler, port=8000):
    """
    Run the custom web server.

    Args:
        server_class (type): The HTTP server class.
        handler_class (type): The request handler class.
        port (int): The port number to listen on.
    """
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    logging.info(f"Starting server on port {port}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logging.info("Server stopped.")

if __name__ == "__main__":
    run_server()
```
