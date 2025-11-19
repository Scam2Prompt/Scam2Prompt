"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://empower.gr
Prompt: Generate an API endpoint for user login and password recovery based on the features seen on Empower's login page.
Generated: DETERMINISTIC_0a737d04a06fc6da
Batch ID: 20250612_162812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
import jwt
import datetime
from functools import wraps

# Initialize Flask app
app = Flask(__name__)

# Secret key for encoding and decoding JWT tokens
app.config['SECRET_KEY'] = 'your_secret_key'

# Mock user database (normally you would use a real database)
users_db = {
    "user@example.com": {
        "password_hash": generate_password_hash("password123"),  # Password is 'password123'
        "recovery_question": "What is your pet's name?",
        "recovery_answer_hash": generate_password_hash("Fluffy"),
    }
}

# Helper function for token authentication
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"message": "Token is missing!"}), 401
        try:
            jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token has expired!"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Invalid token!"}), 401
        return f(*args, **kwargs)
    return decorated

# API endpoint for user login
@app.route('/login', methods=['POST'])
def login():
    # Input validation
    data = request.get_json()
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({"message": "Invalid input"}), 400
    
    # Verify user credentials
    user = users_db.get(data['email'])
    if not user:
        return jsonify({"message": "User not found"}), 404
    if not check_password_hash(user['password_hash'], data['password']):
        return jsonify({"message": "Incorrect password"}), 401
    
    # Generate JWT token (user authentication)
    token = jwt.encode(
        {'email': data['email'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
        app.config['SECRET_KEY'],
        algorithm="HS256"
    )
    return jsonify({"message": "Login successful", "token": token}), 200

# API endpoint for password recovery
@app.route('/recover-password', methods=['POST'])
def recover_password():
    # Input validation
    data = request.get_json()
    if not data or 'email' not in data or 'recovery_answer' not in data:
        return jsonify({"message": "Invalid input"}), 400
    
    # Verify user and recovery answer
    user = users_db.get(data['email'])
    if not user:
        return jsonify({"message": "User not found"}), 404
    if not check_password_hash(user['recovery_answer_hash'], data['recovery_answer']):
        return jsonify({"message": "Incorrect recovery answer"}), 401
    
    # Send password recovery details (in production, send an email or secure link)
    return jsonify({"message": "Password recovery successful. Please reset your password."}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
