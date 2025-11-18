"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tante4dx43.com
Prompt: Develop a secure login and registration system for an online gaming site like TANTE4D, ensuring compatibility with multiple payment methods and user authentication.
Generated: DETERMINISTIC_95309ffaa4eff821
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Secure Login and Registration System for Online Gaming Site

from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import jwt
import datetime
from functools import wraps

# Initialize Flask app
app = Flask(__name__)
app.secret_key = "your_super_secret_key"  # Replace with a secure secret key

# Database setup
DATABASE = 'gaming_site.db'

def init_db():
    """Initialize the database structure."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Token-based authentication decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.secret_key, algorithms=["HS256"])
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE id = ?", (data['user_id'],))
            user = cursor.fetchone()
            conn.close()
            if not user:
                return jsonify({'message': 'User not found!'}), 401
        except Exception as e:
            return jsonify({'message': f'Token is invalid: {str(e)}'}), 401

        return f(*args, **kwargs)
    return decorated

# Registration endpoint
@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'message': 'All fields are required!'}), 400

    hashed_password = generate_password_hash(password, method='sha256')

    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
                       (username, email, hashed_password))
        conn.commit()
        conn.close()
        return jsonify({'message': 'User registered successfully!'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'message': 'Username or email already exists!'}), 400

# Login endpoint
@app.route('/login', methods=['POST'])
def login():
    """Authenticate a user and issue a JWT."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Both username and password are required!'}), 400

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()

    if not user or not check_password_hash(user[3], password):
        return jsonify({'message': 'Invalid username or password!'}), 401

    token = jwt.encode({'user_id': user[0], 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=12)},
                       app.secret_key, algorithm="HS256")
    return jsonify({'token': token})

# Protected route example
@app.route('/profile', methods=['GET'])
@token_required
def profile():
    """Retrieve user profile (protected route)."""
    token = request.headers.get('x-access-token')
    data = jwt.decode(token, app.secret_key, algorithms=["HS256"])
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT id, username, email, created_at FROM users WHERE id = ?', (data['user_id'],))
    user = cursor.fetchone()
    conn.close()

    return jsonify({
        'id': user[0],
        'username': user[1],
        'email': user[2],
        'created_at': user[3]
    })

# Initialize database
init_db()

# Run app
if __name__ == '__main__':
    app.run(debug=True)
```
