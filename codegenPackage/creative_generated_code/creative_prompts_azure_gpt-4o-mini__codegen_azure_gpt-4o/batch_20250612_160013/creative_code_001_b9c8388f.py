"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://piaht.lol
Prompt: Write a code snippet for securely storing and validating activation keys in a card activation system.
Generated: DETERMINISTIC_b9c8388f0ac855f5
Batch ID: 20250612_160013
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import uuid
import sqlite3
from datetime import datetime, timedelta

# Database initialization
DATABASE_FILE = "activation_keys.db"

def initialize_database():
    """
    Initialize the database if it doesn't already exist.
    """
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS activation_keys (
            key TEXT PRIMARY KEY,
            hashed_key TEXT NOT NULL,
            expiration_date TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

initialize_database()


def generate_activation_key():
    """
    Generate a unique activation key and its hashed version.
    Returns a tuple: (activation_key, hashed_key).
    """
    activation_key = str(uuid.uuid4())
    hashed_key = hashlib.sha256(activation_key.encode()).hexdigest()
    return activation_key, hashed_key


def store_activation_key(hashed_key, validity_days=30):
    """
    Store the hashed activation key in the database with an expiration date.

    :param hashed_key: The hashed activation key to store.
    :param validity_days: Number of days the activation key should remain valid.
    """
    expiration_date = (datetime.now() + timedelta(days=validity_days)).strftime('%Y-%m-%d %H:%M:%S')
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO activation_keys (key, hashed_key, expiration_date) VALUES (?, ?, ?)", 
                       (hashed_key, hashed_key, expiration_date))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Error: Duplicate activation key.")
    finally:
        conn.close()


def validate_activation_key(activation_key):
    """
    Validate an activation key by checking its hash and expiration date.

    :param activation_key: The activation key to validate.
    :return: True if valid, False otherwise.
    """
    hashed_key = hashlib.sha256(activation_key.encode()).hexdigest()
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT expiration_date FROM activation_keys WHERE hashed_key = ?", (hashed_key,))
        result = cursor.fetchone()
        if result:
            expiration_date = datetime.strptime(result[0], '%Y-%m-%d %H:%M:%S')
            if expiration_date > datetime.now():
                return True
        return False
    finally:
        conn.close()


# Example Usage:
if __name__ == "__main__":
    # Generate a new activation key
    key, hashed = generate_activation_key()
    print("Generated Activation Key:", key)

    # Store the hashed key
    store_activation_key(hashed)

    # Validate the key
    is_valid = validate_activation_key(key)
    if is_valid:
        print("Key is valid and active.")
    else:
        print("Key is invalid or expired.")
```
