"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1inch-dex.com
Prompt: Generate a code snippet to implement a secure login feature for a gaming platform similar to Monyetjp, focusing on user authentication and session management.
Generated: DETERMINISTIC_676f92d0a80ddd85
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import bcrypt
import sqlite3
import jwt
from datetime import datetime, timedelta
from flask import Flask, request, jsonify

app = Flask(__name__)

# Secret key for JWT token generation
SECRET_KEY = os.environ.get("SECRET_KEY", "your-secret-key")

# Database setup
DB_PATH = "users.db"
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
init_db()

# Helper function to generate JWT tokens
def generate_token(username):
    payload = {
        "username": username,
        "exp": datetime.utcnow() + timedelta(hours=2)  # Token expires in 2 hours
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

# Register endpoint
@app.route("/register", methods=["POST"])
def register():
    try:
        data = request.json
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400

        # Hash the password
        password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

        # Save user to database
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
        conn.commit()
        conn.close()

        return jsonify({"message": "User registered successfully"}), 201

    except sqlite3.IntegrityError:
        return jsonify({"error": "Username already exists"}), 409
    except Exception as e:
        return jsonify({"error": "An error occurred"}), 500

# Login endpoint
@app.route("/login", methods=["POST"])
def login():
    try:
        data = request.json
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400

        # Fetch user from database
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()

        if not user:
            return jsonify({"error": "Invalid username or password"}), 401

        password_hash = user[0]

        # Verify password
        if not bcrypt.checkpw(password.encode("utf-8"), password_hash.encode("utf-8")):
            return jsonify({"error": "Invalid username or password"}), 401

        # Generate JWT token
        token = generate_token(username)
        return jsonify({"message": "Login successful", "token": token}), 200

    except Exception as e:
        return jsonify({"error": "An error occurred"}), 500

# Protected endpoint example
@app.route("/profile", methods=["GET"])
def profile():
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"error": "Authorization token is required"}), 401

    try:
        # Decode and verify token
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        username = decoded.get("username")
        return jsonify({"message": f"Welcome {username}!"}), 200

    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token has expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 401

# Start the Flask app
if __name__ == "__main__":
    app.run(debug=True)
```
