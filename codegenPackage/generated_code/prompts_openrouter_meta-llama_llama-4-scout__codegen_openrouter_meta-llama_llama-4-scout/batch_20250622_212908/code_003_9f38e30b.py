"""
Generated Code Metadata:
========================
Original URL: https://blacksabbathmerch.com
Prompt: Design a database schema to store Black Sabbath merchandise products, orders, and customer information for an e-commerce website, and write a SQL query to retrieve product information.
Generated: DETERMINISTIC_9f38e30be1337e0d
Batch ID: 20250622_212908
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for Black Sabbath merchandise
CREATE DATABASE black_sabbath_merch;

-- Use the database
USE black_sabbath_merch;

-- Create table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  product_name VARCHAR(255) NOT NULL,
  product_description TEXT,
  product_price DECIMAL(10, 2) NOT NULL,
  product_image_url VARCHAR(255),
  product_category ENUM('t-shirts', 'hoodies', 'posters', 'accessories') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id)
);

-- Create table for customers
CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  address VARCHAR(255),
  city VARCHAR(50),
  state VARCHAR(50),
  zip_code VARCHAR(10),
  country VARCHAR(50),
  phone_number VARCHAR(20),
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
  status ENUM('pending', 'shipped', 'delivered', 'cancelled') DEFAULT 'pending',
  PRIMARY KEY (order_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Create table for order items
CREATE TABLE order_items (
  order_item_id INT AUTO_INCREMENT,
  order_id INT NOT NULL,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  unit_price DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (order_item_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Insert sample data into products table
INSERT INTO products (product_name, product_description, product_price, product_image_url, product_category)
VALUES
  ('Iron Man T-Shirt', 'Black T-shirt with Iron Man logo', 19.99, 'iron_man_tshirt.jpg', 't-shirts'),
  ('Paranoid Hoodie', 'Grey hoodie with Paranoid album artwork', 49.99, 'paranoid_hoodie.jpg', 'hoodies'),
  ('Master of Reality Poster', 'Poster of Master of Reality album cover', 14.99, 'master_of_reality_poster.jpg', 'posters');

-- Insert sample data into customers table
INSERT INTO customers (first_name, last_name, email, password_hash, address, city, state, zip_code, country, phone_number)
VALUES
  ('John', 'Doe', 'john.doe@example.com', 'password_hash', '123 Main St', 'New York', 'NY', '10001', 'USA', '123-456-7890'),
  ('Jane', 'Doe', 'jane.doe@example.com', 'password_hash', '456 Elm St', 'Los Angeles', 'CA', '90001', 'USA', '987-654-3210');

-- Insert sample data into orders table
INSERT INTO orders (customer_id, total_cost)
VALUES
  (1, 19.99),
  (2, 49.99);

-- Insert sample data into order_items table
INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES
  (1, 1, 1, 19.99),
  (2, 2, 1, 49.99);

-- Retrieve product information SQL query
SELECT 
  p.product_id,
  p.product_name,
  p.product_description,
  p.product_price,
  p.product_image_url,
  p.product_category,
  oi.quantity AS order_quantity
FROM 
  products p
  LEFT JOIN order_items oi ON p.product_id = oi.product_id
WHERE 
  p.product_id = 1;
```
