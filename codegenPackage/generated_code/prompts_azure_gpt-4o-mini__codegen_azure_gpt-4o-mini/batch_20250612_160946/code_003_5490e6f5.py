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

```python
from http.server import BaseHTTPRequestHandler, HTTPServer

class CustomHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    Custom HTTP request handler that serves a user-friendly message
    when no content is available.
    """

    def do_GET(self):
        """
        Handle GET requests. If the requested content is not found,
        serve a custom 404 error page.
        """
        # Define the content for the custom 404 page
        self.send_response(404)  # Send a 404 Not Found response
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Custom HTML content for the 404 error page
        error_message = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Page Not Found</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
                h1 { color: #ff0000; }
                p { font-size: 18px; }
            </style>
        </head>
        <body>
            <h1>404 - Page Not Found</h1>
            <p>Sorry, the page you are looking for does not exist.</p>
            <p>Please check the URL or return to the <a href="/">home page</a>.</p>
        </body>
        </html>
        """
        
        # Write the custom error message to the response
        self.wfile.write(error_message.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=CustomHTTPRequestHandler, port=8080):
    """
    Run the HTTP server with the specified handler class and port.
    
    Args:
        server_class: The class of the server to run.
        handler_class: The request handler class to use.
        port: The port number to listen on.
    """
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Server is shutting down...')
    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        httpd.server_close()
        print('Server closed.')

if __name__ == "__main__":
    run()
```
