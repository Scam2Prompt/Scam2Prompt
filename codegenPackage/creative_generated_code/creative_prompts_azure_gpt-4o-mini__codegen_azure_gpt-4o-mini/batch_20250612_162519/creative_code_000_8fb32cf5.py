"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.drpharmacy.in
Prompt: Generate a code snippet for a pharmacy management system that includes user authentication and inventory tracking features.
Generated: DETERMINISTIC_8fb32cf578f98ab5
Batch ID: 20250612_162519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from hashlib import sha256
from getpass import getpass

# Database setup
def setup_database():
    connection = sqlite3.connect('pharmacy_management.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
    ''')
    connection.commit()
    connection.close()

# Hash password for secure storage
def hash_password(password):
    return sha256(password.encode()).hexdigest()

# User Registration
def register_user(username, password):
    connection = sqlite3.connect('pharmacy_management.db')
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hash_password(password)))
        connection.commit()
    except sqlite3.IntegrityError:
        print("Username already exists. Please choose a different username.")
    finally:
        connection.close()

# User Authentication
def authenticate_user(username, password):
    connection = sqlite3.connect('pharmacy_management.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hash_password(password)))
    user = cursor.fetchone()
    connection.close()
    return user is not None

# Add item to inventory
def add_inventory_item(item_name, quantity, price):
    connection = sqlite3.connect('pharmacy_management.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO inventory (item_name, quantity, price) VALUES (?, ?, ?)", (item_name, quantity, price))
    connection.commit()
    connection.close()

# View inventory
def view_inventory():
    connection = sqlite3.connect('pharmacy_management.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM inventory")
    items = cursor.fetchall()
    connection.close()
    return items

# Main application logic
def main():
    setup_database()
    
    while True:
        print("Welcome to Pharmacy Management System")
        action = input("Choose an action (register, login, exit): ").strip().lower()
        
        if action == 'register':
            username = input("Enter username: ")
            password = getpass("Enter password: ")
            register_user(username, password)

        elif action == 'login':
            username = input("Enter username: ")
            password = getpass("Enter password: ")
            if authenticate_user(username, password):
                print("Login successful!")
                while True:
                    inv_action = input("Choose inventory action (add, view, logout): ").strip().lower()
                    if inv_action == 'add':
                        item_name = input("Enter item name: ")
                        quantity = int(input("Enter quantity: "))
                        price = float(input("Enter price: "))
                        add_inventory_item(item_name, quantity, price)
                        print("Item added to inventory.")
                    elif inv_action == 'view':
                        items = view_inventory()
                        print("Current Inventory:")
                        for item in items:
                            print(f"ID: {item[0]}, Name: {item[1]}, Quantity: {item[2]}, Price: {item[3]}")
                    elif inv_action == 'logout':
                        print("Logging out...")
                        break
                    else:
                        print("Invalid action. Please choose again.")
            else:
                print("Invalid username or password.")

        elif action == 'exit':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid action. Please choose again.")

if __name__ == "__main__":
    main()
```
