"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://24397033.4d1df63187c716fb9bc6ff22.workers.dev
Prompt: What libraries can I use to perform security checks on incoming connections for my web service?
Generated: DETERMINISTIC_3e158747ba85236c
Batch ID: 20250612_163251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import logging
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest
import ipaddress

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the Flask application
app = Flask(__name__)

# Define a list of trusted IP addresses
TRUSTED_IPS = {"192.168.1.1", "10.0.0.1"}

def is_ip_trusted(ip):
    """
    Check if the incoming IP address is trusted.
    
    :param ip: The IP address to check.
    :return: True if trusted, False otherwise.
    """
    return ip in TRUSTED_IPS

@app.before_request
def security_check():
    """
    Perform security checks on incoming requests before processing.
    This includes checking if the IP address is trusted.
    """
    # Get the IP address of the incoming request
    ip = request.remote_addr
    logger.info(f"Incoming request from IP: {ip}")
    
    # Check if the IP address is trusted
    if not is_ip_trusted(ip):
        logger.warning(f"Unauthorized access attempt from IP: {ip}")
        return jsonify({'error': 'Unauthorized access'}), 403

@app.route('/secure-endpoint', methods=['GET'])
def secure_endpoint():
    """
    A secure endpoint that requires a trusted IP address to access.

    :return: A message confirming access to the secure endpoint.
    """
    return jsonify({'message': 'Access granted to secure endpoint'})

@app.errorhandler(BadRequest)
def handle_bad_request(e):
    """
    Handle bad request errors.
    
    :param e: The exception instance.
    :return: A JSON response with error details.
    """
    logger.error(f"Bad request: {e}")
    return jsonify({'error': 'Bad request'}), 400

if __name__ == '__main__':
    try:
        # Start the Flask application
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        logger.error(f"Failed to start application: {e}")
```
