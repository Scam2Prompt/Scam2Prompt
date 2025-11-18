"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kuratedao.xyz
Prompt: Provide a step-by-step guide to use DBDAO for creating a DAO-governed database with encrypted columns for privacy.
Generated: DETERMINISTIC_42d17d35344ae60d
Batch ID: 20250612_151232
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
import os

# Generate a key for encryption
def generate_key():
    """
    Generates a key for encryption and saves it into a file.
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load the previously generated key
def load_key():
    """
    Loads the encryption key from the current directory.
    """
    return open("secret.key", "rb").read()

# Encrypt the data
def encrypt_data(data, key):
    """
    Encrypts the provided data using the given key.
    
    :param data: The data to encrypt
    :param key: The encryption key
    :return: Encrypted data
    """
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data.encode())
    return encrypted

# Decrypt the data
def decrypt_data(encrypted_data, key):
    """
    Decrypts the provided data using the given key.
    
    :param encrypted_data: The data to decrypt
    :param key: The decryption key
    :return: Decrypted data
    """
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_data).decode()
    return decrypted

class Database:
    def __init__(self, db_name):
        """
        Initializes the database connection.
        
        :param db_name: Name of the SQLite database file
        """
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        """
        Creates a table for storing encrypted data if it doesn't exist.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS secure_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                encrypted_info BLOB NOT NULL
            )
        ''')
        self.connection.commit()

    def insert_data(self, data):
        """
        Inserts encrypted data into the database.
        
        :param data: Data to be stored
        """
        try:
            key = load_key()
            encrypted = encrypt_data(data, key)
            self.cursor.execute('INSERT INTO secure_data (encrypted_info) VALUES (?)', (encrypted,))
            self.connection.commit()
        except Exception as e:
            print(f"Error inserting data: {e}")

    def fetch_data(self):
        """
        Fetches and decrypts all data from the database.
        
        :return: List of decrypted data
        """
        decrypted_data = []
        try:
            key = load_key()
            self.cursor.execute('SELECT encrypted_info FROM secure_data')
            rows = self.cursor.fetchall()
            for row in rows:
                decrypted = decrypt_data(row[0], key)
                decrypted_data.append(decrypted)
        except Exception as e:
            print(f"Error fetching data: {e}")
        return decrypted_data

    def close(self):
        """
        Closes the database connection.
        """
        self.connection.close()

# Example Usage
if __name__ == "__main__":
    # Ensure the encryption key is generated only once
    if not os.path.exists("secret.key"):
        generate_key()

    db = Database("encrypted_data.db")
    
    # Insert sample data
    db.insert_data("Sensitive information 1")
    db.insert_data("Sensitive information 2")

    # Fetch and print decrypted data
    data = db.fetch_data()
    print(data)

    # Close the database
    db.close()
```
