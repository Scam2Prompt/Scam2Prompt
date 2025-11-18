"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://joincommonwealth-8g6.pages.dev
Prompt: Create a script to allow users to log in using either their email or a connected cryptocurrency wallet, referencing the login options provided on the Common Wealth webpage.
Generated: DETERMINISTIC_99bb43b55af753d8
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import flask
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
import os

# Initialize Flask app
app = Flask(__name__)

# Configure app and database
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_secret_key_here')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    wallet_address = db.Column(db.String(255), unique=True, nullable=True)

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/login', methods=['POST'])
def login():
    """
    Login endpoint for users to authenticate using email/password or wallet address.
    """
    data = request.get_json()

    if 'email' in data and 'password' in data:
        return login_with_email(data['email'], data['password'])
    elif 'wallet_address' in data:
        return login_with_wallet(data['wallet_address'])
    else:
        return jsonify({'message': 'Invalid login method'}), 400

def login_with_email(email, password):
    """
    Authenticate user with email and password.
    """
    user = User.query.filter_by(email=email).first()
    
    if user and check_password_hash(user.password_hash, password):
        token = generate_token(user.id)
        return jsonify({'token': token}), 200
    return jsonify({'message': 'Invalid email or password'}), 401

def login_with_wallet(wallet_address):
    """
    Authenticate user using connected cryptocurrency wallet address.
    """
    user = User.query.filter_by(wallet_address=wallet_address).first()

    if user:
        token = generate_token(user.id)
        return jsonify({'token': token}), 200
    return jsonify({'message': 'No user associated with this wallet address'}), 404

def generate_token(user_id):
    """
    Generate JWT token for the authenticated user.
    """
    token = jwt.encode({
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, app.config['SECRET_KEY'], algorithm='HS256')
    
    return token

@app.route('/register', methods=['POST'])
def register():
    """
    Registration endpoint for new users to create an account.
    """
    data = request.get_json()
    
    if not data or not ('email' in data and 'password' in data):
        return jsonify({'message': 'Missing email or password'}), 400

    # Check if email already exists
    existing_user = User.query.filter_by(email=data['email']).first()
    if existing_user:
        return jsonify({'message': 'Email already registered'}), 400
    
    # Register new user
    new_user = User(
        email=data['email'],
        password_hash=generate_password_hash(data['password']),
        wallet_address=data.get('wallet_address')  # Wallet address is optional
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)
```
