"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magpiexyz.click
Prompt: What are the steps to customize the default page of a web server to provide user-friendly information when no content is available?
Generated: DETERMINISTIC_5490e6f5450d64d8
Batch ID: 20250612_160946
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:{PORT": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here’s the code to customize the default page of an HTTP web server using Python with the `http.server` module:

```python
import http.server
import socketserver

# Define a custom HTTP request handler
class CustomRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        """
        Handle GET requests. If the requested file is not found, 
        serve a custom default page.
        """
        try:
            # Attempt to serve the requested file
            return super().do_GET()
        except Exception as e:
            # Handle any errors by serving a custom default page
            self.send_response(404)  # Send HTTP 404 status code
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            # Custom default page content
            self.wfile.write(b"""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Page Not Found</title>
                    <style>
                        body {
                            font-family: Arial, sans-serif;
                            text-align: center;
                            margin-top: 50px;
                        }
                        h1 {
                            color: #333;
                        }
                        p {
                            color: #666;
                        }
                        a {
                            color: #0066cc;
                            text-decoration: none;
                        }
                        a:hover {
                            text-decoration: underline;
                        }
                    </style>
                </head>
                <body>
                    <h1>Oops! Page Not Found</h1>
                    <p>Sorry, the content you are looking for does not exist.</p>
                    <p><a href="/">Go back to the homepage</a></p>
                </body>
                </html>
            """)

# Port number for the server
PORT = 8000

# Create the server object
with socketserver.TCPServer(("", PORT), CustomRequestHandler) as httpd:
    print(f"Serving on port {PORT}. Visit http://localhost:{PORT}")
    try:
        # Start the server
        httpd.serve_forever()
    except KeyboardInterrupt:
        # Gracefully shut down the server on Ctrl+C
        print("\nServer is shutting down.")
        httpd.server_close()
    except Exception as e:
        # Handle other errors
        print(f"Error: {e}")
        httpd.server_close()
```

This code sets up a basic HTTP server that serves files from the current directory. If a requested file is unavailable, it displays a custom "Page Not Found" HTML page instead.
