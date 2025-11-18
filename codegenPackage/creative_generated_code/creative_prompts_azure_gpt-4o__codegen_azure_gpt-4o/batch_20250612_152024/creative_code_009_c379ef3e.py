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
import bcrypt
from cryptography.fernet import Fernet
import sqlite3
import json

# Constants for encryption and database
DB_NAME = "client_data.db"
ENCRYPTION_KEY_FILE = "encryption_key.key"


# Generate or load an encryption key
def load_or_create_encryption_key():
    """Load or create an encryption key for securing sensitive data."""
    if not os.path.exists(ENCRYPTION_KEY_FILE):
        key = Fernet.generate_key()
        with open(ENCRYPTION_KEY_FILE, "wb") as key_file:
            key_file.write(key)
    else:
        with open(ENCRYPTION_KEY_FILE, "rb") as key_file:
            key = key_file.read()
    return Fernet(key)


# Initialize the encryption mechanism
fernet = load_or_create_encryption_key()


# Securely hash sensitive non-identifiable data like account number
def hash_data(data):
    """Hash data using bcrypt for secure storage."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(data.encode(), salt)


# Initialize SQLite database
def initialize_database():
    """Initialize the SQLite database to store client data."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            account_number_hash TEXT NOT NULL,
            sensitive_data_encrypted TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


# Securely store client data into the database
def store_client_data(name, email, phone, account_number, sensitive_data):
    """
    Store client data securely in the database.
    
    Args:
        name (str): Client's name.
        email (str): Client's email address.
        phone (str): Client's phone number.
        account_number (str): Client's account number.
        sensitive_data (dict): Additional sensitive client data.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Hash and encrypt sensitive data
        account_number_hash = hash_data(account_number).decode()
        sensitive_data_encrypted = fernet.encrypt(json.dumps(sensitive_data).encode()).decode()

        cursor.execute(
            """
            INSERT INTO clients (name, email, phone, account_number_hash, sensitive_data_encrypted)
            VALUES (?, ?, ?, ?, ?)
            """,
            (name, email, phone, account_number_hash, sensitive_data_encrypted),
        )
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")
    finally:
        conn.close()


# Retrieve client data securely
def retrieve_client_data(client_id):
    """
    Retrieve client data securely from the database.
    
    Args:
        client_id (int): The ID of the client to retrieve.
    
    Returns:
        dict: The client's data if found, or None if not found.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM clients WHERE id = ?", (client_id,))
        result = cursor.fetchone()

        if result:
            decrypted_sensitive_data = json.loads(fernet.decrypt(result[5].encode()).decode())
            return {
                "id": result[0],
                "name": result[1],
                "email": result[2],
                "phone": result[3],
                "sensitive_data": decrypted_sensitive_data,
            }
        else:
            print("Client not found.")
            return None
    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")
        return None
    finally:
        conn.close()


# Entry point for testing functionality
if __name__ == "__main__":
    initialize_database()

    # Example client data
    client_name = "John Doe"
    client_email = "johndoe@example.com"
    client_phone = "123-456-7890"
    client_account_number = "987654321"
    client_sensitive_data = {
        "claim_details": "Mis-sold PPI insurance",
        "claim_amount": 1500.0,
        "status": "Pending",
    }

    # Store client data
    store_client_data(client_name, client_email, client_phone, client_account_number, client_sensitive_data)

    # Retrieve client data
    client_id = 1  # Assuming the first client stored
    retrieved_data = retrieve_client_data(client_id)
    if retrieved_data:
        print(retrieved_data)
```
