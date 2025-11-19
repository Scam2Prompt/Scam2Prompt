"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://purplebr.com
Prompt: How can I implement a referral program in my online gaming platform similar to DewaTogel's 15% extra bonus for inviting friends?
Generated: DETERMINISTIC_f9fd79594fa45588
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Referral Program Implementation for an Online Gaming Platform
Author: YourName
Date: YYYY-MM-DD
Description:
- This program implements a referral system where users receive a bonus (15% in this case)
  when they invite friends to join the platform and those friends make a deposit.
- This is a simplified implementation with database operations using SQLite for demonstration.
"""

import sqlite3
from decimal import Decimal

# Database setup
DB_NAME = "gaming_platform.db"

def setup_database():
    """
    Sets up the database schema for the referral program.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        referral_code TEXT UNIQUE,
        referred_by TEXT,
        balance DECIMAL DEFAULT 0
    );
    """)
    
    # Transactions table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        amount DECIMAL NOT NULL,
        type TEXT NOT NULL, -- 'deposit' or 'bonus'
        FOREIGN KEY (user_id) REFERENCES users (id)
    );
    """)
    
    conn.commit()
    conn.close()

setup_database()

# Referral system constants
BONUS_PERCENTAGE = Decimal("0.15")

# Functions
def generate_referral_code(username):
    """
    Generates a unique referral code for the user based on their username.
    """
    return f"REF-{username.upper()}"

def register_user(username, referred_by=None):
    """
    Registers a new user in the system. If referred_by is provided, links the user
    to the referrer.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        referral_code = generate_referral_code(username)
        cursor.execute("""
        INSERT INTO users (username, referral_code, referred_by) VALUES (?, ?, ?);
        """, (username, referral_code, referred_by))
        conn.commit()
        print(f"User '{username}' registered successfully. Referral Code: {referral_code}")
    except sqlite3.IntegrityError:
        print(f"Error: Username '{username}' or referral code already exists.")
    finally:
        conn.close()

def deposit(user_id, amount):
    """
    Processes a deposit for a user. If the user was referred by another user,
    awards the referrer a bonus.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        # Validate user ID
        cursor.execute("SELECT id, referred_by FROM users WHERE id = ?;", (user_id,))
        user = cursor.fetchone()
        if not user:
            print("Error: User not found.")
            return

        referred_by = user[1]

        # Update user's balance
        cursor.execute("UPDATE users SET balance = balance + ? WHERE id = ?;", (amount, user_id))
        
        # Record the deposit transaction
        cursor.execute("""
        INSERT INTO transactions (user_id, amount, type) VALUES (?, ?, ?);
        """, (user_id, amount, 'deposit'))
        
        # Award bonus to referrer
        if referred_by:
            cursor.execute("SELECT id FROM users WHERE referral_code = ?;", (referred_by,))
            referrer = cursor.fetchone()
            if referrer:
                referrer_id = referrer[0]
                bonus = amount * BONUS_PERCENTAGE
                cursor.execute("UPDATE users SET balance = balance + ? WHERE id = ?;", (bonus, referrer_id))
                cursor.execute("""
                INSERT INTO transactions (user_id, amount, type) VALUES (?, ?, ?);
                """, (referrer_id, bonus, 'bonus'))
                
                print(f"Bonus of {bonus} awarded to referrer (ID: {referrer_id}) for user {user_id}'s deposit.")
        
        conn.commit()
        print(f"Deposit of {amount} processed successfully for user (ID: {user_id}).")
    except Exception as e:
        print(f"Error during deposit: {e}")
    finally:
        conn.close()

def get_user_balance(user_id):
    """
    Retrieves the balance of a user.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT balance FROM users WHERE id = ?;", (user_id,))
        balance = cursor.fetchone()
        if balance:
            return Decimal(balance[0])
        else:
            print("Error: User not found.")
            return None
    finally:
        conn.close()

# Example Usage
if __name__ == "__main__":
    # Register users
    register_user("Alice")
    register_user("Bob", referred_by="REF-ALICE")
    
    # Process deposits
    deposit(1, Decimal("100"))
    deposit(2, Decimal("200"))
    
    # Check balances
    print("Alice's Balance:", get_user_balance(1))
    print("Bob's Balance:", get_user_balance(2))
```
