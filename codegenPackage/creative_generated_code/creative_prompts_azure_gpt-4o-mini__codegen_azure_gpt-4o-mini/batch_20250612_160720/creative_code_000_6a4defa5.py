"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://refconegypt.net
Prompt: What are the key features of the cgi-bin directory on the Refcon Egypt website?
Generated: DETERMINISTIC_6a4defa5035b1346
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

class CGIRequestHandler(BaseHTTPRequestHandler):
    """Custom HTTP request handler for processing CGI requests."""

    def do_GET(self):
        """Handle GET requests."""
        try:
            # Define the path to the cgi-bin directory
            cgi_bin_path = os.path.join(os.getcwd(), 'cgi-bin')

            # Check if the requested CGI script exists
            script_name = self.path.strip('/')
            script_path = os.path.join(cgi_bin_path, script_name)

            if os.path.isfile(script_path) and os.access(script_path, os.X_OK):
                # Execute the script and send the response back
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = self.run_cgi_script(script_path)
                self.wfile.write(output.encode())
            else:
                # Respond with a 404 error if the script is not found
                self.send_error(404, "File not found")
        except Exception as e:
            # Handle any unexpected errors
            self.send_error(500, f"Internal Server Error: {str(e)}")

    def run_cgi_script(self, script_path):
        """Execute the CGI script and return its output."""
        import subprocess
        
        # Run the CGI script and capture its output
        result = subprocess.run(
            [script_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Check for errors in executing the script
        if result.returncode != 0:
            return f"Error executing script: {result.stderr}"

        return result.stdout

def run(server_class=HTTPServer, handler_class=CGIRequestHandler, port=8000):
    """Run the HTTP server with the specified handler."""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)

    try:
        print(f'Server running on port {port}...')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Stopping server...')
    finally:
        httpd.server_close()

if __name__ == "__main__":
    run()
```
