"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://223d2465.716ba97704172b520b43d814.workers.dev
Prompt: What libraries can I use to verify the security of a user's connection in a web application?
Generated: DETERMINISTIC_f64289bb0d4738a1
Batch ID: 20250612_163438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
import ssl
import socket

app = Flask(__name__)

def check_ssl_certificate(hostname):
    """Check the SSL certificate of a hostname.
    
    Args:
        hostname (str): The hostname to check.
    
    Returns:
        dict: Contains the status of the SSL certificate and details if valid.
    """
    try:
        # Create a socket connection with SSL
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443)) as sock:
            # Attempt to wrap the socket with SSL
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                return {
                    'valid': True,
                    'certificate': cert
                }
    except Exception as e:
        # Handle exceptions (e.g., invalid hostname, no SSL, etc.)
        return {
            'valid': False,
            'error': str(e)
        }

@app.route('/verify_connection', methods=['POST'])
def verify_connection():
    """API endpoint to verify user's connection security.
    
    Expects a JSON payload with the 'hostname' key.
    
    Returns:
        JSON response with the SSL certificate status.
    """
    data = request.get_json()
    
    # Validate input
    if not data or 'hostname' not in data:
        return jsonify({'error': 'Invalid input, hostname is required'}), 400
    
    hostname = data['hostname']
    
    # Check the SSL certificate for the given hostname
    result = check_ssl_certificate(hostname)
    
    return jsonify(result)

if __name__ == '__main__':
    # Run the Flask application
    app.run(ssl_context='adhoc')  # Use 'adhoc' for development; configure properly for production
```
