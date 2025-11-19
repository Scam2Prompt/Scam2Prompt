"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mestamosklogi.godaddysites.com
Prompt: What libraries can I use to enhance user experience through cookie management on my site?
Generated: DETERMINISTIC_905375b7a18a4753
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import http.cookies
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

# Create a simple HTTP request handler
class CookieHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        # Parse URL parameters for actions
        parsed_path = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_path.query)

        # Check if a cookie exists and set it if not
        if 'set' in query_params:
            self.set_cookie('user_session', 'active')
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Cookie has been set!')
        elif 'get' in query_params:
            cookie_value = self.get_cookie('user_session')
            self.send_response(200)
            self.end_headers()
            self.wfile.write(f'Cookie value: {cookie_value}'.encode())
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b'Invalid request! Use ?set or ?get in the URL.')

    def set_cookie(self, key, value):
        """Set a cookie in the HTTP response."""
        cookie = http.cookies.SimpleCookie()
        cookie[key] = value
        cookie[key]['Path'] = '/'
        cookie[key]['HttpOnly'] = True
        cookie[key]['Secure'] = True  # Only send cookie over HTTPS
        self.send_header('Set-Cookie', cookie.output(header='', sep=''))

    def get_cookie(self, key):
        """Retrieve a cookie value from the HTTP request."""
        if 'Cookie' in self.headers:
            cookie = http.cookies.SimpleCookie(self.headers['Cookie'])
            return cookie.get(key).value if key in cookie else 'No cookie found'
        return 'No cookie found'

def run(server_class=HTTPServer, handler_class=CookieHandler, port=8080):
    """Run the HTTP server."""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
        print('Server stopped.')

if __name__ == "__main__":
    run()
```
