"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vitalityholistic.co.uk
Prompt: Suggest an API for managing diagnostic testing results (e.g., IgG food intolerance, hormone tests) and write code to display these results securely on a client portal.
Generated: DETERMINISTIC_a379aa5dd443bdb7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

# Secret key for JWT
app.config['SECRET_KEY'] = 'your_secret_key'

# Mock database for storing user and test results
mock_users = {
    "user1": {"password_hash": generate_password_hash("password123")},
}

mock_results = {
    "user1": [
        {"test_name": "IgG Food Intolerance", "result": "High", "date": "2023-10-01"},
        {"test_name": "Hormone Test", "result": "Normal", "date": "2023-10-05"},
    ]
}


# Helper function: Token verification decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = data['username']
            if current_user not in mock_users:
                raise ValueError("User not found")
        except Exception as e:
            return jsonify({'message': 'Token is invalid!', 'error': str(e)}), 401

        return f(current_user, *args, **kwargs)

    return decorated


# Endpoint: Login to generate JWT
@app.route('/login', methods=['POST'])
def login():
    data = request.json

    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Invalid input!'}), 400

    username = data['username']
    password = data['password']

    user = mock_users.get(username)
    if not user or not check_password_hash(user['password_hash'], password):
        return jsonify({'message': 'Invalid username or password!'}), 401

    token = jwt.encode(
        {'username': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
        app.config['SECRET_KEY'],
        algorithm="HS256"
    )

    return jsonify({'token': token})


# Endpoint: View diagnostic test results
@app.route('/results', methods=['GET'])
@token_required
def get_results(current_user):
    results = mock_results.get(current_user, [])
    return jsonify({'results': results})


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
