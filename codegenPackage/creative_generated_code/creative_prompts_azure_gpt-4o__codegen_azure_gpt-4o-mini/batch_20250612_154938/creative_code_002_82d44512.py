"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://changelly.ws
Prompt: Generate code for a referral program system that tracks user referrals and calculates passive income based on exchange transactions, inspired by Changelly's referral program.
Generated: DETERMINISTIC_82d4451280fdb3c5
Batch ID: 20250612_154938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from decimal import Decimal

# Constants for commission percentages
REFERRAL_COMMISSION_PERCENTAGE = Decimal('0.05')  # 5% commission

# Database setup
def init_db():
    """Initialize the SQLite database and create necessary tables."""
    conn = sqlite3.connect('referral_program.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            referral_code TEXT UNIQUE NOT NULL,
            referred_by TEXT,
            balance DECIMAL(10, 2) DEFAULT 0.00
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            amount DECIMAL(10, 2),
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')
    conn.commit()
    conn.close()

# User registration with referral tracking
def register_user(username, referred_by=None):
    """Register a new user and assign them a unique referral code."""
    conn = sqlite3.connect('referral_program.db')
    cursor = conn.cursor()
    
    # Generate a unique referral code (using username for simplicity)
    referral_code = username.lower() + "_ref"

    try:
        cursor.execute('''
            INSERT INTO users (username, referral_code, referred_by)
            VALUES (?, ?, ?)
        ''', (username, referral_code, referred_by))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Error: Username or referral code already exists.")
    finally:
        conn.close()

# Record a transaction and calculate commission for referrals
def record_transaction(username, amount):
    """Record a transaction for a user and calculate commissions for referrals."""
    conn = sqlite3.connect('referral_program.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT id, referred_by FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    
    if user is None:
        print("Error: User not found.")
        conn.close()
        return

    user_id, referred_by = user
    try:
        # Insert transaction into the database
        cursor.execute('''
            INSERT INTO transactions (user_id, amount)
            VALUES (?, ?)
        ''', (user_id, amount))
        conn.commit()
        
        # Calculate referral commission
        if referred_by:
            cursor.execute('SELECT balance FROM users WHERE referral_code = ?', (referred_by,))
            referrer = cursor.fetchone()
            if referrer:
                referrer_balance = referrer[0]
                commission = amount * REFERRAL_COMMISSION_PERCENTAGE
                # Update referrer's balance
                cursor.execute('''
                    UPDATE users
                    SET balance = ?
                    WHERE referral_code = ?
                ''', (referrer_balance + commission, referred_by))
                conn.commit()
                
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

# Check user balance
def get_user_balance(username):
    """Return the balance of a user."""
    conn = sqlite3.connect('referral_program.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT balance FROM users WHERE username = ?', (username,))
    balance = cursor.fetchone()
    conn.close()
    
    if balance is not None:
        return balance[0]
    else:
        print("Error: User not found.")
        return None

# Initialize the database
if __name__ == "__main__":
    init_db()
```
