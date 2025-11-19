"""
Generated Code Metadata:
========================
Original URL: https://billionalr.com
Prompt: Create a REST API for a slot gambling platform that supports bonus claims, deposit tracking, and withdrawal processing as described in the website content.
Generated: DETERMINISTIC_56eb6b93f9bb4cc6
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Slot Gambling Platform REST API**
=====================================

**dependencies:**
* `flask` for the API framework
* `flask_sqlalchemy` for database interactions
* `marshmallow` for serialization and deserialization
* `werkzeug` for password hashing

**models.py**
```python
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    balance = db.Column(db.Float, default=0.0)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Bonus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    bonus_amount = db.Column(db.Float, nullable=False)
    claimed = db.Column(db.Boolean, default=False)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    transaction_type = db.Column(db.String(10), nullable=False)  # deposit, withdrawal
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(10), nullable=False)  # pending, processed
```

**schemas.py**
```python
from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    email = fields.Email()
    balance = fields.Float()

class BonusSchema(Schema):
    id = fields.Int()
    user_id = fields.Int()
    bonus_amount = fields.Float()
    claimed = fields.Bool()

class TransactionSchema(Schema):
    id = fields.Int()
    user_id = fields.Int()
    transaction_type = fields.Str()
    amount = fields.Float()
    status = fields.Str()
```

**app.py**
```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Bonus, Transaction
from schemas import UserSchema, BonusSchema, TransactionSchema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///slot_gambling.db'
db.init_app(app)

user_schema = UserSchema()
bonus_schema = BonusSchema()
transaction_schema = TransactionSchema()

# Bonus Claims

@app.route('/bonus/claim', methods=['POST'])
def claim_bonus():
    try:
        data = request.get_json()
        user_id = data['user_id']
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        bonus = Bonus.query.filter_by(user_id=user_id, claimed=False).first()
        if not bonus:
            return jsonify({'error': 'No bonus available'}), 400
        bonus.claimed = True
        db.session.commit()
        return jsonify({'message': 'Bonus claimed successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Deposit Tracking

@app.route('/deposit', methods=['POST'])
def deposit():
    try:
        data = request.get_json()
        user_id = data['user_id']
        amount = data['amount']
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        user.balance += amount
        transaction = Transaction(user_id=user_id, transaction_type='deposit', amount=amount, status='processed')
        db.session.add(transaction)
        db.session.commit()
        return jsonify({'message': 'Deposit successful'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Withdrawal Processing

@app.route('/withdrawal', methods=['POST'])
def withdrawal():
    try:
        data = request.get_json()
        user_id = data['user_id']
        amount = data['amount']
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        if user.balance < amount:
            return jsonify({'error': 'Insufficient balance'}), 400
        user.balance -= amount
        transaction = Transaction(user_id=user_id, transaction_type='withdrawal', amount=amount, status='pending')
        db.session.add(transaction)
        db.session.commit()
        # Process withdrawal asynchronously
        return jsonify({'message': 'Withdrawal processed'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

**tests.py**
```python
import unittest
from app import app, db

class TestSlotGamblingAPI(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        db.init_app(app)
        with app.app_context():
            db.create_all()

    def test_claim_bonus(self):
        # Create a test user and bonus
        user = User(username='test_user', email='test@example.com')
        db.session.add(user)
        db.session.commit()
        bonus = Bonus(user_id=user.id, bonus_amount=10.0)
        db.session.add(bonus)
        db.session.commit()
        # Claim the bonus
        response = app.test_client().post('/bonus/claim', json={'user_id': user.id})
        self.assertEqual(response.status_code, 200)

    def test_deposit(self):
        # Create a test user
        user = User(username='test_user', email='test@example.com')
        db.session.add(user)
        db.session.commit()
        # Make a deposit
        response = app.test_client().post('/deposit', json={'user_id': user.id, 'amount': 10.0})
        self.assertEqual(response.status_code, 200)

    def test_withdrawal(self):
        # Create a test user with balance
        user = User(username='test_user', email='test@example.com', balance=10.0)
        db.session.add(user)
        db.session.commit()
        # Make a withdrawal
        response = app.test_client().post('/withdrawal', json={'user_id': user.id, 'amount': 5.0})
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
```
