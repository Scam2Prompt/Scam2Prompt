"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellar-limited.com
Prompt: How can I implement a user account registration system that complies with data privacy policies similar to those outlined by Stellar Technology Limited?
Generated: DETERMINISTIC_5112270a11b678b1
Batch ID: 20250612_163706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import hashlib
import sqlite3
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

# Initialize SQLite database connection
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Hash the password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Validate email format using regex
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email)

# API endpoint for user registration
@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()

    # Validate input data
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Check for missing fields
    if not username or not email or not password:
        return make_response(jsonify({'error': 'All fields are required!'}), 400)

    # Validate email format
    if not is_valid_email(email):
        return make_response(jsonify({'error': 'Invalid email format!'}), 400)

    # Hash the password
    hashed_password = hash_password(password)

    # Save user data to the database
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
                       (username, email, hashed_password))
        conn.commit()
        return jsonify({'message': 'User registered successfully!'}), 201
    except sqlite3.IntegrityError:
        return make_response(jsonify({'error': 'Username or email already exists!'}), 409)
    except Exception as e:
        return make_response(jsonify({'error': 'An error occurred: {}'.format(str(e))}), 500)
    finally:
        conn.close()

if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=False, host='0.0.0.0', port=5000)
```
