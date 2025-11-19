"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1wapdj.top
Prompt: How can I implement a user authentication system for a sports betting application like 1win?
Generated: DETERMINISTIC_79b23deab110cd9a
Batch ID: 20250612_164217
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python-based implementation for a user authentication system using Flask and SQLite. The code ensures clean structure, proper error handling, and best practices. Note that this is a simplified example and should be extended for production use (e.g., by adding encryption, rate-limiting, and other security measures).

```python
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os

app = Flask(__name__)

DATABASE_FILE = "sports_betting_auth.db"


def init_db():
    """
    Initialize SQLite database. Creates users table if it does not exist.
    """
    if not os.path.exists(DATABASE_FILE):
        connection = sqlite3.connect(DATABASE_FILE)
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)
        connection.commit()
        connection.close()


def get_db_connection():
    """
    Establish and return a connection to the SQLite database.
    """
    try:
        connection = sqlite3.connect(DATABASE_FILE)
        connection.row_factory = sqlite3.Row
        return connection
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        raise


@app.route("/register", methods=["POST"])
def register_user():
    """
    Register a new user. Requires 'username' and 'password' fields in the request JSON.
    """
    try:
        data = request.json
        username = data.get("username")
        password = data.get("password")

        # Validate input
        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400

        # Hash password for security
        hashed_password = generate_password_hash(password)

        # Insert user into the database
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        connection.commit()
        connection.close()

        return jsonify({"message": "User registered successfully"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Username already exists"}), 400
    except Exception as e:
        print(f"Error during registration: {e}")
        return jsonify({"error": "Internal server error"}), 500


@app.route("/login", methods=["POST"])
def login_user():
    """
    Authenticate user login. Requires 'username' and 'password' fields in the request JSON.
    """
    try:
        data = request.json
        username = data.get("username")
        password = data.get("password")

        # Validate input
        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400

        # Retrieve user from the database
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        connection.close()

        if user and check_password_hash(user["password"], password):
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"error": "Invalid username or password"}), 401
    except Exception as e:
        print(f"Error during login: {e}")
        return jsonify({"error": "Internal server error"}), 500


@app.route("/users", methods=["GET"])
def list_users():
    """
    (Admin-only) List all registered users. For demonstration purposes only.
    """
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id, username FROM users")
        users = cursor.fetchall()
        connection.close()

        user_list = [{"id": user["id"], "username": user["username"]} for user in users]
        return jsonify(user_list), 200
    except Exception as e:
        print(f"Error during user listing: {e}")
        return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    # Initialize database before starting the application
    init_db()
    app.run(debug=True)
```

### Features:
- **Registration**: Users can register with a unique username and password.
- **Login**: Users can authenticate with their credentials.
- **Admin-only Listing**: For demonstration, lists users (add authentication for admin privileges in production).
- **Error Handling**: Handles database errors, input validation, and general exceptions.
- **Password Hashing**: Uses `Werkzeug` for secure password storage.

### Prerequisites:
- Install dependencies using: `pip install flask werkzeug`
- Run the script using: `python app.py`
