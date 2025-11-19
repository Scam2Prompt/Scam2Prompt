"""
Generated Code Metadata:
========================
Original URL: https://smardex.live
Prompt: Describe the typical content of a web server's default page when no website is present at the accessed URL.
Generated: DETERMINISTIC_542275159da89a61
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from http.server import BaseHTTPRequestHandler, HTTPServer

class DefaultPageHandler(BaseHTTPRequestHandler):
    """
    A simple HTTP request handler that serves a default page
    when no website is present at the accessed URL.
    """

    def do_GET(self):
        """
        Handle GET requests.
        Responds with a default page indicating that no website is present.
        """
        self.send_response(404)  # Send a 404 Not Found response
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Default page content
        default_page_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>404 Not Found</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
                h1 { font-size: 50px; }
                p { font-size: 20px; }
            </style>
        </head>
        <body>
            <h1>404 Not Found</h1>
            <p>The requested URL was not found on this server.</p>
            <p>Please check the URL and try again.</p>
        </body>
        </html>
        """
        
        # Write the default page content to the response
        self.wfile.write(default_page_content.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=DefaultPageHandler, port=8080):
    """
    Run the HTTP server with the specified handler class and port.
    
    Args:
        server_class: The class of the server to run (default: HTTPServer).
        handler_class: The request handler class (default: DefaultPageHandler).
        port: The port on which to run the server (default: 8080).
    """
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    
    try:
        httpd.serve_forever()  # Start the server
    except KeyboardInterrupt:
        print('Server stopped by user.')
    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        httpd.server_close()  # Ensure the server is closed properly

if __name__ == "__main__":
    run()  # Run the server
```
