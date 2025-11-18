"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theecomarena.com
Prompt: Write code to implement a private label product listing and inventory management system for Amazon, following the automation strategies outlined by Ecom Arena.
Generated: DETERMINISTIC_3d6b4d721f81720d
Batch ID: 20250612_153224
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
from typing import List, Dict, Any

class InventoryManagementSystem:
    """
    A class to manage a private label product listing and inventory for Amazon.
    """

    def __init__(self, db_file: str):
        """
        Initializes the InventoryManagementSystem with a database connection.

        :param db_file: Path to the SQLite database file.
        """
        self.conn = self.create_connection(db_file)
        self.create_table()

    def create_connection(self, db_file: str) -> sqlite3.Connection:
        """
        Creates a database connection to the SQLite database specified by db_file.

        :param db_file: Path to the SQLite database file.
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_table(self):
        """
        Creates the products table if it does not exist.
        """
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            sku TEXT NOT NULL UNIQUE,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        );"""
        try:
            cursor = self.conn.cursor()
            cursor.execute(create_table_sql)
            print("Products table created.")
        except Error as e:
            print(f"Error creating table: {e}")

    def add_product(self, name: str, sku: str, quantity: int, price: float):
        """
        Adds a new product to the inventory.

        :param name: Name of the product.
        :param sku: Stock Keeping Unit of the product.
        :param quantity: Available quantity of the product.
        :param price: Price of the product.
        """
        insert_sql = """INSERT INTO products (name, sku, quantity, price) VALUES (?, ?, ?, ?)"""
        try:
            cursor = self.conn.cursor()
            cursor.execute(insert_sql, (name, sku, quantity, price))
            self.conn.commit()
            print(f"Product added: {name}, SKU: {sku}, Quantity: {quantity}, Price: {price}")
        except Error as e:
            print(f"Error adding product: {e}")

    def update_product(self, sku: str, quantity: int = None, price: float = None):
        """
        Updates an existing product's quantity and/or price.

        :param sku: Stock Keeping Unit of the product to update.
        :param quantity: New quantity of the product (optional).
        :param price: New price of the product (optional).
        """
        update_sql = "UPDATE products SET"
        parameters = []
        
        if quantity is not None:
            update_sql += " quantity = ?,"
            parameters.append(quantity)
        
        if price is not None:
            update_sql += " price = ?,"
            parameters.append(price)
        
        update_sql = update_sql.rstrip(',') + " WHERE sku = ?"
        parameters.append(sku)
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(update_sql, parameters)
            self.conn.commit()
            print(f"Product updated: SKU: {sku}, Quantity: {quantity}, Price: {price}")
        except Error as e:
            print(f"Error updating product: {e}")

    def list_products(self) -> List[Dict[str, Any]]:
        """
        Lists all products in the inventory.

        :return: A list of dictionaries representing each product.
        """
        select_sql = "SELECT * FROM products"
        products = []
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(select_sql)
            rows = cursor.fetchall()

            for row in rows:
                products.append({
                    "id": row[0],
                    "name": row[1],
                    "sku": row[2],
                    "quantity": row[3],
                    "price": row[4]
                })
            print("Products listed.")
        except Error as e:
            print(f"Error listing products: {e}")
        
        return products

    def close_connection(self):
        """
        Closes the database connection.
        """
        if self.conn:
            self.conn.close()
            print("Database connection closed.")


# Example usage
if __name__ == "__main__":
    db_path = "inventory.db"
    ims = InventoryManagementSystem(db_path)
    
    ims.add_product("Sample Product", "SP001", 50, 19.99)
    ims.update_product("SP001", quantity=45)
    products = ims.list_products()
    
    for product in products:
        print(product)
    
    ims.close_connection()
```
