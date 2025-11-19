"""
Generated Code Metadata:
========================
Original URL: https://uosolutions.site
Prompt: Write a Python script to create a basic web server that serves a single webpage with a copyright notice.
Generated: DETERMINISTIC_d4676c56f09ba4cb
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import http.server
import socketserver
from datetime import datetime

# Define the HTML content with copyright notice
HTML_CONTENT = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Basic Web Server</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            text-align: center;
        }}
        .container {{
            max-width: 800px;
            margin: 0 auto;
        }}
        .copyright {{
            margin-top: 50px;
            font-size: 0.8em;
            color: #666;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to the Basic Web Server</h1>
        <p>This is a simple webpage served by a Python HTTP server.</p>
        <div class="copyright">
            &copy; {datetime.now().year} Basic Web Server. All rights reserved.
        </div>
    </div>
</body>
</html>
"""

class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(HTML_CONTENT.encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'404 Not Found')

def run_server(port=8000):
    with socketserver.TCPServer(("", port), SimpleHTTPRequestHandler) as httpd:
        print(f"Serving at port {port}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    run_server()
```
