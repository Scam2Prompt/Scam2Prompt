"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonanzavc.com
Prompt: Write a Python function to generate unique referral codes for users upon registration, ensuring the codes are securely stored in a database.
Generated: DETERMINISTIC_12fe9edc2bae3c1c
Batch ID: 20250612_154058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import string
import sqlite3
from sqlite3 import Error

# Database configuration
DATABASE = 'referral_codes.db'

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"Error creating database connection: {e}")
    return conn

def create_table(conn):
    """Create a table for storing referral codes if it does not exist."""
    try:
        sql_create_codes_table = """
        CREATE TABLE IF NOT EXISTS referral_codes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT NOT NULL UNIQUE,
            user_id INTEGER NOT NULL
        );"""
        cursor = conn.cursor()
        cursor.execute(sql_create_codes_table)
    except Error as e:
        print(f"Error creating table: {e}")

def generate_referral_code(length=8):
    """Generate a unique referral code."""
    characters = string.ascii_uppercase + string.digits
    while True:
        code = ''.join(random.choices(characters, k=length))
        yield code

def store_referral_code(conn, user_id, code):
    """Store the referral code in the database."""
    try:
        sql_insert_code = """INSERT INTO referral_codes (code, user_id)
                             VALUES (?, ?);"""
        cursor = conn.cursor()
        cursor.execute(sql_insert_code, (code, user_id))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Referral code {code} already exists. Generating a new one.")
        return False
    except Error as e:
        print(f"Error storing referral code: {e}")
        return False
    return True

def create_referral_code_for_user(user_id):
    """Generate and store a unique referral code for a new user."""
    conn = create_connection(DATABASE)
    if conn is None:
        return None

    create_table(conn)

    code_generator = generate_referral_code()
    while True:
        code = next(code_generator)
        if store_referral_code(conn, user_id, code):
            print(f"Generated referral code: {code} for user_id: {user_id}")
            break

    conn.close()
    return code

# Example usage (uncomment to run in a real scenario):
# user_id = 1  # Assume this is the new user's ID
# create_referral_code_for_user(user_id)
```
