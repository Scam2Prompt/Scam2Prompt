"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethairdrop.org
Prompt: Develop a script to handle user authentication and subscription management for a 3D model repository, ensuring secure access to premium content.
Generated: DETERMINISTIC_e70251c4481fd927
Batch ID: 20250612_154322
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

# Constants
SECRET_KEY = "your_secret_key"  # Replace with a strong secret key
DATABASE_FILE = "subscriptions.db"
JWT_EXPIRATION_MINUTES = 60
HASH_ROUNDS = 12

# Database setup (if not exists)
def setup_database():
    """Initialize the database schema if it doesn't exist."""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            subscription_level TEXT NOT NULL CHECK(subscription_level IN ('free', 'premium')),
            subscription_expiry DATE
        )
    """)
    conn.commit()
    conn.close()

# User registration
def register_user(username, password, subscription_level='free'):
    """
    Register a new user.

    Args:
        username (str): The username.
        password (str): The user's password.
        subscription_level (str): Subscription level ('free' or 'premium').
    Returns:
        str: Success message or error.
    """
    try:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(HASH_ROUNDS))
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (username, password_hash, subscription_level, subscription_expiry)
            VALUES (?, ?, ?, ?)
        """, (username, hashed_password.decode('utf-8'), subscription_level, None))
        conn.commit()
        conn.close()
        return "User registered successfully."
    except sqlite3.IntegrityError:
        return "Username already exists."

# User login
def login_user(username, password):
    """
    Authenticate a user and generate a JWT if successful.

    Args:
        username (str): The username.
        password (str): The user's password.
    Returns:
        str: JWT token or error message.
    """
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash, subscription_level, subscription_expiry FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()

    if user and bcrypt.checkpw(password.encode('utf-8'), user[0].encode('utf-8')):
        subscription_level = user[1]
        subscription_expiry = user[2]
        if subscription_level == 'premium' and subscription_expiry and datetime.strptime(subscription_expiry, '%Y-%m-%d') < datetime.now():
            subscription_level = 'free'  # Downgrade expired premium users to free

        payload = {
            "username": username,
            "subscription_level": subscription_level,
            "exp": datetime.utcnow() + timedelta(minutes=JWT_EXPIRATION_MINUTES)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return token
    return "Invalid username or password."

# Subscription upgrade
def upgrade_subscription(username, days=30):
    """
    Upgrade a user's subscription to premium.

    Args:
        username (str): The username.
        days (int): Number of days to extend the subscription.
    Returns:
        str: Success message or error.
    """
    try:
        expiry_date = datetime.now() + timedelta(days=days)
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE users
            SET subscription_level = 'premium', subscription_expiry = ?
            WHERE username = ?
        """, (expiry_date.strftime('%Y-%m-%d'), username))
        conn.commit()
        conn.close()
        return "Subscription upgraded successfully."
    except sqlite3.Error as e:
        return f"Error upgrading subscription: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Setup database
    setup_database()

    # Register a user
    print(register_user("test_user", "secure_password"))

    # Login the user and get a JWT
    token = login_user("test_user", "secure_password")
    print(f"JWT Token: {token}")

    # Upgrade the user's subscription
    print(upgrade_subscription("test_user"))
```

Before running this script, ensure you securely manage the `SECRET_KEY`, and properly handle sensitive data in production.
