"""
Generated Code Metadata:
========================
Original URL: https://magicenen-nfts.blogspot.com
Prompt: Design a database schema to store shoe products with attributes like name, price, brand, category, and payment options (e.g., 3x, 5x, 7x installments), inspired by the content of https://magicenen-nfts.blogspot.com.
Generated: DETERMINISTIC_d628ab41dd0cb2ae
Batch ID: 20250622_205007
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
CREATE DATABASE shoe_store;

-- Use database
USE shoe_store;

-- Create table for brands
CREATE TABLE brands (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (name)
);

-- Create table for categories
CREATE TABLE categories (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (name)
);

-- Create table for shoe products
CREATE TABLE shoe_products (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  brand_id INT NOT NULL,
  category_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (brand_id) REFERENCES brands(id) ON DELETE CASCADE,
  FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
);

-- Create table for payment options
CREATE TABLE payment_options (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  installments INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (name)
);

-- Create table for shoe product payment options
CREATE TABLE shoe_product_payment_options (
  id INT AUTO_INCREMENT,
  shoe_product_id INT NOT NULL,
  payment_option_id INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (shoe_product_id) REFERENCES shoe_products(id) ON DELETE CASCADE,
  FOREIGN KEY (payment_option_id) REFERENCES payment_options(id) ON DELETE CASCADE,
  UNIQUE KEY (shoe_product_id, payment_option_id)
);

-- Insert sample data
INSERT INTO brands (name) VALUES
  ('Nike'),
  ('Adidas'),
  ('Converse');

INSERT INTO categories (name) VALUES
  ('Sneakers'),
  ('Boots'),
  ('Sandals');

INSERT INTO shoe_products (name, price, brand_id, category_id) VALUES
  ('Nike Air Max', 100.00, 1, 1),
  ('Adidas Superstar', 80.00, 2, 1),
  ('Converse Chuck Taylor', 60.00, 3, 1);

INSERT INTO payment_options (name, installments) VALUES
  ('3x Installments', 3),
  ('5x Installments', 5),
  ('7x Installments', 7);

INSERT INTO shoe_product_payment_options (shoe_product_id, payment_option_id, price) VALUES
  (1, 1, 33.33),
  (1, 2, 20.00),
  (1, 3, 14.29),
  (2, 1, 26.67),
  (2, 2, 16.00),
  (2, 3, 11.43),
  (3, 1, 20.00),
  (3, 2, 12.00),
  (3, 3, 8.57);
```

```python
# shoe_store.py

import mysql.connector
from mysql.connector import Error

class ShoeStore:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Connected to database")
        except Error as e:
            print(f"Error connecting to database: {e}")

    def get_shoe_products(self):
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT 
                    sp.id,
                    sp.name,
                    sp.price,
                    b.name AS brand,
                    c.name AS category
                FROM 
                    shoe_products sp
                JOIN 
                    brands b ON sp.brand_id = b.id
                JOIN 
                    categories c ON sp.category_id = c.id
            """
            cursor.execute(query)
            return cursor.fetchall()
        except Error as e:
            print(f"Error getting shoe products: {e}")
            return []

    def get_payment_options(self, shoe_product_id):
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT 
                    po.name,
                    po.installments,
                    spp.price
                FROM 
                    shoe_product_payment_options spp
                JOIN 
                    payment_options po ON spp.payment_option_id = po.id
                WHERE 
                    spp.shoe_product_id = %s
            """
            cursor.execute(query, (shoe_product_id,))
            return cursor.fetchall()
        except Error as e:
            print(f"Error getting payment options: {e}")
            return []

# Usage
if __name__ == "__main__":
    host = "localhost"
    database = "shoe_store"
    user = "root"
    password = "password"

    shoe_store = ShoeStore(host, database, user, password)
    shoe_store.connect()

    shoe_products = shoe_store.get_shoe_products()
    for product in shoe_products:
        print(product)

    payment_options = shoe_store.get_payment_options(1)
    for option in payment_options:
        print(option)
```
