"""
Generated Code Metadata:
========================
Original URL: https://kraken-crypto.yivesites.com
Prompt: Design a database schema to store product information, customer data, and order details for an e-commerce website like Apelbet, considering factors such as scalability and data security.
Generated: DETERMINISTIC_088018baacd65faf
Batch ID: 20250622_205335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for e-commerce website
CREATE DATABASE apelbet_ecommerce;

-- Use the database
USE apelbet_ecommerce;

-- Create table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  product_name VARCHAR(255) NOT NULL,
  product_description TEXT,
  product_price DECIMAL(10, 2) NOT NULL,
  product_image_url VARCHAR(255),
  product_category VARCHAR(100) NOT NULL,
  product_subcategory VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id)
);

-- Create table for customers
CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  phone_number VARCHAR(20),
  address_line_1 VARCHAR(255) NOT NULL,
  address_line_2 VARCHAR(255),
  city VARCHAR(100) NOT NULL,
  state VARCHAR(100) NOT NULL,
  postal_code VARCHAR(20) NOT NULL,
  country VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (customer_id)
);

-- Create table for orders
CREATE TABLE orders (
  order_id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  total_cost DECIMAL(10, 2) NOT NULL,
  order_status VARCHAR(50) NOT NULL DEFAULT 'pending',
  payment_method VARCHAR(100) NOT NULL,
  payment_date TIMESTAMP,
  PRIMARY KEY (order_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

-- Create table for order items
CREATE TABLE order_items (
  order_item_id INT AUTO_INCREMENT,
  order_id INT NOT NULL,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  unit_price DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (order_item_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create table for payments
CREATE TABLE payments (
  payment_id INT AUTO_INCREMENT,
  order_id INT NOT NULL,
  payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  payment_amount DECIMAL(10, 2) NOT NULL,
  payment_method VARCHAR(100) NOT NULL,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_orders_customer_id ON orders (customer_id);
CREATE INDEX idx_order_items_order_id ON order_items (order_id);
CREATE INDEX idx_order_items_product_id ON order_items (product_id);
CREATE INDEX idx_payments_order_id ON payments (order_id);

-- Create views for easier data retrieval
CREATE VIEW customer_order_summary AS
SELECT 
  c.customer_id,
  c.first_name,
  c.last_name,
  o.order_id,
  o.order_date,
  o.total_cost
FROM 
  customers c
  JOIN orders o ON c.customer_id = o.customer_id;

CREATE VIEW product_sales_summary AS
SELECT 
  p.product_id,
  p.product_name,
  SUM(oi.quantity) AS total_quantity_sold,
  SUM(oi.quantity * oi.unit_price) AS total_revenue
FROM 
  products p
  JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY 
  p.product_id, p.product_name;
```

```python
import mysql.connector
from mysql.connector import Error

class DatabaseConnector:
    def __init__(self, host_name, db_name, user_name, user_password):
        self.host_name = host_name
        self.db_name = db_name
        self.user_name = user_name
        self.user_password = user_password
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host_name,
                database=self.db_name,
                user=self.user_name,
                password=self.user_password
            )
            print("Connection to database established")
        except Error as e:
            print(f"Error: '{e}'")

    def execute_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"Error: '{e}'")

    def read_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"Error: '{e}'")

# Example usage
if __name__ == "__main__":
    db_connector = DatabaseConnector(
        host_name="localhost",
        db_name="apelbet_ecommerce",
        user_name="your_username",
        user_password="your_password"
    )
    db_connector.connect()

    # Create tables
    with open("database_schema.sql", "r") as f:
        queries = f.read().split(";")
        for query in queries:
            if query.strip():
                db_connector.execute_query(query)

    # Insert sample data
    insert_product_query = """
        INSERT INTO products (product_name, product_description, product_price)
        VALUES ('Sample Product', 'This is a sample product', 19.99)
    """
    db_connector.execute_query(insert_product_query)

    # Retrieve data
    retrieve_product_query = "SELECT * FROM products"
    products = db_connector.read_query(retrieve_product_query)
    for product in products:
        print(product)
```
