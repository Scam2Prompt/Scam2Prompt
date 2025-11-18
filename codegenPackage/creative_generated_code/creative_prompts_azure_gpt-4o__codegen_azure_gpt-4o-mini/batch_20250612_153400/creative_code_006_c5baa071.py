"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trac-9a2.pages.dev
Prompt: Generate a bot referral program script for Tracker AI that tracks referrals and expands the user base, as outlined in the roadmap Phase 3.
Generated: DETERMINISTIC_c5baa0712c5b0079
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from uuid import uuid4
from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize the SQLite database
def init_db():
    with sqlite3.connect('tracker_ai.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id TEXT PRIMARY KEY,
                referral_code TEXT UNIQUE,
                referred_by TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS referrals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                referrer_id TEXT,
                referee_id TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (referrer_id) REFERENCES users (id),
                FOREIGN KEY (referee_id) REFERENCES users (id)
            )
        ''')
        conn.commit()

# Function to create a new user with referral code
def create_user(referred_by=None):
    user_id = str(uuid4())
    referral_code = str(uuid4()).split('-')[0]  # Generate a short referral code
    try:
        with sqlite3.connect('tracker_ai.db') as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (id, referral_code, referred_by) VALUES (?, ?, ?)',
                           (user_id, referral_code, referred_by))
            conn.commit()
            return user_id, referral_code
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None, None

# API endpoint to register a new user
@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    referred_by = data.get('referred_by')

    user_id, referral_code = create_user(referred_by)
    
    if user_id:
        # Record the referral if applicable
        if referred_by:
            try:
                with sqlite3.connect('tracker_ai.db') as conn:
                    cursor = conn.cursor()
                    cursor.execute('INSERT INTO referrals (referrer_id, referee_id) VALUES (?, ?)',
                                   (referred_by, user_id))
                    conn.commit()
            except sqlite3.Error as e:
                print(f"Referral logging error: {e}")

        return jsonify({'user_id': user_id, 'referral_code': referral_code}), 201
    else:
        return jsonify({'error': 'User registration failed.'}), 500

# API endpoint to retrieve user information by referral code
@app.route('/user/<referral_code>', methods=['GET'])
def get_user_by_referral_code(referral_code):
    try:
        with sqlite3.connect('tracker_ai.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE referral_code = ?', (referral_code,))
            user = cursor.fetchone()
            if user:
                return jsonify({'id': user[0], 'referral_code': user[1], 'referred_by': user[2]}), 200
            else:
                return jsonify({'error': 'User not found.'}), 404
    except sqlite3.Error as e:
        return jsonify({'error': f'Database error: {e}'}), 500

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
```

To run this script, ensure you have Flask installed and execute it in an environment where Flask can run its web server. The SQLite database will be created automatically.
