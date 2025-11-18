"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://westrockhomo.multitransportador.com.br
Prompt: Suggest best practices for implementing secure authentication when accessing the MultiTMS platform via a web application.
Generated: DETERMINISTIC_8cc87ad27fcda476
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Secure Authentication for accessing MultiTMS platform via a web application.
# Language: Python
# Framework: Flask

from flask import Flask, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

# Secret key for JWT (Ensure this is kept secure)
app.config['SECRET_KEY'] = 'your_super_secret_key'

# Mock database for demonstration purposes
users_db = {
    'example_user': generate_password_hash('example_password', method='sha256')
}

# Decorator for verifying JWT tokens
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')  # Get token from Authorization header
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        
        try:
            # Decode token using the secret key
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = data['username']
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'}), 401
        
        return f(current_user, *args, **kwargs)
    return decorated

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    auth_data = request.json
    
    if not auth_data or not auth_data.get('username') or not auth_data.get('password'):
        return jsonify({'message': 'Invalid request. Please provide username and password.'}), 400
    
    username = auth_data['username']
    password = auth_data['password']
    
    stored_password_hash = users_db.get(username)
    if not stored_password_hash or not check_password_hash(stored_password_hash, password):
        return jsonify({'message': 'Invalid username or password.'}), 401
    
    # Generate JWT token
    token = jwt.encode({
        'username': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expires in 1 hour
    }, app.config['SECRET_KEY'], algorithm="HS256")
    
    return jsonify({'token': token})

# Secure route example
@app.route('/secure-data', methods=['GET'])
@token_required
def secure_data(current_user):
    return jsonify({'message': f'Hello {current_user}, this is your secure data!'})

# Error handling for catching undefined routes
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'message': 'Route not found'}), 404)

# Run the application
if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for production
```

This code demonstrates secure authentication best practices using password hashing, JWT tokens, and token expiration for accessing secure endpoints.
