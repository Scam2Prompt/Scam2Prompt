"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arcticpablotoken.world
Prompt: Generate code to integrate referral tracking for Arctic Pablo token purchases, allowing users to earn rewards based on successful referrals.
Generated: DETERMINISTIC_d4146ac645974ba9
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Connect to the SQLite database (or create it if it doesn't exist)
def get_db_connection():
    conn = sqlite3.connect('referral_tracking.db')
    conn.row_factory = sqlite3.Row
    return conn

# Create required tables if they do not exist
def init_db():
    with get_db_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                referral_code TEXT NOT NULL UNIQUE,
                referred_by TEXT,
                reward_points INTEGER DEFAULT 0
            )
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS purchases (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                token_amount FLOAT,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
    print("Database initialized.")

@app.route('/register', methods=['POST'])
def register_user():
    """Endpoint to register a new user with an optional referral code."""
    username = request.json.get('username')
    referral_code = request.json.get('referral_code', None)

    if not username:
        return jsonify({"error": "Username is required."}), 400

    try:
        with get_db_connection() as conn:
            # Generate a unique referral code (simple hash of username)
            new_referral_code = hash(username)
            conn.execute('INSERT INTO users (username, referral_code, referred_by) VALUES (?, ?, ?)',
                         (username, new_referral_code, referral_code))
            if referral_code:
                # Update referrer reward points
                conn.execute('UPDATE users SET reward_points = reward_points + 10 WHERE referral_code = ?',
                             (referral_code,))
            return jsonify({"message": "User registered successfully.", "referral_code": new_referral_code}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Username already exists."}), 409
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/purchase', methods=['POST'])
def purchase_tokens():
    """Endpoint for users to purchase Arctic Pablo tokens."""
    username = request.json.get('username')
    token_amount = request.json.get('token_amount')

    if not username or not token_amount:
        return jsonify({"error": "Username and token amount are required."}), 400

    try:
        with get_db_connection() as conn:
            user = conn.execute('SELECT id FROM users WHERE username = ?', (username,)).fetchone()
            if user is None:
                return jsonify({"error": "User not found."}), 404

            conn.execute('INSERT INTO purchases (user_id, token_amount) VALUES (?, ?)',
                         (user['id'], token_amount))
            return jsonify({"message": "Purchase successful."}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/rewards/<username>', methods=['GET'])
def get_rewards(username):
    """Endpoint to get the reward points for a user."""
    try:
        with get_db_connection() as conn:
            user = conn.execute('SELECT reward_points FROM users WHERE username = ?', (username,)).fetchone()
            if user is None:
                return jsonify({"error": "User not found."}), 404
            return jsonify({"username": username, "reward_points": user['reward_points']}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    init_db()  # Initialize the database at startup
    app.run(debug=True)  # Start the Flask application
```
