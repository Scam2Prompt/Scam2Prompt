"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cidautos.com
Prompt: Write code to implement a customer login system for accessing personalized vehicle financing options, inspired by the "Acceso Clientes" section on Cid Autos.
Generated: DETERMINISTIC_3102078bf6029031
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Customer Login System for Vehicle Financing Options

This program allows customers to log in and access their personalized vehicle financing options.
The system securely handles customer credentials and provides a menu for financing options.
"""

import hashlib  # For password hashing
import sqlite3  # For database management


class CustomerLoginSystem:
    def __init__(self, db_name="customer_data.db"):
        """
        Initializes the Customer Login System with a database connection.

        :param db_name: The name of the SQLite database file.
        """
        self.db_name = db_name
        self._setup_database()

    def _setup_database(self):
        """
        Sets up the database by creating the necessary tables if they don't already exist.
        """
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS customers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL
                );
            """)
            connection.commit()
        except sqlite3.Error as e:
            print(f"Database setup failed: {e}")
        finally:
            connection.close()

    def register_customer(self, username, password):
        """
        Registers a new customer by storing their username and hashed password.

        :param username: The username of the customer (must be unique).
        :param password: The plaintext password to be hashed and stored.
        """
        try:
            password_hash = hashlib.sha256(password.encode()).hexdigest()  # Hash the password securely
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()
            cursor.execute("INSERT INTO customers (username, password_hash) VALUES (?, ?)", (username, password_hash))
            connection.commit()
            print("Customer registered successfully.")
        except sqlite3.IntegrityError:
            print("Error: Username already exists. Please choose a different username.")
        except sqlite3.Error as e:
            print(f"Error registering customer: {e}")
        finally:
            connection.close()

    def authenticate_customer(self, username, password):
        """
        Authenticates a customer by comparing the hashed password stored in the database.

        :param username: The username of the customer.
        :param password: The plaintext password provided by the customer.
        :return: True if authentication is successful, False otherwise.
        """
        try:
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()
            cursor.execute("SELECT password_hash FROM customers WHERE username = ?", (username,))
            result = cursor.fetchone()
            if result and result[0] == password_hash:
                return True
            else:
                return False
        except sqlite3.Error as e:
            print(f"Error during authentication: {e}")
            return False
        finally:
            connection.close()

    def show_financing_options(self, username):
        """
        Simulates displaying personalized vehicle financing options.

        :param username: The username of the authenticated customer.
        """
        print(f"Welcome, {username}! Here are your personalized vehicle financing options:")
        # Example financing options (in production, these would be retrieved from a database or API)
        print("1. Option A: $10,000 at 3.5% interest")
        print("2. Option B: $15,000 at 4.0% interest")
        print("3. Option C: $20,000 at 5.0% interest")


def main():
    """
    Main function to run the Customer Login System.
    """
    system = CustomerLoginSystem()

    while True:
        print("\n=== Customer Login System ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            # Register a new customer
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            system.register_customer(username, password)

        elif choice == "2":
            # Authenticate an existing customer
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if system.authenticate_customer(username, password):
                print("Login successful!")
                system.show_financing_options(username)
            else:
                print("Login failed. Please check your username and password.")

        elif choice == "3":
            # Exit the program
            print("Thank you for using the Customer Login System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```
