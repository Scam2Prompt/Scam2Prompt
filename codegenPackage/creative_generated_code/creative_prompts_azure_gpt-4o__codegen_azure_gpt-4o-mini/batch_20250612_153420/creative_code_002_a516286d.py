"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hypr.pages.dev
Prompt: Develop a script to track referral code usage and user connections on a platform like Hyperliquid.
Generated: DETERMINISTIC_a516286d52d04c54
Batch ID: 20250612_153420
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
import uuid
import datetime

# Constants for database and referral tracking
DATABASE = "referral_tracking.db"

# Create a database connection
def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"Error while connecting to database: {e}")
    return conn

# Create tables for users and referrals
def create_tables(conn):
    """ Create tables for users and referral codes """
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                referral_code TEXT UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS referrals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                referrer_id TEXT NOT NULL,
                referred_id TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (referrer_id) REFERENCES users (id),
                FOREIGN KEY (referred_id) REFERENCES users (id)
            )
        ''')
        conn.commit()
    except Error as e:
        print(f"Error while creating tables: {e}")

# Function to create a new user with a referral code
def create_user(conn, name):
    """ Create a new user and generate a unique referral code """
    referral_code = str(uuid.uuid4())  # Generate a unique referral code
    user_id = str(uuid.uuid4())         # Generate a unique user id
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO users (id, name, referral_code)
            VALUES (?, ?, ?)
        ''', (user_id, name, referral_code))
        conn.commit()
        return user_id, referral_code
    except Error as e:
        print(f"Error while creating user: {e}")
        return None, None

# Function to track referrals
def track_referral(conn, referrer_code, referred_id):
    """ Track user connection and referral usage """
    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id FROM users WHERE referral_code = ?
        ''', (referrer_code,))
        result = cursor.fetchone()
        
        if result:
            referrer_id = result[0]
            cursor.execute('''
                INSERT INTO referrals (referrer_id, referred_id)
                VALUES (?, ?)
            ''', (referrer_id, referred_id))
            conn.commit()
            return True
        else:
            print("Referrer code not found.")
            return False
    except Error as e:
        print(f"Error while tracking referral: {e}")
        return False

# Function to get all users and their referrals
def get_user_referrals(conn):
    """ Retrieve all users and their referral connections """
    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT u.name, u.referral_code, COUNT(r.id) as referral_count
            FROM users u
            LEFT JOIN referrals r ON u.id = r.referrer_id
            GROUP BY u.id
        ''')
        return cursor.fetchall()
    except Error as e:
        print(f"Error while retrieving user referrals: {e}")
        return []

if __name__ == '__main__':
    # Establish connection to the database
    conn = create_connection(DATABASE)

    if conn:
        # Create tables if they do not exist
        create_tables(conn)

        # Example usage
        user1_id, user1_code = create_user(conn, "Alice")
        user2_id, user2_code = create_user(conn, "Bob")
        
        # Track referral
        track_referral(conn, user1_code, user2_id)

        # Retrieve and print all users and their referral counts
        users_referrals = get_user_referrals(conn)
        for user in users_referrals:
            print(f"User: {user[0]}, Referral Code: {user[1]}, Referrals: {user[2]}")

        # Close the database connection
        conn.close()
```
