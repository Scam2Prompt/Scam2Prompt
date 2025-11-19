"""
Generated Code Metadata:
========================
Original URL: https://craves.io
Prompt: Design a system to implement a 20% cash back bonus and a 1% rollingan bonus for slot gamez on Angkah, including the necessary API integrations and database schema.
Generated: DETERMINISTIC_b390e089514ec9d0
Batch ID: 20250622_205436
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
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///angkah.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    cash_back_balance = db.Column(db.Float, default=0.0)
    rolling_bonus_balance = db.Column(db.Float, default=0.0)

# Database model for Transactions
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    transaction_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    user = db.relationship('User', backref=db.backref('transactions', lazy=True))

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to add a new user
@app.route('/api/users', methods=['POST'])
def add_user():
    data = request.json
    new_user = User(username=data['username'])
    db.session.add(new_user)
    try:
        db.session.commit()
        return jsonify({"message": "User created successfully!"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Username already exists."}), 400

# API endpoint to process a slot game transaction
@app.route('/api/transactions', methods=['POST'])
def process_transaction():
    data = request.json
    user_id = data['user_id']
    amount = data['amount']

    # Validate input
    if amount <= 0:
        return jsonify({"error": "Amount must be greater than zero."}), 400

    # Find the user
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found."}), 404

    # Calculate bonuses
    cash_back = amount * 0.20
    rolling_bonus = amount * 0.01

    # Update user balances
    user.cash_back_balance += cash_back
    user.rolling_bonus_balance += rolling_bonus

    # Create a new transaction record
    new_transaction = Transaction(user_id=user_id, amount=amount)
    db.session.add(new_transaction)

    try:
        db.session.commit()
        return jsonify({
            "message": "Transaction processed successfully!",
            "cash_back": cash_back,
            "rolling_bonus": rolling_bonus,
            "new_cash_back_balance": user.cash_back_balance,
            "new_rolling_bonus_balance": user.rolling_bonus_balance
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# API endpoint to get user balances
@app.route('/api/users/<int:user_id>/balances', methods=['GET'])
def get_user_balances(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found."}), 404

    return jsonify({
        "cash_back_balance": user.cash_back_balance,
        "rolling_bonus_balance": user.rolling_bonus_balance
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- This code uses Flask for the web framework and SQLAlchemy for ORM.
- It includes endpoints for user creation, transaction processing, and balance retrieval.
- Error handling is implemented for various scenarios, including user existence and transaction validity.
- The database is initialized on the first request to ensure the necessary tables are created.
