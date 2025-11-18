"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bbmanews.com
Prompt: Write a script to securely store and retrieve user credentials for logging into a credit portal.
Generated: DETERMINISTIC_ca628f22b9ae771d
Batch ID: 20250612_153547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import hashlib
import bcrypt
import sqlite3
from cryptography.fernet import Fernet

# Constants
DB_FILE = "credentials.db"
KEY_FILE = "key.key"

# Utility function to generate a symmetric encryption key
def generate_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)

# Load the encryption key
def load_key():
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()

# Securely hash a user password
def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

# Verify a password against its hash
def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password)

# Initialize the database
def initialize_database():
    if not os.path.exists(DB_FILE):
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password_hash BLOB,
            encrypted_data BLOB
        )
        """)
        conn.commit()
        conn.close()

# Store user credentials securely
def store_credentials(username, password, secret_data):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Hash the password
    password_hash = hash_password(password)

    # Encrypt the secret data
    key = load_key()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(secret_data.encode())

    try:
        cursor.execute("""
        INSERT INTO users (username, password_hash, encrypted_data)
        VALUES (?, ?, ?)
        """, (username, password_hash, encrypted_data))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Error: Username already exists.")
    finally:
        conn.close()

# Retrieve user credentials securely
def retrieve_credentials(username, password):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT password_hash, encrypted_data FROM users WHERE username = ?", (username,))
    user_data = cursor.fetchone()
    conn.close()

    if not user_data:
        print("Error: User not found.")
        return None

    password_hash, encrypted_data = user_data

    # Verify the password
    if not verify_password(password, password_hash):
        print("Error: Invalid password.")
        return None

    # Decrypt the secret data
    key = load_key()
    fernet = Fernet(key)
    secret_data = fernet.decrypt(encrypted_data).decode()

    return secret_data

# Main function to demonstrate functionality
if __name__ == "__main__":
    generate_key()  # Generate encryption key (if not already generated)
    initialize_database()  # Initialize the database

    # Example usage
    username = "john_doe"
    password = "secure_password"
    secret_data = "My credit portal secret data."

    print("\nStoring credentials...")
    store_credentials(username, password, secret_data)

    print("\nRetrieving credentials...")
    retrieved_data = retrieve_credentials(username, password)
    if retrieved_data:
        print(f"Retrieved secret data: {retrieved_data}")
```
