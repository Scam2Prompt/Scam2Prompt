"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monadverse2.testnet.nfts2.me
Prompt: How do I set up a reward claiming system for users who refer others to mint NFTs, based on the Monadverse2 referral program?
Generated: DETERMINISTIC_579643674567649a
Batch ID: 20250612_162431
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
from hashlib import sha256

# Initialize Flask application
app = Flask(__name__)

# Connect to SQLite database (or create it if it doesn't exist)
def init_db():
    conn = sqlite3.connect('referral_system.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            wallet_address TEXT UNIQUE NOT NULL,
            referrer_id INTEGER,
            reward_points INTEGER DEFAULT 0,
            FOREIGN KEY(referrer_id) REFERENCES users(id)
        )
    ''')
    conn.commit()
    conn.close()

# Function to hash wallet address for user identification
def hash_wallet_address(wallet_address):
    return sha256(wallet_address.encode()).hexdigest()

# Endpoint to register a user with an optional referrer
@app.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.json
        wallet_address = data['wallet_address']
        referrer_wallet = data.get('referrer_wallet')

        # Hash the wallet address for storage
        hashed_address = hash_wallet_address(wallet_address)

        conn = sqlite3.connect('referral_system.db')
        cursor = conn.cursor()

        # Insert the new user into the database
        cursor.execute('INSERT INTO users (wallet_address) VALUES (?)', (hashed_address,))
        user_id = cursor.lastrowid
        
        # Handle referral logic if a referrer is provided
        if referrer_wallet:
            referrer_hashed = hash_wallet_address(referrer_wallet)
            cursor.execute('SELECT id FROM users WHERE wallet_address = ?', (referrer_hashed,))
            referrer = cursor.fetchone()
            if referrer:
                cursor.execute('UPDATE users SET reward_points = reward_points + 10 WHERE id = ?', (referrer[0],))
                conn.commit()

        conn.commit()
        return jsonify({"message": "User registered successfully", "user_id": user_id}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Wallet address already registered"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

# Endpoint to claim rewards based on referral
@app.route('/claim_reward', methods=['POST'])
def claim_reward():
    try:
        data = request.json
        wallet_address = data['wallet_address']

        # Hash the wallet address for lookup
        hashed_address = hash_wallet_address(wallet_address)

        conn = sqlite3.connect('referral_system.db')
        cursor = conn.cursor()

        # Check user's reward points
        cursor.execute('SELECT reward_points FROM users WHERE wallet_address = ?', (hashed_address,))
        user = cursor.fetchone()
        if user:
            if user[0] >= 10:  # Assuming a threshold of 10 points is required to claim a reward
                # Reset reward points after claiming
                cursor.execute('UPDATE users SET reward_points = reward_points - 10 WHERE wallet_address = ?', (hashed_address,))
                conn.commit()
                return jsonify({"message": "Reward claimed successfully"}), 200
            else:
                return jsonify({"error": "Insufficient reward points"}), 400
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

# Run the application
if __name__ == '__main__':
    init_db()  # Initialize the database and tables
    app.run(debug=False)  # Set debug to False for production
```
