"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://innwallets.com
Prompt: Generate a Python script to onboard new customers through a simple flow using a centralized wallet aggregator platform, similar to the solution provided by InnWallets.
Generated: DETERMINISTIC_7213f426ab7003fe
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
customer_onboarding.py

This script handles the onboarding of new customers through a centralized wallet aggregator platform.
It includes user input validation, wallet creation, database storage, and error handling.

Dependencies:
- Python 3.x
- `sqlite3` for local database storage
"""

import sqlite3


class WalletAggregatorPlatform:
    def __init__(self):
        """
        Initialize the wallet aggregator platform by setting up
        the local SQLite database connection and creating required tables.
        """
        self.db_connection = sqlite3.connect("wallet_platform.db")
        self.cursor = self.db_connection.cursor()
        self._initialize_database()

    def _initialize_database(self):
        """
        Create a customers table in the database if it doesn't exist.
        """
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS customers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    wallet_id TEXT UNIQUE NOT NULL
                )
            """)
            self.db_connection.commit()
        except sqlite3.Error as e:
            print(f"Database initialization error: {e}")

    def create_customer(self, name, email):
        """
        Onboard a new customer by creating a wallet and storing their info 
        in the database.

        Args:
            name (str): The customer's name.
            email (str): The customer's unique email address.
        
        Returns:
            dict: Details of the created customer (id, name, email, wallet_id).
        """
        try:
            # Ensure name and email are valid
            if not name or not email:
                raise ValueError("Name and email must not be empty.")

            # Generate a wallet ID (simple UUID for demonstration purposes)
            wallet_id = f"WALLET-{hash(email) % 1000000}"

            # Insert the customer data into the database
            self.cursor.execute("""
                INSERT INTO customers (name, email, wallet_id)
                VALUES (?, ?, ?)
            """, (name, email, wallet_id))
            self.db_connection.commit()

            # Retrieve the inserted customer data
            customer_id = self.cursor.lastrowid
            return {"id": customer_id, "name": name, "email": email, "wallet_id": wallet_id}

        except sqlite3.IntegrityError:
            print("Error: Email or wallet ID already exists. Please use unique values.")
        except ValueError as ve:
            print(f"Validation Error: {ve}")
        except sqlite3.Error as e:
            print(f"Database Error: {e}")

        return None

    def close(self):
        """
        Close the database connection.
        """
        self.db_connection.close()


def main():
    """
    Main function to handle the user input flow for onboarding new customers.
    """
    print("Welcome to the Wallet Aggregator Platform!")
    platform = WalletAggregatorPlatform()

    try:
        while True:
            print("\n--- New Customer Onboarding ---")
            name = input("Enter customer name: ").strip()
            email = input("Enter customer email: ").strip()

            # Attempt to create the customer
            customer = platform.create_customer(name, email)
            if customer:
                print("\nCustomer successfully onboarded!")
                print(f"Customer Details: {customer}")
            else:
                print("Failed to onboard customer. Please try again.")

            # Check if user wants to process another customer
            another = input("\nDo you want to onboard another customer? (yes/no): ").strip().lower()
            if another != "yes":
                print("Exiting onboarding process.")
                break
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        platform.close()


if __name__ == "__main__":
    main()
```
