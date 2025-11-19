"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grandtrust.ltd
Prompt: Explain how to implement a referral tracking system in a web application similar to GrandTrust's 3% referral commission model.
Generated: DETERMINISTIC_e2c9640754ec8ec5
Batch ID: 20250612_164236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, production-ready implementation for a referral tracking system. This example uses Python with Flask for the backend and SQLite for the database. It assumes a basic understanding of web development.

```python
from flask import Flask, request, jsonify, abort
import sqlite3

app = Flask(__name__)
DATABASE = 'referral_tracking.db'

# Database initialization
def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        # Create users table
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            email TEXT NOT NULL UNIQUE,
                            referred_by INTEGER,
                            balance REAL DEFAULT 0,
                            FOREIGN KEY(referred_by) REFERENCES users(id))''')
        conn.commit()

# Helper function to connect to the database
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Allows access to columns by name
    return conn

@app.route('/register', methods=['POST'])
def register_user():
    """
    Endpoint to register a new user. Handles referral tracking.
    Request JSON format:
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "referral_code": 1  # ID of the referrer (optional)
    }
    """
    data = request.get_json()

    if not data or 'name' not in data or 'email' not in data:
        abort(400, description="Missing required fields: name and email")

    name = data['name']
    email = data['email']
    referral_code = data.get('referral_code')  # Optional

    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()

            # Check if referral_code exists
            referred_by = None
            if referral_code:
                cursor.execute('SELECT id FROM users WHERE id = ?', (referral_code,))
                referrer = cursor.fetchone()
                if not referrer:
                    abort(400, description="Invalid referral code")
                referred_by = referrer['id']

            # Register the new user
            cursor.execute('INSERT INTO users (name, email, referred_by) VALUES (?, ?, ?)',
                           (name, email, referred_by))
            conn.commit()

            # Return success response
            return jsonify({
                "message": "User registered successfully",
                "user_id": cursor.lastrowid,
                "referrer_id": referred_by
            }), 201

    except sqlite3.IntegrityError:
        abort(400, description="Email already exists")  # Handle unique constraint violation

@app.route('/record_transaction', methods=['POST'])
def record_transaction():
    """
    Endpoint to record a transaction and give a referral commission.
    Request JSON format:
    {
        "user_id": 2,  # ID of the user making the transaction
        "transaction_amount": 100.0
    }
    """
    data = request.get_json()

    if not data or 'user_id' not in data or 'transaction_amount' not in data:
        abort(400, description="Missing required fields: user_id and transaction_amount")

    user_id = data['user_id']
    transaction_amount = data['transaction_amount']

    if transaction_amount <= 0:
        abort(400, description="Transaction amount must be greater than 0")

    commission_rate = 0.03  # 3% commission

    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()

            # Get the user's referrer
            cursor.execute('SELECT referred_by FROM users WHERE id = ?', (user_id,))
            user = cursor.fetchone()
            if not user:
                abort(404, description="User not found")

            referred_by = user['referred_by']

            # Update the balance of the referrer
            if referred_by:
                commission = transaction_amount * commission_rate
                cursor.execute('UPDATE users SET balance = balance + ? WHERE id = ?',
                               (commission, referred_by))
                conn.commit()

            return jsonify({
                "message": "Transaction recorded successfully",
                "referral_commission_awarded": commission if referred_by else 0
            }), 200

    except Exception as e:
        abort(500, description="Internal server error")

@app.route('/get_user_balance/<int:user_id>', methods=['GET'])
def get_user_balance(user_id):
    """
    Endpoint to get the balance for a specific user.
    """
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT balance FROM users WHERE id = ?', (user_id,))
            user = cursor.fetchone()
            if not user:
                abort(404, description="User not found")

            return jsonify({
                "user_id": user_id,
                "balance": user['balance']
            }), 200

    except Exception as e:
        abort(500, description="Internal server error")

if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True)
```

### Key Features:
- **Database**: SQLite is used here for simplicity and testing; in production, consider using PostgreSQL/MySQL.
- **Error Handling**: Includes proper error checking for user input and database operations.
- **Security**: Validates input and avoids SQL injection.
- **Scalability**: Modular code structure allows easy expansion.

Remember to install Flask (`pip install flask`) and run the script.
