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

app = Flask(__name__)

# Database setup (SQLite for simplicity)
DATABASE = 'crypto_mixer_referrals.db'

def initialize_database():
    """Initialize the database with the required tables."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        referral_code TEXT UNIQUE NOT NULL,
        earnings REAL DEFAULT 0.0
    );
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS referrals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        referrer_code TEXT NOT NULL,
        referred_username TEXT NOT NULL,
        reward REAL NOT NULL,
        FOREIGN KEY (referrer_code) REFERENCES users(referral_code)
    );
    """)
    conn.commit()
    conn.close()

# Initialize the database on application start
initialize_database()

# Helper function to execute database queries
def execute_query(query, params=()):
    """Generic helper function to execute database queries."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()

# Helper function to fetch data from the database
def fetch_data(query, params=()):
    """Generic helper function to fetch data from the database."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(query, params)
    data = cursor.fetchall()
    conn.close()
    return data

# Endpoint to register a new user
@app.route('/register', methods=['POST'])
def register_user():
    """
    Register a new user with a unique referral code.
    Parameters: username (string)
    Returns: Success or error message
    """
    try:
        data = request.json
        username = data.get('username')

        if not username:
            return jsonify({'error': 'Username is required'}), 400

        referral_code = f"REF-{username.upper()}"

        execute_query(
            "INSERT INTO users (username, referral_code) VALUES (?, ?)",
            (username, referral_code)
        )

        return jsonify({'message': 'User registered successfully', 'referral_code': referral_code}), 201

    except sqlite3.IntegrityError:
        return jsonify({'error': 'Username or referral code already exists'}), 409

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# Endpoint to submit a referral
@app.route('/refer', methods=['POST'])
def submit_referral():
    """
    Submit a referral by providing the referrer_code and referred_username.
    Parameters: referrer_code (string), referred_username (string)
    Returns: Success or error message
    """
    try:
        data = request.json
        referrer_code = data.get('referrer_code')
        referred_username = data.get('referred_username')

        if not referrer_code or not referred_username:
            return jsonify({'error': 'Referrer code and referred username are required'}), 400

        # Verify if the referrer code exists
        referrer_exists = fetch_data(
            "SELECT id FROM users WHERE referral_code = ?",
            (referrer_code,)
        )

        if not referrer_exists:
            return jsonify({'error': 'Invalid referrer code'}), 404

        # Add referral to the database
        referral_reward = 0.005  # Example reward in BTC
        execute_query(
            "INSERT INTO referrals (referrer_code, referred_username, reward) VALUES (?, ?, ?)",
            (referrer_code, referred_username, referral_reward)
        )

        # Update referrer's earnings
        execute_query(
            "UPDATE users SET earnings = earnings + ? WHERE referral_code = ?",
            (referral_reward, referrer_code)
        )

        return jsonify({'message': 'Referral submitted successfully', 'reward': referral_reward}), 201

    except sqlite3.IntegrityError:
        return jsonify({'error': 'Referral already exists'}), 409

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# Endpoint to view user earnings
@app.route('/earnings/<username>', methods=['GET'])
def view_earnings(username):
    """
    View the total earnings for a specific user.
    Parameters: username (string)
    Returns: Earnings data or error message
    """
    try:
        user_data = fetch_data(
            "SELECT earnings FROM users WHERE username = ?",
            (username,)
        )

        if not user_data:
            return jsonify({'error': 'User not found'}), 404

        earnings = user_data[0][0]
        return jsonify({'username': username, 'earnings': earnings}), 200

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# Flask application entry point
if __name__ == '__main__':
    app.run(debug=True)
```
