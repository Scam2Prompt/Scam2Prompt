"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magpiexyz.click
Prompt: Generate a code snippet for setting up a web server that displays a custom default page when no website is hosted at a specific address.
Generated: DETERMINISTIC_19875c6784bb90f3
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from http.server import HTTPServer, BaseHTTPRequestHandler

# Define a custom HTTP request handler
class CustomDefaultPageHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """
        Handles GET requests and displays a custom default page when no specific
        website is hosted at the address.
        """
        try:
            # Set HTTP response status code to 200 (OK)
            self.send_response(200)
            
            # Set response headers
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            # Custom default page content
            default_page = """
            <html>
            <head>
                <title>Default Page</title>
            </head>
            <body>
                <h1>Welcome!</h1>
                <p>This is the default page. No website is hosted at this address.</p>
            </body>
            </html>
            """
            
            # Send the default page as the response
            self.wfile.write(default_page.encode('utf-8'))
        
        except Exception as e:
            # Handle any unexpected errors gracefully
            self.send_error(500, f"Internal Server Error: {str(e)}")

# Function to start the web server
def run_server(port=8080):
    """
    Starts an HTTP web server on the specified port. Displays a custom default page
    if no website is hosted at the specified address.
    
    Args:
        port (int): The port number to bind the server to (default is 8080).
    """
    try:
        # Create the HTTP server instance
        server_address = ('', port)
        httpd = HTTPServer(server_address, CustomDefaultPageHandler)
        
        print(f"Starting web server on port {port}...")
        
        # Start the server and keep it running
        httpd.serve_forever()
    except KeyboardInterrupt:
        # Gracefully handle server shutdown on user interruption
        print("\nShutting down the server...")
        httpd.server_close()
    except Exception as e:
        # Handle other errors during server setup
        print(f"Error: {str(e)}")

# Entry point of the script
if __name__ == "__main__":
    # Run the server on port 8080
    run_server(port=8080)
```
