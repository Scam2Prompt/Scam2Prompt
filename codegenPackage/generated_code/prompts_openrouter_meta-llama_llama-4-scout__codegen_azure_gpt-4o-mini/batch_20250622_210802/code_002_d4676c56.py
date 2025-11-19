"""
Generated Code Metadata:
========================
Original URL: https://uosolutions.site
Prompt: Write a Python script to create a basic web server that serves a single webpage with a copyright notice.
Generated: DETERMINISTIC_d4676c56f09ba4cb
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import http.server
import socketserver

# Define the port for the web server
PORT = 8000

# Create a request handler that serves a simple HTML page
class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Set the response code to 200 (OK)
        self.send_response(200)
        # Set the content type to HTML
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # HTML content to be served
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Simple Web Server</title>
        </head>
        <body>
            <h1>Welcome to My Web Server</h1>
            <p>&copy; 2023 Your Name. All rights reserved.</p>
        </body>
        </html>
        """
        
        # Write the HTML content to the response
        self.wfile.write(html_content.encode('utf-8'))

# Function to run the web server
def run(server_class=http.server.HTTPServer, handler_class=SimpleHTTPRequestHandler):
    # Create an instance of the server
    with server_class(("", PORT), handler_class) as httpd:
        print(f"Serving on port {PORT}")
        try:
            # Start the server
            httpd.serve_forever()
        except KeyboardInterrupt:
            # Handle server shutdown gracefully
            print("\nServer is shutting down.")
            httpd.server_close()

# Entry point of the script
if __name__ == "__main__":
    run()
```
