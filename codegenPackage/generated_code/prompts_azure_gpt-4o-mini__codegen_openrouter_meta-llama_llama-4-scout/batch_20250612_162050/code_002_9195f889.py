"""
Generated Code Metadata:
========================
Original URL: https://webdhise.com
Prompt: How can I build a maintenance mode page for my website, inspired by the message on Webdhise?
Generated: DETERMINISTIC_9195f8897af47041
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# maintenance_mode.py

from http.server import BaseHTTPRequestHandler, HTTPServer
import datetime
import json

class MaintenanceModeHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(503)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        maintenance_message = {
            "message": "We are currently performing scheduled maintenance.",
            "title": "Maintenance Mode",
            "details": "Our website is currently undergoing scheduled maintenance. Please check back later.",
            "estimated_time": self.get_estimated_time()
        }

        self.wfile.write(json.dumps(maintenance_message).encode())

    def get_estimated_time(self):
        # For demonstration purposes, assume maintenance will be done in 30 minutes
        estimated_time = datetime.datetime.now() + datetime.timedelta(minutes=30)
        return estimated_time.strftime("%Y-%m-%d %H:%M:%S")


def run_server(server_class=HTTPServer, handler_class=MaintenanceModeHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting maintenance mode server on port {port}...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Stopping maintenance mode server...')
    finally:
        httpd.server_close()


if __name__ == "__main__":
    run_server()
```

```html
<!-- index.html (for a simple static maintenance page, not used in this Python example but provided for context) -->

<!DOCTYPE html>
<html>
<head>
    <title>Maintenance Mode</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
        }
    </style>
</head>
<body>
    <h1>Maintenance Mode</h1>
    <p>We are currently performing scheduled maintenance.</p>
    <p>Please check back later.</p>
</body>
</html>
```
