"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demirsoft.com
Prompt: Generate code to create a customer and inventory tracking system using DemirSoft's "PetShop ve Veteriner SMS Müşteri ve Stok Takip Programı."
Generated: DETERMINISTIC_4df100a249e7c0db
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from sqlite3 import Error

class Database:
    """Database class to handle SQLite database connection and operations."""
    
    def __init__(self, db_file):
        """Initialize the Database object with the database file."""
        self.connection = None
        try:
            self.connection = sqlite3.connect(db_file)
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"Error '{e}' occurred during database connection")

    def disconnect(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Disconnected from SQLite DB")

class Customer:
    """Customer class to manage customer data."""
    
    def __init__(self, db):
        self.db = db

    def create_customer(self, name, phone):
        """Create a new customer in the database."""
        cursor = self.db.connection.cursor()
        try:
            cursor.execute("INSERT INTO customers (name, phone) VALUES (?, ?)", (name, phone))
            self.db.connection.commit()
            print(f"Customer {name} created successfully")
        except Error as e:
            print(f"Error '{e}' occurred while creating customer")

class Inventory:
    """Inventory class to manage inventory items."""
    
    def __init__(self, db):
        self.db = db

    def add_item(self, item_name, quantity):
        """Add a new item to the inventory."""
        cursor = self.db.connection.cursor()
        try:
            cursor.execute("INSERT INTO inventory (item_name, quantity) VALUES (?, ?)", (item_name, quantity))
            self.db.connection.commit()
            print(f"Item {item_name} added to inventory successfully")
        except Error as e:
            print(f"Error '{e}' occurred while adding inventory item")

def main():
    """Main function to run the customer and inventory tracking system."""
    db = Database("petshop_veterinary.db")

    # Create tables if they do not exist
    cursor = db.connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL
    );
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT NOT NULL,
        quantity INTEGER NOT NULL
    );
    """)

    # Create customer and inventory management instances
    customer_manager = Customer(db)
    inventory_manager = Inventory(db)

    # Example usage
    customer_manager.create_customer("John Doe", "123-456-7890")
    inventory_manager.add_item("Dog Food", 50)

    # Close the database connection
    db.disconnect()

if __name__ == "__main__":
    main()
```
