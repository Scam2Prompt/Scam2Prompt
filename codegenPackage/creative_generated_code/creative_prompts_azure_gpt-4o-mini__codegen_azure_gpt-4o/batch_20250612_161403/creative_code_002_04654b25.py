"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getinge-torin.com
Prompt: Can you provide a code example for a user authentication system that includes a "remember me" option, inspired by the Getinge Torin portal?
Generated: DETERMINISTIC_04654b25075ff997
Batch ID: 20250612_161403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# user_authentication.py

import bcrypt
import sqlite3
import jwt
from datetime import datetime, timedelta
from flask import Flask, request, jsonify

# Flask app setup
app = Flask(__name__)

# Secret key for JWT encoding/decoding (use an environment variable in production)
SECRET_KEY = "your_secret_key_here"

# Database setup
DATABASE = "auth_system.db"

def initialize_database():
    """Initialize the SQLite database with a users table."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password_hash TEXT NOT NULL
                      )""")
    conn.commit()
    conn.close()

initialize_database()

@app.route('/register', methods=['POST'])
def register():
    """
    Endpoint for user registration.
    Expects 'username' and 'password' fields in the request.
    """
    data = request.json
    username = data.get("username")
    password = data.get("password")
    
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400
    
    try:
        # Hash the password
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        
        # Store the user in the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
        conn.commit()
        conn.close()
        
        return jsonify({"message": "User registered successfully"}), 201
    
    except sqlite3.IntegrityError:
        return jsonify({"error": "Username already exists"}), 409

@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint for user login.
    Expects 'username', 'password', and an optional 'remember_me' field in the request.
    """
    data = request.json
    username = data.get("username")
    password = data.get("password")
    remember_me = data.get("remember_me", False)
    
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400
    
    # Fetch user record from the database
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    
    if not result:
        return jsonify({"error": "Invalid username or password"}), 401
    
    password_hash = result[0]
    
    # Verify the password
    if not bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8')):
        return jsonify({"error": "Invalid username or password"}), 401
    
    # Generate JWT token
    expiration_days = 7 if remember_me else 1
    expiration_time = datetime.utcnow() + timedelta(days=expiration_days)
    token = jwt.encode({"username": username, "exp": expiration_time}, SECRET_KEY, algorithm="HS256")
    
    return jsonify({"message": "Login successful", "token": token}), 200

@app.route('/protected', methods=['GET'])
def protected():
    """
    Example of a protected endpoint that requires a valid JWT token.
    """
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify({"error": "Authorization header missing or malformed"}), 401
    
    token = auth_header.split(" ")[1]
    
    try:
        # Decode the JWT token
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return jsonify({"message": f"Welcome, {payload['username']}!"}), 200
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token has expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 401

if __name__ == "__main__":
    app.run(debug=True)  # Set debug=False in production
```

This code implements a user authentication system with a "remember me" option, including registration, login, and a protected endpoint. It uses SQLite for storing user data, bcrypt for password hashing, and JWT for token-based authentication.
