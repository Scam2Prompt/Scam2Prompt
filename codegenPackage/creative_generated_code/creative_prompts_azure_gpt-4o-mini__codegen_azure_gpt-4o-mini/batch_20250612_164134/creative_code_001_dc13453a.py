"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eigenlayer.magpiey.xyz
Prompt: How can I configure a web server to show a specific HTML page when no content is available at the given URL?
Generated: DETERMINISTIC_dc13453ae681102a
Batch ID: 20250612_164134
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    """Custom request handler that serves a specific HTML page for 404 errors."""
    
    def do_GET(self):
        """Handle GET requests."""
        try:
            # Attempt to serve the requested file
            super().do_GET()
        except FileNotFoundError:
            # If the file is not found, serve the custom 404 page
            self.send_error(404, "File not found")
    
    def send_error(self, code, message=None):
        """Override send_error to display a custom 404 HTML page."""
        self.send_response(code)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Load the custom 404 error page
        if code == 404:
            self.wfile.write(self.get_custom_404_page().encode('utf-8'))
        else:
            # Fallback to the default error message
            self.wfile.write(f"<html><body><h1>{code}: {message}</h1></body></html>".encode('utf-8'))

    def get_custom_404_page(self):
        """Return the content of the custom 404 HTML page."""
        return """
        <html>
        <head><title>Page Not Found</title></head>
        <body>
            <h1>404 - Page Not Found</h1>
            <p>Sorry, the page you are looking for does not exist.</p>
            <a href="/">Go to Homepage</a>
        </body>
        </html>
        """

def run(server_class=HTTPServer, handler_class=CustomHTTPRequestHandler, port=8000):
    """Run the HTTP server with the specified handler."""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    
    # Use a try-except block to handle server errors gracefully
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        httpd.server_close()
        print("Server closed.")

if __name__ == "__main__":
    run()
```
