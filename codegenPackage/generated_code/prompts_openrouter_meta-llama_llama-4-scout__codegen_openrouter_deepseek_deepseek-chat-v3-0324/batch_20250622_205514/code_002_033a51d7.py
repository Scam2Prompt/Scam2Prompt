"""
Generated Code Metadata:
========================
Original URL: https://cartenoir.org
Prompt: "Generate a code snippet for a custom server solution that meets the requirements of a secure on-premise infrastructure, as described in the Carte Noir Consulting project for BFR Gaming."
Generated: DETERMINISTIC_033a51d72e7a0d43
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import ssl
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
import logging
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import base64
import json
import hmac
import hashlib
from datetime import datetime, timedelta
import secrets

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('server.log'),
        logging.StreamHandler()
    ]
)

# Security configuration
SECRET_KEY = os.environ.get('SERVER_SECRET_KEY', secrets.token_hex(32))
TOKEN_EXPIRATION_MINUTES = 30
MAX_REQUEST_SIZE = 1024 * 1024  # 1MB
RATE_LIMIT_REQUESTS = 100
RATE_LIMIT_WINDOW_MINUTES = 1

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""
    pass

class SecureRequestHandler(BaseHTTPRequestHandler):
    """Custom secure request handler with authentication and rate limiting."""
    
    tokens = {}
    request_counts = {}

    def __init__(self, *args, **kwargs):
        self.authenticated = False
        self.client_ip = None
        super().__init__(*args, **kwargs)

    def _rate_limit_check(self):
        """Check and enforce rate limiting."""
        now = datetime.now()
        window_start = now - timedelta(minutes=RATE_LIMIT_WINDOW_MINUTES)
        
        # Clean up old entries
        self.request_counts = {
            ip: count for ip, count in self.request_counts.items()
            if self.tokens[ip]['last_request'] >= window_start
        }
        
        if self.client_ip not in self.request_counts:
            self.request_counts[self.client_ip] = 0
        
        self.request_counts[self.client_ip] += 1
        
        if self.request_counts[self.client_ip] > RATE_LIMIT_REQUESTS:
            self.send_error(429, "Rate limit exceeded")
            return False
        return True

    def _validate_token(self, token):
        """Validate JWT token."""
        if token not in self.tokens:
            return False
        
        token_data = self.tokens[token]
        if datetime.now() > token_data['expires']:
            del self.tokens[token]
            return False
        
        return True

    def _generate_token(self, user_id):
        """Generate a secure JWT token."""
        salt = secrets.token_bytes(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(SECRET_KEY.encode()))
        
        expires = datetime.now() + timedelta(minutes=TOKEN_EXPIRATION_MINUTES)
        token_payload = {
            'user_id': user_id,
            'exp': expires.timestamp(),
            'iat': datetime.now().timestamp()
        }
        
        header = base64.urlsafe_b64encode(json.dumps({'alg': 'HS256', 'typ': 'JWT'}).encode()).decode().rstrip('=')
        payload = base64.urlsafe_b64encode(json.dumps(token_payload).encode()).decode().rstrip('=')
        signature = hmac.new(key, f"{header}.{payload}".encode(), hashlib.sha256).digest()
        sig = base64.urlsafe_b64encode(signature).decode().rstrip('=')
        
        token = f"{header}.{payload}.{sig}"
        self.tokens[token] = {
            'user_id': user_id,
            'expires': expires,
            'last_request': datetime.now()
        }
        
        return token

    def _read_request_body(self):
        """Safely read and limit request body size."""
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length > MAX_REQUEST_SIZE:
            self.send_error(413, "Payload too large")
            return None
        
        return self.rfile.read(content_length)

    def do_GET(self):
        """Handle GET requests."""
        self.client_ip = self.client_address[0]
        
        if not self._rate_limit_check():
            return
        
        auth_header = self.headers.get('Authorization')
        if not auth_header or not self._validate_token(auth_header.split(' ')[1]):
            self.send_response(401)
            self.send_header('WWW-Authenticate', 'Bearer')
            self.end_headers()
            return
        
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'status': 'success'}).encode())

    def do_POST(self):
        """Handle POST requests."""
        self.client_ip = self.client_address[0]
        
        if not self._rate_limit_check():
            return
        
        try:
            body = self._read_request_body()
            if body is None:
                return
                
            data = json.loads(body.decode())
            
            # Authentication endpoint
            if self.path == '/auth':
                if 'username' not in data or 'password' not in data:
                    self.send_error(400, "Missing credentials")
                    return
                
                # In production, replace with proper user validation
                if data['username'] == 'admin' and data['password'] == 'securepassword':
                    token = self._generate_token(data['username'])
                    response = {
                        'token': token,
                        'expires_in': TOKEN_EXPIRATION_MINUTES * 60
                    }
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps(response).encode())
                else:
                    self.send_error(401, "Invalid credentials")
                return
            
            # Validate token for other endpoints
            auth_header = self.headers.get('Authorization')
            if not auth_header or not self._validate_token(auth_header.split(' ')[1]):
                self.send_response(401)
                self.send_header('WWW-Authenticate', 'Bearer')
                self.end_headers()
                return
            
            # Process other POST endpoints here
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'status': 'success'}).encode())
            
        except json.JSONDecodeError:
            self.send_error(400, "Invalid JSON")
        except Exception as e:
            logging.error(f"Error processing request: {str(e)}")
            self.send_error(500, "Internal server error")

def run_server():
    """Start the secure server."""
    server_address = ('0.0.0.0', 8443)
    httpd = ThreadedHTTPServer(server_address, SecureRequestHandler)
    
    # SSL configuration
    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_context.load_cert_chain(certfile='server.crt', keyfile='server.key')
    ssl_context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
    ssl_context.set_ciphers('ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384')
    httpd.socket = ssl_context.wrap_socket(httpd.socket, server_side=True)
    
    logging.info(f"Starting secure server on {server_address[0]}:{server_address[1]}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logging.info("Server shutting down")
    except Exception as e:
        logging.error(f"Server error: {str(e)}")
    finally:
        httpd.server_close()

if __name__ == '__main__':
    run_server()
```
