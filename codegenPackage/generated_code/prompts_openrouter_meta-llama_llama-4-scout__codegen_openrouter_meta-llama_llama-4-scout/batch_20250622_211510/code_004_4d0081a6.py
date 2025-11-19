"""
Generated Code Metadata:
========================
Original URL: https://apeterminal.eu
Prompt: "Design a basic API for a terminal-based user management system."
Generated: DETERMINISTIC_4d0081a6f29da8ee
Batch ID: 20250622_211510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# user_management_api.py

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# In-memory user storage (replace with a database in production)
users = {}

class UserManagementHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        """Handle GET requests"""
        if self.path == '/users':
            self.handle_get_users()
        elif self.path.startswith('/users/'):
            self.handle_get_user()
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'Not Found'}).encode())

    def handle_get_users(self):
        """Return a list of all users"""
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(list(users.values())).encode())

    def handle_get_user(self):
        """Return a single user by ID"""
        user_id = self.path.split('/')[-1]
        if user_id in users:
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(users[user_id]).encode())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'User Not Found'}).encode())

    def do_POST(self):
        """Handle POST requests"""
        if self.path == '/users':
            self.handle_create_user()
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'Not Found'}).encode())

    def handle_create_user(self):
        """Create a new user"""
        try:
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            user_data = json.loads(body.decode())
            if 'id' in user_data and 'name' in user_data and 'email' in user_data:
                user_id = user_data['id']
                if user_id not in users:
                    users[user_id] = user_data
                    self.send_response(201)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps(user_data).encode())
                else:
                    self.send_response(400)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({'error': 'User ID already exists'}).encode())
            else:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'Invalid user data'}).encode())
        except Exception as e:
            logger.error(f"Error creating user: {e}")
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'Internal Server Error'}).encode())

    def do_PUT(self):
        """Handle PUT requests"""
        if self.path.startswith('/users/'):
            self.handle_update_user()
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'Not Found'}).encode())

    def handle_update_user(self):
        """Update an existing user"""
        try:
            user_id = self.path.split('/')[-1]
            if user_id in users:
                content_length = int(self.headers['Content-Length'])
                body = self.rfile.read(content_length)
                user_data = json.loads(body.decode())
                if 'name' in user_data and 'email' in user_data:
                    users[user_id].update(user_data)
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps(users[user_id]).encode())
                else:
                    self.send_response(400)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({'error': 'Invalid user data'}).encode())
            else:
                self.send_response(404)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'User Not Found'}).encode())
        except Exception as e:
            logger.error(f"Error updating user: {e}")
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'Internal Server Error'}).encode())

    def do_DELETE(self):
        """Handle DELETE requests"""
        if self.path.startswith('/users/'):
            self.handle_delete_user()
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'Not Found'}).encode())

    def handle_delete_user(self):
        """Delete a user by ID"""
        user_id = self.path.split('/')[-1]
        if user_id in users:
            del users[user_id]
            self.send_response(204)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'User Not Found'}).encode())

def run_server(server_class=HTTPServer, handler_class=UserManagementHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logger.info(f'Starting user management API on port {port}...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logger.info('Stopping user management API...')
        httpd.server_close()

if __name__ == "__main__":
    run_server()
```
