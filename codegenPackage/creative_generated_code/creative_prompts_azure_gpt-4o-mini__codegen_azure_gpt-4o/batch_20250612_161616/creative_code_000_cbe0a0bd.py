"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itscool.srv.br
Prompt: How can I implement a cashless payment system for school meals similar to the NO CASH initiative described on the It's Cool website?
Generated: DETERMINISTIC_cbe0a0bd470358aa
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation of a cashless payment system for school meals:

```python
import sqlite3
from datetime import datetime

# Database setup
DB_NAME = "school_meals.db"

def initialize_database():
    """
    Initializes the SQLite database for the cashless payment system.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Create users table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            balance REAL NOT NULL DEFAULT 0.0
        )
        """)

        # Create transactions table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            transaction_type TEXT CHECK(transaction_type IN ('deposit', 'purchase')) NOT NULL,
            timestamp TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
        """)

        conn.commit()
    except Exception as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

# User management
def add_user(name, initial_balance=0.0):
    """
    Adds a new user to the database.
    
    :param name: Name of the user
    :param initial_balance: Initial balance for the user (default: 0.0)
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO users (name, balance) VALUES (?, ?)", (name, initial_balance))
        conn.commit()
        print(f"User '{name}' added successfully.")
    except Exception as e:
        print(f"Error adding user: {e}")
    finally:
        conn.close()

def get_user(user_id):
    """
    Retrieves user information by user ID.
    
    :param user_id: ID of the user to retrieve
    :return: User information as a dictionary or None if not found
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        user = cursor.fetchone()
        
        if user:
            return {"user_id": user[0], "name": user[1], "balance": user[2]}
        else:
            print(f"User with ID {user_id} not found.")
            return None
    except Exception as e:
        print(f"Error retrieving user: {e}")
    finally:
        conn.close()

# Payment and transaction system
def deposit_funds(user_id, amount):
    """
    Deposits funds into the user's account.
    
    :param user_id: ID of the user
    :param amount: Amount to deposit
    """
    if amount <= 0:
        print("Amount must be greater than 0.")
        return

    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Update user balance
        cursor.execute("UPDATE users SET balance = balance + ? WHERE user_id = ?", (amount, user_id))
        
        # Add to transactions table
        cursor.execute("""
        INSERT INTO transactions (user_id, amount, transaction_type, timestamp) 
        VALUES (?, ?, 'deposit', ?)
        """, (user_id, amount, datetime.now().isoformat()))
        
        conn.commit()
        print(f"Deposited ${amount:.2f} to user ID {user_id}.")
    except Exception as e:
        print(f"Error depositing funds: {e}")
    finally:
        conn.close()

def purchase_meal(user_id, price):
    """
    Processes a meal purchase for the user.
    
    :param user_id: ID of the user
    :param price: Price of the meal
    """
    if price <= 0:
        print("Price must be greater than 0.")
        return

    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Check user balance
        cursor.execute("SELECT balance FROM users WHERE user_id = ?", (user_id,))
        user = cursor.fetchone()
        
        if user and user[0] >= price:
            # Deduct the price and update balance
            cursor.execute("UPDATE users SET balance = balance - ? WHERE user_id = ?", (price, user_id))
            
            # Add to transactions table
            cursor.execute("""
            INSERT INTO transactions (user_id, amount, transaction_type, timestamp) 
            VALUES (?, ?, 'purchase', ?)
            """, (user_id, -price, datetime.now().isoformat()))
            
            conn.commit()
            print(f"Purchase successful. ${price:.2f} deducted from user ID {user_id}.")
        else:
            print("Insufficient balance or user not found.")
    except Exception as e:
        print(f"Error processing meal purchase: {e}")
    finally:
        conn.close()

# Transaction history
def get_transaction_history(user_id):
    """
    Retrieves the transaction history for a user.
    
    :param user_id: ID of the user
    :return: List of transactions
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM transactions WHERE user_id = ?", (user_id,))
        transactions = cursor.fetchall()
        
        return [
            {
                "transaction_id": t[0],
                "user_id": t[1],
                "amount": t[2],
                "transaction_type": t[3],
                "timestamp": t[4]
            }
            for t in transactions
        ]
    except Exception as e:
        print(f"Error retrieving transaction history: {e}")
        return []
    finally:
        conn.close()

# Example usage
if __name__ == "__main__":
    initialize_database()
    add_user("Alice", 10.0)
    add_user("Bob", 5.0)
    
    deposit_funds(1, 20.0)
    purchase_meal(1, 5.0)
    
    user = get_user(1)
    print(f"User info: {user}")
    
    history = get_transaction_history(1)
    print("Transaction history:")
    for transaction in history:
        print(transaction)
```

This code is designed to be clean, modular, and production-ready with error handling and comments provided where necessary. It uses SQLite to handle user data and transactions.
