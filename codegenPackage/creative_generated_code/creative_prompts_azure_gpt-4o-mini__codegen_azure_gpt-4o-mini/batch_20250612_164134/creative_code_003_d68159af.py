"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eigenlayer.magpiey.xyz
Prompt: What are the steps to customize the default page of a web server to improve user experience when the site is not available?
Generated: DETERMINISTIC_d68159af12c951aa
Batch ID: 20250612_164134
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from http.server import BaseHTTPRequestHandler, HTTPServer

class CustomErrorHandler(BaseHTTPRequestHandler):
    """Custom error handler to display a user-friendly message when the server is unavailable."""

    def do_GET(self):
        """Handle GET requests."""
        self.send_response(503)  # Service Unavailable
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(self.generate_error_page().encode('utf-8'))

    def generate_error_page(self):
        """Generate a custom error page."""
        return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Service Unavailable</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding: 50px;
                    background-color: #f9f9f9;
                }
                h1 {
                    color: #d9534f;
                }
                p {
                    font-size: 18px;
                }
            </style>
        </head>
        <body>
            <h1>Service Unavailable</h1>
            <p>We are currently experiencing technical difficulties. Please try again later.</p>
        </body>
        </html>
        """

def run(server_class=HTTPServer, handler_class=CustomErrorHandler, port=8080):
    """Run the HTTP server with the custom error handler."""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Serving on port {port}...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
        print('Server stopped.')

if __name__ == "__main__":
    run()
```
