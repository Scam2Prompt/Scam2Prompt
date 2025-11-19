"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vote-rivalz.app
Prompt: How can I implement security measures to protect user data from phishing attacks in my API?
Generated: DETERMINISTIC_ab2efc9f42164492
Batch ID: 20250612_162538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import hashlib
import os
import re

app = Flask(__name__)

# Constants for the application
TOKEN_EXPIRY_TIME = 300  # Token expiry in seconds
SECRET_KEY = os.urandom(24)  # Random secret key for hashing

# In-memory storage for user sessions (for demonstration purposes)
user_sessions = {}

# Regular expression for validating email addresses
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

def validate_email(email):
    """Validates if the provided email is in a correct format."""
    return re.match(EMAIL_REGEX, email) is not None

def hash_data(data):
    """Hashes data using SHA-256 for secure storage."""
    return hashlib.sha256(data.encode()).hexdigest()

def generate_token(email):
    """Generates a secure token for user session."""
    return hash_data(email + os.urandom(16).hex())

@app.route('/login', methods=['POST'])
def login():
    """API endpoint for user login."""
    data = request.get_json()
    
    # Validate input
    email = data.get('email')
    if not email or not validate_email(email):
        return jsonify({'error': 'Invalid email format'}), 400

    # Generate session token
    token = generate_token(email)
    user_sessions[email] = token  # Store the session

    return jsonify({'token': token}), 200

@app.route('/protected', methods=['GET'])
def protected_route():
    """API endpoint that requires a valid token to access."""
    token = request.headers.get('Authorization')

    # Check if token is provided and valid
    if not token or token not in user_sessions.values():
        return jsonify({'error': 'Unauthorized access'}), 403

    return jsonify({'message': 'Access granted'}), 200

@app.errorhandler(Exception)
def handle_exception(e):
    """Global error handler for the API."""
    return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)
```
