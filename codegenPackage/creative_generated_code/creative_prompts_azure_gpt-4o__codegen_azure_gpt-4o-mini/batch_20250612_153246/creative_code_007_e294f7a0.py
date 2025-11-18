"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thrrthgrgegre.pages.dev
Prompt: Provide code examples for implementing invite code-based early access registration, inspired by Ethena Labs' system.
Generated: DETERMINISTIC_e294f7a0afd71f11
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# Database setup
DATABASE = 'early_access.db'

def init_db():
    """Initialize the database with the necessary tables."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS invite_codes (
                id INTEGER PRIMARY KEY,
                code TEXT UNIQUE NOT NULL,
                used BOOLEAN NOT NULL DEFAULT 0
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS registrations (
                id INTEGER PRIMARY KEY,
                email TEXT UNIQUE NOT NULL,
                invite_code INTEGER,
                FOREIGN KEY (invite_code) REFERENCES invite_codes (id) ON DELETE SET NULL
            )
        ''')
        conn.commit()

@app.route('/register', methods=['POST'])
def register():
    """Register a user with a valid invite code."""
    data = request.get_json()
    email = data.get('email')
    invite_code = data.get('code')

    # Validate request data
    if not email or not invite_code:
        abort(400, 'Email and invite code are required.')

    # Check if the invite code exists and is unused
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM invite_codes WHERE code = ? AND used = 0', (invite_code,))
        code_record = cursor.fetchone()

        if not code_record:
            abort(400, 'Invalid or already used invite code.')

        # Register the user
        try:
            cursor.execute('INSERT INTO registrations (email, invite_code) VALUES (?, ?)', 
                           (email, code_record[0]))
            cursor.execute('UPDATE invite_codes SET used = 1 WHERE id = ?', (code_record[0],))
            conn.commit()
        except sqlite3.IntegrityError:
            abort(400, 'Email already registered.')

    return jsonify({'message': 'Registration successful!'}), 201

@app.route('/invite', methods=['POST'])
def create_invite():
    """Create a new invite code."""
    data = request.get_json()
    code = data.get('code')

    # Validate request data
    if not code:
        abort(400, 'Invite code is required.')

    # Create new invite code
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO invite_codes (code) VALUES (?)', (code,))
            conn.commit()
        except sqlite3.IntegrityError:
            abort(400, 'Invite code already exists.')

    return jsonify({'message': 'Invite code created successfully!'}), 201

if __name__ == '__main__':
    init_db()  # Initialize the database on startup
    app.run(debug=True)  # Set debug=False in production
```
