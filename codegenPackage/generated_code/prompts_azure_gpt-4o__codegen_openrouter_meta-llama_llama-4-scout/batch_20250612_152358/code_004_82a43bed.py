"""
Generated Code Metadata:
========================
Original URL: https://getfree.co.in
Prompt: Suggest tools or frameworks to build a referral tracking system for cryptocurrency faucets, referencing the referral and earning features mentioned on GetFree.co.in.
Generated: DETERMINISTIC_82a43bed15e4f333
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_tracking_system.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
import logging

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///referral_tracking.db'
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class User(db.Model):
    """Represents a user in the referral tracking system."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    referral_code = db.Column(db.String(100), unique=True, nullable=False)
    earnings = db.Column(db.Float, default=0.0)

    def __init__(self, username, password, referral_code):
        self.username = username
        self.password = generate_password_hash(password)
        self.referral_code = referral_code

    def __repr__(self):
        return f"User('{self.username}', '{self.referral_code}')"

class Referral(db.Model):
    """Represents a referral in the referral tracking system."""
    id = db.Column(db.Integer, primary_key=True)
    referrer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    referred_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    reward = db.Column(db.Float, default=0.0)

    def __init__(self, referrer_id, referred_id, reward):
        self.referrer_id = referrer_id
        self.referred_id = referred_id
        self.reward = reward

    def __repr__(self):
        return f"Referral('{self.referrer_id}', '{self.referred_id}')"

@app.route('/register', methods=['POST'])
def register_user():
    """Registers a new user with a referral code."""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid request data'}), 400

        username = data.get('username')
        password = data.get('password')
        referral_code = data.get('referral_code')

        if not username or not password or not referral_code:
            return jsonify({'error': 'Missing required fields'}), 400

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return jsonify({'error': 'Username already exists'}), 400

        new_user = User(username, password, referral_code)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        logger.error(str(e))
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/login', methods=['POST'])
def login_user():
    """Logs in a user and returns their referral code and earnings."""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid request data'}), 400

        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'error': 'Missing required fields'}), 400

        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return jsonify({'error': 'Invalid credentials'}), 401

        return jsonify({'referral_code': user.referral_code, 'earnings': user.earnings}), 200
    except Exception as e:
        logger.error(str(e))
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/refer', methods=['POST'])
def create_referral():
    """Creates a new referral and rewards the referrer."""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid request data'}), 400

        referrer_id = data.get('referrer_id')
        referred_id = data.get('referred_id')
        reward = data.get('reward')

        if not referrer_id or not referred_id or not reward:
            return jsonify({'error': 'Missing required fields'}), 400

        referrer = User.query.get(referrer_id)
        referred = User.query.get(referred_id)

        if not referrer or not referred:
            return jsonify({'error': 'Invalid user IDs'}), 400

        new_referral = Referral(referrer_id, referred_id, reward)
        db.session.add(new_referral)
        referrer.earnings += reward
        db.session.commit()

        return jsonify({'message': 'Referral created successfully'}), 201
    except Exception as e:
        logger.error(str(e))
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
