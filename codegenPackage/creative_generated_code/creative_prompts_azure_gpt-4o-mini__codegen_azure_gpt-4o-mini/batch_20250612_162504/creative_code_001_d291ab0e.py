"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celesfia.site
Prompt: "What are the best practices for ensuring user data privacy in API development, as discussed on celesfia.site?"
Generated: DETERMINISTIC_d291ab0e67d2adcf
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import os
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Load environment variables for configurations (e.g., SECRET_KEY)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_secret_key')

# In-memory storage for demonstration (use a database in production)
user_data = {}

def validate_email(email):
    # Simple email validation
    return "@" in email and "." in email

@app.route('/register', methods=['POST'])
def register_user():
    """Register a new user and hash their password."""
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({"error": "Email and password are required."}), 400

        if not validate_email(email):
            return jsonify({"error": "Invalid email format."}), 400

        # Hash the password for security
        hashed_password = generate_password_hash(password)
        user_data[email] = hashed_password

        logging.info(f"User registered: {email}")
        return jsonify({"message": "User registered successfully."}), 201
    except Exception as e:
        logging.error(f"Error during registration: {str(e)}")
        return jsonify({"error": "An error occurred during registration."}), 500

@app.route('/login', methods=['POST'])
def login_user():
    """Authenticate a user by comparing hashed password."""
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({"error": "Email and password are required."}), 400

        # Check if the user exists and verify password
        hashed_password = user_data.get(email)
        if not hashed_password or not check_password_hash(hashed_password, password):
            return jsonify({"error": "Invalid email or password."}), 401

        logging.info(f"User logged in: {email}")
        return jsonify({"message": "Login successful."}), 200
    except Exception as e:
        logging.error(f"Error during login: {str(e)}")
        return jsonify({"error": "An error occurred during login."}), 500

if __name__ == '__main__':
    # Start the Flask application
    app.run(host='0.0.0.0', port=5000)
```
