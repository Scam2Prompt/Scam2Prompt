"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://empower.gr
Prompt: What are the best practices for designing a secure login interface, inspired by Empower's login functionality?
Generated: DETERMINISTIC_f9343f0f719e8121
Batch ID: 20250612_162812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import bcrypt  # For hashing passwords
import re  # For validating email format
import sqlite3  # For database connection
from flask import Flask, request, jsonify, session  # Web framework for API handling

# Initialize Flask application
app = Flask(__name__)
app.secret_key = "your_secret_key"  # Secret key for session management

# Database connection setup
DATABASE = "users.db"

# Password hashing configuration
SALT_ROUNDS = 12  # Number of rounds for bcrypt hashing

# Regular expression for email validation
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'


# Helper function to create the database and users table if not exists
def initialize_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


# Helper function to validate email format
def is_valid_email(email):
    return re.match(EMAIL_REGEX, email) is not None


# Helper function to hash passwords
def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt(SALT_ROUNDS))


# Helper function to verify passwords
def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password)


# Route to handle user registration
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')

        # Validate input
        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400
        if not is_valid_email(email):
            return jsonify({"error": "Invalid email format"}), 400
        if len(password) < 8:
            return jsonify({"error": "Password must be at least 8 characters long"}), 400

        # Hash the password
        password_hash = hash_password(password)

        # Store the user in the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (email, password_hash) VALUES (?, ?)", (email, password_hash))
        conn.commit()
        conn.close()

        return jsonify({"message": "User registered successfully"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Email already exists"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route to handle user login
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')

        # Validate input
        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400

        # Retrieve user from the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT password_hash FROM users WHERE email = ?", (email,))
        result = cursor.fetchone()
        conn.close()

        if not result:
            return jsonify({"error": "Invalid email or password"}), 401

        stored_password_hash = result[0]

        # Verify the provided password against the stored hash
        if not verify_password(password, stored_password_hash):
            return jsonify({"error": "Invalid email or password"}), 401

        # Store session information for login persistence
        session['user'] = email

        return jsonify({"message": "Login successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route to handle user logout
@app.route('/logout', methods=['POST'])
def logout():
    try:
        session.pop('user', None)
        return jsonify({"message": "Logout successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Main execution point
if __name__ == "__main__":
    initialize_db()  # Ensure the database is ready before starting the app
    app.run(debug=True)
```
