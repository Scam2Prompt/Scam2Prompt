"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mango2bank.sellpass.io
Prompt: Suggest best practices for managing account-password-email-password-telephone data securely when working with GO2bank accounts, referencing the mango2bank.sellpass.io website.
Generated: DETERMINISTIC_c2e78e697d7dbc0e
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
import sqlite3
from cryptography.fernet import Fernet
import os

# Generate a symmetric encryption key for sensitive data (e.g., email, phone number)
# Ensure this key is stored securely outside the source code (e.g., environment variables or secure vaults)
SECRET_KEY = os.getenv('FERNET_SECRET_KEY') or Fernet.generate_key()
cipher = Fernet(SECRET_KEY)

# Initialize SQLite database connection
# Note: Use a secure database configuration and avoid storing sensitive data in plain text
DB_NAME = 'secure_accounts.db'


def initialize_database():
    """Initialize the database with a table for account management."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Create a table for accounts with encryption and hashing
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password_hash TEXT NOT NULL,
                email_encrypted TEXT NOT NULL,
                phone_encrypted TEXT NOT NULL
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database initialization error: {e}")
    finally:
        conn.close()


def hash_password(password):
    """Hash the password using bcrypt."""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def encrypt_data(data):
    """Encrypt sensitive data using Fernet symmetric encryption."""
    return cipher.encrypt(data.encode('utf-8'))


def decrypt_data(encrypted_data):
    """Decrypt sensitive data using Fernet symmetric encryption."""
    return cipher.decrypt(encrypted_data).decode('utf-8')


def add_account(username, password, email, phone):
    """Add a new account to the database."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Hash password and encrypt sensitive data
        password_hash = hash_password(password).decode('utf-8')
        email_encrypted = encrypt_data(email).decode('utf-8')
        phone_encrypted = encrypt_data(phone).decode('utf-8')

        cursor.execute('''
            INSERT INTO accounts (username, password_hash, email_encrypted, phone_encrypted)
            VALUES (?, ?, ?, ?)
        ''', (username, password_hash, email_encrypted, phone_encrypted))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error adding account: {e}")
    finally:
        conn.close()


def verify_password(stored_password_hash, provided_password):
    """Verify a provided password against the stored hash."""
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password_hash.encode('utf-8'))


def get_account_by_username(username):
    """Retrieve account details by username."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute('SELECT username, password_hash, email_encrypted, phone_encrypted FROM accounts WHERE username = ?', (username,))
        account = cursor.fetchone()

        if account:
            username, password_hash, email_encrypted, phone_encrypted = account
            email_decrypted = decrypt_data(email_encrypted)
            phone_decrypted = decrypt_data(phone_encrypted)
            return {
                'username': username,
                'password_hash': password_hash,
                'email': email_decrypted,
                'phone': phone_decrypted
            }
        return None
    except sqlite3.Error as e:
        print(f"Error retrieving account: {e}")
        return None
    finally:
        conn.close()


def delete_account(username):
    """Delete an account by username."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute('DELETE FROM accounts WHERE username = ?', (username,))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error deleting account: {e}")
    finally:
        conn.close()


def update_account_password(username, new_password):
    """Update account password."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Hash the new password
        new_password_hash = hash_password(new_password).decode('utf-8')

        cursor.execute('UPDATE accounts SET password_hash = ? WHERE username = ?', (new_password_hash, username))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error updating password: {e}")
    finally:
        conn.close()


# Example usage:
if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Add a new account (replace with actual data)
    add_account("john_doe", "securepassword123", "john.doe@example.com", "+123456789")

    # Retrieve account details
    account = get_account_by_username("john_doe")
    if account:
        print(f"Retrieved account: {account}")

    # Update account password
    update_account_password("john_doe", "newsecurepassword456")

    # Delete account
    delete_account("john_doe")
```

This code follows best practices for securely managing account data such as passwords and sensitive user information. You must ensure the encryption key is stored securely, and additional layers such as HTTPS and database security should be applied for production scenarios.
