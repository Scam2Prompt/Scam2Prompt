"""
Generated Code Metadata:
========================
Original URL: https://npcgrant.online
Prompt: Generate a basic code snippet for a web server to list directory contents, similar to the provided webpage.
Generated: DETERMINISTIC_0ed8fd02bd969a7c
Batch ID: 20250622_211021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

class DirectoryListingHandler(SimpleHTTPRequestHandler):
    """Custom request handler to list directory contents."""

    def do_GET(self):
        """Handle GET requests."""
        # Serve the directory listing for the requested path
        if self.path == '/':
            self.list_directory_contents()
        else:
            super().do_GET()

    def list_directory_contents(self):
        """List the contents of the current directory."""
        try:
            # Get the list of files and directories
            entries = os.listdir('.')
            # Create an HTML response
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # Start HTML document
            self.wfile.write(b"<html><head><title>Directory Listing</title></head><body>")
            self.wfile.write(b"<h1>Directory Listing</h1><ul>")

            # Add each entry to the HTML list
            for entry in entries:
                self.wfile.write(f"<li><a href='{entry}'>{entry}</a></li>".encode())

            # End HTML document
            self.wfile.write(b"</ul></body></html>")
        except Exception as e:
            self.send_error(500, f"Internal Server Error: {str(e)}")

def run(server_class=HTTPServer, handler_class=DirectoryListingHandler, port=8000):
    """Run the HTTP server."""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server stopped by user.")
    finally:
        httpd.server_close()

if __name__ == "__main__":
    run()
```
