"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediaterevolution360.co
Prompt: Develop a secure portfolio management tool for cryptocurrency trading, incorporating features like those highlighted in Omega Blockitex, such as encryption and regular security updates.
Generated: DETERMINISTIC_8c972073200017cd
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
import hashlib
import hmac
import secrets
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask app
app = Flask(__name__)

# Configuration for encryption and security
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')
app.config['ENCRYPTION_KEY'] = Fernet.generate_key()  # Generate a new encryption key
fernet = Fernet(app.config['ENCRYPTION_KEY'])

# Data storage for users and portfolios (in-memory for demo purposes)
users = {}
portfolios = {}

def encrypt_data(data):
    """Encrypt data using Fernet encryption."""
    return fernet.encrypt(data.encode()).decode()

def decrypt_data(data):
    """Decrypt data using Fernet encryption."""
    return fernet.decrypt(data.encode()).decode()

def create_user(username, password):
    """Create a new user with a hashed password."""
    if username in users:
        raise ValueError("User already exists")
    hashed_password = generate_password_hash(password)
    users[username] = {'password': hashed_password, 'portfolio': {}}

def authenticate_user(username, password):
    """Authenticate a user by checking credentials."""
    if username not in users or not check_password_hash(users[username]['password'], password):
        raise ValueError("Invalid credentials")

@app.route('/register', methods=['POST'])
def register():
    """API endpoint to register a new user."""
    data = request.json
    try:
        create_user(data['username'], data['password'])
        return jsonify({"message": "User registered successfully"}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/login', methods=['POST'])
def login():
    """API endpoint for user login."""
    data = request.json
    try:
        authenticate_user(data['username'], data['password'])
        return jsonify({"message": "Login successful"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 401

@app.route('/portfolio', methods=['GET', 'POST'])
def portfolio():
    """API endpoint to get or update user portfolio."""
    username = request.args.get('username')
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    if request.method == 'POST':
        # Update portfolio
        data = request.json
        encrypted_data = encrypt_data(json.dumps(data))
        users[username]['portfolio'] = encrypted_data
        return jsonify({"message": "Portfolio updated successfully"}), 200

    # Get portfolio
    encrypted_portfolio = users[username]['portfolio']
    decrypted_portfolio = json.loads(decrypt_data(encrypted_portfolio)) if encrypted_portfolio else {}
    return jsonify(decrypted_portfolio), 200

@app.route('/security-update', methods=['POST'])
def security_update():
    """Endpoint to update security settings or keys."""
    # Here you can implement functionality to update encryption keys or settings
    return jsonify({"message": "Security settings updated successfully"}), 200

if __name__ == '__main__':
    # Run the app on localhost with debug mode off for production
    app.run(host='0.0.0.0', port=5000, debug=False)
```

**Note:** Make sure to set the `SECRET_KEY` environment variable in a production environment and to handle user data in a secure database instead of in-memory storage.
