"""
Generated Code Metadata:
========================
Original URL: https://npcgrant.online
Prompt: Generate a basic code snippet for a web server to list directory contents, similar to the provided webpage.
Generated: DETERMINISTIC_0ed8fd02bd969a7c
Batch ID: 20250622_211021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import http.server
import os

class DirectoryListingHandler(http.server.SimpleHTTPRequestHandler):
    """
    Custom handler to list directory contents.
    """

    def do_GET(self):
        """
        Handle GET requests.
        """
        # Check if the requested path exists
        if os.path.exists(self.path) and os.path.isdir(self.path):
            # List directory contents
            self.list_directory(self.path)
        else:
            # Handle file requests or non-existent paths
            super().do_GET()

    def list_directory(self, path):
        """
        List directory contents.

        Args:
            path (str): The path to the directory.
        """
        try:
            # Get a list of files and directories in the path
            files_and_dirs = os.listdir(path)

            # Send a response with a directory listing
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            # Create an HTML response
            response = self.directory_listing_html(path, files_and_dirs)
            self.wfile.write(response.encode())
        except Exception as e:
            # Handle any exceptions
            self.send_response(500)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(f"Error: {str(e)}".encode())

    def directory_listing_html(self, path, files_and_dirs):
        """
        Generate an HTML response for a directory listing.

        Args:
            path (str): The path to the directory.
            files_and_dirs (list): A list of files and directories.

        Returns:
            str: The HTML response.
        """
        html = f"""
        <html>
            <head>
                <title>Directory Listing: {path}</title>
            </head>
            <body>
                <h1>Directory Listing: {path}</h1>
                <ul>
        """
        for file_or_dir in files_and_dirs:
            html += f"<li><a href='{os.path.join(path, file_or_dir)}'>{file_or_dir}</a></li>\n"
        html += """
                </ul>
            </body>
        </html>
        """
        return html


def run_server(server_class=http.server.HTTPServer, handler_class=DirectoryListingHandler, port=8000):
    """
    Run the web server.

    Args:
        server_class: The server class to use.
        handler_class: The handler class to use.
        port (int): The port to listen on.
    """
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting web server on port {port}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping web server...")
    finally:
        httpd.server_close()


if __name__ == "__main__":
    run_server()
```
