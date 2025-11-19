"""
Generated Code Metadata:
========================
Original URL: https://promo-official.com
Prompt: Design a simple database schema for storing product information, including prices, discounts, and product names, for an e-commerce platform like Promo Official.
Generated: DETERMINISTIC_5d448ae0f996b312
Batch ID: 20250622_204920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the e-commerce platform
CREATE DATABASE ecommerce_platform;

-- Use the ecommerce_platform database
USE ecommerce_platform;

-- Create a table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  product_name VARCHAR(255) NOT NULL,
  product_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id)
);

-- Create a table for prices
CREATE TABLE prices (
  price_id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (price_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create a table for discounts
CREATE TABLE discounts (
  discount_id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  discount_type ENUM('percentage', 'fixed') NOT NULL,
  discount_value DECIMAL(10, 2) NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (discount_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create a table for product images
CREATE TABLE product_images (
  image_id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  image_url VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (image_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create a stored procedure to add a new product
DELIMITER //
CREATE PROCEDURE add_product(
  IN p_product_name VARCHAR(255),
  IN p_product_description TEXT,
  IN p_price DECIMAL(10, 2)
)
BEGIN
  DECLARE new_product_id INT;
  INSERT INTO products (product_name, product_description)
  VALUES (p_product_name, p_product_description);
  SET new_product_id = LAST_INSERT_ID();
  INSERT INTO prices (product_id, price)
  VALUES (new_product_id, p_price);
END//
DELIMITER ;

-- Create a stored procedure to update a product price
DELIMITER //
CREATE PROCEDURE update_product_price(
  IN p_product_id INT,
  IN p_new_price DECIMAL(10, 2)
)
BEGIN
  UPDATE prices
  SET price = p_new_price
  WHERE product_id = p_product_id;
END//
DELIMITER ;

-- Create a stored procedure to add a discount
DELIMITER //
CREATE PROCEDURE add_discount(
  IN p_product_id INT,
  IN p_discount_type ENUM('percentage', 'fixed'),
  IN p_discount_value DECIMAL(10, 2),
  IN p_start_date DATE,
  IN p_end_date DATE
)
BEGIN
  INSERT INTO discounts (product_id, discount_type, discount_value, start_date, end_date)
  VALUES (p_product_id, p_discount_type, p_discount_value, p_start_date, p_end_date);
END//
DELIMITER ;
```

```python
import mysql.connector
from mysql.connector import Error

class ECommerceDatabase:
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

  def add_product(self, product_name, product_description, price):
    try:
      cursor = self.connection.cursor()
      cursor.callproc('add_product', [product_name, product_description, price])
      self.connection.commit()
      print("Product added successfully")
    except Error as e:
      print(f"Error: '{e}'")

  def update_product_price(self, product_id, new_price):
    try:
      cursor = self.connection.cursor()
      cursor.callproc('update_product_price', [product_id, new_price])
      self.connection.commit()
      print("Product price updated successfully")
    except Error as e:
      print(f"Error: '{e}'")

  def add_discount(self, product_id, discount_type, discount_value, start_date, end_date):
    try:
      cursor = self.connection.cursor()
      cursor.callproc('add_discount', [product_id, discount_type, discount_value, start_date, end_date])
      self.connection.commit()
      print("Discount added successfully")
    except Error as e:
      print(f"Error: '{e}'")

# Example usage
if __name__ == "__main__":
  db = ECommerceDatabase('localhost', 'ecommerce_platform', 'username', 'password')
  db.connect()
  db.add_product('Test Product', 'This is a test product', 19.99)
  db.update_product_price(1, 14.99)
  db.add_discount(1, 'percentage', 10.00, '2024-01-01', '2024-12-31')
```
