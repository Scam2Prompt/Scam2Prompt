"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://91224d72.5bab219c7482a7cd39bd1d22.workers.dev
Prompt: Write a code snippet that demonstrates how to enhance security checks for user connections in a web service.
Generated: DETERMINISTIC_c21a767ac2fcbfff
Batch ID: 20250612_164321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import re
from flask import Flask, request, jsonify
from werkzeug.security import safe_str_cmp

app = Flask(__name__)

# Define a list of allowed IPs (can be fetched from a secure config management system)
ALLOWED_IPS = {"192.168.1.100", "203.0.113.50"}

# Define a regex for validating User-Agent headers
USER_AGENT_REGEX = re.compile(r"^[a-zA-Z0-9\-\/\.\(\);]+$")

# Function to validate User-Agent header
def validate_user_agent(user_agent):
    return bool(USER_AGENT_REGEX.match(user_agent))

# Function to validate API keys
def validate_api_key(api_key):
    # Example static key validation (In production, use a secure key storage system)
    VALID_API_KEY = "secure_api_key_123"
    return safe_str_cmp(api_key, VALID_API_KEY)

@app.route('/secure-endpoint', methods=['POST'])
def secure_endpoint():
    """
    A secure endpoint that performs enhanced security checks
    """
    try:
        # Validate the client's IP address
        client_ip = request.remote_addr
        if client_ip not in ALLOWED_IPS:
            return jsonify({"error": "Forbidden: Unauthorized IP address"}), 403
        
        # Validate User-Agent header
        user_agent = request.headers.get("User-Agent")
        if not user_agent or not validate_user_agent(user_agent):
            return jsonify({"error": "Forbidden: Invalid User-Agent"}), 403
        
        # Validate API key (passed in request headers)
        api_key = request.headers.get("X-API-Key")
        if not api_key or not validate_api_key(api_key):
            return jsonify({"error": "Forbidden: Invalid API Key"}), 403
        
        # If all checks pass, process the request
        data = request.json  # Assuming JSON payload
        if not data:
            return jsonify({"error": "Bad Request: Missing JSON payload"}), 400
        
        # Example processing of the data
        return jsonify({"message": "Request processed successfully", "data": data}), 200

    except Exception as e:
        # Log the error (in production, use a logging library)
        print(f"Unexpected error: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

# Run the Flask app (not recommended for production directly; use WSGI servers)
if __name__ == '__main__':
    app.run(debug=True)  # Disable debug in production
```
