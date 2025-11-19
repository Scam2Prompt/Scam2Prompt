"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eigenlayer.magpiey.xyz
Prompt: Write a script to create a default web page for a server that currently shows a "no website" message.
Generated: DETERMINISTIC_17accb03f9e69894
Batch ID: 20250612_164134
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

# Define the default HTML content for the web page
DEFAULT_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 50px;
        }
        h1 {
            color: #333;
        }
        p {
            font-size: 18px;
        }
    </style>
</head>
<body>
    <h1>Welcome to Our Web Server!</h1>
    <p>This is the default web page. You can replace this with your own content.</p>
</body>
</html>
"""

# Define a custom request handler to serve the default page
class DefaultHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Respond with the default HTML if the request is for the root URL
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            # Write the default HTML content to the response
            self.wfile.write(DEFAULT_HTML.encode('utf-8'))
        else:
            # Use the default handler for all other requests
            super().do_GET()

def run(server_class=HTTPServer, handler_class=DefaultHandler, port=8000):
    """Start the HTTP server."""
    server_address = ('', port)
    try:
        httpd = server_class(server_address, handler_class)
        print(f'Serving on port {port}...')
        httpd.serve_forever()
    except Exception as e:
        print(f'Error occurred while starting the server: {e}')
    finally:
        httpd.server_close()
        print('Server has been stopped.')

if __name__ == "__main__":
    run()
```

This Python script creates a simple HTTP server that serves a default web page when accessed. The server listens on port 8000 by default and can be modified as needed.
