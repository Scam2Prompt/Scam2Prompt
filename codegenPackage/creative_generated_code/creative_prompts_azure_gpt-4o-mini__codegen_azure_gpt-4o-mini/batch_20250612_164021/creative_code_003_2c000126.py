"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://formssubmitting.online
Prompt: How do I integrate a password verification system for form submissions in a web app?
Generated: DETERMINISTIC_2c0001269faefb5f
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import re

app = Flask(__name__)

# In-memory user store for demonstration; in production, use a database
users_db = {}

def is_valid_password(password):
    """Validate the password based on specific criteria."""
    # Password must be at least 8 characters long and contain a number
    if len(password) < 8 or not re.search(r'\d', password):
        return False
    return True

@app.route('/register', methods=['POST'])
def register_user():
    """Register a new user by storing their username and password."""
    data = request.get_json()
    
    username = data.get('username')
    password = data.get('password')

    # Validate input
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    if username in users_db:
        return jsonify({"error": "Username already exists"}), 409

    if not is_valid_password(password):
        return jsonify({"error": "Password must be at least 8 characters long and contain a number"}), 400

    # Hash the password for secure storage
    hashed_password = generate_password_hash(password)
    users_db[username] = hashed_password

    return jsonify({"message": "User registered successfully"}), 201


@app.route('/login', methods=['POST'])
def login_user():
    """Verify user credentials and respond accordingly."""
    data = request.get_json()
    
    username = data.get('username')
    password = data.get('password')

    # Validate input
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400
    
    stored_password = users_db.get(username)

    # Check if the username exists and verify the password
    if not stored_password or not check_password_hash(stored_password, password):
        return jsonify({"error": "Invalid username or password"}), 401

    return jsonify({"message": "Login successful"}), 200


if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```

### Requirements
Make sure to install Flask and Werkzeug before running the code:
```bash
pip install Flask Werkzeug
```
