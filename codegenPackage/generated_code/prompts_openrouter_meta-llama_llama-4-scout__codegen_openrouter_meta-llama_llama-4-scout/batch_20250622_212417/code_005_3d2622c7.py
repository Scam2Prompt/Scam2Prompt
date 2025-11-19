"""
Generated Code Metadata:
========================
Original URL: https://codyalt.com
Prompt: Design a database schema for an e-commerce platform that manages products, orders, and customers for a business like PureKana or skyMD, with SQL code for data insertion and querying.
Generated: DETERMINISTIC_3d2622c74a47fc95
Batch ID: 20250622_212417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for e-commerce platform
CREATE DATABASE ecommerce_platform;

-- Use the ecommerce_platform database
USE ecommerce_platform;

-- Create table for customers
CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  city VARCHAR(100),
  state VARCHAR(100),
  zip_code VARCHAR(10),
  country VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (customer_id)
);

-- Create table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  product_name VARCHAR(255) NOT NULL,
  product_description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  stock_quantity INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id)
);

-- Create table for orders
CREATE TABLE orders (
  order_id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  total_cost DECIMAL(10, 2) NOT NULL,
  status VARCHAR(50) NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (order_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Create table for order items
CREATE TABLE order_items (
  order_item_id INT AUTO_INCREMENT,
  order_id INT NOT NULL,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (order_item_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Insert sample data into customers table
INSERT INTO customers (first_name, last_name, email, phone_number, address, city, state, zip_code, country)
VALUES
  ('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'New York', 'NY', '10001', 'USA'),
  ('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', '456 Park Ave', 'Los Angeles', 'CA', '90001', 'USA'),
  ('Bob', 'Smith', 'bob.smith@example.com', '555-123-4567', '789 Oak St', 'Chicago', 'IL', '60001', 'USA');

-- Insert sample data into products table
INSERT INTO products (product_name, product_description, price, stock_quantity)
VALUES
  ('CBD Oil', 'PureKana CBD Oil 1000mg', 49.99, 100),
  ('CBD Gummies', 'SkyMD CBD Gummies 25mg', 29.99, 50),
  ('CBD Topical Cream', 'PureKana CBD Topical Cream 500mg', 39.99, 75);

-- Insert sample data into orders table
INSERT INTO orders (customer_id, total_cost)
VALUES
  (1, 49.99),
  (2, 29.99),
  (3, 89.98);

-- Insert sample data into order_items table
INSERT INTO order_items (order_id, product_id, quantity)
VALUES
  (1, 1, 1),
  (2, 2, 1),
  (3, 1, 1),
  (3, 3, 1);

-- Query to retrieve all customers with their orders
SELECT c.customer_id, c.first_name, c.last_name, o.order_id, o.order_date, o.total_cost
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id;

-- Query to retrieve all products with their order items
SELECT p.product_id, p.product_name, oi.order_id, oi.quantity
FROM products p
LEFT JOIN order_items oi ON p.product_id = oi.product_id;

-- Query to retrieve total sales by product
SELECT p.product_name, SUM(oi.quantity) AS total_quantity, SUM(oi.quantity * p.price) AS total_revenue
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.product_name;

-- Query to retrieve customer order history
SELECT c.customer_id, c.first_name, c.last_name, o.order_id, o.order_date, o.total_cost
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
ORDER BY c.customer_id;
```
