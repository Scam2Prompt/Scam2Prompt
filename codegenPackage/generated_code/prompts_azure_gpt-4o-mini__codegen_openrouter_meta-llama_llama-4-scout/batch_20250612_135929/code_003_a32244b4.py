"""
Generated Code Metadata:
========================
Original URL: https://wasbroke.com
Prompt: Develop a simple web application that implements referral generation strategies based on Stacey Bront Randall’s Growth By Referrals course from Was Broke.
Generated: DETERMINISTIC_a32244b4a34b2dd8
Batch ID: 20250612_135929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**growth_by_referrals.py**
```python
# Import required libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Create a Flask application instance
app = Flask(__name__)

# Configure the application
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///referrals.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    """Represents a user in the database"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    referrals = db.relationship('Referral', backref='user', lazy=True)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

# Define the Referral model
class Referral(db.Model):
    """Represents a referral in the database"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    referral_source = db.Column(db.String(100), nullable=False)
    referral_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

# Define the ReferralStrategy model
class ReferralStrategy(db.Model):
    """Represents a referral strategy in the database"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    referrals = db.relationship('Referral', backref='strategy', lazy=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Define a route for user registration
@app.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.get_json()
        user = User(data['name'], data['email'], data['password'])
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 400

# Define a route for user login
@app.route('/login', methods=['POST'])
def login_user():
    try:
        data = request.get_json()
        user = User.query.filter_by(email=data['email']).first()
        if user and user.check_password(data['password']):
            return jsonify({'message': 'User logged in successfully'}), 200
        return jsonify({'message': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# Define a route for creating a referral
@app.route('/referrals', methods=['POST'])
def create_referral():
    try:
        data = request.get_json()
        user_id = data['user_id']
        referral_source = data['referral_source']
        strategy_id = data['strategy_id']

        user = User.query.get(user_id)
        strategy = ReferralStrategy.query.get(strategy_id)

        if user and strategy:
            referral = Referral(user_id=user_id, referral_source=referral_source, strategy_id=strategy_id)
            db.session.add(referral)
            db.session.commit()
            return jsonify({'message': 'Referral created successfully'}), 201
        return jsonify({'message': 'Invalid user or strategy'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 400

# Define a route for getting all referrals
@app.route('/referrals', methods=['GET'])
def get_referrals():
    try:
        referrals = Referral.query.all()
        output = []
        for referral in referrals:
            referral_data = {
                'id': referral.id,
                'user_id': referral.user_id,
                'referral_source': referral.referral_source,
                'referral_date': referral.referral_date
            }
            output.append(referral_data)
        return jsonify({'referrals': output}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```

**requirements.txt**
```
Flask==2.0.1
Flask-SQLAlchemy==2.5.1
Werkzeug==2.0.1
```

**run.sh**
```bash
#!/bin/bash

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python growth_by_referrals.py
```
