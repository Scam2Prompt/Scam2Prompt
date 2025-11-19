"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sup10xtrade.i.ng
Prompt: Create a REST API specification for a financial investment platform that includes features like user registration, investment tracking, and withdrawal requests, inspired by the services of 10x Investment.
Generated: DETERMINISTIC_46d4848d4b02d48c
Batch ID: 20250612_160220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

# Initialize Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///investments.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    investments = db.relationship('Investment', backref='owner', lazy=True)

# Investment model
class Investment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Withdrawal model
class Withdrawal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Create the database tables
with app.app_context():
    db.create_all()

# User Registration Endpoint
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Check if user already exists
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'User already exists'}), 400

    # Create a new user
    hashed_password = generate_password_hash(password, method='sha256')
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully'}), 201

# Investment Tracking Endpoint
@app.route('/api/invest', methods=['POST'])
def invest():
    data = request.get_json()
    username = data.get('username')
    amount = data.get('amount')

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404

    # Create a new investment
    new_investment = Investment(user_id=user.id, amount=amount)
    db.session.add(new_investment)
    db.session.commit()
    
    return jsonify({'message': 'Investment recorded'}), 201

# Withdrawal Request Endpoint
@app.route('/api/withdraw', methods=['POST'])
def withdraw():
    data = request.get_json()
    username = data.get('username')
    amount = data.get('amount')

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404

    # Create a withdrawal request
    new_withdrawal = Withdrawal(user_id=user.id, amount=amount)
    db.session.add(new_withdrawal)
    db.session.commit()
    
    return jsonify({'message': 'Withdrawal request submitted'}), 201

# Retrieve User Investments
@app.route('/api/investments/<username>', methods=['GET'])
def get_investments(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404

    investments = Investment.query.filter_by(user_id=user.id).all()
    investment_list = [{'id': inv.id, 'amount': inv.amount, 'created_at': inv.created_at} for inv in investments]
    
    return jsonify({'investments': investment_list}), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
