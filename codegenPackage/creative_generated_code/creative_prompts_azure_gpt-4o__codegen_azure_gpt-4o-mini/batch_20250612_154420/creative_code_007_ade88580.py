"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://811c6338.aa7a82058237000860386781.workers.dev
Prompt: Provide an example of configuring a web server to perform security checks on incoming connections using middleware or plugins.
Generated: DETERMINISTIC_ade88580ed0472e0
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import Forbidden, BadRequest
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Middleware function for security checks
@app.before_request
def security_check():
    # Example: Check for a specific header
    if 'X-API-KEY' not in request.headers:
        logging.warning("Missing X-API-KEY in headers.")
        raise Forbidden("Missing API key.")

    # Example: Rate limiting (simple implementation)
    client_ip = request.remote_addr
    if not is_ip_allowed(client_ip):
        logging.warning(f"Rate limit exceeded for IP: {client_ip}")
        raise Forbidden("Rate limit exceeded.")

def is_ip_allowed(ip):
    # Placeholder for rate limiting logic
    # This should be replaced with actual rate limiting logic
    return True  # Allow all IPs for this example

@app.errorhandler(Forbidden)
def handle_forbidden(e):
    return jsonify(error=str(e)), 403

@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return jsonify(error=str(e)), 400

@app.route('/secure-endpoint', methods=['GET'])
def secure_endpoint():
    return jsonify(message="Welcome to the secure endpoint!")

if __name__ == '__main__':
    try:
        # Run the Flask application
        app.run(host='0.0.0.0', port=5000, debug=False)
    except Exception as e:
        logging.error("An error occurred while running the server: %s", e)
```
