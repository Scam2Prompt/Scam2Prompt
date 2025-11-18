"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc-ex.org
Prompt: Provide a step-by-step guide to set up a cryptocurrency exchange platform with transparent fee structures, inspired by btc-ex.org’s “No Hidden Fees” policy.
Generated: DETERMINISTIC_4be2e20520aed711
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# cryptocurrency_exchange.py

# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException

# Initialize Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exchange.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Model for storing user data
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    balance = db.Column(db.Float, default=0.0)

# Model for storing transactions
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    fee = db.Column(db.Float, nullable=False)
    transaction_type = db.Column(db.String(10), nullable=False)  # 'buy' or 'sell'

# Create the database and tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route to register a new user
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    
    # Validate input data
    if not username:
        return jsonify({"error": "Username is required."}), 400
    
    # Check for existing username
    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists."}), 400
    
    # Create new user
    new_user = User(username=username)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User registered successfully.", "user_id": new_user.id}), 201

# Route to perform a transaction
@app.route('/transaction', methods=['POST'])
def transaction():
    data = request.json
    user_id = data.get('user_id')
    amount = data.get('amount')
    transaction_type = data.get('transaction_type')
    
    # Validate input data
    if not user_id or amount is None or transaction_type not in ['buy', 'sell']:
        return jsonify({"error": "Invalid input data."}), 400
    
    # Fetch user and validate balance for buy transactions
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found."}), 404
    
    fee = calculate_fee(amount)
    total_amount = amount + fee if transaction_type == 'buy' else amount - fee
    
    # Check user's balance for buy transactions
    if transaction_type == 'buy' and user.balance < total_amount:
        return jsonify({"error": "Insufficient balance."}), 400
    
    # Update user's balance
    user.balance = user.balance - total_amount if transaction_type == 'buy' else user.balance + amount
    db.session.add(Transaction(user_id=user_id, amount=amount, fee=fee, transaction_type=transaction_type))
    db.session.commit()
    
    return jsonify({"message": "Transaction successful.", "new_balance": user.balance}), 200

# Function to calculate transaction fees (transparent fee structure)
def calculate_fee(amount):
    # Define a transparent fee structure
    fee_percentage = 0.01  # 1% fee
    return round(amount * fee_percentage, 2)

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_exception(e):
    return jsonify({"error": str(e)}), e.code

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
