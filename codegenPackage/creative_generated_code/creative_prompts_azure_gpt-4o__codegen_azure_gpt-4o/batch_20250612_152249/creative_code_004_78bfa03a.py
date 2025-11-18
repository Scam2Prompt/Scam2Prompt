"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://juridiskklinik.se
Prompt: Suggest tools or libraries to securely store sensitive client data for a law firm handling cases like domestic violence and immigration, as outlined on juridiskklinik.se.
Generated: DETERMINISTIC_78bfa03a329997ae
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a Python example showing how to securely store sensitive client data using encryption libraries. This code utilizes `cryptography` for encryption and `sqlite3` for database storage.

```python
import sqlite3
from cryptography.fernet import Fernet
import os

# Generate or load an encryption key
def get_encryption_key():
    """Generates or retrieves the encryption key from a secure location."""
    key_file = "encryption_key.key"
    if not os.path.exists(key_file):
        # Generate a new key if it doesn't exist
        key = Fernet.generate_key()
        with open(key_file, "wb") as key_out:
            key_out.write(key)
        return key
    else:
        # Read an existing key
        with open(key_file, "rb") as key_in:
            return key_in.read()

# Initialize encryption
encryption_key = get_encryption_key()
cipher_suite = Fernet(encryption_key)

# Database setup
DATABASE_NAME = "secure_client_data.db"

def initialize_database():
    """Creates a SQLite database to store encrypted sensitive client data."""
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    # Create a table (if not exists) with columns for encrypted data
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS client_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            encrypted_address BLOB NOT NULL,
            encrypted_phone BLOB NOT NULL,
            encrypted_notes BLOB NOT NULL
        );
    """)
    connection.commit()
    connection.close()

# Function to encrypt and store client data
def store_client_data(name: str, address: str, phone: str, notes: str):
    """Encrypts and stores client data securely in the database."""
    try:
        encrypted_address = cipher_suite.encrypt(address.encode())
        encrypted_phone = cipher_suite.encrypt(phone.encode())
        encrypted_notes = cipher_suite.encrypt(notes.encode())

        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO client_data (name, encrypted_address, encrypted_phone, encrypted_notes)
            VALUES (?, ?, ?, ?);
        """, (name, encrypted_address, encrypted_phone, encrypted_notes))
        connection.commit()
        connection.close()
        print("Data securely stored.")
    except Exception as e:
        print(f"Error storing client data: {e}")

# Function to decrypt and retrieve client data
def retrieve_client_data(client_id: int):
    """Decrypts and retrieves client data securely from the database."""
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()
        cursor.execute("SELECT name, encrypted_address, encrypted_phone, encrypted_notes FROM client_data WHERE id = ?", (client_id,))
        result = cursor.fetchone()
        connection.close()

        if result:
            name, encrypted_address, encrypted_phone, encrypted_notes = result
            decrypted_address = cipher_suite.decrypt(encrypted_address).decode()
            decrypted_phone = cipher_suite.decrypt(encrypted_phone).decode()
            decrypted_notes = cipher_suite.decrypt(encrypted_notes).decode()
            
            return {
                "name": name,
                "address": decrypted_address,
                "phone": decrypted_phone,
                "notes": decrypted_notes
            }
        else:
            print(f"No data found for client ID {client_id}.")
            return None
    except Exception as e:
        print(f"Error retrieving client data: {e}")

# Initialize database
initialize_database()

# Example usage
if __name__ == "__main__":
    # Store client data
    store_client_data("Jane Doe", "123 Secure St", "+123456789", "Sensitive notes about the case.")

    # Retrieve and display client data
    client_data = retrieve_client_data(1)
    if client_data:
        print("Retrieved client data:", client_data)
```

**Important Notes**:
- Ensure the encryption key (`encryption_key.key`) is stored securely, e.g., in a secure vault or environment variable, and not exposed publicly.
- Regularly back up and secure the SQLite database with proper access controls.
- Consider more advanced database solutions for production environments, such as PostgreSQL or MySQL, with encryption at rest and access control features.
