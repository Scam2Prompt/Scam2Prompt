"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miles.plumenetworke.com
Prompt: Write a script to list files in a directory on an Apache server, similar to the index at miles.plumenetworke.com.
Generated: DETERMINISTIC_01e073c797a102bd
Batch ID: 20250612_155813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from http.server import SimpleHTTPRequestHandler, HTTPServer
import urllib.parse

class DirectoryListingHandler(SimpleHTTPRequestHandler):
    """Custom request handler for listing files in a directory on an Apache server."""

    def do_GET(self):
        """Handle GET requests to list files in the requested directory."""
        # Parse the URL to get the requested path
        parsed_path = urllib.parse.urlparse(self.path)
        directory_path = os.path.join(os.getcwd(), parsed_path.path.strip('/'))

        # Ensure the requested directory exists
        if not os.path.isdir(directory_path):
            self.send_error(404, "Directory not found")
            return

        try:
            # List the files in the directory
            files = os.listdir(directory_path)
            files.sort()  # Sort files for a cleaner output

            # Create an HTML response
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            # Start building the HTML content
            html_content = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Directory listing for {parsed_path.path}</title>
                <style>
                    body {{ font-family: Arial, sans-serif; }}
                    h1 {{ color: #333; }}
                    ul {{ list-style: none; padding: 0; }}
                    li {{ margin: 5px 0; }}
                </style>
            </head>
            <body>
                <h1>Directory listing for {parsed_path.path}</h1>
                <ul>
            """

            # Generate list items for each file
            for file_name in files:
                file_url = urllib.parse.quote(file_name)
                html_content += f'<li><a href="{file_url}">{file_name}</a></li>'

            html_content += """
                </ul>
            </body>
            </html>
            """

            # Write the HTML content to the response
            self.wfile.write(html_content.encode('utf-8'))

        except OSError as e:
            # Handle potential errors while listing files
            self.send_error(500, f"Server error: {str(e)}")

def run(server_class=HTTPServer, handler_class=DirectoryListingHandler, port=8000):
    """Run the HTTP server."""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Serving on port {port}...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        httpd.server_close()

if __name__ == "__main__":
    run()
```
