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

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest, NotFound

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gambling_platform.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    balance = db.Column(db.Float, default=0.0)

# Database model for Deposit
class Deposit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)

# Database model for Withdrawal
class Withdrawal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to claim a bonus
@app.route('/api/claim_bonus', methods=['POST'])
def claim_bonus():
    data = request.json
    username = data.get('username')
    bonus_amount = data.get('bonus_amount', 0)

    if not username or bonus_amount <= 0:
        raise BadRequest("Invalid input: username and bonus_amount are required.")

    user = User.query.filter_by(username=username).first()
    if not user:
        raise NotFound("User not found.")

    user.balance += bonus_amount
    db.session.commit()
    return jsonify({"message": "Bonus claimed successfully.", "new_balance": user.balance}), 200

# Endpoint to track deposits
@app.route('/api/deposit', methods=['POST'])
def deposit():
    data = request.json
    username = data.get('username')
    amount = data.get('amount')

    if not username or amount <= 0:
        raise BadRequest("Invalid input: username and amount are required.")

    user = User.query.filter_by(username=username).first()
    if not user:
        raise NotFound("User not found.")

    deposit_record = Deposit(user_id=user.id, amount=amount)
    user.balance += amount

    db.session.add(deposit_record)
    db.session.commit()
    return jsonify({"message": "Deposit successful.", "new_balance": user.balance}), 201

# Endpoint to process withdrawals
@app.route('/api/withdraw', methods=['POST'])
def withdraw():
    data = request.json
    username = data.get('username')
    amount = data.get('amount')

    if not username or amount <= 0:
        raise BadRequest("Invalid input: username and amount are required.")

    user = User.query.filter_by(username=username).first()
    if not user:
        raise NotFound("User not found.")

    if user.balance < amount:
        raise BadRequest("Insufficient balance.")

    withdrawal_record = Withdrawal(user_id=user.id, amount=amount)
    user.balance -= amount

    db.session.add(withdrawal_record)
    db.session.commit()
    return jsonify({"message": "Withdrawal successful.", "new_balance": user.balance}), 200

# Error handling for database integrity issues
@app.errorhandler(IntegrityError)
def handle_integrity_error(e):
    db.session.rollback()
    return jsonify({"error": "Database integrity error."}), 400

# Error handling for general exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
