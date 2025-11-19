"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://treasury.casino
Prompt: Outline a RESTful API design for managing user accounts and transactions at Treasury Brisbane Casino, incorporating security measures mentioned on their site.
Generated: DETERMINISTIC_b8aaaa9daafd0d2a
Batch ID: 20250612_161231
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

# Secret key for JWT encoding/decoding
app.config['SECRET_KEY'] = 'your_secret_key'

# Sample in-memory storage for demonstration purposes
users = {}
transactions = {}

# Helper function for token-based authentication
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = users.get(data['email'])
            if not current_user:
                raise Exception('User not found')
        except Exception as e:
            return jsonify({'message': f'Token is invalid: {str(e)}'}), 401
        return f(current_user, *args, **kwargs)
    return decorated

# Route for user registration
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({'message': 'Email and password are required!'}), 400

    if email in users:
        return jsonify({'message': 'User already exists!'}), 400

    hashed_password = generate_password_hash(password, method='sha256')
    users[email] = {'email': email, 'password': hashed_password}
    return jsonify({'message': 'User registered successfully!'}), 201

# Route for user login
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    user = users.get(email)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({'message': 'Invalid email or password!'}), 401

    token = jwt.encode(
        {'email': email, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)},
        app.config['SECRET_KEY'],
        algorithm="HS256"
    )
    return jsonify({'token': token}), 200

# Route for creating a transaction
@app.route('/api/transactions', methods=['POST'])
@token_required
def create_transaction(current_user):
    data = request.get_json()
    transaction_id = str(len(transactions) + 1)
    amount = data.get('amount')
    description = data.get('description')

    if not amount or not description:
        return jsonify({'message': 'Amount and description are required!'}), 400

    transactions[transaction_id] = {
        'id': transaction_id,
        'user_email': current_user['email'],
        'amount': amount,
        'description': description,
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return jsonify({'message': 'Transaction created successfully!', 'transaction': transactions[transaction_id]}), 201

# Route for retrieving all transactions for a user
@app.route('/api/transactions', methods=['GET'])
@token_required
def get_transactions(current_user):
    user_transactions = [
        transaction for transaction in transactions.values()
        if transaction['user_email'] == current_user['email']
    ]
    return jsonify({'transactions': user_transactions}), 200

# Route for retrieving a specific transaction
@app.route('/api/transactions/<transaction_id>', methods=['GET'])
@token_required
def get_transaction(current_user, transaction_id):
    transaction = transactions.get(transaction_id)
    if not transaction or transaction['user_email'] != current_user['email']:
        return jsonify({'message': 'Transaction not found or access denied!'}), 404

    return jsonify({'transaction': transaction}), 200

# Error handler for 404 routes
@app.errorhandler(404)
def not_found(error):
    return jsonify({'message': 'Resource not found!'}), 404

# Run the API
if __name__ == '__main__':
    app.run(debug=True)
```
