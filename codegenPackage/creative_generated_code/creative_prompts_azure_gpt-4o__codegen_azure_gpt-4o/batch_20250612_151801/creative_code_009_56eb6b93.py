"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://billionalr.com
Prompt: Create a REST API for a slot gambling platform that supports bonus claims, deposit tracking, and withdrawal processing as described in the website content.
Generated: DETERMINISTIC_56eb6b93f9bb4cc6
Batch ID: 20250612_151801
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
from sqlalchemy.exc import IntegrityError
import uuid

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///slot_gambling.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(50), unique=True, nullable=False)
    balance = db.Column(db.Float, default=0)

class Transaction(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # "deposit", "withdrawal", or "bonus"
    amount = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Routes
@app.route('/api/bonus', methods=['POST'])
def claim_bonus():
    """Allow a user to claim a bonus."""
    try:
        data = request.json
        username = data.get('username')
        bonus_amount = data.get('bonus_amount')

        if not username or not bonus_amount:
            return jsonify({"error": "Username and bonus amount are required."}), 400

        user = User.query.filter_by(username=username).first()
        if not user:
            return jsonify({"error": "User not found."}), 404

        user.balance += bonus_amount
        
        # Log the transaction
        transaction = Transaction(user_id=user.id, type="bonus", amount=bonus_amount)
        db.session.add(transaction)
        db.session.commit()

        return jsonify({"message": "Bonus claimed successfully.", "new_balance": user.balance}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/api/deposit', methods=['POST'])
def deposit():
    """Track a user's deposit."""
    try:
        data = request.json
        username = data.get('username')
        deposit_amount = data.get('deposit_amount')

        if not username or not deposit_amount:
            return jsonify({"error": "Username and deposit amount are required."}), 400

        user = User.query.filter_by(username=username).first()
        if not user:
            return jsonify({"error": "User not found."}), 404

        user.balance += deposit_amount
        
        # Log the transaction
        transaction = Transaction(user_id=user.id, type="deposit", amount=deposit_amount)
        db.session.add(transaction)
        db.session.commit()

        return jsonify({"message": "Deposit processed successfully.", "new_balance": user.balance}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/api/withdraw', methods=['POST'])
def withdraw():
    """Process a user's withdrawal."""
    try:
        data = request.json
        username = data.get('username')
        withdrawal_amount = data.get('withdrawal_amount')

        if not username or not withdrawal_amount:
            return jsonify({"error": "Username and withdrawal amount are required."}), 400

        user = User.query.filter_by(username=username).first()
        if not user:
            return jsonify({"error": "User not found."}), 404

        if user.balance < withdrawal_amount:
            return jsonify({"error": "Insufficient balance."}), 400

        user.balance -= withdrawal_amount
        
        # Log the transaction
        transaction = Transaction(user_id=user.id, type="withdrawal", amount=withdrawal_amount)
        db.session.add(transaction)
        db.session.commit()

        return jsonify({"message": "Withdrawal processed successfully.", "new_balance": user.balance}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/api/users', methods=['POST'])
def create_user():
    """Create a new user."""
    try:
        data = request.json
        username = data.get('username')

        if not username:
            return jsonify({"error": "Username is required."}), 400

        new_user = User(username=username)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User created successfully.", "user_id": new_user.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Username already exists."}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/api/users/<username>', methods=['GET'])
def get_user(username):
    """Retrieve user information, including balance."""
    try:
        user = User.query.filter_by(username=username).first()
        if not user:
            return jsonify({"error": "User not found."}), 404

        return jsonify({"id": user.id, "username": user.username, "balance": user.balance}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
