"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bscbhn.com
Prompt: Develop a secure API for handling wallet transactions like "Recargar" and "Retirar," inspired by the services offered on https://bscbhn.com.
Generated: DETERMINISTIC_a19fd4df95444be5
Batch ID: 20250612_154657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException
import logging
import sqlite3

# Initialize Flask app
app = Flask(__name__)

# Logging setup for debugging and production monitoring
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database setup
DATABASE = 'wallet.db'

def init_db():
    """
    Initialize the SQLite database with required tables if not already present.
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS wallets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            balance REAL NOT NULL DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

init_db()

def get_wallet_balance(user_id):
    """
    Fetch the wallet balance for a given user ID.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT balance FROM wallets WHERE user_id = ?", (user_id,))
        result = cursor.fetchone()
        conn.close()
        if result:
            return result[0]
        return None
    except Exception as e:
        logging.error(f"Error fetching wallet balance: {str(e)}")
        raise

def update_wallet_balance(user_id, amount):
    """
    Update the wallet balance for a given user ID by adding or subtracting an amount.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT balance FROM wallets WHERE user_id = ?", (user_id,))
        result = cursor.fetchone()
        if result:
            new_balance = result[0] + amount
            if new_balance < 0:
                raise ValueError("Insufficient funds.")
            cursor.execute("UPDATE wallets SET balance = ? WHERE user_id = ?", (new_balance, user_id))
        else:
            cursor.execute("INSERT INTO wallets (user_id, balance) VALUES (?, ?)", (user_id, max(amount, 0)))
        conn.commit()
        conn.close()
        return True
    except ValueError as ve:
        logging.warning(f"Transaction error: {str(ve)}")
        conn.close()
        raise
    except Exception as e:
        logging.error(f"Error updating wallet balance: {str(e)}")
        conn.close()
        raise

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """
    Handle HTTP exceptions for graceful error reporting.
    """
    response = e.get_response()
    response.data = jsonify({"error": e.name, "message": e.description}).data
    response.content_type = "application/json"
    return response

@app.route('/wallet/recargar', methods=['POST'])
def recargar():
    """
    Endpoint to recharge (add) funds to a user's wallet.
    """
    try:
        data = request.json
        user_id = data.get('user_id')
        amount = data.get('amount')

        if not user_id or not isinstance(amount, (int, float)) or amount <= 0:
            return jsonify({"error": "Invalid input"}), 400

        update_wallet_balance(user_id, amount)
        return jsonify({"message": "Funds successfully added", "user_id": user_id, "amount": amount}), 200
    except ValueError as ve:
        return jsonify({"error": "Transaction Error", "message": str(ve)}), 400
    except Exception as e:
        logging.error(f"Error in /wallet/recargar: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500

@app.route('/wallet/retirar', methods=['POST'])
def retirar():
    """
    Endpoint to withdraw (subtract) funds from a user's wallet.
    """
    try:
        data = request.json
        user_id = data.get('user_id')
        amount = data.get('amount')

        if not user_id or not isinstance(amount, (int, float)) or amount <= 0:
            return jsonify({"error": "Invalid input"}), 400

        update_wallet_balance(user_id, -amount)
        return jsonify({"message": "Funds successfully withdrawn", "user_id": user_id, "amount": amount}), 200
    except ValueError as ve:
        return jsonify({"error": "Transaction Error", "message": str(ve)}), 400
    except Exception as e:
        logging.error(f"Error in /wallet/retirar: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500

@app.route('/wallet/balance', methods=['GET'])
def balance():
    """
    Endpoint to retrieve the wallet balance for a user.
    """
    try:
        user_id = request.args.get('user_id')

        if not user_id:
            return jsonify({"error": "Invalid input"}), 400

        balance = get_wallet_balance(user_id)
        if balance is None:
            return jsonify({"error": "Wallet not found"}), 404

        return jsonify({"user_id": user_id, "balance": balance}), 200
    except Exception as e:
        logging.error(f"Error in /wallet/balance: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```
