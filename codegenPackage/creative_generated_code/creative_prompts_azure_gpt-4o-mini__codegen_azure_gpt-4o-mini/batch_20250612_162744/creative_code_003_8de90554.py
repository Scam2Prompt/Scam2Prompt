"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum.io-v2.org
Prompt: Generate a Python script that checks if JavaScript is enabled in a browser before accessing a webpage.
Generated: DETERMINISTIC_8de905540929feab
Batch ID: 20250612_162744
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import sys
import http.server
import socketserver
from urllib.parse import urlparse

# Constants
PORT = 8000

# HTML template for the web page
HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Check</title>
    <script>
        // JavaScript function to notify that JavaScript is enabled
        document.addEventListener("DOMContentLoaded", function() {
            document.getElementById("js-enabled").style.display = "block";
            document.getElementById("js-disabled").style.display = "none";
        });
    </script>
</head>
<body>
    <h1>JavaScript Check</h1>
    <div id="js-disabled">
        <p>JavaScript is disabled in your browser. Please enable JavaScript to access the content.</p>
    </div>
    <div id="js-enabled" style="display: none;">
        <p>JavaScript is enabled! You can now access the content.</p>
    </div>
</body>
</html>
"""

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    """Handles HTTP requests."""
    
    def do_GET(self):
        """Responds to GET requests."""
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(HTML_PAGE.encode('utf-8'))

def run(server_class=http.server.HTTPServer, handler_class=RequestHandler):
    """Runs the HTTP server."""
    try:
        with socketserver.TCPServer(("", PORT), handler_class) as httpd:
            print(f"Serving on port {PORT}")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped by user")
        sys.exit(0)
    except Exception as e:
        print(f"Error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run()
```
