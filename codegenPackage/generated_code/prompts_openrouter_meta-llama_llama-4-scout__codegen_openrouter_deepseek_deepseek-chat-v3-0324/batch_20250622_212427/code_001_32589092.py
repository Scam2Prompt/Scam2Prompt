"""
Generated Code Metadata:
========================
Original URL: https://www.magpiexyz.click
Prompt: Write a simple HTTP server response in Python that returns a default webpage indicating no website is configured at the requested address.
Generated: DETERMINISTIC_32589092ebb0fa9f
Batch ID: 20250622_212427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver

class DefaultResponseHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests by returning a default response page."""
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        response_html = """
        <html>
            <head>
                <title>No Website Configured</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        text-align: center;
                        margin-top: 50px;
                        color: #333;
                    }
                    h1 {
                        color: #555;
                    }
                </style>
            </head>
            <body>
                <h1>No Website Configured</h1>
                <p>The requested address does not have a website configured.</p>
            </body>
        </html>
        """
        
        self.wfile.write(response_html.encode('utf-8'))

def run_server(port=8080):
    """Run the HTTP server on the specified port."""
    server_address = ('', port)
    httpd = HTTPServer(server_address, DefaultResponseHandler)
    print(f"Server running on port {port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped")
        httpd.server_close()

if __name__ == '__main__':
    run_server()
```
