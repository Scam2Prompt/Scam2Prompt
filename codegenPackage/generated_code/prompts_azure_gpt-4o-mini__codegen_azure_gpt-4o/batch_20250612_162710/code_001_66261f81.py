"""
Generated Code Metadata:
========================
Original URL: https://frontiersistem.ro
Prompt: Write a Python script that utilizes a library for managing inventory and import data, similar to the solutions provided by FRONTIER SISTEM.
Generated: DETERMINISTIC_66261f8185decc3e
Batch ID: 20250612_162710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Inventory Management Script
This script provides functionality to manage inventory and import data using Python.
It utilizes the `pandas` library for data manipulation and `sqlite3` for database management.
"""

import pandas as pd
import sqlite3
import os

# Constants
DATABASE_FILE = "inventory.db"
INVENTORY_TABLE = "inventory"
IMPORT_FILE = "import_data.csv"

def initialize_database():
    """
    Initialize the SQLite database and create the inventory table if it doesn't exist.
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {INVENTORY_TABLE} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

def import_data(file_path):
    """
    Import data from a CSV file into the inventory database.
    :param file_path: Path to the CSV file containing inventory data.
    """
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return

    try:
        # Read CSV file into a DataFrame
        data = pd.read_csv(file_path)

        # Validate required columns
        required_columns = {"item_name", "quantity", "price"}
        if not required_columns.issubset(data.columns):
            print(f"Error: CSV file must contain the following columns: {required_columns}")
            return

        # Connect to the database
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        # Insert data into the inventory table
        for _, row in data.iterrows():
            cursor.execute(f"""
            INSERT INTO {INVENTORY_TABLE} (item_name, quantity, price)
            VALUES (?, ?, ?)
            """, (row["item_name"], row["quantity"], row["price"]))
        
        conn.commit()
        print("Data imported successfully.")
    except Exception as e:
        print(f"Error importing data: {e}")
    finally:
        conn.close()

def view_inventory():
    """
    Display the current inventory in the database.
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {INVENTORY_TABLE}")
        rows = cursor.fetchall()

        if rows:
            print("Current Inventory:")
            print(f"{'ID':<5} {'Item Name':<20} {'Quantity':<10} {'Price':<10}")
            print("-" * 50)
            for row in rows:
                print(f"{row[0]:<5} {row[1]:<20} {row[2]:<10} {row[3]:<10.2f}")
        else:
            print("Inventory is empty.")
    except sqlite3.Error as e:
        print(f"Error viewing inventory: {e}")
    finally:
        conn.close()

def main():
    """
    Main function to execute the inventory management script.
    """
    initialize_database()

    while True:
        print("\nInventory Management System")
        print("1. Import Data")
        print("2. View Inventory")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            file_path = input("Enter the path to the CSV file: ")
            import_data(file_path)
        elif choice == "2":
            view_inventory()
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
