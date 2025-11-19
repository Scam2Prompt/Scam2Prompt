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
from http.server import SimpleHTTPRequestHandler, HTTPServer
import os
import json
import urllib.parse

class DirectoryLister(SimpleHTTPRequestHandler):
    def do_GET(self):
        try:
            # Parse the path and handle URL encoding
            path = self.translate_path(self.path)
            if os.path.isdir(path):
                # List directory contents
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                
                contents = []
                for name in sorted(os.listdir(path)):
                    full_path = os.path.join(path, name)
                    is_dir = os.path.isdir(full_path)
                    size = os.path.getsize(full_path) if not is_dir else 0
                    contents.append({
                        'name': name,
                        'type': 'directory' if is_dir else 'file',
                        'size': size
                    })
                
                self.wfile.write(json.dumps(contents).encode('utf-8'))
            else:
                # Serve files normally
                super().do_GET()
        except Exception as e:
            self.send_error(500, f"Server error: {str(e)}")

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, DirectoryLister)
    print(f"Serving on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
```
