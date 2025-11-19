"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://summar.com
Prompt: Describe how to set up a referral program for freight factoring using Summar Financial's guidelines and provide sample code for tracking referrals.
Generated: DETERMINISTIC_99f5393512e93196
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Referral Program for Freight Factoring
This script sets up a referral program to track referrals using Summar Financial's guidelines.
"""

import uuid  # To generate unique referral codes
import sqlite3  # For database operations
import logging  # For error logging

# Configure logging
logging.basicConfig(
    filename="referral_program.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Database setup
DB_FILE = "referral_program.db"

def setup_database():
    """
    Initializes the database and creates necessary tables.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Create the users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            )
        """)

        # Create the referrals table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS referrals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                referrer_id INTEGER NOT NULL,
                referral_code TEXT UNIQUE NOT NULL,
                referred_email TEXT UNIQUE NOT NULL,
                redeemed BOOLEAN DEFAULT 0,
                FOREIGN KEY (referrer_id) REFERENCES users (id)
            )
        """)

        conn.commit()
    except Exception as e:
        logging.error(f"Error setting up database: {e}")
    finally:
        conn.close()

def generate_referral_code():
    """
    Generates a unique referral code.
    """
    return str(uuid.uuid4())[:8]  # Shorten to 8 characters for simplicity

def register_user(name, email):
    """
    Registers a new user in the system.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        logging.info(f"User {name} registered successfully.")
    except sqlite3.IntegrityError:
        logging.error(f"Email {email} is already registered.")
    except Exception as e:
        logging.error(f"Error registering user: {e}")
    finally:
        conn.close()

def create_referral(referrer_email, referred_email):
    """
    Creates a referral entry in the system.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Get the referrer ID
        cursor.execute("SELECT id FROM users WHERE email = ?", (referrer_email,))
        referrer = cursor.fetchone()

        if not referrer:
            logging.error(f"Referrer email {referrer_email} not found.")
            return

        referral_code = generate_referral_code()

        # Insert referral entry
        cursor.execute("""
            INSERT INTO referrals (referrer_id, referral_code, referred_email) 
            VALUES (?, ?, ?)
        """, (referrer[0], referral_code, referred_email))

        conn.commit()
        logging.info(f"Referral created successfully for {referrer_email} with code {referral_code}.")
    except sqlite3.IntegrityError:
        logging.error(f"Referred email {referred_email} is already in the system.")
    except Exception as e:
        logging.error(f"Error creating referral: {e}")
    finally:
        conn.close()

def redeem_referral(referral_code):
    """
    Redeems a referral using the referral code.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Check and update the referral
        cursor.execute("""
            UPDATE referrals
            SET redeemed = 1
            WHERE referral_code = ? AND redeemed = 0
        """, (referral_code,))
        
        if cursor.rowcount == 0:
            logging.error(f"Invalid or already redeemed referral code: {referral_code}")
        else:
            conn.commit()
            logging.info(f"Referral code {referral_code} redeemed successfully.")
    except Exception as e:
        logging.error(f"Error redeeming referral code: {e}")
    finally:
        conn.close()

# Main Program Execution
if __name__ == "__main__":
    # Set up the database
    setup_database()

    # Example usage
    register_user("Alice Smith", "alice@example.com")
    register_user("Bob Johnson", "bob@example.com")
    create_referral("alice@example.com", "charlie@example.com")
    redeem_referral("abcd1234")  # Replace with actual generated referral code
```
