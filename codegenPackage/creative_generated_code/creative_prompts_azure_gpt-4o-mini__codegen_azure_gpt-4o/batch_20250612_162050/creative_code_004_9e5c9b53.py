"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yourmaidinheaven.com
Prompt: Illustrate how to implement a user authentication system for a cleaning service platform, ensuring trust and security like Maid in Heaven's vetted cleaning staff.
Generated: DETERMINISTIC_9e5c9b5340416b48
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import bcrypt  # For password hashing
import sqlite3  # For database management
import jwt  # For JSON Web Token authentication
import datetime  # For timestamp handling

# Constants for security
JWT_SECRET = "your_secret_key_here"  # Replace this with a secure random key in production
JWT_ALGORITHM = "HS256"  # Algorithm used for token encoding
TOKEN_EXPIRATION_MINUTES = 60  # Token expiration duration

# Database connection setup
def initialize_database():
    """Initialize the database with necessary tables."""
    conn = sqlite3.connect("cleaning_service.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def hash_password(password):
    """
    Hash a plain-text password using bcrypt.
    :param password: The plain-text password.
    :return: The hashed password.
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt).decode()

def verify_password(plain_password, hashed_password):
    """
    Verify a plain-text password against its hashed counterpart.
    :param plain_password: The plain-text password.
    :param hashed_password: The hashed password.
    :return: True if the password matches, False otherwise.
    """
    return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())

def create_user(username, password, email):
    """
    Create a new user in the database.
    :param username: The username of the user.
    :param password: The plain-text password of the user.
    :param email: The email of the user.
    """
    conn = sqlite3.connect("cleaning_service.db")
    cursor = conn.cursor()
    try:
        hashed_password = hash_password(password)
        cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
                       (username, hashed_password, email))
        conn.commit()
        print("User created successfully!")
    except sqlite3.IntegrityError:  # Handle duplicate username or email
        print("Error: Username or email already exists.")
    finally:
        conn.close()

def authenticate_user(username, password):
    """
    Authenticate a user based on username and password.
    :param username: The username of the user.
    :param password: The plain-text password of the user.
    :return: A JWT token if authentication succeeds, None otherwise.
    """
    conn = sqlite3.connect("cleaning_service.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()

    if result:
        stored_password = result[0]
        if verify_password(password, stored_password):
            # Generate JWT token upon successful authentication
            payload = {
                "username": username,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=TOKEN_EXPIRATION_MINUTES)
            }
            token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
            return token
    return None

def decode_token(token):
    """
    Decode a JWT token.
    :param token: The JWT token.
    :return: The decoded payload if the token is valid, None otherwise.
    """
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        print("Error: Token has expired.")
    except jwt.InvalidTokenError:
        print("Error: Invalid token.")
    return None

# Example usage
if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Create a new user (run this once to create a user)
    # create_user("maidinheaven_user", "securePassword123", "user@example.com")

    # Authenticate a user
    token = authenticate_user("maidinheaven_user", "securePassword123")
    if token:
        print("Authentication successful!")
        print("JWT Token:", token)

        # Decode the token (for verification purposes)
        decoded_payload = decode_token(token)
        if decoded_payload:
            print("Decoded Token Payload:", decoded_payload)
    else:
        print("Authentication failed!")
```
