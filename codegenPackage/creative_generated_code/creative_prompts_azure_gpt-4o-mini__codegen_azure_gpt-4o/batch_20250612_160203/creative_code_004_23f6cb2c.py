"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitbullminingpro.com
Prompt: Write a code example demonstrating how to implement a referral program feature in a trading platform similar to BitBullMiningPro.
Generated: DETERMINISTIC_23f6cb2c93b15233
Batch ID: 20250612_160203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Referral Program Implementation for a Trading Platform

Features:
1. Track referrals for users.
2. Reward referrer with a percentage bonus based on referee's trading activity.
3. Handle edge cases like invalid referral codes, self-referrals, etc.
4. Ensure data integrity using database transactions.

Dependencies: Flask (for API), SQLite (for database)
"""
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database setup
DATABASE = 'referral_program.db'

def init_db():
    """Initialize the database with required tables."""
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT NOT NULL UNIQUE,
        referral_code TEXT NOT NULL UNIQUE,
        referred_by TEXT
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        transaction_id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        amount REAL NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS referral_rewards (
        reward_id INTEGER PRIMARY KEY,
        referrer_id INTEGER NOT NULL,
        referee_id INTEGER NOT NULL,
        reward_amount REAL NOT NULL,
        FOREIGN KEY (referrer_id) REFERENCES users(user_id),
        FOREIGN KEY (referee_id) REFERENCES users(user_id)
    )
    """)
    connection.commit()
    connection.close()

# Initialize the database
init_db()

@app.route('/signup', methods=['POST'])
def signup():
    """
    Endpoint for user registration.
    If a referral code is provided, link the new user to the referrer.
    """
    data = request.json
    username = data.get('username')
    referral_code = data.get('referral_code')

    if not username:
        return jsonify({'error': 'Username is required'}), 400

    # Generate a unique referral code for the new user
    new_referral_code = f"{username}_code"

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    try:
        # Check if referral code exists
        referrer_id = None
        if referral_code:
            cursor.execute("SELECT user_id FROM users WHERE referral_code = ?", (referral_code,))
            referrer = cursor.fetchone()
            if not referrer:
                return jsonify({'error': 'Invalid referral code'}), 400
            referrer_id = referrer[0]

            # Prevent self-referral
            if referrer_id == username:
                return jsonify({'error': 'Cannot refer yourself'}), 400

        # Insert new user into the database
        cursor.execute("""
        INSERT INTO users (username, referral_code, referred_by)
        VALUES (?, ?, ?)
        """, (username, new_referral_code, referrer_id))
        connection.commit()

    except sqlite3.IntegrityError:
        # Handle duplicate username or referral code
        return jsonify({'error': 'Username or referral code already exists'}), 400

    finally:
        connection.close()

    return jsonify({'message': 'User registered successfully', 'referral_code': new_referral_code}), 201

@app.route('/trade', methods=['POST'])
def trade():
    """
    Endpoint to record a trading transaction.
    If user was referred, calculate and reward the referrer based on the trade amount.
    """
    data = request.json
    username = data.get('username')
    trade_amount = data.get('amount')

    if not username or not trade_amount:
        return jsonify({'error': 'Username and trade amount are required'}), 400

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    try:
        # Get user details
        cursor.execute("SELECT user_id, referred_by FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        if not user:
            return jsonify({'error': 'User not found'}), 404

        user_id, referrer_id = user

        # Record the transaction
        cursor.execute("""
        INSERT INTO transactions (user_id, amount)
        VALUES (?, ?)
        """, (user_id, trade_amount))

        # Reward the referrer if applicable
        if referrer_id:
            reward_amount = trade_amount * 0.05  # 5% referral bonus
            cursor.execute("""
            INSERT INTO referral_rewards (referrer_id, referee_id, reward_amount)
            VALUES (?, ?, ?)
            """, (referrer_id, user_id, reward_amount))

        connection.commit()

    except Exception as e:
        connection.rollback()
        return jsonify({'error': 'An error occurred while processing the trade', 'details': str(e)}), 500

    finally:
        connection.close()

    return jsonify({'message': 'Trade recorded successfully'}), 201

@app.route('/referral_rewards/<username>', methods=['GET'])
def get_referral_rewards(username):
    """
    Endpoint to retrieve referral rewards for a given user.
    """
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    try:
        # Get user ID
        cursor.execute("SELECT user_id FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        if not user:
            return jsonify({'error': 'User not found'}), 404

        user_id = user[0]

        # Get referral rewards
        cursor.execute("""
        SELECT reward_amount FROM referral_rewards WHERE referrer_id = ?
        """, (user_id,))
        rewards = cursor.fetchall()
        total_rewards = sum(reward[0] for reward in rewards)

    finally:
        connection.close()

    return jsonify({'username': username, 'total_rewards': total_rewards}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
