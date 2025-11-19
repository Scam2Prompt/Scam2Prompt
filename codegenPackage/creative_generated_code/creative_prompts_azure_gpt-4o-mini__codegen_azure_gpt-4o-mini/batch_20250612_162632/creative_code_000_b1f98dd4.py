"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://signup-zignaly.app
Prompt: What are the best practices for securing APIs against phishing attacks, as discussed in the context of website security?
Generated: DETERMINISTIC_b1f98dd45ed6cd0c
Batch ID: 20250612_162632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
import time
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# Configuration for API
API_KEY = os.environ.get('API_KEY')
TOKEN_EXPIRY_TIME = 3600  # Token validity in seconds

# In-memory store for API tokens
tokens = {}

def generate_api_token(user_id):
    """
    Generate a secure API token using user_id and current time.
    :param user_id: Unique identifier for the user
    :return: A hashed token
    """
    timestamp = str(int(time.time()))
    token = f"{user_id}:{timestamp}"
    return hashlib.sha256(token.encode()).hexdigest()

def is_token_valid(token):
    """
    Validate the API token and check its expiry.
    :param token: The token to validate
    :return: Boolean indicating validity
    """
    if token not in tokens:
        return False

    user_id, timestamp = tokens[token]
    if time.time() > float(timestamp) + TOKEN_EXPIRY_TIME:
        # Token has expired
        del tokens[token]
        return False
    return True

@app.route('/secure-endpoint', methods=['POST'])
def secure_endpoint():
    """
    A secure API endpoint that only accepts valid API tokens.
    :return: JSON response indicating success
    """
    token = request.headers.get('Authorization')
    if not token or not is_token_valid(token):
        abort(401)  # Unauthorized access

    # Logic for the secure operation
    return jsonify({"message": "Access granted. Secure operation executed."})

@app.route('/generate-token', methods=['POST'])
def generate_token():
    """
    Endpoint to generate an API token for a user.
    :return: JSON response containing the token
    """
    user_id = request.json.get('user_id')
    if not user_id:
        abort(400, "User ID is required")

    token = generate_api_token(user_id)
    tokens[token] = (user_id, str(int(time.time())))
    return jsonify({"token": token})

if __name__ == '__main__':
    # Ensure the app runs safely
    app.run(host='0.0.0.0', port=5000, debug=False)
```
