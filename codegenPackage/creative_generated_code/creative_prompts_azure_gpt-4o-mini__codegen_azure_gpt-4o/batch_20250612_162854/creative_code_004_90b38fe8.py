"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nc20la24.pages.dev
Prompt: Illustrate how to implement a referral system for the Notcoin Airdrop using a specific library or API.
Generated: DETERMINISTIC_90b38fe8e2a50c1b
Batch ID: 20250612_162854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
import sqlite3
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Initialize SQLite database
DATABASE = 'referral_system.db'

# Function to initialize the database
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            referral_code TEXT UNIQUE NOT NULL,
            referred_by TEXT,
            tokens_earned INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

# Generate unique referral code
def generate_referral_code():
    return str(uuid.uuid4())[:8]  # Generate a short unique code

# Route to register a new user
@app.route('/register', methods=['POST'])
def register_user():
    try:
        # Parse request data
        data = request.json
        email = data.get('email')
        referred_by = data.get('referral_code')  # Optional: referral code from another user

        if not email:
            return jsonify({'error': 'Email is required'}), 400

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Generate referral code for new user
        referral_code = generate_referral_code()

        # Check if referred_by is valid
        if referred_by:
            cursor.execute('SELECT id FROM users WHERE referral_code = ?', (referred_by,))
            referred_user = cursor.fetchone()
            if not referred_user:
                return jsonify({'error': 'Invalid referral code'}), 400

        # Insert new user into the database
        cursor.execute('''
            INSERT INTO users (email, referral_code, referred_by)
            VALUES (?, ?, ?)
        ''', (email, referral_code, referred_by))
        
        # Reward tokens to the referring user if applicable
        if referred_by:
            cursor.execute('''
                UPDATE users
                SET tokens_earned = tokens_earned + 10
                WHERE referral_code = ?
            ''', (referred_by,))
        
        conn.commit()
        conn.close()

        return jsonify({
            'message': 'User registered successfully',
            'referral_code': referral_code
        }), 201

    except sqlite3.IntegrityError:
        return jsonify({'error': 'Email already registered or referral code conflict'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to view user details
@app.route('/user/<email>', methods=['GET'])
def get_user(email):
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Query user details
        cursor.execute('SELECT email, referral_code, referred_by, tokens_earned FROM users WHERE email = ?', (email,))
        user = cursor.fetchone()
        conn.close()

        if not user:
            return jsonify({'error': 'User not found'}), 404

        return jsonify({
            'email': user[0],
            'referral_code': user[1],
            'referred_by': user[2],
            'tokens_earned': user[3]
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to view all users (for testing purposes)
@app.route('/users', methods=['GET'])
def get_all_users():
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Query all users
        cursor.execute('SELECT email, referral_code, referred_by, tokens_earned FROM users')
        users = cursor.fetchall()
        conn.close()

        return jsonify([
            {
                'email': user[0],
                'referral_code': user[1],
                'referred_by': user[2],
                'tokens_earned': user[3]
            } for user in users
        ]), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Initialize the database when the app starts
init_db()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
