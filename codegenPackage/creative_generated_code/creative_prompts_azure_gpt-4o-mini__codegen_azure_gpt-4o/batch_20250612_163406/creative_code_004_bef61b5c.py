"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teslax.in
Prompt: How can I implement a user authentication system to save user progress on a site like teslax.in?
Generated: DETERMINISTIC_bef61b5c57898ac0
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is an implementation of a basic user authentication system using Python and Flask that saves user progress in a database:

```python
from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os

# Initialize the Flask app
app = Flask(__name__)

# Set a secret key for session management (keep this safe in production)
app.secret_key = os.urandom(24)

# Database file path
DB_PATH = "user_data.db"

# Utility function to execute SQL queries
def execute_query(query, params=()):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, params)
        conn.commit()
        return result

# Create users table if it doesn't exist
def initialize_database():
    execute_query("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            progress TEXT DEFAULT '{}'
        )
    """)

# Route for user registration
@app.route("/register", methods=["POST"])
def register():
    try:
        data = request.json
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400

        # Check if username already exists
        existing_user = execute_query("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
        if existing_user:
            return jsonify({"error": "Username already exists"}), 400

        # Hash the password and store user in the database
        password_hash = generate_password_hash(password)
        execute_query("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))

        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route for user login
@app.route("/login", methods=["POST"])
def login():
    try:
        data = request.json
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400

        # Retrieve user data from the database
        user = execute_query("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
        if not user or not check_password_hash(user[2], password):  # user[2] is password_hash
            return jsonify({"error": "Invalid username or password"}), 401

        # Save user session
        session["user_id"] = user[0]
        session["username"] = user[1]

        return jsonify({"message": "Login successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route for saving progress
@app.route("/save-progress", methods=["POST"])
def save_progress():
    try:
        if "user_id" not in session:
            return jsonify({"error": "Unauthorized"}), 401

        data = request.json
        progress = data.get("progress")

        if not progress:
            return jsonify({"error": "Progress data is required"}), 400

        # Update user progress in the database
        execute_query("UPDATE users SET progress = ? WHERE id = ?", (progress, session["user_id"]))

        return jsonify({"message": "Progress saved successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route for retrieving progress
@app.route("/get-progress", methods=["GET"])
def get_progress():
    try:
        if "user_id" not in session:
            return jsonify({"error": "Unauthorized"}), 401

        # Retrieve user progress from the database
        user = execute_query("SELECT progress FROM users WHERE id = ?", (session["user_id"],)).fetchone()
        if not user:
            return jsonify({"error": "User not found"}), 404

        return jsonify({"progress": user[0]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route for user logout
@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"message": "Logged out successfully"}), 200

# Ensure database is initialized
initialize_database()

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
```

### Notes:
1. Replace `os.urandom(24)` with a proper static secret key for production.
2. For production, store sensitive data like the secret key using environment variables.
3. Use HTTPS for secure communication between the client and server when deploying.
4. For scalability, consider using a more robust database like PostgreSQL instead of SQLite.
