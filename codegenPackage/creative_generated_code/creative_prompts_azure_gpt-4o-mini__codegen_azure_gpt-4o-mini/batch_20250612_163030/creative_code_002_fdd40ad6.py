"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soulmagic.live
Prompt: What steps should I take to resolve permission issues leading to a "403 Forbidden" error on my server?
Generated: DETERMINISTIC_fdd40ad69faa1790
Batch ID: 20250612_163030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.errorhandler(403)
def forbidden_error(error):
    """Handle 403 Forbidden errors."""
    response = jsonify({'message': 'Forbidden: You do not have permission to access this resource.'})
    response.status_code = 403
    return response

@app.route('/resource', methods=['GET'])
def access_resource():
    """Endpoint to access a protected resource."""
    if not check_permissions(request):
        # Log the error
        logging.warning("Access denied for IP: %s", request.remote_addr)
        return forbidden_error(403)
    
    return jsonify({'message': 'Access granted to the resource.'})

def check_permissions(request):
    """
    Check if the user has permission to access the resource.
    
    Args:
    - request: Flask request object
    
    Returns:
    - bool: True if the user has permission, False otherwise
    """
    # Simulated permission check (this could be replaced with actual logic)
    user_ip = request.remote_addr
    allowed_ips = os.getenv('ALLOWED_IPS', '').split(',')

    return user_ip in allowed_ips

if __name__ == '__main__':
    # Set the allowed IPs as an environment variable for security
    os.environ['ALLOWED_IPS'] = '127.0.0.1,192.168.1.100'

    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
```
