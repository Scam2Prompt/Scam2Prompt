"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medurex.com
Prompt: Generate a Python script that manages clinical trial data, ensuring data integrity and security, similar to the data management techniques mentioned on Medurex's website.
Generated: DETERMINISTIC_aa60ccb9cbf9d2a5
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from sqlite3 import Error
from cryptography.fernet import Fernet
import os

# Constants
DB_FILE = "clinical_trial.db"
ENCRYPTION_KEY_FILE = "secret.key"

# Generate or load encryption key
def load_or_create_key():
    if not os.path.exists(ENCRYPTION_KEY_FILE):
        key = Fernet.generate_key()
        with open(ENCRYPTION_KEY_FILE, 'wb') as key_file:
            key_file.write(key)
    else:
        with open(ENCRYPTION_KEY_FILE, 'rb') as key_file:
            key = key_file.read()
    return key

ENCRYPTION_KEY = load_or_create_key()
CIPHER = Fernet(ENCRYPTION_KEY)

# Initialize database
def init_db():
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        # Create table if not exists
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clinical_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                participant_id TEXT NOT NULL,
                encrypted_data TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()
    except Error as e:
        print(f"Error initializing database: {e}")

# Add clinical trial data securely
def add_clinical_data(participant_id, sensitive_data):
    try:
        encrypted_data = CIPHER.encrypt(sensitive_data.encode())
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clinical_data (participant_id, encrypted_data) VALUES (?, ?)", 
                       (participant_id, encrypted_data.decode()))
        conn.commit()
        conn.close()
        print("Data added successfully.")
    except Error as e:
        print(f"Error adding clinical data: {e}")

# Retrieve clinical trial data securely
def get_clinical_data(participant_id):
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT encrypted_data FROM clinical_data WHERE participant_id = ?", (participant_id,))
        result = cursor.fetchone()
        conn.close()
        
        if result:
            encrypted_data = result[0]
            decrypted_data = CIPHER.decrypt(encrypted_data.encode()).decode()
            return decrypted_data
        else:
            print("No data found for the given participant ID.")
            return None
    except Error as e:
        print(f"Error retrieving clinical data: {e}")
        return None

# Main function for testing
def main():
    # Initialize database
    init_db()

    # Example operations
    participant_id = "P12345"
    sensitive_data = "Blood Pressure: 120/80, Heart Rate: 72"

    # Add clinical data
    add_clinical_data(participant_id, sensitive_data)

    # Retrieve clinical data
    retrieved_data = get_clinical_data(participant_id)
    if retrieved_data:
        print("Retrieved clinical data:", retrieved_data)

if __name__ == "__main__":
    main()
```
