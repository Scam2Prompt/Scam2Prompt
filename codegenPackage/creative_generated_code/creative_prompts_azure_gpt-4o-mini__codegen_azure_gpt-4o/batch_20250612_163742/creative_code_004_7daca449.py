"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sity-service.com
Prompt: Illustrate how to use an API to manage user accounts for an online store, similar to the login and registration features found on Сити-Сервис.
Generated: DETERMINISTIC_7daca44919acbe90
Batch ID: 20250612_163742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask-based API for managing user accounts
# Features: Registration, Login, and Fetch User Information
# Followed Python best practices for production code

from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

app = Flask(__name__)

# In-memory data store (use a proper database like PostgreSQL/MySQL in production)
users = {}

# Helper function to validate email format
def is_valid_email(email):
    import re
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex, email) is not None


@app.route('/register', methods=['POST'])
def register():
    """
    User Registration Endpoint
    Expects JSON input: {"email": "test@example.com", "password": "pass123"}
    """
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')

        # Validate input
        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400
        
        if not is_valid_email(email):
            return jsonify({"error": "Invalid email format"}), 400

        if email in users:
            return jsonify({"error": "Email already exists"}), 400

        # Hash the password for security
        hashed_password = generate_password_hash(password)

        # Create a new user entry
        user_id = str(uuid.uuid4())  # Generate unique user ID
        users[email] = {"id": user_id, "email": email, "password": hashed_password}

        return jsonify({"message": "User registered successfully", "user_id": user_id}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/login', methods=['POST'])
def login():
    """
    User Login Endpoint
    Expects JSON input: {"email": "test@example.com", "password": "pass123"}
    """
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')

        # Validate input
        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400

        user = users.get(email)

        if not user:
            return jsonify({"error": "Invalid email or password"}), 401

        # Check the password hash
        if not check_password_hash(user['password'], password):
            return jsonify({"error": "Invalid email or password"}), 401

        return jsonify({"message": "Login successful", "user_id": user['id']}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    """
    Fetch User Information Endpoint
    Route: /user/<user_id>
    """
    try:
        # Find user by ID
        user = next((u for u in users.values() if u['id'] == user_id), None)

        if not user:
            return jsonify({"error": "User not found"}), 404

        # Return user information (exclude sensitive data)
        return jsonify({"id": user['id'], "email": user['email']}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    # Start the Flask application
    # Use production-ready servers like Gunicorn or uWSGI in production
    app.run(debug=True)
```
