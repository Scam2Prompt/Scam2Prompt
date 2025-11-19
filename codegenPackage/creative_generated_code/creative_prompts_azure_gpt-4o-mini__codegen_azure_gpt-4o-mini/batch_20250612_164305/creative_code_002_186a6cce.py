"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thekygrand.com
Prompt: Write a Python script that lists files in a directory and serves them over HTTP, similar to the index page of thekygrand.com.
Generated: DETERMINISTIC_186a6ccec4bd02fb
Batch ID: 20250612_164305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import http.server
import socketserver
from urllib.parse import unquote

# Define the port for the HTTP server
PORT = 8000

# Handler for serving files
class DirectoryHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Decode the URL path
        path = unquote(self.path)
        
        # If the path is a directory, list its contents
        if path.endswith('/'):
            self.list_directory(self.path)
        else:
            # Serve the requested file
            super().do_GET()

    def list_directory(self, path):
        # Attempt to list the directory
        try:
            # Get the list of files and directories
            items = os.listdir(path)
            items.sort()  # Sort items for consistent display
        except OSError as e:
            self.send_error(404, f"Cannot list directory: {e}")
            return
        
        # Create HTML response for the directory listing
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        # Start HTML document
        self.wfile.write(b'<!doctype html><html><head><title>Directory Listing</title></head><body>')
        self.wfile.write(b'<h1>Directory listing</h1><ul>')
        
        # Create links for each item in the directory
        for item in items:
            item_path = os.path.join(path, item)
            item_url = self.path + item + ('/' if os.path.isdir(item_path) else '')
            self.wfile.write(f'<li><a href="{item_url}">{item}</a></li>'.encode())
        
        # End HTML document
        self.wfile.write(b'</ul></body></html>')

def run(server_class=http.server.HTTPServer, handler_class=DirectoryHandler):
    # Set the server address and port
    server_address = ('', PORT)
    
    # Create the HTTP server
    httpd = server_class(server_address, handler_class)
    print(f"Serving HTTP on port {PORT}...")
    
    try:
        # Start serving the HTTP requests
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server stopped by user.")
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        httpd.server_close()

if __name__ == "__main__":
    # Run the server
    run()
```
