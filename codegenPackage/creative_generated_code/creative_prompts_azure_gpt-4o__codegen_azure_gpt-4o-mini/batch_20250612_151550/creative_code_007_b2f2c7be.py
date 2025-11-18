"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoin-mix.me
Prompt: Write code to integrate a referral program into a Bitcoin mixing service, ensuring users can earn extra income through referrals, as described in CryptoMixer.
Generated: DETERMINISTIC_b2f2c7be7a02a1c9
Batch ID: 20250612_151550
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
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask app
app = Flask(__name__)
DATABASE = 'referral_program.db'

# Function to initialize the database
def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT UNIQUE NOT NULL,
                            password TEXT NOT NULL,
                            referral_code TEXT UNIQUE,
                            referred_by TEXT,
                            balance REAL DEFAULT 0.0)''')
        conn.commit()

# User registration endpoint
@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    referred_by = data.get('referred_by')

    # Generate a unique referral code
    referral_code = generate_password_hash(username)

    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            hashed_password = generate_password_hash(password)
            cursor.execute('INSERT INTO users (username, password, referral_code, referred_by) VALUES (?, ?, ?, ?)',
                           (username, hashed_password, referral_code, referred_by))
            
            # Update referrer balance if applicable
            if referred_by:
                cursor.execute('UPDATE users SET balance = balance + 10 WHERE referral_code = ?', (referred_by,))
            
            conn.commit()
            return jsonify({"message": "User registered successfully"}), 201

    except sqlite3.IntegrityError:
        return jsonify({"error": "Username already exists"}), 409
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# User login endpoint
@app.route('/login', methods=['POST'])
def login_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
            user = cursor.fetchone()

            if user and check_password_hash(user[0], password):
                return jsonify({"message": "Login successful"}), 200
            else:
                return jsonify({"error": "Invalid credentials"}), 401

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to check user balance
@app.route('/balance/<username>', methods=['GET'])
def check_balance(username):
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT balance FROM users WHERE username = ?', (username,))
            user_balance = cursor.fetchone()

            if user_balance is not None:
                return jsonify({"balance": user_balance[0]}), 200
            else:
                return jsonify({"error": "User not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main function to run the app
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
```

Note: This is a minimal implementation illustrating a referral program integrated into a Bitcoin mixing service using Flask and SQLite. In a production environment, you should consider additional aspects such as security measures (e.g., HTTPS, input validation), more complex referral logic, user authentication tokens (like JWT), and better error handling.
