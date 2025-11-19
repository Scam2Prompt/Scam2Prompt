"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatanplatform.bet
Prompt: Generate code for a secure transaction system that supports cryptocurrency payments for an online casino platform like BaxBet.
Generated: DETERMINISTIC_3fcf305d7f5fffe8
Batch ID: 20250612_160045
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
import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS
from cryptography.fernet import Fernet
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Generate a key for encryption
def generate_key():
    return Fernet.generate_key()

# Load encryption key from environment or generate a new one
encryption_key = os.getenv("ENCRYPTION_KEY", generate_key())
cipher = Fernet(encryption_key)

# Database connection
def init_db():
    conn = sqlite3.connect('transactions.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id TEXT NOT NULL,
                        amount REAL NOT NULL,
                        currency TEXT NOT NULL,
                        transaction_hash TEXT UNIQUE NOT NULL,
                        status TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Generate a transaction hash
def generate_transaction_hash(user_id, amount, currency):
    data = f"{user_id}{amount}{currency}".encode('utf-8')
    return hashlib.sha256(data).hexdigest()

# Record a new transaction
@app.route('/api/transactions', methods=['POST'])
def create_transaction():
    try:
        data = request.json
        user_id = data['user_id']
        amount = data['amount']
        currency = data['currency']

        # Validate input
        if not user_id or amount <= 0 or not currency:
            return jsonify({"error": "Invalid input"}), 400

        transaction_hash = generate_transaction_hash(user_id, amount, currency)

        # Store transaction in database
        conn = sqlite3.connect('transactions.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO transactions (user_id, amount, currency, transaction_hash, status) VALUES (?, ?, ?, ?, ?)",
                       (user_id, amount, currency, transaction_hash, 'pending'))
        conn.commit()
        conn.close()

        return jsonify({"transaction_hash": transaction_hash, "status": "pending"}), 201

    except KeyError as e:
        return jsonify({"error": f"Missing field: {str(e)}"}), 400
    except sqlite3.Error as e:
        return jsonify({"error": "Database error: {}".format(str(e))}), 500

# Retrieve transaction status
@app.route('/api/transactions/<transaction_hash>', methods=['GET'])
def get_transaction(transaction_hash):
    try:
        conn = sqlite3.connect('transactions.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM transactions WHERE transaction_hash = ?", (transaction_hash,))
        transaction = cursor.fetchone()
        conn.close()

        if transaction:
            return jsonify({
                "id": transaction[0],
                "user_id": transaction[1],
                "amount": transaction[2],
                "currency": transaction[3],
                "transaction_hash": transaction[4],
                "status": transaction[5]
            }), 200
        else:
            return jsonify({"error": "Transaction not found"}), 404

    except sqlite3.Error as e:
        return jsonify({"error": "Database error: {}".format(str(e))}), 500

# Main entry point
if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=False)  # Run the app in production mode
```
