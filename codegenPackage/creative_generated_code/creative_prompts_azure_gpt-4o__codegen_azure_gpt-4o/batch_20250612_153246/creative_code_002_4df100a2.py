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


class PetShopInventoryManagement:
    """
    A customer and inventory tracking system for a pet shop using SQLite.
    This system provides functionalities to manage customers and inventory.
    """

    def __init__(self):
        """
        Initializes the database connection and creates necessary tables.
        """
        self.conn = sqlite3.connect("petshop.db")
        self.cursor = self.conn.cursor()
        self._initialize_tables()

    def _initialize_tables(self):
        """
        Creates the required tables for the customer and inventory tracking system.
        """
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL UNIQUE,
                email TEXT UNIQUE,
                address TEXT
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS inventory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_name TEXT NOT NULL,
                description TEXT,
                quantity INTEGER NOT NULL CHECK(quantity >= 0),
                price REAL NOT NULL CHECK(price >= 0)
            )
        """)
        self.conn.commit()

    def add_customer(self, name, phone, email=None, address=None):
        """
        Adds a new customer to the database.
        :param name: Customer's name
        :param phone: Customer's phone number
        :param email: Customer's email address (optional)
        :param address: Customer's address (optional)
        """
        try:
            self.cursor.execute("""
                INSERT INTO customers (name, phone, email, address)
                VALUES (?, ?, ?, ?)
            """, (name, phone, email, address))
            self.conn.commit()
            print("Customer added successfully!")
        except sqlite3.IntegrityError as e:
            print(f"Error adding customer: {e}")

    def add_inventory_item(self, item_name, description, quantity, price):
        """
        Adds a new item to the inventory.
        :param item_name: Name of the item
        :param description: Description of the item
        :param quantity: Quantity of the item
        :param price: Price of the item
        """
        try:
            self.cursor.execute("""
                INSERT INTO inventory (item_name, description, quantity, price)
                VALUES (?, ?, ?, ?)
            """, (item_name, description, quantity, price))
            self.conn.commit()
            print("Inventory item added successfully!")
        except sqlite3.IntegrityError as e:
            print(f"Error adding inventory item: {e}")

    def update_inventory_quantity(self, item_id, new_quantity):
        """
        Updates the quantity of an inventory item.
        :param item_id: ID of the item
        :param new_quantity: New quantity value
        """
        try:
            self.cursor.execute("""
                UPDATE inventory
                SET quantity = ?
                WHERE id = ?
            """, (new_quantity, item_id))
            self.conn.commit()
            if self.cursor.rowcount > 0:
                print("Inventory updated successfully!")
            else:
                print("Item not found.")
        except sqlite3.Error as e:
            print(f"Error updating inventory: {e}")

    def list_customers(self):
        """
        Fetches and displays all customers from the database.
        """
        self.cursor.execute("SELECT * FROM customers")
        customers = self.cursor.fetchall()
        if customers:
            for customer in customers:
                print(customer)
        else:
            print("No customers found.")

    def list_inventory(self):
        """
        Fetches and displays all inventory items from the database.
        """
        self.cursor.execute("SELECT * FROM inventory")
        inventory = self.cursor.fetchall()
        if inventory:
            for item in inventory:
                print(item)
        else:
            print("No inventory items found.")

    def __del__(self):
        """
        Ensures the database connection is closed when the object is deleted.
        """
        self.conn.close()


# Example Usage
if __name__ == "__main__":
    system = PetShopInventoryManagement()

    # Adding sample customers
    system.add_customer("John Doe", "555-1234", "john.doe@example.com", "123 Elm Street")
    system.add_customer("Jane Smith", "555-5678", "jane.smith@example.com", "456 Oak Avenue")

    # Adding sample inventory items
    system.add_inventory_item("Dog Food", "Premium dry dog food", 50, 20.99)
    system.add_inventory_item("Cat Toy", "Interactive cat toy", 150, 5.49)

    # Listing all customers
    print("\nCustomers:")
    system.list_customers()

    # Listing all inventory items
    print("\nInventory:")
    system.list_inventory()

    # Updating inventory quantity
    system.update_inventory_quantity(1, 45)

    # Listing updated inventory
    print("\nUpdated Inventory:")
    system.list_inventory()
```

This Python code implements a customer and inventory tracking system using SQLite. It is well-commented, error-handled, and follows best practices to ensure clarity and maintainability.
