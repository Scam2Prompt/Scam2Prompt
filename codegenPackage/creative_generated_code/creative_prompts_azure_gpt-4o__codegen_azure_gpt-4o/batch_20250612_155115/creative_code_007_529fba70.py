"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allorashopping.com
Prompt: Design a backend API endpoint to handle user authentication for an e-commerce platform, including login, sign-up, and password reset functionality.
Generated: DETERMINISTIC_529fba7042885d6e
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s a clean, production-ready implementation in Python using the Flask framework:

```python
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

# Secret key for JWT encoding/decoding
app.config['SECRET_KEY'] = 'your_secret_key_here'

# In-memory database for demonstration purposes
users_db = {}

# Helper function: Token authentication decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')  # Expecting "Bearer <token>"
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            token = token.split()[1]  # Extract token from "Bearer <token>"
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = users_db.get(data['email'])
            if not current_user:
                raise ValueError("Invalid token user")
        except Exception as e:
            return jsonify({'message': f'Token is invalid: {str(e)}'}), 401
        return f(current_user, *args, **kwargs)
    return decorated

# Endpoint: User sign-up
@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    # Validate input
    if not email or not password:
        return jsonify({'message': 'Email and password are required!'}), 400
    if email in users_db:
        return jsonify({'message': 'User already exists!'}), 400
    
    # Hash password before storing it
    hashed_password = generate_password_hash(password, method='sha256')
    users_db[email] = {'email': email, 'password': hashed_password}
    
    return jsonify({'message': 'User registered successfully!'}), 201

# Endpoint: User login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    # Validate input
    if not email or not password:
        return jsonify({'message': 'Email and password are required!'}), 400
    
    user = users_db.get(email)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({'message': 'Invalid email or password!'}), 401
    
    # Generate JWT token
    token = jwt.encode(
        {
            'email': email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        },
        app.config['SECRET_KEY'],
        algorithm="HS256"
    )
    
    return jsonify({'message': 'Login successful!', 'token': token}), 200

# Endpoint: Password reset
@app.route('/password-reset', methods=['POST'])
def password_reset():
    data = request.json
    email = data.get('email')
    new_password = data.get('new_password')
    
    # Validate input
    if not email or not new_password:
        return jsonify({'message': 'Email and new password are required!'}), 400
    
    user = users_db.get(email)
    if not user:
        return jsonify({'message': 'User not found!'}), 404
    
    # Update password
    hashed_password = generate_password_hash(new_password, method='sha256')
    user['password'] = hashed_password
    
    return jsonify({'message': 'Password reset successfully!'}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
