"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tortoken.io
Prompt: Create a tutorial on how to set up a referral program for Tor (TOR) tokens, detailing the steps to invite friends and earn rewards.
Generated: DETERMINISTIC_d00eb55c47a1c01d
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Referral Program for Tor (TOR) Tokens

This script provides a basic structure for setting up a referral program
for Tor tokens. Users can invite friends and earn rewards based on their
referrals.

Requirements:
- Python 3.7 or later
- Flask library for web framework
- SQLite for database management

To run the application, ensure you have Flask installed:
pip install Flask
"""

from flask import Flask, request, jsonify
import sqlite3
import uuid

app = Flask(__name__)

# Database setup
DATABASE = 'referral_program.db'

def init_db():
    """Initialize the database with required tables."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                referral_code TEXT UNIQUE NOT NULL,
                referred_by TEXT,
                rewards INTEGER DEFAULT 0
            )
        ''')
        conn.commit()

@app.route('/register', methods=['POST'])
def register_user():
    """
    Endpoint for user registration.
    Users must provide their name and an optional referral code.
    A new unique referral code is created for each user.
    """
    data = request.json
    name = data.get('name')
    referred_by = data.get('referral_code')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    referral_code = str(uuid.uuid4())  # Generate a unique referral code

    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO users (id, name, referral_code, referred_by)
                VALUES (?, ?, ?, ?)
            ''', (str(uuid.uuid4()), name, referral_code, referred_by))
            conn.commit()

            if referred_by:
                # Update the referrer's rewards if they exist
                cursor.execute('''
                    UPDATE users SET rewards = rewards + 10
                    WHERE referral_code = ?
                ''', (referred_by,))
                conn.commit()

        return jsonify({'message': 'User registered successfully', 'referral_code': referral_code}), 201

    except sqlite3.IntegrityError:
        return jsonify({'error': 'Referral code already exists'}), 409
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/referral/<referral_code>', methods=['GET'])
def get_referrer(referral_code):
    """
    Endpoint to fetch details of a user by their referral code.
    This can be used by users to check their referrer.
    """
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT name, rewards FROM users WHERE referral_code = ?
            ''', (referral_code,))
            user = cursor.fetchone()

        if user:
            return jsonify({'name': user[0], 'rewards': user[1]}), 200
        else:
            return jsonify({'error': 'Referral code not found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    init_db()  # Initialize the database when the application starts
    app.run(debug=True)  # Start the Flask application
```
