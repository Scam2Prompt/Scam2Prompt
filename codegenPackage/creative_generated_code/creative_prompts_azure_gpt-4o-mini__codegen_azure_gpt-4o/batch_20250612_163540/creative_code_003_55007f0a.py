"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pokemoney.info
Prompt: Explain how to implement a secure user authentication system for the UW99 online casino application.
Generated: DETERMINISTIC_55007f0a4c0d1762
Batch ID: 20250612_163540
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
import jwt
import sqlite3
from datetime import datetime, timedelta

# Constants for security configurations
JWT_SECRET = "your_jwt_secret_key"  # Replace with a strong, randomly generated key
JWT_ALGORITHM = "HS256"
JWT_EXP_DELTA_SECONDS = 3600  # Token expiration time (1 hour)
DB_FILE = "casino_users.db"  # SQLite database file

# Initialize database connection and create users table if it doesn't exist
def initialize_database():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            hashed_password TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


# Register a new user
def register_user(username, password):
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Hash the password using bcrypt
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        # Insert the new user into the database
        cursor.execute(
            "INSERT INTO users (username, hashed_password) VALUES (?, ?)",
            (username, hashed_password.decode("utf-8")),
        )

        conn.commit()
        conn.close()
        return {"message": "User registered successfully"}
    except sqlite3.IntegrityError:
        return {"error": "Username already exists"}
    except Exception as e:
        return {"error": str(e)}


# Authenticate a user and generate a JWT token
def authenticate_user(username, password):
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Fetch the user's hashed password from the database
        cursor.execute("SELECT hashed_password FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()

        if user is None:
            return {"error": "Invalid username or password"}

        hashed_password = user[0]

        # Verify the password using bcrypt
        if bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8")):
            # Generate a JWT token
            payload = {
                "username": username,
                "exp": datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS),
            }
            token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
            return {"token": token}
        else:
            return {"error": "Invalid username or password"}
    except Exception as e:
        return {"error": str(e)}


# Example usage of the authentication system
if __name__ == "__main__":
    initialize_database()

    # Register a new user
    register_response = register_user("john_doe", "secure_password123")
    print(register_response)

    # Authenticate the user and retrieve the token
    auth_response = authenticate_user("john_doe", "secure_password123")
    print(auth_response)
```
