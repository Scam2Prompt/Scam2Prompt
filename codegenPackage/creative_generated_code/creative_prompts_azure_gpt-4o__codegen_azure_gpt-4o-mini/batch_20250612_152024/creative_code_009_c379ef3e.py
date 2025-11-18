"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financialrecoverysolutions.co.uk
Prompt: Write code to securely store and manage client data for financial mis-selling claims, adhering to the data protection standards mentioned by Financial Recovery Solutions Ltd.
Generated: DETERMINISTIC_c379ef3e34c45b2b
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import sqlite3
from cryptography.fernet import Fernet
from contextlib import closing

# Generate a key for encryption and decryption
# Keep this key secure; it should not be hardcoded in production code
def generate_key():
    return Fernet.generate_key()

# Load the encryption key from a secure location
def load_key(path):
    with open(path, "rb") as key_file:
        return key_file.read()

# Encrypt the client data
def encrypt_data(data, key):
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())

# Decrypt the client data
def decrypt_data(encrypted_data, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data).decode()

# Database handler to manage client data
class ClientDataManager:
    def __init__(self, db_path, key_path):
        self.db_path = db_path
        self.key_path = key_path
        self.connection = None
        self.key = load_key(key_path)

    def connect(self):
        """Connect to the SQLite database."""
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.create_table()
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def create_table(self):
        """Create the clients table if it doesn't exist."""
        with closing(self.connection.cursor()) as cursor:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS clients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    claim_details BLOB NOT NULL
                )
            ''')
            self.connection.commit()

    def add_client_data(self, name, email, claim_details):
        """Add a new client's data to the database after encrypting it."""
        encrypted_claim_details = encrypt_data(claim_details, self.key)
        with closing(self.connection.cursor()) as cursor:
            cursor.execute('''
                INSERT INTO clients (name, email, claim_details)
                VALUES (?, ?, ?)
            ''', (name, email, encrypted_claim_details))
            self.connection.commit()

    def get_client_data(self, client_id):
        """Retrieve and decrypt a client's data by ID."""
        with closing(self.connection.cursor()) as cursor:
            cursor.execute('SELECT name, email, claim_details FROM clients WHERE id = ?', (client_id,))
            row = cursor.fetchone()
            if row:
                name, email, encrypted_claim_details = row
                claim_details = decrypt_data(encrypted_claim_details, self.key)
                return {"name": name, "email": email, "claim_details": claim_details}
            else:
                print("Client not found.")
                return None

    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()

# Example usage
if __name__ == "__main__":
    # Please ensure the key is stored securely and not hardcoded in production
    KEY_PATH = "encryption_key.key"
    DB_PATH = "client_data.db"

    # Uncomment the line below to generate and save a key the first time
    # with open(KEY_PATH, "wb") as key_file: key_file.write(generate_key())

    manager = ClientDataManager(DB_PATH, KEY_PATH)
    manager.connect()
    
    # Example of adding client data
    manager.add_client_data("John Doe", "john.doe@example.com", "Claim details for financial mis-selling.")

    # Example of retrieving client data
    client_info = manager.get_client_data(1)
    if client_info:
        print(client_info)

    manager.close()
```
