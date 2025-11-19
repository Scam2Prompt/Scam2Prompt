"""
Generated Code Metadata:
========================
Original URL: https://magpiexyz.click
Prompt: What are the steps to customize the default page of a web server to provide user-friendly information when no content is available?
Generated: DETERMINISTIC_5490e6f5450d64d8
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Custom Default Page for Web Server**
=====================================

### Using Python with http.server

```python
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

class CustomRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Check if the requested URL is the root URL
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            # Send a user-friendly message
            self.wfile.write(b"""
            <html>
                <head>
                    <title>Welcome</title>
                </head>
                <body>
                    <h1>Welcome to our website!</h1>
                    <p>We're currently working on some exciting content. Please check back later.</p>
                </body>
            </html>
            """)
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            # Send a 404 message
            self.wfile.write(b"""
            <html>
                <head>
                    <title>404 Not Found</title>
                </head>
                <body>
                    <h1>404 Not Found</h1>
                    <p>The requested URL was not found on our server.</p>
                </body>
            </html>
            """)

def run_server(server_class=HTTPServer, handler_class=CustomRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info(f'Starting httpd on port {port}...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logging.info('Stopping httpd...')
        httpd.server_close()

if __name__ == "__main__":
    run_server()
```

### Using Node.js with http

```javascript
const http = require('http');
const fs = require('fs');
const path = require('path');

// Define a port
const port = 8000;

// Create a server
const server = http.createServer((req, res) => {
    // Check if the requested URL is the root URL
    if (req.url === '/') {
        res.writeHead(200, {'Content-Type': 'text/html'});
        // Send a user-friendly message
        res.end(`
        <html>
            <head>
                <title>Welcome</title>
            </head>
            <body>
                <h1>Welcome to our website!</h1>
                <p>We're currently working on some exciting content. Please check back later.</p>
            </body>
        </html>
        `);
    } else {
        res.writeHead(404, {'Content-Type': 'text/html'});
        // Send a 404 message
        res.end(`
        <html>
            <head>
                <title>404 Not Found</title>
            </head>
            <body>
                <h1>404 Not Found</h1>
                <p>The requested URL was not found on our server.</p>
            </body>
        </html>
        `);
    }
});

// Start the server
server.listen(port, () => {
    console.log(`Server running on port ${port}`);
});

// Handle errors
server.on('error', (err) => {
    console.error(`Error occurred: ${err}`);
});

process.on('SIGINT', () => {
    console.log('Stopping server...');
    server.close();
});
```

### Using Apache HTTP Server with .htaccess

Create a `.htaccess` file in your document root:

```bash
ErrorDocument 404 /404.html
```

Create a `404.html` file in your document root:

```html
<html>
    <head>
        <title>404 Not Found</title>
    </head>
    <body>
        <h1>404 Not Found</h1>
        <p>The requested URL was not found on our server.</p>
    </body>
</html>
```

Create an `index.html` file in your document root for a user-friendly default page:

```html
<html>
    <head>
        <title>Welcome</title>
    </head>
    <body>
        <h1>Welcome to our website!</h1>
        <p>We're currently working on some exciting content. Please check back later.</p>
    </body>
</html>
```
