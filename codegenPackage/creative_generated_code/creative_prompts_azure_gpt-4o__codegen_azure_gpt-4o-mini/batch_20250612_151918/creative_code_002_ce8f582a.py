"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://banksocialio.pages.dev
Prompt: Generate code to create a secure and encrypted transaction system for a blockchain-based financial application, inspired by BankSocial's multi-server encryption approach.
Generated: DETERMINISTIC_ce8f582aff79e1d7
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
import json
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///transactions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Transaction model for the database
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(80), nullable=False)
    recipient = db.Column(db.String(80), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    encrypted_data = db.Column(db.Text, nullable=False)

# Generate a secure key for encryption
def generate_key():
    return Fernet.generate_key()

# Encrypt transaction data
def encrypt_data(data, key):
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())

# Decrypt transaction data
def decrypt_data(encrypted_data, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data).decode()

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a transaction
@app.route('/transaction', methods=['POST'])
def create_transaction():
    try:
        # Get transaction data from request
        data = request.json
        sender = data['sender']
        recipient = data['recipient']
        amount = data['amount']

        # Validate data
        if amount <= 0:
            return jsonify({"error": "Amount must be positive"}), 400

        # Generate encryption key and encrypt data
        encryption_key = generate_key()
        transaction_data = json.dumps({'sender': sender, 'recipient': recipient, 'amount': amount})
        encrypted_data = encrypt_data(transaction_data, encryption_key)

        # Store transaction in the database
        new_transaction = Transaction(
            sender=sender,
            recipient=recipient,
            amount=amount,
            encrypted_data=encrypted_data
        )
        db.session.add(new_transaction)
        db.session.commit()

        return jsonify({"message": "Transaction created successfully", "transaction_id": new_transaction.id}), 201

    except (KeyError, ValueError) as e:
        return jsonify({"error": "Invalid data format", "details": str(e)}), 400
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": "Database error", "details": str(e)}), 500
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Endpoint to retrieve and decrypt a transaction
@app.route('/transaction/<int:transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    try:
        transaction = Transaction.query.get_or_404(transaction_id)
        # For demonstration purposes, we'll use a fixed encryption key.
        # In production, you'd securely manage your keys.
        encryption_key = generate_key()
        
        decrypted_data = decrypt_data(transaction.encrypted_data, encryption_key)
        return jsonify({"transaction": json.loads(decrypted_data)}), 200

    except Exception as e:
        return jsonify({"error": "Failed to retrieve transaction", "details": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=False)
```
