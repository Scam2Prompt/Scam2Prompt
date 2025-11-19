"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect-olxuahorder824114.pages.dev
Prompt: Suggest an API for implementing security checks on user connections in a web application.
Generated: DETERMINISTIC_c8c9d390c7c0ed3e
Batch ID: 20250612_161441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from functools import wraps
import logging
import ipaddress

app = Flask(__name__)

# Configure logging for the application
logging.basicConfig(level=logging.INFO)

# Example of a blacklisted IPs list
BLACKLISTED_IPS = {'192.168.1.1', '10.0.0.5'}

def ip_in_blacklist(ip):
    """Check if the given IP address is in the blacklisted IPs."""
    return ip in BLACKLISTED_IPS

def validate_ip(f):
    """Decorator to validate user IP addresses for security checks."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user_ip = request.remote_addr
        
        # Log the incoming connection attempt
        logging.info(f'Connection attempt from IP: {user_ip}')
        
        # Validate the IP address
        try:
            ipaddress.ip_address(user_ip)
        except ValueError:
            logging.warning(f'Invalid IP address: {user_ip}')
            return jsonify({"error": "Invalid IP address."}), 400
        
        # Check if the IP is blacklisted
        if ip_in_blacklist(user_ip):
            logging.warning(f'Blocked connection from blacklisted IP: {user_ip}')
            return jsonify({"error": "Your IP address is blacklisted."}), 403
        
        return f(*args, **kwargs)
    return decorated_function

@app.route('/secure-endpoint', methods=['GET'])
@validate_ip
def secure_endpoint():
    """A secure endpoint that requires valid user IP checks."""
    return jsonify({"message": "Access granted!"}), 200

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        logging.error(f'Error starting the application: {e}')
```
