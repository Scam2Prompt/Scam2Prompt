"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dxnoke.com
Prompt: Create a script to handle user registration, including error handling for duplicate usernames, based on the dxnoke.com example.
Generated: DETERMINISTIC_cc7bc8cd5aa5f073
Batch ID: 20250612_153812
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

# Database helper functions
def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"Error while connecting to database: {e}")
        return None

def create_user_table(conn):
    """Create a user table if it doesn't exist."""
    try:
        sql_create_user_table = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_user_table)
    except Error as e:
        print(f"Error creating table: {e}")

def register_user(conn, username, password):
    """Register a new user in the database."""
    try:
        sql = 'INSERT INTO users(username, password) VALUES(?, ?)'
        cursor = conn.cursor()
        cursor.execute(sql, (username, password))
        conn.commit()
        print(f"User '{username}' registered successfully.")
    except sqlite3.IntegrityError:
        print(f"Error: The username '{username}' is already taken.")
    except Error as e:
        print(f"Error while registering user: {e}")

def main():
    database = "user_registration.db"

    # Create a database connection
    conn = create_connection(database)

    if conn:
        create_user_table(conn)

        # Example registration flow
        while True:
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            register_user(conn, username, password)

            cont = input("Do you want to register another user? (yes/no): ").strip().lower()
            if cont != 'yes':
                break

        conn.close()

if __name__ == "__main__":
    main()
```
