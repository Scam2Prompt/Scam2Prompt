"""
Generated Code Metadata:
========================
Original URL: https://syr-whistler.com
Prompt: How can I secure a CGI directory on my server to prevent unauthorized access, considering best practices for permissions and authentication?
Generated: DETERMINISTIC_1cc90c7255024d89
Batch ID: 20250622_204656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Secure CGI Directory Script

This script implements security measures for a CGI directory including:
- Setting proper file permissions
- Implementing basic authentication
- Logging access attempts
"""

import os
import stat
import hashlib
import base64
from http.server import CGIHTTPRequestHandler, HTTPServer
from functools import partial

# Configuration
CGI_DIR = '/path/to/cgi-bin'  # Replace with your CGI directory path
AUTH_FILE = '/path/to/.htpasswd'  # Replace with your auth file path
LOG_FILE = '/var/log/cgi_access.log'  # Replace with your log file path
ALLOWED_USERS = {'admin': 'hashed_password'}  # Replace with actual hashed passwords

def setup_directory_permissions():
    """Set secure permissions for CGI directory and files"""
    try:
        # Set directory permissions to 711 (rwx--x--x)
        os.chmod(CGI_DIR, stat.S_IRWXU | stat.S_IXGRP | stat.S_IXOTH)
        
        # Set permissions for files in CGI directory (750 - rwxr-x---)
        for root, dirs, files in os.walk(CGI_DIR):
            for d in dirs:
                os.chmod(os.path.join(root, d), stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP)
            for f in files:
                os.chmod(os.path.join(root, f), stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP | S_IXGRP)
    except Exception as e:
        log_error(f"Permission setup failed: {str(e)}")
        raise

def hash_password(password):
    """Hash password using SHA-256 with salt"""
    salt = os.urandom(16)
    return hashlib.sha256(salt + password.encode()).hexdigest()

def verify_password(username, password):
    """Verify user credentials"""
    if username not in ALLOWED_USERS:
        return False
    
    # In production, compare with stored hashed password from auth file
    stored_hash = ALLOWED_USERS[username]
    input_hash = hashlib.sha256(password.encode()).hexdigest()
    return stored_hash == input_hash

def log_access(ip, username, success):
    """Log access attempts"""
    status = "SUCCESS" if success else "FAILURE"
    log_entry = f"{ip} - {username} - {status}\n"
    try:
        with open(LOG_FILE, 'a') as f:
            f.write(log_entry)
    except IOError as e:
        print(f"Failed to log access: {str(e)}")

class SecureCGIHandler(CGIHTTPRequestHandler):
    """Custom CGI handler with authentication"""
    
    def do_AUTH(self):
        """Handle Basic Authentication"""
        auth_header = self.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Basic '):
            self.send_auth_challenge()
            return False
        
        try:
            encoded_creds = auth_header.split(' ')[1]
            decoded_creds = base64.b64decode(encoded_creds).decode('utf-8')
            username, password = decoded_creds.split(':', 1)
            
            if verify_password(username, password):
                log_access(self.client_address[0], username, True)
                return True
            else:
                log_access(self.client_address[0], username, False)
                self.send_auth_challenge()
                return False
        except Exception as e:
            log_access(self.client_address[0], "UNKNOWN", False)
            self.send_auth_challenge()
            return False
    
    def send_auth_challenge(self):
        """Send authentication challenge"""
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm="CGI Access"')
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Authentication required')
    
    def is_cgi(self):
        """Override to add authentication check"""
        if not self.do_AUTH():
            return False
        return super().is_cgi()

def run_server():
    """Run the secured CGI server"""
    try:
        setup_directory_permissions()
        handler = partial(SecureCGIHandler, cgi_directories=[CGI_DIR])
        server = HTTPServer(('localhost', 8000), handler)
        print(f"Secured CGI server running on port 8000")
        server.serve_forever()
    except Exception as e:
        print(f"Server error: {str(e)}")
        raise

if __name__ == '__main__':
    run_server()
```
