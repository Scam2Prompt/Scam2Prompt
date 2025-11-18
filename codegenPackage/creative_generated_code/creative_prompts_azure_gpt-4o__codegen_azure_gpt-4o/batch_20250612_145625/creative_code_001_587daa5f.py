"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kangamoon-claim.pages.dev
Prompt: Generate code for a dashboard interface that allows users to register, buy $KANG tokens, confirm orders, and view their token balance, based on Kangamoon's presale process.
Generated: DETERMINISTIC_587daa5f22e0c1e3
Batch ID: 20250612_145625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, jsonify, session
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'secure_secret_key_for_sessions'
app.config['SESSION_TYPE'] = 'filesystem'

# Initialize session
Session(app)

# Mock database (in production, use a real database like MySQL/Postgres)
users_db = {}
transactions_db = {}

# Constants for $KANG token purchase
KANG_TOKEN_PRICE = 0.10  # Price per $KANG in USD

# Routes
@app.route('/')
def dashboard():
    """Render the dashboard interface."""
    if 'user_id' in session:
        user = users_db.get(session['user_id'])
        return render_template('dashboard.html', user=user)
    return render_template('login.html')

@app.route('/register', methods=['POST'])
def register():
    """Handle user registration."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    if username in users_db:
        return jsonify({'error': 'Username already exists'}), 409

    # Create user
    user_id = str(uuid.uuid4())
    users_db[username] = {
        'user_id': user_id,
        'username': username,
        'password': generate_password_hash(password),
        'balance': 0  # User's $KANG token balance
    }

    return jsonify({'message': 'User registered successfully', 'user_id': user_id}), 201

@app.route('/login', methods=['POST'])
def login():
    """Handle user login."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    user = users_db.get(username)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({'error': 'Invalid credentials'}), 401

    # Set session
    session['user_id'] = user['user_id']
    return jsonify({'message': 'Login successful'})

@app.route('/logout', methods=['POST'])
def logout():
    """Handle user logout."""
    session.pop('user_id', None)
    return jsonify({'message': 'Logout successful'})

@app.route('/buy_tokens', methods=['POST'])
def buy_tokens():
    """Allow user to buy $KANG tokens."""
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401

    user_id = session['user_id']
    user = next((u for u in users_db.values() if u['user_id'] == user_id), None)

    data = request.json
    usd_amount = data.get('usd_amount')

    if not usd_amount or usd_amount <= 0:
        return jsonify({'error': 'Invalid amount'}), 400

    # Calculate tokens and update balance
    tokens_to_buy = usd_amount / KANG_TOKEN_PRICE
    user['balance'] += tokens_to_buy

    # Record transaction
    transaction_id = str(uuid.uuid4())
    transactions_db[transaction_id] = {
        'transaction_id': transaction_id,
        'user_id': user_id,
        'tokens': tokens_to_buy,
        'usd_amount': usd_amount,
    }

    return jsonify({'message': 'Tokens purchased successfully', 'tokens': tokens_to_buy, 'balance': user['balance']}), 200

@app.route('/confirm_order', methods=['POST'])
def confirm_order():
    """Confirm the purchase of tokens."""
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401

    user_id = session['user_id']
    data = request.json
    transaction_id = data.get('transaction_id')

    if not transaction_id or transaction_id not in transactions_db:
        return jsonify({'error': 'Invalid or missing transaction ID'}), 400

    transaction = transactions_db[transaction_id]
    if transaction['user_id'] != user_id:
        return jsonify({'error': 'Unauthorized transaction'}), 403

    return jsonify({'message': 'Order confirmed', 'transaction': transaction}), 200

@app.route('/view_balance', methods=['GET'])
def view_balance():
    """View user's $KANG token balance."""
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401

    user_id = session['user_id']
    user = next((u for u in users_db.values() if u['user_id'] == user_id), None)

    return jsonify({'balance': user['balance']}), 200

if __name__ == '__main__':
    # In production, use a WSGI server like Gunicorn instead of Flask's built-in server
    app.run(debug=True)
```
