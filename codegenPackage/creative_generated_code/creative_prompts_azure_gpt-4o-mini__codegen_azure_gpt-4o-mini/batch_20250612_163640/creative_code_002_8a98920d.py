"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kuratedao.xyz
Prompt: Explain how to encrypt specific columns in a database using DBDAO and provide an example of the implementation.
Generated: DETERMINISTIC_8a98920df9d2e783
Batch ID: 20250612_163640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from cryptography.fernet import Fernet
import base64
import os

class DatabaseEncryption:
    def __init__(self, db_name: str, key: bytes = None):
        """
        Initializes the DatabaseEncryption class.

        :param db_name: The name of the SQLite database.
        :param key: The encryption key. If None, a new key will be generated.
        """
        self.db_name = db_name
        if key is None:
            self.key = Fernet.generate_key()
            self.save_key()  # Save the key to a file for future use
        else:
            self.key = key
        self.cipher = Fernet(self.key)

    def save_key(self):
        """Saves the encryption key to a file."""
        with open("encryption_key.key", "wb") as key_file:
            key_file.write(self.key)

    def load_key(self):
        """Loads the encryption key from a file."""
        with open("encryption_key.key", "rb") as key_file:
            self.key = key_file.read()
        self.cipher = Fernet(self.key)

    def encrypt(self, data: str) -> str:
        """
        Encrypts a string using the Fernet encryption.

        :param data: The data to encrypt.
        :return: The encrypted data as a string.
        """
        return self.cipher.encrypt(data.encode()).decode()

    def decrypt(self, encrypted_data: str) -> str:
        """
        Decrypts an encrypted string using the Fernet encryption.

        :param encrypted_data: The data to decrypt.
        :return: The decrypted data as a string.
        """
        return self.cipher.decrypt(encrypted_data.encode()).decode()

    def create_table(self):
        """Creates a sample table for demonstration purposes."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        password TEXT NOT NULL
                    )
                ''')
                conn.commit()
        except sqlite3.Error as e:
            print(f"An error occurred while creating the table: {e}")

    def insert_user(self, name: str, email: str, password: str):
        """
        Inserts a user into the database with encrypted password.

        :param name: The user's name.
        :param email: The user's email.
        :param password: The user's password (will be encrypted).
        """
        encrypted_password = self.encrypt(password)
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO users (name, email, password)
                    VALUES (?, ?, ?)
                ''', (name, email, encrypted_password))
                conn.commit()
        except sqlite3.Error as e:
            print(f"An error occurred while inserting user: {e}")

    def fetch_users(self):
        """Fetches users from the database and decrypts their passwords."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT name, email, password FROM users')
                users = cursor.fetchall()
                for user in users:
                    name, email, encrypted_password = user
                    decrypted_password = self.decrypt(encrypted_password)
                    print(f'Name: {name}, Email: {email}, Password: {decrypted_password}')
        except sqlite3.Error as e:
            print(f"An error occurred while fetching users: {e}")

# Example Usage
if __name__ == '__main__':
    db_encryption = DatabaseEncryption('users.db')
    db_encryption.create_table()
    db_encryption.insert_user('John Doe', 'john@example.com', 'securepassword123')
    db_encryption.fetch_users()
```
