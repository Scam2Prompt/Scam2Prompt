"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brokereo.com
Prompt: Generate code to create a searchable database of closed accounts and refunded balances, based on the procedures described in Brokereo's Terms and Conditions.
Generated: DETERMINISTIC_acbd649f249abe30
Batch ID: 20250612_154111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

# Define the database name
DATABASE_NAME = "brokereo_accounts.db"

# Connect to the database (it will be created if it doesn't exist)
connection = sqlite3.connect(DATABASE_NAME)

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Create the `closed_accounts` table if it doesn't already exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS closed_accounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Unique identifier for each record
    account_number TEXT NOT NULL,          -- Account number
    account_holder_name TEXT NOT NULL,     -- Name of the account holder
    refunded_balance REAL NOT NULL,        -- Refunded balance amount
    closure_date TEXT NOT NULL             -- Date of account closure
)
""")

connection.commit()


def add_closed_account(account_number, account_holder_name, refunded_balance, closure_date):
    """
    Adds a record of a closed account to the database.

    :param account_number: The account number of the closed account.
    :param account_holder_name: The name of the account holder.
    :param refunded_balance: The balance refunded upon account closure.
    :param closure_date: The date the account was closed.
    """
    try:
        cursor.execute("""
        INSERT INTO closed_accounts (account_number, account_holder_name, refunded_balance, closure_date)
        VALUES (?, ?, ?, ?)
        """, (account_number, account_holder_name, refunded_balance, closure_date))
        connection.commit()
        print("Closed account added successfully!")
    except Exception as e:
        print(f"Error adding closed account: {e}")


def search_closed_accounts(query):
    """
    Searches for closed accounts based on a given query.

    :param query: The search query (searches account number and account holder name).
    :return: A list of matching records.
    """
    try:
        cursor.execute("""
        SELECT * FROM closed_accounts
        WHERE account_number LIKE ? OR account_holder_name LIKE ?
        """, (f"%{query}%", f"%{query}%"))
        results = cursor.fetchall()
        return results
    except Exception as e:
        print(f"Error searching closed accounts: {e}")
        return []


def display_results(results):
    """
    Displays the results of a search query in a readable format.

    :param results: The list of records to display.
    """
    if results:
        print("Search Results:")
        print("-" * 50)
        for row in results:
            print(f"ID: {row[0]}")
            print(f"Account Number: {row[1]}")
            print(f"Account Holder: {row[2]}")
            print(f"Refunded Balance: {row[3]}")
            print(f"Closure Date: {row[4]}")
            print("-" * 50)
    else:
        print("No matching records found.")


def main():
    """
    Main function that demonstrates the functionality of the database.
    """
    print("Welcome to the Brokereo Closed Accounts Database.")
    while True:
        print("\nMenu:")
        print("1. Add Closed Account")
        print("2. Search Closed Accounts")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            # Add a closed account
            account_number = input("Enter account number: ").strip()
            account_holder_name = input("Enter account holder name: ").strip()
            refunded_balance = float(input("Enter refunded balance: ").strip())
            closure_date = input("Enter closure date (YYYY-MM-DD): ").strip()
            add_closed_account(account_number, account_holder_name, refunded_balance, closure_date)

        elif choice == "2":
            # Search for closed accounts
            query = input("Enter search query (account number or account holder name): ").strip()
            results = search_closed_accounts(query)
            display_results(results)

        elif choice == "3":
            # Exit the program
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    try:
        main()
    finally:
        # Ensure database connection is closed properly
        connection.close()
```
