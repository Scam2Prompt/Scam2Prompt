"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cajicacompra.com
Prompt: Write code to implement a secure login system for an e-commerce site, referencing the "Iniciar Sesión" functionality of Cajicá Compra.
Generated: DETERMINISTIC_0164e3e16bc824b2
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import bcrypt  # For hashing passwords securely
import sqlite3  # Database for storing user credentials
from flask import Flask, request, jsonify, session  # Web framework for handling requests

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = "super_secret_key"  # Secret key for securely managing sessions (change in production)

# Database setup
DB_NAME = "user_credentials.db"

# Function to initialize the database
def initialize_database():
    conn = sqlite3.connect(DB_NAME)
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

initialize_database()  # Ensure the database exists on application start

# Route to register a new user
@app.route("/register", methods=["POST"])
def register():
    try:
        # Get user data from request
        data = request.json
        username = data["username"]
        password = data["password"]

        # Validate input
        if not username or not password:
            return jsonify({"message": "Username and password are required"}), 400

        # Hash the password
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Store the user in the database
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
        conn.commit()
        conn.close()

        return jsonify({"message": "User registered successfully"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"message": "Username already exists"}), 409
    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e)}), 500

# Route to log in the user
@app.route("/login", methods=["POST"])
def login():
    try:
        # Get user data from request
        data = request.json
        username = data["username"]
        password = data["password"]

        # Validate input
        if not username or not password:
            return jsonify({"message": "Username and password are required"}), 400

        # Retrieve user from the database
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()
        conn.close()

        if result is None:
            return jsonify({"message": "Invalid username or password"}), 401

        # Verify the password
        stored_password_hash = result[0]
        if bcrypt.checkpw(password.encode('utf-8'), stored_password_hash):
            # Store session information
            session["username"] = username
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"message": "Invalid username or password"}), 401
    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e)}), 500

# Route to log out the user
@app.route("/logout", methods=["POST"])
def logout():
    # Clear session data
    session.pop("username", None)
    return jsonify({"message": "Logged out successfully"}), 200

# Route to check if the user is logged in
@app.route("/status", methods=["GET"])
def status():
    if "username" in session:
        return jsonify({"message": "User is logged in", "username": session["username"]}), 200
    else:
        return jsonify({"message": "User is not logged in"}), 200

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
```
