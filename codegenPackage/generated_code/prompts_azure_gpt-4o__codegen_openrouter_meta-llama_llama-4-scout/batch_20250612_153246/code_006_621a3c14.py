"""
Generated Code Metadata:
========================
Original URL: https://aulaferretera.com
Prompt: Suggest tools or APIs to systematize operations in a hardware store, as described in "¿Cómo Abrir y Sistematizar tu Ferretería?" from Aula Ferretera.
Generated: DETERMINISTIC_621a3c1468da8eb9
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hardware_store_management.py

import sqlite3
from typing import Dict, List

class HardwareStore:
    def __init__(self, db_name: str):
        """
        Initialize the hardware store management system.

        Args:
        - db_name (str): The name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Create the necessary tables in the database.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT,
                price REAL NOT NULL,
                stock INTEGER NOT NULL DEFAULT 0
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY,
                customer_id INTEGER NOT NULL,
                product_id INTEGER NOT NULL,
                sale_date DATE NOT NULL,
                quantity INTEGER NOT NULL,
                total REAL NOT NULL,
                FOREIGN KEY (customer_id) REFERENCES customers (id),
                FOREIGN KEY (product_id) REFERENCES products (id)
            )
        ''')

        self.conn.commit()

    def add_product(self, product: Dict):
        """
        Add a new product to the database.

        Args:
        - product (Dict): A dictionary containing the product information.
        """
        try:
            self.cursor.execute('''
                INSERT INTO products (name, description, price, stock)
                VALUES (?, ?, ?, ?)
            ''', (product['name'], product['description'], product['price'], product['stock']))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding product: {e}")

    def add_customer(self, customer: Dict):
        """
        Add a new customer to the database.

        Args:
        - customer (Dict): A dictionary containing the customer information.
        """
        try:
            self.cursor.execute('''
                INSERT INTO customers (name, email, phone)
                VALUES (?, ?, ?)
            ''', (customer['name'], customer['email'], customer['phone']))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding customer: {e}")

    def record_sale(self, sale: Dict):
        """
        Record a new sale in the database.

        Args:
        - sale (Dict): A dictionary containing the sale information.
        """
        try:
            self.cursor.execute('''
                INSERT INTO sales (customer_id, product_id, sale_date, quantity, total)
                VALUES (?, ?, ?, ?, ?)
            ''', (sale['customer_id'], sale['product_id'], sale['sale_date'], sale['quantity'], sale['total']))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error recording sale: {e}")

    def get_products(self) -> List[Dict]:
        """
        Retrieve a list of all products in the database.

        Returns:
        - List[Dict]: A list of dictionaries containing the product information.
        """
        try:
            self.cursor.execute('SELECT * FROM products')
            rows = self.cursor.fetchall()
            return [{'id': row[0], 'name': row[1], 'description': row[2], 'price': row[3], 'stock': row[4]} for row in rows]
        except sqlite3.Error as e:
            print(f"Error retrieving products: {e}")
            return []

    def get_customers(self) -> List[Dict]:
        """
        Retrieve a list of all customers in the database.

        Returns:
        - List[Dict]: A list of dictionaries containing the customer information.
        """
        try:
            self.cursor.execute('SELECT * FROM customers')
            rows = self.cursor.fetchall()
            return [{'id': row[0], 'name': row[1], 'email': row[2], 'phone': row[3]} for row in rows]
        except sqlite3.Error as e:
            print(f"Error retrieving customers: {e}")
            return []

    def get_sales(self) -> List[Dict]:
        """
        Retrieve a list of all sales in the database.

        Returns:
        - List[Dict]: A list of dictionaries containing the sale information.
        """
        try:
            self.cursor.execute('SELECT * FROM sales')
            rows = self.cursor.fetchall()
            return [{'id': row[0], 'customer_id': row[1], 'product_id': row[2], 'sale_date': row[3], 'quantity': row[4], 'total': row[5]} for row in rows]
        except sqlite3.Error as e:
            print(f"Error retrieving sales: {e}")
            return []

def main():
    store = HardwareStore('hardware_store.db')

    # Add some products
    products = [
        {'name': 'Hammer', 'description': 'A hammer for driving nails', 'price': 10.99, 'stock': 10},
        {'name': 'Screwdriver', 'description': 'A screwdriver for driving screws', 'price': 5.99, 'stock': 20},
    ]
    for product in products:
        store.add_product(product)

    # Add some customers
    customers = [
        {'name': 'John Doe', 'email': 'john@example.com', 'phone': '123-456-7890'},
        {'name': 'Jane Doe', 'email': 'jane@example.com', 'phone': '987-654-3210'},
    ]
    for customer in customers:
        store.add_customer(customer)

    # Record some sales
    sales = [
        {'customer_id': 1, 'product_id': 1, 'sale_date': '2022-01-01', 'quantity': 2, 'total': 21.98},
        {'customer_id': 2, 'product_id': 2, 'sale_date': '2022-01-15', 'quantity': 3, 'total': 17.97},
    ]
    for sale in sales:
        store.record_sale(sale)

    # Retrieve and print the products, customers, and sales
    print("Products:")
    for product in store.get_products():
        print(product)

    print("\nCustomers:")
    for customer in store.get_customers():
        print(customer)

    print("\nSales:")
    for sale in store.get_sales():
        print(sale)

if __name__ == '__main__':
    main()
```
