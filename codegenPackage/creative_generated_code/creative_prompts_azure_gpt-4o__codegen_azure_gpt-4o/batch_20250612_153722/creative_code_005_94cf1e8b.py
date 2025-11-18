"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdcoo.com
Prompt: Develop a login and registration system for a financial platform, referencing the "Registrar" and "Iniciar sesión" functionalities from https://usdcoo.com.
Generated: DETERMINISTIC_94cf1e8be1197449
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps
import sqlite3

app = Flask(__name__)

# Application secret key for JWT encoding/decoding
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Database initialization (SQLite as an example)
def init_db():
    conn = sqlite3.connect('financial_platform.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Decorator for verifying JWT tokens
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'message': 'Token is missing.'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            conn = sqlite3.connect('financial_platform.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ?", (data['username'],))
            user = cursor.fetchone()
            conn.close()
            if not user:
                raise Exception('User not found')
        except Exception as e:
            return jsonify({'message': 'Invalid token.', 'error': str(e)}), 401

        return f(*args, **kwargs)
    return decorated

# Registration endpoint
@app.route('/registrar', methods=['POST'])
def register():
    data = request.get_json()

    # Input validation
    if not data or not data.get('username') or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Missing required fields.'}), 400

    # Hash the password
    hashed_password = generate_password_hash(data['password'], method='sha256')

    try:
        conn = sqlite3.connect('financial_platform.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                       (data['username'], data['email'], hashed_password))
        conn.commit()
        conn.close()
        return jsonify({'message': 'User registered successfully!'}), 201
    except sqlite3.IntegrityError as e:
        return jsonify({'message': 'Registration failed.', 'error': str(e)}), 400

# Login endpoint
@app.route('/iniciar-sesion', methods=['POST'])
def login():
    data = request.get_json()

    # Input validation
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Missing required fields.'}), 400

    conn = sqlite3.connect('financial_platform.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (data['username'],))
    user = cursor.fetchone()
    conn.close()

    if user and check_password_hash(user[3], data['password']):
        token = jwt.encode({'username': user[1], 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)},
                           app.config['SECRET_KEY'], algorithm="HS256")
        return jsonify({'message': 'Login successful!', 'token': token}), 200

    return jsonify({'message': 'Invalid username or password.'}), 401

# Example protected route
@app.route('/protected', methods=['GET'])
@token_required
def protected():
    return jsonify({'message': 'You have accessed a protected route.'}), 200

# Error handling for unhandled routes
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'message': 'Route not found.'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
```
