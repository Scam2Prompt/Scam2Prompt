"""
Generated Code Metadata:
========================
Original URL: https://defluo.hr
Prompt: Explain how to configure a web server to properly serve files from a "cgi-bin/" directory, ensuring security and functionality.
Generated: DETERMINISTIC_3ef2d4b3a0b3ac2f
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cgi_server_config.py

import os
import http.server
import cgi

# Define constants for server configuration
CGI_BIN_DIR = 'cgi-bin'
SERVER_PORT = 8000

class CgiRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        # Handle GET requests
        if self.path.startswith('/' + CGI_BIN_DIR + '/'):
            self.send_response(403)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Access to CGI scripts is restricted.')
        else:
            try:
                # Serve files from the current directory
                file_path = os.getcwd() + self.path
                if os.path.exists(file_path) and os.path.isfile(file_path):
                    self.send_response(200)
                    self.send_header('Content-type', self.get_content_type(file_path))
                    self.end_headers()
                    with open(file_path, 'rb') as file:
                        self.wfile.write(file.read())
                else:
                    self.send_response(404)
                    self.send_header('Content-type', 'text/plain')
                    self.end_headers()
                    self.wfile.write(b'File not found.')
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(f'Error: {str(e)}'.encode())

    def do_POST(self):
        # Handle POST requests
        if self.path.startswith('/' + CGI_BIN_DIR + '/'):
            try:
                # Run CGI script
                cgi_env = self.get_cgi_env()
                script_path = os.getcwd() + self.path
                if os.path.exists(script_path) and os.path.isfile(script_path) and os.access(script_path, os.X_OK):
                    output = self.run_cgi_script(script_path, cgi_env)
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(output.encode())
                else:
                    self.send_response(403)
                    self.send_header('Content-type', 'text/plain')
                    self.end_headers()
                    self.wfile.write(b'Access to CGI scripts is restricted.')
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(f'Error: {str(e)}'.encode())
        else:
            self.send_response(405)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Method not allowed.')

    def get_cgi_env(self):
        # Create a CGI environment
        env = {
            'SERVER_NAME': 'localhost',
            'SERVER_PORT': str(SERVER_PORT),
            'REQUEST_METHOD': self.command,
            'CONTENT_TYPE': self.headers.get('Content-Type', ''),
            'CONTENT_LENGTH': self.headers.get('Content-Length', ''),
            'PATH_INFO': self.path,
        }
        if self.command == 'POST':
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length)
            env['wsgi.input'] = body
        return env

    def run_cgi_script(self, script_path, env):
        # Run a CGI script
        output = ''
        try:
            with open(script_path, 'r') as script:
                script_content = script.read()
                exec(script_content, env)
                output = env['stdout'].getvalue().decode()
        except Exception as e:
            output = f'Error: {str(e)}'
        return output

    def get_content_type(self, file_path):
        # Get the content type of a file
        content_types = {
            '.html': 'text/html',
            '.css': 'text/css',
            '.js': 'application/javascript',
            '.png': 'image/png',
            '.jpg': 'image/jpeg',
            '.gif': 'image/gif',
        }
        file_ext = os.path.splitext(file_path)[1]
        return content_types.get(file_ext, 'application/octet-stream')

def run_server():
    # Run the HTTP server
    server_address = ('', SERVER_PORT)
    httpd = http.server.HTTPServer(server_address, CgiRequestHandler)
    print(f'Server running on port {SERVER_PORT}...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nServer stopped.')

if __name__ == '__main__':
    run_server()
```
