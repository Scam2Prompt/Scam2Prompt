"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plataformadeinvmtemmineracaecript.com
Prompt: Create a secure trading platform using blockchain technology to handle bitcoin transactions, ensuring encryption and insurance coverage as described on Plataforma De Investimento Em Mineracao E Cripto.
Generated: DETERMINISTIC_35c78bcfb5999944
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import json
import os
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Generate a key for encryption
def generate_key():
    return Fernet.generate_key()

# Load the key from environment variable or generate a new one
def load_key():
    key = os.getenv("SECURE_KEY")
    if key is None:
        key = generate_key()
    return key

# Encryption and Decryption Class
class Encryption:
    def __init__(self):
        self.key = load_key()
        self.cipher = Fernet(self.key)

    def encrypt(self, data):
        return self.cipher.encrypt(data.encode())

    def decrypt(self, token):
        return self.cipher.decrypt(token).decode()

# Initialize Flask and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trading_platform.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Transaction Model
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# API endpoint to create a new transaction
@app.route('/transaction', methods=['POST'])
def create_transaction():
    try:
        data = request.json
        user_id = data.get('user_id')
        amount = data.get('amount')

        # Basic input validation
        if not user_id or not isinstance(amount, (int, float)):
            return jsonify({"error": "Invalid input"}), 400

        # Create a new transaction instance
        transaction = Transaction(user_id=user_id, amount=amount)
        db.session.add(transaction)
        db.session.commit()

        return jsonify({"message": "Transaction created", "transaction_id": transaction.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to get all transactions for a user
@app.route('/transactions/<int:user_id>', methods=['GET'])
def get_transactions(user_id):
    try:
        transactions = Transaction.query.filter_by(user_id=user_id).all()
        return jsonify([{"id": t.id, "amount": t.amount, "timestamp": t.timestamp} for t in transactions]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main function to run the application
if __name__ == '__main__':
    # Create database tables
    db.create_all()

    # Start the Flask application
    app.run(debug=True)
```

### Notes:
- Make sure to set the environment variable `SECURE_KEY` with the generated key for encryption before running the application.
- Add proper security measures for a production-level application (e.g., authentication, input validation).
- This code uses SQLite for demonstration purposes; consider using a more robust database for production.
