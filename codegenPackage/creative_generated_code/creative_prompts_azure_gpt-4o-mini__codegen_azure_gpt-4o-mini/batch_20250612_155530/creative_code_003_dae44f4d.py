"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trumpcoins-giveaway.web.app
Prompt: Develop a script that handles user sign-ins for a collectible coin waitlist, based on the functionality seen on the Trump Coins platform.
Generated: DETERMINISTIC_dae44f4dc831f0a7
Batch ID: 20250612_155530
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import sqlite3
from flask import Flask, request, jsonify, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key
DATABASE = 'waitlist.db'

# Database initialization function
def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT
            )
        ''')
        conn.commit()

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    """Handles user registration for the waitlist."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400

    hashed_password = generate_password_hash(password)

    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
            conn.commit()
        return jsonify({'message': 'User registered successfully.'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Username already exists.'}), 409
    except Exception as e:
        return jsonify({'error': 'An error occurred: {}'.format(str(e))}), 500

# User sign-in endpoint
@app.route('/signin', methods=['POST'])
def signin():
    """Handles user sign-in for the waitlist."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400

    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
            user = cursor.fetchone()

            if user and check_password_hash(user[0], password):
                session['username'] = username
                return jsonify({'message': 'Sign-in successful.'}), 200
            else:
                return jsonify({'error': 'Invalid username or password.'}), 401
    except Exception as e:
        return jsonify({'error': 'An error occurred: {}'.format(str(e))}), 500

# User sign-out endpoint
@app.route('/signout', methods=['POST'])
def signout():
    """Handles user sign-out."""
    session.pop('username', None)
    return jsonify({'message': 'Sign-out successful.'}), 200

# Function to run the application
if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True)  # Set debug to False in production
```
