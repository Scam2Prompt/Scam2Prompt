"""
Generated Code Metadata:
========================
Original URL: https://smartd.org.ls
Prompt: Generate HTML code for a simple directory listing page that displays folder names, last modified dates, and sizes, similar to the content of https://smartd.org.ls.
Generated: DETERMINISTIC_7e78f66bb91662a0
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer

class DirectoryListingHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            # Get the current working directory
            cwd = os.getcwd()

            # Get the list of files and directories in the current working directory
            files_and_dirs = os.listdir(cwd)

            # Send the HTTP response header
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # Send the HTML content
            self.wfile.write(b'<!DOCTYPE html><html><head><title>Directory Listing</title></head><body>')
            self.wfile.write(b'<h1>Directory Listing</h1>')
            self.wfile.write(b'<table border="1">')
            self.wfile.write(b'<tr><th>Name</th><th>Last Modified</th><th>Size</th></tr>')

            for file_or_dir in files_and_dirs:
                file_path = os.path.join(cwd, file_or_dir)

                # Get the file stats
                file_stats = os.stat(file_path)

                # Get the last modified date
                last_modified_date = datetime.datetime.fromtimestamp(file_stats.st_mtime).strftime('%Y-%m-%d %H:%M')

                # Get the file size
                if os.path.isdir(file_path):
                    file_size = 'Dir'
                else:
                    file_size = f'{file_stats.st_size} bytes'

                # Write the table row
                self.wfile.write(f'<tr><td><a href="{file_or_dir}">{file_or_dir}</a></td><td>{last_modified_date}</td><td>{file_size}</td></tr>'.encode())

            self.wfile.write(b'</table>')
            self.wfile.write(b'</body></html>')

        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(f'Error: {str(e)}'.encode())

def run_server(server_class=HTTPServer, handler_class=DirectoryListingHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting directory listing server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=8000, help='Port to listen on')
    args = parser.parse_args()
    run_server(port=args.port)
```
