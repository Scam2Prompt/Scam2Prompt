"""
Generated Code Metadata:
========================
Original URL: https://daplatform.one
Prompt: "What are some best practices for securing APIs on a data platform, and how can they be implemented?"
Generated: DETERMINISTIC_11958f0ce2b6e0fc
Batch ID: 20250622_211811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from functools import wraps
from datetime import datetime, timedelta
import secrets
import string
import jwt
from flask import Flask, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask app
app = Flask(__name__)

# Configuration settings
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', secrets.token_hex(32))
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', secrets.token_hex(32))
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=30)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=1)

# Mock database for demonstration
users_db = {}

# Helper function to generate API keys
def generate_api_key(length=32):
    chars = string.ascii_letters + string.digits
    return ''.join(secrets.choice(chars) for _ in range(length))

# Authentication decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        
        try:
            data = jwt.decode(token, app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
            current_user = users_db.get(data['public_id'])
            if not current_user:
                return jsonify({'message': 'User not found!'}), 401
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'}), 401
        
        return f(current_user, *args, **kwargs)
    return decorated

# Rate limiting decorator (simplified)
def rate_limit(max_requests, time_window):
    def decorator(f):
        request_counts = {}
        
        @wraps(f)
        def wrapper(*args, **kwargs):
            ip = request.remote_addr
            now = datetime.now()
            key = f"{ip}:{now.minute // time_window}"
            
            if key not in request_counts:
                request_counts[key] = 1
            else:
                request_counts[key] += 1
                
            if request_counts[key] > max_requests:
                return jsonify({'message': 'Too many requests!'}), 429
                
            return f(*args, **kwargs)
        return wrapper
    return decorator

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Username and password required!'}), 400
    
    if data['username'] in users_db:
        return jsonify({'message': 'User already exists!'}), 400
    
    hashed_password = generate_password_hash(data['password'], method='sha256')
    api_key = generate_api_key()
    public_id = secrets.token_hex(16)
    
    users_db[data['username']] = {
        'public_id': public_id,
        'username': data['username'],
        'password': hashed_password,
        'api_key': api_key,
        'is_admin': False
    }
    
    return jsonify({
        'message': 'User created successfully!',
        'api_key': api_key
    }), 201

# Login endpoint
@app.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    
    if not auth or not auth.username or not auth.password:
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate': 'Basic realm="Login required!"'}
        )
    
    user = users_db.get(auth.username)
    if not user or not check_password_hash(user['password'], auth.password):
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate': 'Basic realm="Login required!"'}
        )
    
    token = jwt.encode({
        'public_id': user['public_id'],
        'exp': datetime.utcnow() + app.config['JWT_ACCESS_TOKEN_EXPIRES']
    }, app.config['JWT_SECRET_KEY'])
    
    return jsonify({'token': token})

# Protected endpoint example
@app.route('/protected', methods=['GET'])
@token_required
@rate_limit(max_requests=100, time_window=1)
def protected(current_user):
    return jsonify({'message': f'Hello {current_user["username"]}! This is a protected endpoint.'})

# Health check endpoint
@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(ssl_context='adhoc', host='0.0.0.0', port=5000)
```
