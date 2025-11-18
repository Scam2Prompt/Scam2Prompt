"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptobalancer.co.uk
Prompt: Suggest methods to implement secure login functionality for a cryptocurrency management tool like CryptoBalancer.
Generated: DETERMINISTIC_f3a79d74c7c3324e
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Secure Login Functionality for a Cryptocurrency Management Tool
Language: Python
"""

# Required imports
import bcrypt  # For password hashing
import sqlite3  # For database management
import jwt  # For JSON Web Tokens (JWT) - user authentication
import os  # For managing environment variables
from datetime import datetime, timedelta

# Environment variable for JWT secret key
JWT_SECRET = os.getenv("JWT_SECRET", "your_jwt_secret_key")  # Replace in production with a secure key from env variables
JWT_ALGORITHM = "HS256"
TOKEN_EXPIRATION_MINUTES = 30

# Database setup (for demonstration purposes, SQLite is used)
DATABASE_FILE = "crypto_balancer.db"

def initialize_database():
    """
    Initializes the database with a users table if it doesn't already exist.
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def hash_password(password):
    """
    Hashes a plain-text password using bcrypt.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(password, hashed_password):
    """
    Verifies a plain-text password against a hashed password.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def register_user(username, password):
    """
    Registers a new user with a hashed password.
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        password_hash = hash_password(password)
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
        conn.commit()
        return {"message": "User registered successfully"}
    except sqlite3.IntegrityError:
        return {"error": "Username already exists"}
    except sqlite3.Error as e:
        return {"error": f"Database error: {e}"}
    finally:
        conn.close()

def authenticate_user(username, password):
    """
    Authenticates a user and returns a JWT token if successful.
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        if not user:
            return {"error": "Invalid username or password"}
        if verify_password(password, user[0]):
            token = generate_jwt(username)
            return {"message": "Authentication successful", "token": token}
        else:
            return {"error": "Invalid username or password"}
    except sqlite3.Error as e:
        return {"error": f"Database error: {e}"}
    finally:
        conn.close()

def generate_jwt(username):
    """
    Generates a JWT for a given username.
    """
    payload = {
        "username": username,
        "exp": datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRATION_MINUTES)
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token

def verify_jwt(token):
    """
    Verifies a JWT and returns the decoded payload if valid.
    """
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return {"valid": True, "payload": payload}
    except jwt.ExpiredSignatureError:
        return {"valid": False, "error": "Token has expired"}
    except jwt.InvalidTokenError:
        return {"valid": False, "error": "Invalid token"}

# Example usage
if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Register a sample user
    result = register_user("sample_user", "secure_password123")
    print(result)

    # Authenticate the sample user
    auth_result = authenticate_user("sample_user", "secure_password123")
    print(auth_result)

    # Verify the JWT
    if "token" in auth_result:
        token = auth_result["token"]
        verification_result = verify_jwt(token)
        print(verification_result)
```
