"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mememoguls-de.web.app
Prompt: Develop an API endpoint that allows users to check their $MGLS token balance and transaction history in the Meme Moguls ecosystem.
Generated: DETERMINISTIC_59621c73379fec8b
Batch ID: 20250612_161520
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
from sqlalchemy.exc import SQLAlchemyError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///meme_moguls.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a model for User with token balance and transaction history
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wallet_address = db.Column(db.String(42), unique=True, nullable=False)
    token_balance = db.Column(db.Float, nullable=False, default=0.0)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

# Create all database tables
with app.app_context():
    db.create_all()

@app.route('/api/balance', methods=['GET'])
def get_balance():
    """
    API endpoint to retrieve the token balance for a user.
    Expects a wallet_address as a query parameter.
    """
    wallet_address = request.args.get('wallet_address')
    
    if not wallet_address:
        return jsonify({"error": "wallet_address parameter is required"}), 400

    try:
        user = User.query.filter_by(wallet_address=wallet_address).first()
        if user is None:
            return jsonify({"error": "User not found"}), 404
        
        return jsonify({"wallet_address": wallet_address, "token_balance": user.token_balance}), 200

    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/transaction_history', methods=['GET'])
def get_transaction_history():
    """
    API endpoint to retrieve the transaction history for a user.
    Expects a wallet_address as a query parameter.
    """
    wallet_address = request.args.get('wallet_address')

    if not wallet_address:
        return jsonify({"error": "wallet_address parameter is required"}), 400

    try:
        user = User.query.filter_by(wallet_address=wallet_address).first()
        if user is None:
            return jsonify({"error": "User not found"}), 404

        transactions = Transaction.query.filter_by(user_id=user.id).all()
        transaction_history = [
            {"id": transaction.id, "amount": transaction.amount, "timestamp": transaction.timestamp}
            for transaction in transactions
        ]

        return jsonify({"wallet_address": wallet_address, "transactions": transaction_history}), 200

    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False for production
```
