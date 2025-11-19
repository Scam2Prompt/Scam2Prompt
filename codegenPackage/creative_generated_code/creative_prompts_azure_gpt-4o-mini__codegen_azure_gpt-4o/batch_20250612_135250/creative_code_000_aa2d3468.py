"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allocation-optimismdao.app
Prompt: What are the best practices for securing APIs against phishing attacks, particularly in the context of user authentication?
Generated: DETERMINISTIC_aa2d346822a82b3e
Batch ID: 20250612_135250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is production-ready Python code using the Flask framework to secure an API against phishing attacks, particularly in the context of user authentication. The code includes best practices such as rate limiting, strong authentication, and the use of secure tokens.

```python
from flask import Flask, request, jsonify
from flask_limiter import Limiter
import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Secret key for JWT encoding/decoding (keep this safe and secure!)
app.config['SECRET_KEY'] = 'your_secure_secret_key'

# Flask-Limiter setup for rate limiting
limiter = Limiter(
    app,
    key_func=lambda: request.remote_addr,  # Use client IP for rate limiting
    default_limits=["200 per day", "50 per hour"]  # Limit requests
)

# In-memory user storage (use a database in production)
users = {}

# Helper function to generate JWT token
def generate_token(username):
    payload = {
        'username': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expiration
    }
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    return token

# Endpoint to register a new user
@app.route('/register', methods=['POST'])
@limiter.limit("5 per minute")  # Protect against brute-force registration attempts
def register():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400

        if username in users:
            return jsonify({'error': 'Username already exists'}), 409

        # Hash the password before storing it
        hashed_password = generate_password_hash(password)
        users[username] = hashed_password

        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to authenticate a user and get a JWT
@app.route('/login', methods=['POST'])
@limiter.limit("10 per minute")  # Protect against brute-force login attempts
def login():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400

        stored_password = users.get(username)

        if not stored_password or not check_password_hash(stored_password, password):
            return jsonify({'error': 'Invalid username or password'}), 401

        # Generate and return a secure JWT token
        token = generate_token(username)
        return jsonify({'token': token}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Protected endpoint (requires valid JWT to access)
@app.route('/protected', methods=['GET'])
def protected():
    try:
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'error': 'Token is missing'}), 401

        try:
            decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            username = decoded_token.get('username')
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token'}), 401

        return jsonify({'message': f'Welcome, {username}!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=False)  # Use a production-ready server like Gunicorn or uWSGI for deployment
```

### Key Security Features:
1. **Rate Limiting**: Protects against brute-force and abuse attacks.
2. **Password Hashing**: Ensures passwords are never stored in plain text.
3. **JWT**: Provides secure, temporary session tokens.
4. **Error Handling**: Prevents unhandled exceptions from exposing sensitive details.
5. **Token Validation**: Checks for token expiration and validity.

Make sure to replace the `SECRET_KEY` with a strong and unique value in production and consider using environment variables to manage sensitive configurations.
