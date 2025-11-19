"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-93--quirky-shannon-80b532.netlify.app
Prompt: Write a code snippet that demonstrates how to secure web services, inspired by Nikko Williard’s focus on computing security at FOSS@RIT.
Generated: DETERMINISTIC_655dbec4d06fab8a
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_limiter import Limiter  # Prevent brute-force attacks with rate limiting
from flask_limiter.util import get_remote_address
from werkzeug.security import generate_password_hash, check_password_hash
import jwt  # For token-based authentication
import datetime
from functools import wraps

# Initialize the Flask application
app = Flask(__name__)

# Set a secret key for signing JWT tokens (ensure this is kept secure in production)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Initialize the rate limiter
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"]
)

# In-memory user storage (replace with a database in production)
users_db = {}

# Error handler for generic security errors
@app.errorhandler(429)
def rate_limit_error(e):
    return jsonify({'error': 'rate limit exceeded'}), 429

# Utility function for token verification
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')  # Expect Bearer token

        if not token:
            return jsonify({'error': 'Token is missing!'}), 401

        try:
            # Decode the token
            data = jwt.decode(token.split(" ")[1], app.config['SECRET_KEY'], algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token!'}), 401

        return f(*args, **kwargs)
    return decorated

# Route for user registration (hashed passwords for security)
@app.route('/register', methods=['POST'])
@limiter.limit("10 per minute")  # Apply rate limiting to prevent abuse
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required!'}), 400

    if username in users_db:
        return jsonify({'error': 'User already exists!'}), 409

    # Hash the password before storing it
    hashed_password = generate_password_hash(password, method='sha256')
    users_db[username] = hashed_password

    return jsonify({'message': 'User registered successfully!'}), 201

# Route for user login (JWT token for session)
@app.route('/login', methods=['POST'])
@limiter.limit("10 per minute")  # Apply rate limiting to prevent abuse
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required!'}), 400

    hashed_password = users_db.get(username)

    if not hashed_password or not check_password_hash(hashed_password, password):
        return jsonify({'error': 'Invalid username or password!'}), 401

    # Generate a JWT token for the user
    token = jwt.encode({
        'username': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expires in 1 hour
    }, app.config['SECRET_KEY'], algorithm="HS256")

    return jsonify({'token': token}), 200

# Protected route (requires valid token)
@app.route('/secure-data', methods=['GET'])
@token_required
def secure_data():
    return jsonify({'data': 'This is a secure resource'}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Use debug=False in production
```
