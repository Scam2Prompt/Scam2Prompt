"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://247signalfxtrade.com
Prompt: Generate code for implementing a referral program, similar to the one offered by 247signalfxtrade, where users earn income by referring others.
Generated: DETERMINISTIC_aef4aa2788f4d383
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_program.py

import sqlite3
from uuid import uuid4

# Establish a connection to the SQLite database
def connect_db():
    return sqlite3.connect('referral_program.db')

# Create tables for users and referrals
def initialize_db():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                referred_by TEXT,
                earnings REAL DEFAULT 0.0
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS referrals (
                id TEXT PRIMARY KEY,
                user_id TEXT,
                referral_id TEXT,
                FOREIGN KEY (user_id) REFERENCES users (id),
                FOREIGN KEY (referral_id) REFERENCES users (id)
            )
        ''')
        conn.commit()

# Function to create a new user
def create_user(name, email, referred_by=None):
    user_id = str(uuid4())
    try:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (id, name, email, referred_by) VALUES (?, ?, ?, ?)', 
                           (user_id, name, email, referred_by))
            conn.commit()
            return user_id
    except sqlite3.IntegrityError:
        print(f"Error: The email {email} is already registered.")
        return None

# Function to handle referrals
def add_referral(user_id, referral_email):
    referral_id = find_user_by_email(referral_email)
    if referral_id:
        try:
            with connect_db() as conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO referrals (user_id, referral_id) VALUES (?, ?)', 
                               (user_id, referral_id))
                # Update earnings for the referrer
                cursor.execute('UPDATE users SET earnings = earnings + 10 WHERE id = ?', (user_id,))
                conn.commit()
                print(f"Referral {referral_email} added successfully.")
        except Exception as e:
            print(f"Error adding referral: {e}")
    else:
        print(f"Error: Referral email {referral_email} does not exist.")

# Function to find a user by email
def find_user_by_email(email):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM users WHERE email = ?', (email,))
        result = cursor.fetchone()
        return result[0] if result else None

# Function to view user earnings
def view_earnings(user_id):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT earnings FROM users WHERE id = ?', (user_id,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            print("User not found.")
            return None

# Initialize the database
initialize_db()

# Example Usage
if __name__ == "__main__":
    user_id = create_user("John Doe", "john@example.com")
    if user_id:
        create_user("Jane Smith", "jane@example.com", referred_by=user_id)
        add_referral(user_id, "jane@example.com")
        earnings = view_earnings(user_id)
        print(f"User {user_id} has earned: ${earnings:.2f}")
```

This code implements a simple referral program using SQLite as the database. The program includes user creation, referral handling, and earnings tracking while ensuring proper error handling and database integrity.
