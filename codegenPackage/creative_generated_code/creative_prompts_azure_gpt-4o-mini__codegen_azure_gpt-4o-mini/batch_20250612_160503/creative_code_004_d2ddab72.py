"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea-six.vercel.app
Prompt: What are the best practices for building a user account system in an NFT marketplace similar to OpenSea, including wallet integration and profile management?
Generated: DETERMINISTIC_d2ddab72298b5a57
Batch ID: 20250612_160503
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
from flask_sqlalchemy import SQLAlchemy
from web3 import Web3
import os
import bcrypt

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///users.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    """Model representing a user account in the NFT marketplace."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    wallet_address = db.Column(db.String(42), unique=True, nullable=False)

    def set_password(self, password):
        """Hash the password for secure storage."""
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, password):
        """Verify the stored hashed password against the input password."""
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    """Endpoint for user registration."""
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    wallet_address = data.get('wallet_address')

    # Input validation
    if not all([username, email, password, wallet_address]):
        return jsonify({'error': 'All fields are required.'}), 400

    # Check if user already exists
    if User.query.filter((User.username == username) | (User.email == email)).first():
        return jsonify({'error': 'Username or email already exists.'}), 400

    # Create new user
    new_user = User(username=username, email=email, wallet_address=wallet_address)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully!'}), 201

@app.route('/login', methods=['POST'])
def login():
    """Endpoint for user login."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user is None or not user.check_password(password):
        return jsonify({'error': 'Invalid username or password.'}), 401

    return jsonify({'message': 'Login successful!', 'wallet_address': user.wallet_address}), 200

@app.route('/profile', methods=['GET'])
def profile():
    """Endpoint to retrieve user profile information."""
    username = request.args.get('username')

    user = User.query.filter_by(username=username).first()
    if user is None:
        return jsonify({'error': 'User not found.'}), 404

    return jsonify({
        'username': user.username,
        'email': user.email,
        'wallet_address': user.wallet_address
    }), 200

@app.route('/update_wallet', methods=['PUT'])
def update_wallet():
    """Endpoint to update user's wallet address."""
    data = request.json
    username = data.get('username')
    new_wallet_address = data.get('new_wallet_address')

    user = User.query.filter_by(username=username).first()
    if user is None:
        return jsonify({'error': 'User not found.'}), 404

    # Update wallet address
    user.wallet_address = new_wallet_address
    db.session.commit()

    return jsonify({'message': 'Wallet address updated successfully!'}), 200

# Error handling for unhandled exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    """Handle unhandled exceptions."""
    return jsonify({'error': 'An unexpected error occurred.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
