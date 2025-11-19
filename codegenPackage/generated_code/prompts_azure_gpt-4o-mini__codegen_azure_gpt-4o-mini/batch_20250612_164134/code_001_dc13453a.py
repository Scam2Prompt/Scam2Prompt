"""
Generated Code Metadata:
========================
Original URL: https://eigenlayer.magpiey.xyz
Prompt: How can I configure a web server to show a specific HTML page when no content is available at the given URL?
Generated: DETERMINISTIC_dc13453ae681102a
Batch ID: 20250612_164134
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class CustomHTTPRequestHandler(BaseHTTPRequestHandler):
    # Define the path to the custom 404 HTML page
    CUSTOM_404_PAGE = '404.html'

    def do_GET(self):
        """Handle GET requests."""
        # Check if the requested file exists
        if os.path.isfile(self.path[1:]):  # Remove leading '/'
            self.send_response(200)  # OK
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open(self.path[1:], 'r') as file:  # Open requested file
                self.wfile.write(file.read().encode())
        else:
            self.send_error(404)  # Not Found
            self.show_custom_404_page()

    def show_custom_404_page(self):
        """Display a custom 404 error page."""
        try:
            self.send_response(404)  # Not Found
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open(self.CUSTOM_404_PAGE, 'r') as file:  # Open custom 404 page
                self.wfile.write(file.read().encode())
        except FileNotFoundError:
            self.send_response(500)  # Internal Server Error
            self.end_headers()
            self.wfile.write(b"Custom 404 page not found.")

def run(server_class=HTTPServer, handler_class=CustomHTTPRequestHandler, port=8080):
    """Run the HTTP server."""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Server stopped.')
        httpd.server_close()

if __name__ == "__main__":
    run()
```

Make sure to create a `404.html` file in the same directory as this script to serve as the custom error page.
