"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sit.d1jkap9jqfwf3j.amplifyapp.com
Prompt: Design a RESTful API that supports user authentication for exclusive offers on products like Tom Ford fragrances and Kiehl's skincare, similar to the features on Xhawi by Omantel.
Generated: DETERMINISTIC_43c78bfe9ed203ea
Batch ID: 20250612_162347
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
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

# Secret key for encoding and decoding JWT
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Mock database to store user information
users_db = {}

# Mock database for exclusive offers
exclusive_offers = [
    {"id": 1, "product": "Tom Ford Fragrance", "description": "Luxury fragrance", "price": 250},
    {"id": 2, "product": "Kiehl's Skincare", "description": "Premium skincare product", "price": 80}
]

# Utility function to check token validity
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"message": "Token is missing!"}), 401
        
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = users_db.get(data['username'])
            if current_user is None:
                return jsonify({"message": "Invalid token!"}), 401
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token has expired!"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Invalid token!"}), 401

        return f(current_user, *args, **kwargs)
    return decorated

@app.route('/register', methods=['POST'])
def register():
    """
    Endpoint to register a new user.
    Expects JSON payload with 'username' and 'password'.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Username and password are required!"}), 400

    if username in users_db:
        return jsonify({"message": "User already exists!"}), 409

    # Hash the password before storing it
    hashed_password = generate_password_hash(password, method='sha256')
    users_db[username] = {"password": hashed_password}

    return jsonify({"message": "User registered successfully!"}), 201

@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint to log in a user.
    Expects JSON payload with 'username' and 'password'.
    Returns a JWT token upon successful authentication.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Username and password are required!"}), 400

    user = users_db.get(username)
    if user and check_password_hash(user['password'], password):
        # Generate JWT token
        token = jwt.encode(
            {'username': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
            app.config['SECRET_KEY'], algorithm="HS256"
        )
        return jsonify({"token": token}), 200

    return jsonify({"message": "Invalid username or password!"}), 401

@app.route('/offers', methods=['GET'])
@token_required
def get_offers(current_user):
    """
    Endpoint to retrieve exclusive offers.
    Requires a valid JWT token.
    """
    return jsonify({"offers": exclusive_offers}), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors for undefined routes.
    """
    return jsonify({"message": "Resource not found!"}), 404

if __name__ == '__main__':
    app.run(debug=True)
```
