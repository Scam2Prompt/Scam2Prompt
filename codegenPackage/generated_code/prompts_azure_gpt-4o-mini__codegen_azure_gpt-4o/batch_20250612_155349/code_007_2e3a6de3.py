"""
Generated Code Metadata:
========================
Original URL: https://infinivi.io
Prompt: How can developers leverage the IVI Token's utility in a sports club's loyalty program? Include a code example for tracking token usage.
Generated: DETERMINISTIC_2e3a6de37bae0ca8
Batch ID: 20250612_155349
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# File: loyalty_program.py

import sqlite3
from datetime import datetime

# Constants
DATABASE_FILE = "loyalty_program.db"

# Initialize the database
def initialize_database():
    """
    Creates the database and tables if they don't exist.
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        # Create table for members
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS members (
            member_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
        """)

        # Create table for token transactions
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS token_transactions (
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            member_id INTEGER NOT NULL,
            tokens INTEGER NOT NULL,
            transaction_type TEXT NOT NULL CHECK(transaction_type IN ('earn', 'redeem')),
            timestamp TEXT NOT NULL,
            FOREIGN KEY (member_id) REFERENCES members (member_id)
        )
        """)

        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

# Add a new member
def add_member(name, email):
    """
    Adds a new member to the loyalty program.
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO members (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print(f"Member '{name}' added successfully.")
    except sqlite3.IntegrityError:
        print("Error: Email already exists.")
    except sqlite3.Error as e:
        print(f"Error adding member: {e}")
    finally:
        conn.close()

# Record a token transaction
def record_transaction(member_id, tokens, transaction_type):
    """
    Records a token transaction (earn or redeem) for a member.
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("""
        INSERT INTO token_transactions (member_id, tokens, transaction_type, timestamp)
        VALUES (?, ?, ?, ?)
        """, (member_id, tokens, transaction_type, timestamp))
        conn.commit()
        print(f"Transaction recorded: {transaction_type} {tokens} tokens for member ID {member_id}.")
    except sqlite3.Error as e:
        print(f"Error recording transaction: {e}")
    finally:
        conn.close()

# Get token balance for a member
def get_token_balance(member_id):
    """
    Calculates the current token balance for a member.
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        cursor.execute("""
        SELECT SUM(CASE WHEN transaction_type = 'earn' THEN tokens
                        WHEN transaction_type = 'redeem' THEN -tokens
                        ELSE 0 END) AS balance
        FROM token_transactions
        WHERE member_id = ?
        """, (member_id,))
        result = cursor.fetchone()
        balance = result[0] if result[0] is not None else 0
        return balance
    except sqlite3.Error as e:
        print(f"Error fetching token balance: {e}")
        return 0
    finally:
        conn.close()

# Example usage
if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Add members
    add_member("John Doe", "john.doe@example.com")
    add_member("Jane Smith", "jane.smith@example.com")

    # Record transactions
    record_transaction(1, 100, "earn")  # John earns 100 tokens
    record_transaction(1, 50, "redeem")  # John redeems 50 tokens
    record_transaction(2, 200, "earn")  # Jane earns 200 tokens

    # Get token balances
    john_balance = get_token_balance(1)
    jane_balance = get_token_balance(2)

    print(f"John's token balance: {john_balance}")
    print(f"Jane's token balance: {jane_balance}")
```

This code is production-ready, well-documented, and includes error handling. It demonstrates how developers can leverage the IVI Token's utility in a sports club's loyalty program by tracking token usage.
