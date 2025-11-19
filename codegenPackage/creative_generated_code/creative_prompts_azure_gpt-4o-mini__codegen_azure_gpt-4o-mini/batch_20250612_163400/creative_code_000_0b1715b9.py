"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ionetsol.net
Prompt: How can I implement a security verification process similar to the one used by Cloudflare for my web application?
Generated: DETERMINISTIC_0b1715b946f3f289
Batch ID: 20250612_163400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, abort
import hashlib
import secrets
import time

app = Flask(__name__)

# Configuration for security settings
SECURITY_TOKEN_EXPIRY = 300  # Token expiry time in seconds
SECRET_KEY = 'your_secret_key'  # Replace with your actual secret key

# In-memory store for tokens (for demonstration only, use a persistent store in production)
tokens_store = {}

def generate_security_token(user_id):
    """Generate a secure token for the user."""
    token = f"{user_id}:{secrets.token_hex(16)}"
    token_hash = hashlib.sha256(token.encode('utf-8')).hexdigest()
    tokens_store[token_hash] = {
        'user_id': user_id,
        'expiry': time.time() + SECURITY_TOKEN_EXPIRY
    }
    return token_hash

def validate_security_token(token):
    """Validate the security token."""
    token_data = tokens_store.get(token)
    if not token_data:
        return False
    if time.time() > token_data['expiry']:
        del tokens_store[token]  # Remove expired token
        return False
    return True

@app.route('/request_security_token', methods=['POST'])
def request_security_token():
    """Endpoint to request a security token."""
    user_id = request.json.get('user_id')
    if not user_id:
        abort(400, 'User ID is required.')
    
    # Generate and return the security token
    token = generate_security_token(user_id)
    return jsonify({'token': token}), 201

@app.route('/secure_endpoint', methods=['GET'])
def secure_endpoint():
    """A secure endpoint that requires a valid security token."""
    token = request.headers.get('Authorization')
    if not token or not validate_security_token(token):
        abort(401, 'Unauthorized access. Invalid or expired token.')

    return jsonify({'message': 'Access granted to secure endpoint.'})

@app.errorhandler(400)
def handle_bad_request(error):
    """Handle bad requests with a custom message."""
    return jsonify({'error': str(error)}), 400

@app.errorhandler(401)
def handle_unauthorized(error):
    """Handle unauthorized access with a custom message."""
    return jsonify({'error': str(error)}), 401

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)  # Set debug=False in production
```
