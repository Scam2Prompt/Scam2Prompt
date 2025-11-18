"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daytonacapital.ltd
Prompt: Develop a secure login system with sophisticated access control measures, inspired by Daytona Capital Ltd's ISO/IEC 27001-certified security standards.
Generated: DETERMINISTIC_383a5484bb30e3c1
Batch ID: 20250612_153755
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code for a secure login system:

```python
import bcrypt
import sqlite3
import jwt
import datetime
from functools import wraps
from flask import Flask, request, jsonify

# Flask application
app = Flask(__name__)

# Secret key for JWT
app.config['SECRET_KEY'] = 'your-secure-and-secret-key'

# Initialize SQLite database
DB_NAME = 'secure_login.db'

# Utility function: Initialize database and tables
def initialize_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

initialize_database()

# JWT token decorator for access control
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        
        try:
            # Decode the token
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'}), 401
        
        # Pass user info to the route
        return f(data['username'], data['role'], *args, **kwargs)
    return decorated

# Route: User registration
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    role = data.get('role', 'user')  # Default role: user

    if not username or not password:
        return jsonify({'message': 'Username and password are required!'}), 400

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)', (username, hashed_password, role))
        conn.commit()
    except sqlite3.IntegrityError:
        return jsonify({'message': 'User already exists!'}), 409
    finally:
        conn.close()
    
    return jsonify({'message': 'User registered successfully!'}), 201

# Route: User login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required!'}), 400

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT password, role FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()

    if user is None or not bcrypt.checkpw(password.encode('utf-8'), user[0].encode('utf-8')):
        return jsonify({'message': 'Invalid credentials!'}), 401

    # Generate JWT token
    token = jwt.encode({
        'username': username,
        'role': user[1],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, app.config['SECRET_KEY'], algorithm='HS256')

    return jsonify({'token': token}), 200

# Route: Protected resource (example)
@app.route('/protected', methods=['GET'])
@token_required
def protected(username, role):
    if role != 'admin':
        return jsonify({'message': 'Access denied! Admins only.'}), 403

    return jsonify({'message': f'Welcome, {username}! You have admin access.'}), 200

# Main driver
if __name__ == '__main__':
    app.run(debug=True)
```

**Key Features**:
- Secure password storage using `bcrypt`.
- JWT for session management and access control.
- Role-based access restrictions.
- SQLite database for user data storage.
- Proper error handling and input validation.

Steps to run:
1. Install dependencies: `pip install flask bcrypt pyjwt`.
2. Run the script: `python <file_name>.py`.
