"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cybersamurai.live
Prompt: Can you provide a code snippet for configuring a web server to serve files from the public_html directory?
Generated: DETERMINISTIC_045332c3d23c2c05
Batch ID: 20250612_155903
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    """Custom request handler to serve files from the public_html directory."""
    
    def translate_path(self, path):
        """Translate the URL path to a file system path."""
        # Define the directory to serve files from
        public_html_dir = os.path.join(os.getcwd(), 'public_html')
        # Use the parent directory to prevent directory traversal attacks
        return super().translate_path(path.replace('/', os.path.sep, 1)).replace(os.path.sep, os.path.join(os.path.sep, public_html_dir), 1)

def run(server_class=HTTPServer, handler_class=CustomHTTPRequestHandler, port=8000):
    """Run the HTTP server with the configured handler."""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    
    try:
        print(f"Starting HTTP server on port {port}...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down the server.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        httpd.server_close()
        print("Server stopped.")

if __name__ == "__main__":
    run()
```
