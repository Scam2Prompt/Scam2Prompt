"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://24397033.4d1df63187c716fb9bc6ff22.workers.dev
Prompt: Write a code snippet to enhance website security by verifying user connections before allowing access.
Generated: DETERMINISTIC_8ac8ddd7216d9486
Batch ID: 20250612_163251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, abort
from functools import wraps
import ipaddress

app = Flask(__name__)

# Define a list of allowed IP addresses (for demonstration purposes)
# In a production environment, this list can be loaded from a secure config or database
ALLOWED_IPS = ["192.168.1.10", "192.168.1.11"]

def verify_ip(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Get the client's IP address
        client_ip = request.remote_addr

        # Check if the client IP is in the allowed list
        if client_ip not in ALLOWED_IPS:
            # Log the unauthorized access attempt (in production, use a logging framework)
            app.logger.warning(f"Unauthorized access attempt from IP: {client_ip}")
            abort(403)  # Forbidden access

        return f(*args, **kwargs)
    return decorated_function

@app.route('/secure-data', methods=['GET'])
@verify_ip
def secure_data():
    """
    Endpoint to access secure data.
    Only accessible if the user's IP address is verified.
    """
    return jsonify({"message": "Access granted to secure data."})

if __name__ == '__main__':
    # Run the Flask application
    try:
        app.run(host='0.0.0.0', port=5000, debug=False)
    except Exception as e:
        app.logger.error(f"Error starting the application: {e}")
```
