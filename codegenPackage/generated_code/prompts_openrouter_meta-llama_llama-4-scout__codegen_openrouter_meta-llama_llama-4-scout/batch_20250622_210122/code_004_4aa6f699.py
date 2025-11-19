"""
Generated Code Metadata:
========================
Original URL: https://cerlalinda.edu.co
Prompt: Write a Python script to create a simple webpage that announces the development of a new website, similar to the current state of cerlalinda.edu.co.
Generated: DETERMINISTIC_4aa6f69939469de6
Batch ID: 20250622_210122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Parse URL
        parsed_path = urllib.parse.urlparse(self.path)

        # Handle root URL
        if parsed_path.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # Send HTML response
            message = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>Under Construction</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        text-align: center;
                    }
                </style>
            </head>
            <body>
                <h1>Under Construction</h1>
                <p>We are currently developing a new website and this page will be updated soon.</p>
                <p>Thank you for your patience.</p>
            </body>
            </html>
            """
            self.wfile.write(message.encode())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Not Found')

def run_server(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nStopping httpd...')
    httpd.server_close()

if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=8000, help='Server port')
    args = parser.parse_args()
    run_server(port=args.port)
```
