"""
Generated Code Metadata:
========================
Original URL: https://sistemabox.com.br
Prompt: "Write a Python code snippet to implement an ERP system for a small business using Sistemabox's LC SISTEMAS."
Generated: DETERMINISTIC_6ae374c7e6daf5bb
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from sqlite3 import Error

class ERPSystem:
    """A simple ERP system for managing a small business using SQLite."""

    def __init__(self, db_file):
        """Initialize the ERP system with a database connection."""
        self.connection = self.create_connection(db_file)

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
        """Create a table for storing products."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        );"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            print("Products table created successfully.")
        except Error as e:
            print(f"Error creating table: {e}")

    def add_product(self, name, price, quantity):
        """Add a new product to the database."""
        sql = '''INSERT INTO products(name, price, quantity) VALUES(?,?,?)'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (name, price, quantity))
            self.connection.commit()
            print(f"Product '{name}' added successfully.")
        except Error as e:
            print(f"Error adding product: {e}")

    def update_product(self, product_id, name, price, quantity):
        """Update an existing product in the database."""
        sql = '''UPDATE products SET name=?, price=?, quantity=? WHERE id=?'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (name, price, quantity, product_id))
            self.connection.commit()
            print(f"Product ID {product_id} updated successfully.")
        except Error as e:
            print(f"Error updating product: {e}")

    def delete_product(self, product_id):
        """Delete a product from the database."""
        sql = '''DELETE FROM products WHERE id=?'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (product_id,))
            self.connection.commit()
            print(f"Product ID {product_id} deleted successfully.")
        except Error as e:
            print(f"Error deleting product: {e}")

    def list_products(self):
        """List all products in the database."""
        sql = '''SELECT * FROM products'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            products = cursor.fetchall()
            for product in products:
                print(product)
        except Error as e:
            print(f"Error retrieving products: {e}")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    erp = ERPSystem("small_business_erp.db")
    erp.create_table()
    erp.add_product("Widget", 19.99, 100)
    erp.list_products()
    erp.update_product(1, "Widget", 17.99, 150)
    erp.list_products()
    erp.delete_product(1)
    erp.list_products()
    erp.close_connection()
```
