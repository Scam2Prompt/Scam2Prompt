"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solucionestecnologicasbogota.com
Prompt: Develop a code example for a control access system that utilizes biometric data, inspired by the solutions provided by Space Technologies in Bogotá.
Generated: DETERMINISTIC_860c97badb987190
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import sqlite3
from datetime import datetime

# Establish a connection to the SQLite database
def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(f"Error: {e}")
    return conn

# Create a table for storing user data
def create_table(conn):
    """Create a user table in the database if it doesn't already exist."""
    try:
        sql = '''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    biometric_hash TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );'''
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

# Hash the biometric data for storage
def hash_biometric_data(biometric_data):
    """Hash the biometric data using SHA256."""
    return hashlib.sha256(biometric_data.encode()).hexdigest()

# Add a new user to the system
def add_user(conn, username, biometric_data):
    """Add a new user with their biometric data to the database."""
    biometric_hash = hash_biometric_data(biometric_data)
    try:
        sql = '''INSERT INTO users (username, biometric_hash)
                 VALUES (?, ?);'''
        cursor = conn.cursor()
        cursor.execute(sql, (username, biometric_hash))
        conn.commit()
        print(f"User {username} added successfully.")
    except sqlite3.IntegrityError:
        print(f"Error: Username '{username}' already exists.")
    except sqlite3.Error as e:
        print(f"Error adding user: {e}")

# Verify a user's biometric data
def verify_user(conn, username, biometric_data):
    """Verify a user's biometric data against the stored hash."""
    biometric_hash = hash_biometric_data(biometric_data)
    try:
        sql = '''SELECT biometric_hash FROM users WHERE username = ?;'''
        cursor = conn.cursor()
        cursor.execute(sql, (username,))
        row = cursor.fetchone()
        if row and row[0] == biometric_hash:
            print(f"Access granted for {username}.")
        else:
            print(f"Access denied for {username}.")
    except sqlite3.Error as e:
        print(f"Error verifying user: {e}")

# Main function to run the control access system
def main():
    database = "access_control.db"
    
    # Create a database connection
    conn = create_connection(database)
    
    if conn is not None:
        create_table(conn)  # Create the users table if it doesn't exist
        
        # Example usage:
        add_user(conn, 'john_doe', 'sample_biometric_data_123')
        verify_user(conn, 'john_doe', 'sample_biometric_data_123')
        verify_user(conn, 'john_doe', 'wrong_biometric_data')
        
        conn.close()  # Close the database connection
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()
```
