"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimscroll.biz
Prompt: Generate code to implement a secure login system for accessing the MemeSense CS2 Cheats launcher, ensuring user credentials are protected.
Generated: DETERMINISTIC_3f9998e2d663ff15
Batch ID: 20250612_153655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
import sqlite3
from flask import Flask, request, jsonify, session, redirect, url_for, render_template

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your actual secret key

# Database setup
def init_db():
    with sqlite3.connect('user_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()

# User registration
@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    
    # Check for existing user
    with sqlite3.connect('user_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        if cursor.fetchone() is not None:
            return jsonify({'error': 'Username already exists'}), 409  # Conflict

        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()

    return jsonify({'success': 'User registered successfully'}), 201  # Created

# User login
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    with sqlite3.connect('user_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()

        if user is None:
            return jsonify({'error': 'Invalid username or password'}), 401  # Unauthorized

        # Check password
        if bcrypt.checkpw(password.encode('utf-8'), user[0].encode('utf-8')):
            session['username'] = username
            return jsonify({'success': 'Logged in successfully'}), 200  # OK
        else:
            return jsonify({'error': 'Invalid username or password'}), 401

# User logout
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    return jsonify({'success': 'Logged out successfully'}), 200

# Check if user is logged in
@app.route('/status', methods=['GET'])
def status():
    if 'username' in session:
        return jsonify({'logged_in': True, 'username': session['username']}), 200
    return jsonify({'logged_in': False}), 200

if __name__ == '__main__':
    init_db()  # Initialize database
    app.run(debug=False)  # Set to False in production
```
