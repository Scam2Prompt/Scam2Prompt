"""
Generated Code Metadata:
========================
Original URL: https://jupi.red
Prompt: "Create a simple webpage template for a newly created website on Ispmanager, mentioning the server IP address."
Generated: DETERMINISTIC_4a83984c492c2741
Batch ID: 20250622_211412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to our website on Ispmanager</title>
</head>
<body>
    <header>
        <h1>Welcome to our website</h1>
    </header>
    <main>
        <p>Our website is now live on Ispmanager, hosted on server IP address: <span id="server-ip">%SERVER_IP%</span></p>
        <p>Thank you for visiting us!</p>
    </main>
    <footer>
        <p>&copy; 2023 Our Website. All rights reserved.</p>
    </footer>
</body>
</html>
```

```python
# server.py

from http.server import BaseHTTPRequestHandler, HTTPServer
import socket

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            server_ip = socket.gethostbyname(socket.gethostname())
            html = open('index.html', 'r').read().replace('%SERVER_IP%', server_ip)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode())
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(f"An error occurred: {e}".encode())

def run_server(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Server running on port {port}...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nServer stopped.')

if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=8000, help='Server port')
    args = parser.parse_args()
    run_server(port=args.port)
```
