"""
Generated Code Metadata:
========================
Original URL: https://it-ledger.com
Prompt: How can a custom ledger solution be developed using Python, including any relevant frameworks or tools that might be utilized?
Generated: DETERMINISTIC_f4234436e47fcf39
Batch ID: 20250622_212859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Custom Ledger Solution in Python

This script implements a simple custom ledger system using Python. It allows users to add transactions,
view the ledger, and calculate the balance. The solution uses SQLite for data persistence and follows
best practices for clean, maintainable, and production-ready code.
"""

import sqlite3
from datetime import datetime

# Database setup
DB_NAME = "ledger.db"

def initialize_database():
    """
    Initializes the SQLite database and creates the transactions table if it doesn't exist.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                amount REAL NOT NULL,
                date TEXT NOT NULL
            )
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

def add_transaction(description, amount):
    """
    Adds a transaction to the ledger.

    Args:
        description (str): Description of the transaction.
        amount (float): Amount of the transaction (positive for income, negative for expense).
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO transactions (description, amount, date) VALUES (?, ?, ?)",
                       (description, amount, date))
        conn.commit()
        print("Transaction added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding transaction: {e}")
    finally:
        conn.close()

def view_ledger():
    """
    Displays all transactions in the ledger.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM transactions")
        transactions = cursor.fetchall()
        print("Ledger:")
        print("ID | Description | Amount | Date")
        print("-" * 40)
        for transaction in transactions:
            print(f"{transaction[0]} | {transaction[1]} | {transaction[2]} | {transaction[3]}")
    except sqlite3.Error as e:
        print(f"Error viewing ledger: {e}")
    finally:
        conn.close()

def calculate_balance():
    """
    Calculates the current balance based on all transactions.

    Returns:
        float: The current balance.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(amount) FROM transactions")
        balance = cursor.fetchone()[0]
        return balance if balance is not None else 0.0
    except sqlite3.Error as e:
        print(f"Error calculating balance: {e}")
        return 0.0
    finally:
        conn.close()

# Main function to demonstrate the ledger functionality
def main():
    """
    Main function to demonstrate the custom ledger solution.
    """
    initialize_database()

    while True:
        print("\nCustom Ledger System")
        print("1. Add Transaction")
        print("2. View Ledger")
        print("3. Calculate Balance")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter transaction description: ")
            try:
                amount = float(input("Enter transaction amount (positive for income, negative for expense): "))
                add_transaction(description, amount)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif choice == "2":
            view_ledger()
        elif choice == "3":
            balance = calculate_balance()
            print(f"Current Balance: {balance}")
        elif choice == "4":
            print("Exiting the ledger system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point for the script
if __name__ == "__main__":
    main()
```
