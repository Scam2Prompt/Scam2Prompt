"""
Generated Code Metadata:
========================
Original URL: https://aceitescondadoloma.com
Prompt: Develop a simple database schema to store information about olive oil products, customers, and export orders for a company like Aceites Condado Loma, focusing on efficient data retrieval and reporting.
Generated: DETERMINISTIC_edc1a47df204eb69
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database
CREATE DATABASE olive_oil_company;

-- Use database
USE olive_oil_company;

-- Create table for olive oil products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  product_name VARCHAR(255) NOT NULL,
  product_description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  quantity_in_stock INT NOT NULL DEFAULT 0,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id)
);

-- Create table for customers
CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (customer_id)
);

-- Create table for export orders
CREATE TABLE export_orders (
  order_id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  order_date DATE NOT NULL,
  total_cost DECIMAL(10, 2) NOT NULL,
  status ENUM('pending', 'shipped', 'delivered', 'cancelled') NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
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
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (order_item_id),
  FOREIGN KEY (order_id) REFERENCES export_orders(order_id) ON DELETE CASCADE,
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create view for order summaries
CREATE VIEW order_summaries AS
SELECT 
  eo.order_id,
  c.customer_id,
  c.first_name,
  c.last_name,
  eo.order_date,
  eo.total_cost,
  eo.status
FROM 
  export_orders eo
  JOIN customers c ON eo.customer_id = c.customer_id;

-- Create view for product inventory levels
CREATE VIEW product_inventory_levels AS
SELECT 
  p.product_id,
  p.product_name,
  p.quantity_in_stock
FROM 
  products p;

-- Create stored procedure to place an order
DELIMITER //
CREATE PROCEDURE place_order(
  IN customer_id INT,
  IN product_id INT,
  IN quantity INT
)
BEGIN
  DECLARE product_price DECIMAL(10, 2);
  DECLARE total_cost DECIMAL(10, 2);
  DECLARE stock INT;

  -- Check if product exists and has sufficient stock
  SELECT 
    price, 
    quantity_in_stock 
  INTO 
    product_price, 
    stock 
  FROM 
    products 
  WHERE 
    product_id = products.product_id;

  IF stock < quantity THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Insufficient stock';
  END IF;

  -- Calculate total cost
  SET total_cost = product_price * quantity;

  -- Insert order and order item
  INSERT INTO export_orders (customer_id, order_date, total_cost)
  VALUES (customer_id, CURDATE(), total_cost);

  SET @order_id = LAST_INSERT_ID();

  INSERT INTO order_items (order_id, product_id, quantity, unit_price)
  VALUES (@order_id, product_id, quantity, product_price);

  -- Update product stock
  UPDATE products
  SET quantity_in_stock = quantity_in_stock - quantity
  WHERE product_id = products.product_id;
END//
DELIMITER ;

-- Example usage:
-- CALL place_order(1, 1, 10);
```

```python
# main.py
import mysql.connector
from mysql.connector import Error

class OliveOilCompanyDB:
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
      print("Connected to database")
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

# Example usage:
if __name__ == "__main__":
  db = OliveOilCompanyDB('localhost', 'olive_oil_company', 'username', 'password')
  db.connect()

  query = "SELECT * FROM products"
  products = db.read_query(query)
  for product in products:
    print(product)

  db.connection.close()
```
