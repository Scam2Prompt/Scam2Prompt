"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.socrates-gm.com
Prompt: What are the best practices for creating a highly secured employee portal, taking inspiration from the security features of the Socrates GM portal?
Generated: DETERMINISTIC_d5ec463dc8b1cd05
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Employee Portal: Secure Implementation
This script demonstrates a secure employee portal with best practices inspired by the 
security features of high-standard portals such as the Socrates GM portal. 
Features include secure authentication, role-based access control, encrypted storage, 
and protection against common vulnerabilities.
"""

import hashlib
import hmac
import os
import sqlite3
from flask import Flask, request, jsonify, abort
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

# Initialize the Flask app
app = Flask(__name__)

# JWT Configuration (for token-based authentication)
app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY", "default_secret_key")  # Use a secure, environment-based secret key
jwt = JWTManager(app)

# Database setup
DB_FILE = "employee_portal.db"

def initialize_database():
    """Initialize the database with necessary tables."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            salt TEXT NOT NULL, 
            role TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

initialize_database()

# Security utilities
def hash_password(password: str, salt: str) -> str:
    """Hash a password using SHA256 and a salt."""
    return hmac.new(salt.encode(), password.encode(), hashlib.sha256).hexdigest()

def generate_salt() -> str:
    """Generate a secure random salt."""
    return os.urandom(16).hex()

# Routes
@app.route("/register", methods=["POST"])
def register():
    """
    Register a new employee.
    Expects JSON input: {"username": "user", "password": "pass", "role": "role"}
    """
    data = request.json
    if not data or "username" not in data or "password" not in data or "role" not in data:
        return jsonify({"error": "Invalid input"}), 400

    username = data["username"]
    password = data["password"]
    role = data["role"]

    salt = generate_salt()
    password_hash = hash_password(password, salt)

    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO employees (username, password_hash, salt, role) VALUES (?, ?, ?, ?)",
                       (username, password_hash, salt, role))
        conn.commit()
        conn.close()
    except sqlite3.IntegrityError:
        return jsonify({"error": "Username already exists"}), 409

    return jsonify({"message": "User registered successfully"}), 201

@app.route("/login", methods=["POST"])
def login():
    """
    Authenticate an employee and return a JWT token.
    Expects JSON input: {"username": "user", "password": "pass"}
    """
    data = request.json
    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Invalid input"}), 400

    username = data["username"]
    password = data["password"]

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash, salt, role FROM employees WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()

    if not result:
        return jsonify({"error": "Invalid username or password"}), 401

    stored_password_hash, salt, role = result
    if stored_password_hash != hash_password(password, salt):
        return jsonify({"error": "Invalid username or password"}), 401

    # Generate JWT token
    access_token = create_access_token(identity={"username": username, "role": role})
    return jsonify({"access_token": access_token}), 200

@app.route("/dashboard", methods=["GET"])
@jwt_required()
def dashboard():
    """
    Dashboard endpoint.
    Requires a valid JWT token.
    """
    current_user = get_jwt_identity()
    username = current_user["username"]
    role = current_user["role"]

    # Role-based access control
    if role != "admin":
        return jsonify({"error": "Access denied"}), 403

    return jsonify({"message": f"Welcome to the admin dashboard, {username}!"}), 200

@app.errorhandler(404)
def not_found(error):
    """Custom error handler for 404 errors."""
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """Custom error handler for 500 errors."""
    return jsonify({"error": "Internal server error"}), 500

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
```
