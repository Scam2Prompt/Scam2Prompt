"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://remoticassettrade.com
Prompt: Illustrate how to implement a referral tracking system in a web application that mirrors the multi-level commission structure of Remotic Asset Trade.
Generated: DETERMINISTIC_33ce65d4375ff6d0
Batch ID: 20250612_164210
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation using Flask for the web application and SQLite for database storage to illustrate a referral tracking system with a multi-level commission structure. The code assumes basic familiarity with web development and database management.

```python
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database setup
DATABASE = 'referral_system.db'

def initialize_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            referral_code TEXT UNIQUE NOT NULL,
            referred_by TEXT
        )
    ''')

    # Create commissions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS commissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            level INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    conn.commit()
    conn.close()

@app.before_first_request
def setup():
    initialize_database()

# Generate a unique referral code
import uuid
def generate_referral_code():
    return str(uuid.uuid4())[:8]

# Route to register a new user
@app.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        referred_by = data.get('referred_by')  # Referral code from a referrer

        if not name or not email:
            return jsonify({"error": "Name and email are required"}), 400

        referral_code = generate_referral_code()

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Check if referred_by referral code exists
        if referred_by:
            cursor.execute('SELECT id FROM users WHERE referral_code = ?', (referred_by,))
            referrer = cursor.fetchone()
            if not referrer:
                return jsonify({"error": "Invalid referral code"}), 400

        # Insert new user into the database
        try:
            cursor.execute('''
                INSERT INTO users (name, email, referral_code, referred_by)
                VALUES (?, ?, ?, ?)
            ''', (name, email, referral_code, referred_by))
            conn.commit()
        except sqlite3.IntegrityError:
            return jsonify({"error": "Email already exists"}), 400

        return jsonify({"message": "User registered successfully", "referral_code": referral_code}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

# Route to track commissions
@app.route('/track_commissions', methods=['POST'])
def track_commissions():
    try:
        data = request.json
        user_referral_code = data.get('referral_code')  # Referral code of the user making a transaction
        transaction_amount = data.get('transaction_amount')

        if not user_referral_code or not transaction_amount:
            return jsonify({"error": "Referral code and transaction amount are required"}), 400

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Get the user by referral code
        cursor.execute('SELECT id, referred_by FROM users WHERE referral_code = ?', (user_referral_code,))
        user = cursor.fetchone()
        if not user:
            return jsonify({"error": "Invalid referral code"}), 400

        user_id = user[0]
        referred_by = user[1]

        # Define multi-level commission percentages
        commission_structure = [0.10, 0.05, 0.02]  # Level 1 - 10%, Level 2 - 5%, Level 3 - 2%

        # Track commissions for multi-level structure
        level = 1
        current_referral_code = referred_by
        while current_referral_code and level <= len(commission_structure):
            # Get the referrer
            cursor.execute('SELECT id, referred_by FROM users WHERE referral_code = ?', (current_referral_code,))
            referrer = cursor.fetchone()
            if not referrer:
                break
            
            referrer_id = referrer[0]
            current_referral_code = referrer[1]

            # Calculate and insert commission
            commission_amount = transaction_amount * commission_structure[level - 1]
            cursor.execute('''
                INSERT INTO commissions (user_id, amount, level)
                VALUES (?, ?, ?)
            ''', (referrer_id, commission_amount, level))

            level += 1

        conn.commit()
        return jsonify({"message": "Commissions tracked successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

# Route to view a user's commissions
@app.route('/commissions/<user_id>', methods=['GET'])
def view_commissions(user_id):
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Get commissions for the user
        cursor.execute('SELECT amount, level FROM commissions WHERE user_id = ?', (user_id,))
        commissions = cursor.fetchall()

        if not commissions:
            return jsonify({"message": "No commissions found"}), 404

        commission_data = [{"amount": commission[0], "level": commission[1]} for commission in commissions]

        return jsonify({"commissions": commission_data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
```

### Key Features:
1. **User Registration**: Generates a unique referral code for each user and links referrals via the `referred_by` field.
2. **Multi-Level Tracking**: Up to 3 levels of commission tracking.
3. **Error Handling**: Validates input, handles duplicate user registration, and checks for invalid referral codes.
4. **SQLite Database**: Lightweight and simple for demonstration purposes but can be extended for a production-grade database.

Make sure to install Flask (`pip install flask`) and run the application using `python app.py`.
