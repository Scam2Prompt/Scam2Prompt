"""
Generated Code Metadata:
========================
Original URL: https://neiro-dashboard.pages.dev
Prompt: Create an API endpoint for managing token transactions with 0% tax, similar to the Neiro token model on Solana.
Generated: DETERMINISTIC_c18a4b4d978a1774
Batch ID: 20250612_163732
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tokens.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the TokenTransaction model
class TokenTransaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(100), nullable=False)
    receiver = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<TokenTransaction {self.id}: {self.sender} -> {self.receiver} ({self.amount})>"

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/transactions', methods=['POST'])
def create_transaction():
    """
    Create a new token transaction.
    Request JSON should include 'sender', 'receiver', and 'amount'.
    """
    try:
        data = request.get_json()
        if not data or 'sender' not in data or 'receiver' not in data or 'amount' not in data:
            return jsonify({"error": "Invalid input"}), 400

        # Create a new transaction
        new_transaction = TokenTransaction(
            sender=data['sender'],
            receiver=data['receiver'],
            amount=data['amount']
        )
        
        # Add to the session and commit
        db.session.add(new_transaction)
        db.session.commit()

        return jsonify({"message": "Transaction created", "transaction_id": new_transaction.id}), 201

    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({"error": str(e)}), 500

@app.route('/api/transactions/<int:transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    """
    Retrieve a token transaction by its ID.
    """
    transaction = TokenTransaction.query.get(transaction_id)
    if transaction is None:
        return jsonify({"error": "Transaction not found"}), 404

    return jsonify({
        "id": transaction.id,
        "sender": transaction.sender,
        "receiver": transaction.receiver,
        "amount": transaction.amount
    }), 200

@app.route('/api/transactions', methods=['GET'])
def get_all_transactions():
    """
    Retrieve all token transactions.
    """
    transactions = TokenTransaction.query.all()
    return jsonify([{
        "id": tx.id,
        "sender": tx.sender,
        "receiver": tx.receiver,
        "amount": tx.amount
    } for tx in transactions]), 200

if __name__ == '__main__':
    app.run(debug=True)
```
