"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debtridge.online
Prompt: How can I implement password protection for an online shop similar to the one described on debtridge.online?
Generated: DETERMINISTIC_88a5803943befbe2
Batch ID: 20250612_160302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps

# Initialize the Flask application
app = Flask(__name__)

# Secret key for JWT (use a more secure key in production)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Mock database for users (replace with a real database in production)
users_db = {}

# Function to validate token for protected routes
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token')  # Retrieve token from request header
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = users_db.get(data['username'])
            if not current_user:
                raise ValueError('User does not exist.')
        except Exception as e:
            return jsonify({'message': f'Token is invalid! {str(e)}'}), 401
        return f(current_user, *args, **kwargs)
    return decorated

# Route to register new users
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'message': 'Username and Password are required!'}), 400
    
    if username in users_db:
        return jsonify({'message': 'User already exists!'}), 400
    
    # Hash the password for security
    hashed_password = generate_password_hash(password, method='sha256')
    users_db[username] = {'password': hashed_password}
    
    return jsonify({'message': 'User registered successfully!'})

# Route to log in users
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'message': 'Username and Password are required!'}), 400
    
    user = users_db.get(username)
    
    if not user or not check_password_hash(user['password'], password):
        return jsonify({'message': 'Invalid credentials!'}), 401
    
    # Generate token valid for 24 hours
    token = jwt.encode({'username': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)}, app.config['SECRET_KEY'], algorithm="HS256")
    
    return jsonify({'token': token})

# Protected route example
@app.route('/shop', methods=['GET'])
@token_required
def shop(current_user):
    return jsonify({'message': f'Welcome to the shop, {current_user}! Your access is secure.'})

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
