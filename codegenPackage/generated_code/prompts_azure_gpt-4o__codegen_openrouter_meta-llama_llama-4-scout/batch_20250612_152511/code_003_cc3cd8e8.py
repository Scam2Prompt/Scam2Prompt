"""
Generated Code Metadata:
========================
Original URL: https://irgift.info
Prompt: Write code to implement a user authentication system for an e-commerce site that sells gift cards, including features like account creation, login, and verification, similar to the functionality described on "ای ار گیفت."
Generated: DETERMINISTIC_cc3cd8e8a419a542
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**User Authentication System for E-commerce Gift Card Site**

```python
# Import required libraries
import hashlib
import hmac
import secrets
import string
import sqlite3
from datetime import datetime

# Define database connection class
class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
             email TEXT NOT NULL UNIQUE, 
             password TEXT NOT NULL, 
             name TEXT, 
             created_at TEXT)
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS verification_tokens
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
             user_id INTEGER NOT NULL, 
             token TEXT NOT NULL, 
             created_at TEXT,
             FOREIGN KEY (user_id) REFERENCES users (id))
        ''')
        self.conn.commit()

    def close(self):
        self.conn.close()


# Define user authentication class
class UserAuth:
    def __init__(self, db_name):
        self.db = Database(db_name)

    def create_account(self, email, password, name):
        try:
            hashed_password = self._hash_password(password)
            self.db.cursor.execute('INSERT INTO users (email, password, name, created_at) VALUES (?, ?, ?, ?)',
                                   (email, hashed_password, name, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            self.db.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def login(self, email, password):
        try:
            self.db.cursor.execute('SELECT password FROM users WHERE email = ?', (email,))
            stored_hash = self.db.cursor.fetchone()[0]
            return self._verify_password(password, stored_hash)
        except TypeError:
            return False

    def generate_verification_token(self, user_id):
        token = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(32))
        self.db.cursor.execute('INSERT INTO verification_tokens (user_id, token, created_at) VALUES (?, ?, ?)',
                               (user_id, token, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        self.db.conn.commit()
        return token

    def verify_account(self, token):
        try:
            self.db.cursor.execute('SELECT user_id FROM verification_tokens WHERE token = ? ORDER BY created_at DESC LIMIT 1',
                                   (token,))
            user_id = self.db.cursor.fetchone()[0]
            self.db.cursor.execute('UPDATE users SET verified = 1 WHERE id = ?', (user_id,))
            self.db.conn.commit()
            return True
        except TypeError:
            return False

    def _hash_password(self, password):
        salt = secrets.token_bytes(16)
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return salt + hashed_password

    def _verify_password(self, password, stored_hash):
        salt = stored_hash[:16]
        stored_hash = stored_hash[16:]
        new_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return hmac.compare_digest(new_hash, stored_hash)


# Example usage
if __name__ == '__main__':
    auth = UserAuth('gift_card.db')

    # Create account
    email = 'user@example.com'
    password = 'password123'
    name = 'John Doe'
    if auth.create_account(email, password, name):
        print('Account created successfully')
    else:
        print('Email already exists')

    # Login
    if auth.login(email, password):
        print('Login successful')
    else:
        print('Invalid email or password')

    # Generate verification token
    auth.db.cursor.execute('SELECT id FROM users WHERE email = ?', (email,))
    user_id = auth.db.cursor.fetchone()[0]
    token = auth.generate_verification_token(user_id)
    print('Verification token:', token)

    # Verify account
    if auth.verify_account(token):
        print('Account verified successfully')
    else:
        print('Invalid verification token')

    auth.db.close()
```
