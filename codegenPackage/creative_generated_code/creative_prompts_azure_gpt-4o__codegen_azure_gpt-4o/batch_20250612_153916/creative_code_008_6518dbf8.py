"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gominings.net
Prompt: Generate a step-by-step guide for building a referral program similar to GoMining's, including code snippets for tracking referrals and calculating rewards.
Generated: DETERMINISTIC_6518dbf81a39d9d2
Batch ID: 20250612_153916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code for a referral program written in Python. It uses a simple database schema simulation with SQLite to track referrals and calculate rewards.

```python
import sqlite3
from datetime import datetime

# Step 1: Initialize the database
def initialize_database():
    conn = sqlite3.connect('referral_program.db')
    cursor = conn.cursor()

    # Create tables for users and referrals
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS referrals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            referrer_id INTEGER NOT NULL,
            referee_id INTEGER NOT NULL,
            reward REAL DEFAULT 0.0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (referrer_id) REFERENCES users (id),
            FOREIGN KEY (referee_id) REFERENCES users (id)
        )
    ''')
    conn.commit()
    conn.close()

# Step 2: Add a new user
def add_user(name, email):
    try:
        conn = sqlite3.connect('referral_program.db')
        cursor = conn.cursor()

        cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
        conn.commit()
        user_id = cursor.lastrowid
        conn.close()

        return user_id
    except sqlite3.IntegrityError:
        print("Error: Email already exists.")
        return None

# Step 3: Record a referral
def record_referral(referrer_email, referee_name, referee_email):
    try:
        conn = sqlite3.connect('referral_program.db')
        cursor = conn.cursor()

        # Get referrer ID
        cursor.execute('SELECT id FROM users WHERE email = ?', (referrer_email,))
        referrer = cursor.fetchone()

        if referrer is None:
            print("Error: Referrer does not exist.")
            conn.close()
            return

        referrer_id = referrer[0]

        # Add referee to the users table
        referee_id = add_user(referee_name, referee_email)

        if referee_id is None:
            conn.close()
            return

        # Create the referral entry
        cursor.execute('INSERT INTO referrals (referrer_id, referee_id, reward) VALUES (?, ?, ?)', (referrer_id, referee_id, 0.0))
        conn.commit()
        conn.close()

        print(f"Referral recorded: {referrer_email} referred {referee_email}.")
    except Exception as e:
        print(f"Error recording referral: {e}")

# Step 4: Calculate rewards for referrals
def calculate_rewards(referrer_email, reward_amount):
    try:
        conn = sqlite3.connect('referral_program.db')
        cursor = conn.cursor()

        # Get referrer ID
        cursor.execute('SELECT id FROM users WHERE email = ?', (referrer_email,))
        referrer = cursor.fetchone()

        if referrer is None:
            print("Error: Referrer does not exist.")
            conn.close()
            return

        referrer_id = referrer[0]

        # Update rewards for all referees referred by the referrer
        cursor.execute('''
            UPDATE referrals
            SET reward = reward + ?
            WHERE referrer_id = ?
        ''', (reward_amount, referrer_id))

        conn.commit()

        # Fetch updated reward details
        cursor.execute('SELECT referee_id, reward FROM referrals WHERE referrer_id = ?', (referrer_id,))
        reward_data = cursor.fetchall()

        conn.close()

        print(f"Rewards updated for {referrer_email}:")
        for referee_id, reward in reward_data:
            print(f"  Referee ID: {referee_id}, Reward: {reward:.2f}")

    except Exception as e:
        print(f"Error calculating rewards: {e}")

# Step 5: Retrieve referral details
def get_referral_details(referrer_email):
    try:
        conn = sqlite3.connect('referral_program.db')
        cursor = conn.cursor()

        # Get referrer ID
        cursor.execute('SELECT id FROM users WHERE email = ?', (referrer_email,))
        referrer = cursor.fetchone()

        if referrer is None:
            print("Error: Referrer does not exist.")
            conn.close()
            return

        referrer_id = referrer[0]

        # Fetch referral details
        cursor.execute('''
            SELECT u.name, u.email, r.reward
            FROM referrals r
            JOIN users u ON r.referee_id = u.id
            WHERE r.referrer_id = ?
        ''', (referrer_id,))
        referrals = cursor.fetchall()

        conn.close()

        print(f"Referral details for {referrer_email}:")
        for name, email, reward in referrals:
            print(f"  Referee Name: {name}, Email: {email}, Reward: {reward:.2f}")

    except Exception as e:
        print(f"Error retrieving referral details: {e}")

# Main execution and testing
if __name__ == "__main__":
    initialize_database()

    # Add users and record referrals
    add_user("Alice", "alice@example.com")
    add_user("Bob", "bob@example.com")
    record_referral("alice@example.com", "Charlie", "charlie@example.com")
    record_referral("alice@example.com", "Dave", "dave@example.com")

    # Calculate rewards
    calculate_rewards("alice@example.com", 10.0)

    # Fetch referral details
    get_referral_details("alice@example.com")
```

This code defines the core functionality of a referral program, including user management, referral tracking, reward calculation, and referral detail retrieval. It follows Python best practices and includes error handling.
