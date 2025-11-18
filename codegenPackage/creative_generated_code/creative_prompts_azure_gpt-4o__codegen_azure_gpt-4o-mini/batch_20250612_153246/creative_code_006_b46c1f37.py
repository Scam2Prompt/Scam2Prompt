"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demirsoft.com
Prompt: Create a program to manage sales and stock data for a hardware store using DemirSoft's "Hırdavat Yapı Market Barkodlu Satış Programı."
Generated: DETERMINISTIC_b46c1f37674ef30a
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

class HardwareStoreDB:
    """
    This class manages the database for the hardware store sales and stock data.
    It provides methods to create, read, update and delete records.
    """
    
    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)
        self.create_table()

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_table(self):
        """Create sales and stock tables if they do not exist."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS stock (
                    id INTEGER PRIMARY KEY,
                    product_name TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    price REAL NOT NULL
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS sales (
                    id INTEGER PRIMARY KEY,
                    product_id INTEGER NOT NULL,
                    quantity INTEGER NOT NULL,
                    sale_date TEXT NOT NULL,
                    FOREIGN KEY (product_id) REFERENCES stock (id)
                )
            ''')
            self.connection.commit()
            print("Tables created successfully.")
        except Error as e:
            print(f"Error creating tables: {e}")

    def add_product(self, product_name, quantity, price):
        """Add a new product to the stock."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO stock (product_name, quantity, price)
                VALUES (?, ?, ?)
            ''', (product_name, quantity, price))
            self.connection.commit()
            print("Product added successfully.")
        except Error as e:
            print(f"Error adding product: {e}")

    def sell_product(self, product_id, quantity):
        """Record a sale of a product."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('SELECT quantity FROM stock WHERE id = ?', (product_id,))
            current_quantity = cursor.fetchone()
            
            if current_quantity and current_quantity[0] >= quantity:
                # Update stock quantity
                cursor.execute('''
                    UPDATE stock
                    SET quantity = quantity - ?
                    WHERE id = ?
                ''', (quantity, product_id))
                
                # Record the sale
                cursor.execute('''
                    INSERT INTO sales (product_id, quantity, sale_date)
                    VALUES (?, ?, DATE('now'))
                ''', (product_id, quantity))
                
                self.connection.commit()
                print("Sale recorded successfully.")
            else:
                print("Insufficient stock for this sale.")
        except Error as e:
            print(f"Error recording sale: {e}")

    def get_stock(self):
        """Retrieve all stock items."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM stock')
            items = cursor.fetchall()
            return items
        except Error as e:
            print(f"Error fetching stock: {e}")
            return []

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example Usage
if __name__ == "__main__":
    # Initialize the database
    db = HardwareStoreDB("hardware_store.db")

    # Add products
    db.add_product("Hammer", 50, 12.99)
    db.add_product("Nails", 200, 0.10)
    
    # Sell a product
    db.sell_product(1, 5)  # Selling 5 Hammers

    # Get and print stock
    stock_items = db.get_stock()
    print("Current Stock:")
    for item in stock_items:
        print(item)

    # Close the database connection
    db.close_connection()
```
