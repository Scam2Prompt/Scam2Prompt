"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magpiexyz.click
Prompt: What are the steps to customize the default page of a web server to provide user-friendly information when no content is available?
Generated: DETERMINISTIC_5490e6f5450d64d8
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from http.server import BaseHTTPRequestHandler, HTTPServer

class CustomHTTPRequestHandler(BaseHTTPRequestHandler):
    """Custom HTTP Request Handler to serve user-friendly error pages."""

    def do_GET(self):
        """Handle GET requests."""
        # Check if the requested path is valid
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(self.get_home_page().encode())
        else:
            self.send_error(404)

    def get_home_page(self):
        """Return the HTML content for the home page."""
        return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Welcome</title>
        </head>
        <body>
            <h1>Welcome to Our Web Server</h1>
            <p>Thank you for visiting our server.</p>
            <p>If you are seeing this page, it means the requested content is not available.</p>
            <p>Please check the URL or return to the home page.</p>
        </body>
        </html>
        """

    def send_error(self, code, message=None):
        """Override to provide a custom error page."""
        self.send_response(code)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(self.get_error_page(code, message).encode())

    def get_error_page(self, code, message=None):
        """Return the HTML content for the error pages."""
        if message is None:
            message = {
                404: "Page Not Found",
                500: "Internal Server Error"
            }.get(code, "Error")
        
        return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{code} - Error</title>
        </head>
        <body>
            <h1>Error {code}: {message}</h1>
            <p>We are sorry, but the page you are looking for does not exist.</p>
            <p>Please check the URL and try again.</p>
            <p><a href="/">Return to Home</a></p>
        </body>
        </html>
        """

def run(server_class=HTTPServer, handler_class=CustomHTTPRequestHandler, port=8080):
    """Run the server on the specified port."""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Serving on port {port}...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Server is shutting down.')
    finally:
        httpd.server_close()

if __name__ == '__main__':
    run()
```
