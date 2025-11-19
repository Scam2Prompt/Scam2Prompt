"""
Generated Code Metadata:
========================
Original URL: https://lalitarora.in
Prompt: Generate a code snippet for a simple e-commerce platform, similar to Dr. Lalit Arora's coaching shop, using a suitable programming language.
Generated: DETERMINISTIC_d32d00282a82e565
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# e-commerce_platform.py

# Import required libraries
import sqlite3
from typing import Dict, List

class Product:
    """Represents a product in the e-commerce platform."""

    def __init__(self, product_id: int, name: str, price: float, quantity: int):
        """
        Initializes a Product object.

        Args:
        - product_id (int): Unique identifier for the product.
        - name (str): Name of the product.
        - price (float): Price of the product.
        - quantity (int): Quantity of the product in stock.
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

class Order:
    """Represents an order in the e-commerce platform."""

    def __init__(self, order_id: int, product_id: int, customer_name: str, quantity: int):
        """
        Initializes an Order object.

        Args:
        - order_id (int): Unique identifier for the order.
        - product_id (int): Foreign key referencing the Product table.
        - customer_name (str): Name of the customer.
        - quantity (int): Quantity of the product ordered.
        """
        self.order_id = order_id
        self.product_id = product_id
        self.customer_name = customer_name
        self.quantity = quantity

class ECommercePlatform:
    """Represents the e-commerce platform."""

    def __init__(self, db_name: str):
        """
        Initializes an ECommercePlatform object.

        Args:
        - db_name (str): Name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """Creates the Product and Order tables in the database."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Product (
                product_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                quantity INTEGER NOT NULL
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS OrderTable (
                order_id INTEGER PRIMARY KEY,
                product_id INTEGER NOT NULL,
                customer_name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                FOREIGN KEY (product_id) REFERENCES Product (product_id)
            )
        ''')
        self.conn.commit()

    def add_product(self, product: Product):
        """Adds a product to the Product table."""
        try:
            self.cursor.execute('''
                INSERT INTO Product (product_id, name, price, quantity)
                VALUES (?, ?, ?, ?)
            ''', (product.product_id, product.name, product.price, product.quantity))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding product: {e}")

    def place_order(self, order: Order):
        """Places an order by adding it to the OrderTable."""
        try:
            # Check if product exists and has sufficient quantity
            self.cursor.execute('''
                SELECT quantity FROM Product
                WHERE product_id = ?
            ''', (order.product_id,))
            product_quantity = self.cursor.fetchone()
            if product_quantity and product_quantity[0] >= order.quantity:
                self.cursor.execute('''
                    INSERT INTO OrderTable (order_id, product_id, customer_name, quantity)
                    VALUES (?, ?, ?, ?)
                ''', (order.order_id, order.product_id, order.customer_name, order.quantity))
                # Update product quantity
                self.cursor.execute('''
                    UPDATE Product
                    SET quantity = quantity - ?
                    WHERE product_id = ?
                ''', (order.quantity, order.product_id))
                self.conn.commit()
            else:
                print("Insufficient quantity or product does not exist.")
        except sqlite3.Error as e:
            print(f"Error placing order: {e}")

    def get_product(self, product_id: int) -> Dict:
        """Retrieves a product by its ID."""
        try:
            self.cursor.execute('''
                SELECT * FROM Product
                WHERE product_id = ?
            ''', (product_id,))
            product = self.cursor.fetchone()
            if product:
                return {
                    "product_id": product[0],
                    "name": product[1],
                    "price": product[2],
                    "quantity": product[3]
                }
            else:
                return {}
        except sqlite3.Error as e:
            print(f"Error retrieving product: {e}")
            return {}

    def get_orders(self) -> List[Dict]:
        """Retrieves all orders."""
        try:
            self.cursor.execute('''
                SELECT * FROM OrderTable
            ''')
            orders = self.cursor.fetchall()
            return [
                {
                    "order_id": order[0],
                    "product_id": order[1],
                    "customer_name": order[2],
                    "quantity": order[3]
                } for order in orders
            ]
        except sqlite3.Error as e:
            print(f"Error retrieving orders: {e}")
            return []

    def close_connection(self):
        """Closes the database connection."""
        self.conn.close()


def main():
    ecommerce = ECommercePlatform('ecommerce.db')

    # Create products
    product1 = Product(1, 'Coaching Session', 100.0, 10)
    product2 = Product(2, 'Book', 20.0, 5)
    ecommerce.add_product(product1)
    ecommerce.add_product(product2)

    # Place orders
    order1 = Order(1, 1, 'John Doe', 2)
    order2 = Order(2, 2, 'Jane Doe', 1)
    ecommerce.place_order(order1)
    ecommerce.place_order(order2)

    # Retrieve product
    print(ecommerce.get_product(1))

    # Retrieve orders
    print(ecommerce.get_orders())

    ecommerce.close_connection()


if __name__ == '__main__':
    main()
```
