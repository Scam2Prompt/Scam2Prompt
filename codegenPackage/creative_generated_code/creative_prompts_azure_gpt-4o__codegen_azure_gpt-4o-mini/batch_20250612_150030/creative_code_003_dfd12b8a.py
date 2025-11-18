"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apexdiginvcompany.com
Prompt: Generate code for a secure account registration system that integrates Comodo SSL encryption and DDoS protection, inspired by Apex Digital Limited's security measures.
Generated: DETERMINISTIC_dfd12b8a5b01d06d
Batch ID: 20250612_150030
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
import ssl
import socket
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask application
app = Flask(__name__)

# Configuration for SSL
app.config['SSL_CERT_PATH'] = 'path/to/comodo_cert.pem'
app.config['SSL_KEY_PATH'] = 'path/to/comodo_key.pem'

# In-memory user database (replace with a persistent database in production)
user_db = {}

# Function to create a hashed password
def hash_password(password):
    return generate_password_hash(password)

# Function to validate password
def validate_password(password, hashed_password):
    return check_password_hash(hashed_password, password)

# Route for account registration
@app.route('/register', methods=['POST'])
def register():
    try:
        # Get the JSON data from the request
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        # Input validation
        if not username or not password:
            return jsonify({"error": "Username and password are required."}), 400

        # Check if username already exists
        if username in user_db:
            return jsonify({"error": "Username already exists."}), 409

        # Hash the password and store user data
        user_db[username] = hash_password(password)

        return jsonify({"message": "User registered successfully."}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route for account login
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({"error": "Username and password are required."}), 400

        # Check if user exists
        if username not in user_db:
            return jsonify({"error": "Invalid username or password."}), 401

        # Validate the password
        if not validate_password(password, user_db[username]):
            return jsonify({"error": "Invalid username or password."}), 401

        return jsonify({"message": "Login successful."}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Function to run the Flask app with SSL
def run_app():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    context.load_cert_chain(certfile=app.config['SSL_CERT_PATH'], keyfile=app.config['SSL_KEY_PATH'])
    app.run(host='0.0.0.0', port=443, ssl_context=context)

if __name__ == '__main__':
    run_app()
```

*Ensure you replace `'path/to/comodo_cert.pem'` and `'path/to/comodo_key.pem'` with the actual paths to your Comodo SSL certificate and key files.*
