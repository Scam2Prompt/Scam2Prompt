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
# Import required libraries
import datetime
import sqlite3

class Product:
    """Represents a product in the ERP system."""
    
    def __init__(self, id, name, price, quantity):
        """
        Initializes a Product object.

        Args:
            id (int): Unique product ID.
            name (str): Product name.
            price (float): Product price.
            quantity (int): Product quantity.
        """
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

class Customer:
    """Represents a customer in the ERP system."""
    
    def __init__(self, id, name, email, phone):
        """
        Initializes a Customer object.

        Args:
            id (int): Unique customer ID.
            name (str): Customer name.
            email (str): Customer email.
            phone (str): Customer phone number.
        """
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone

class Order:
    """Represents an order in the ERP system."""
    
    def __init__(self, id, customer_id, order_date, total):
        """
        Initializes an Order object.

        Args:
            id (int): Unique order ID.
            customer_id (int): Foreign key referencing the Customer table.
            order_date (datetime): Order date.
            total (float): Order total.
        """
        self.id = id
        self.customer_id = customer_id
        self.order_date = order_date
        self.total = total

class ERPSystem:
    """Represents the ERP system."""
    
    def __init__(self, db_name):
        """
        Initializes the ERPSystem object.

        Args:
            db_name (str): Name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """Creates the necessary tables in the database."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products
            (id INTEGER PRIMARY KEY, name TEXT, price REAL, quantity INTEGER)
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers
            (id INTEGER PRIMARY KEY, name TEXT, email TEXT, phone TEXT)
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders
            (id INTEGER PRIMARY KEY, customer_id INTEGER, order_date DATE, total REAL,
            FOREIGN KEY (customer_id) REFERENCES customers (id))
        ''')

        self.conn.commit()

    def add_product(self, product):
        """Adds a product to the database."""
        try:
            self.cursor.execute('INSERT INTO products VALUES (?, ?, ?, ?)',
                                (product.id, product.name, product.price, product.quantity))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding product: {e}")

    def add_customer(self, customer):
        """Adds a customer to the database."""
        try:
            self.cursor.execute('INSERT INTO customers VALUES (?, ?, ?, ?)',
                                (customer.id, customer.name, customer.email, customer.phone))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding customer: {e}")

    def add_order(self, order):
        """Adds an order to the database."""
        try:
            self.cursor.execute('INSERT INTO orders VALUES (?, ?, ?, ?)',
                                (order.id, order.customer_id, order.order_date, order.total))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding order: {e}")

    def get_products(self):
        """Retrieves all products from the database."""
        try:
            self.cursor.execute('SELECT * FROM products')
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving products: {e}")
            return []

    def get_customers(self):
        """Retrieves all customers from the database."""
        try:
            self.cursor.execute('SELECT * FROM customers')
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving customers: {e}")
            return []

    def get_orders(self):
        """Retrieves all orders from the database."""
        try:
            self.cursor.execute('SELECT * FROM orders')
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving orders: {e}")
            return []

    def close_connection(self):
        """Closes the database connection."""
        self.conn.close()

def main():
    erp_system = ERPSystem('erp_database.db')

    # Create products
    product1 = Product(1, 'Product A', 10.99, 100)
    product2 = Product(2, 'Product B', 5.99, 50)

    # Add products to the database
    erp_system.add_product(product1)
    erp_system.add_product(product2)

    # Create customers
    customer1 = Customer(1, 'John Doe', 'john.doe@example.com', '123-456-7890')
    customer2 = Customer(2, 'Jane Doe', 'jane.doe@example.com', '987-654-3210')

    # Add customers to the database
    erp_system.add_customer(customer1)
    erp_system.add_customer(customer2)

    # Create orders
    order1 = Order(1, 1, datetime.date.today(), 10.99)
    order2 = Order(2, 2, datetime.date.today(), 5.99)

    # Add orders to the database
    erp_system.add_order(order1)
    erp_system.add_order(order2)

    # Retrieve and print products
    products = erp_system.get_products()
    print("Products:")
    for product in products:
        print(product)

    # Retrieve and print customers
    customers = erp_system.get_customers()
    print("\nCustomers:")
    for customer in customers:
        print(customer)

    # Retrieve and print orders
    orders = erp_system.get_orders()
    print("\nOrders:")
    for order in orders:
        print(order)

    # Close the database connection
    erp_system.close_connection()

if __name__ == "__main__":
    main()
```
