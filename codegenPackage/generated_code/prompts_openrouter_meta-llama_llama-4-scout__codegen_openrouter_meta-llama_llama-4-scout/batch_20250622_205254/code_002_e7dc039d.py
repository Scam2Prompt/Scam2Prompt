"""
Generated Code Metadata:
========================
Original URL: https://poly-market.hu
Prompt: Generate a SQL query to manage inventory for an online store like Poly-Market, including tables for products, orders, and customers, with specific columns for product categories and prices.
Generated: DETERMINISTIC_e7dc039d785c6943
Batch ID: 20250622_205254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for online store
CREATE DATABASE online_store;

-- Use the database
USE online_store;

-- Create table for product categories
CREATE TABLE product_categories (
  category_id INT AUTO_INCREMENT,
  category_name VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (category_id)
);

-- Create table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  product_name VARCHAR(255) NOT NULL,
  category_id INT,
  price DECIMAL(10, 2) NOT NULL,
  stock_quantity INT NOT NULL DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id),
  FOREIGN KEY (category_id) REFERENCES product_categories(category_id)
);

-- Create table for customers
CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (customer_id)
);

-- Create table for orders
CREATE TABLE orders (
  order_id INT AUTO_INCREMENT,
  customer_id INT,
  order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  total_cost DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
  status ENUM('pending', 'shipped', 'delivered', 'cancelled') NOT NULL DEFAULT 'pending',
  PRIMARY KEY (order_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Create table for order items
CREATE TABLE order_items (
  order_item_id INT AUTO_INCREMENT,
  order_id INT,
  product_id INT,
  quantity INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (order_item_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Insert sample data into product categories
INSERT INTO product_categories (category_name, description)
VALUES
('Electronics', 'Electronic devices and gadgets'),
('Fashion', 'Clothing and accessories'),
('Home & Kitchen', 'Home decor and kitchen essentials');

-- Insert sample data into products
INSERT INTO products (product_name, category_id, price, stock_quantity)
VALUES
('Smartphone', 1, 599.99, 100),
('T-Shirt', 2, 19.99, 500),
('Coffee Table', 3, 129.99, 50);

-- Insert sample data into customers
INSERT INTO customers (first_name, last_name, email, phone_number, address)
VALUES
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', '456 Elm St');

-- Insert sample data into orders
INSERT INTO orders (customer_id, total_cost)
VALUES
(1, 619.98),
(2, 149.98);

-- Insert sample data into order items
INSERT INTO order_items (order_id, product_id, quantity, price)
VALUES
(1, 1, 1, 599.99),
(1, 2, 1, 19.99),
(2, 3, 1, 129.99),
(2, 2, 1, 19.99);

-- Query to get all products with their categories
SELECT p.product_id, p.product_name, pc.category_name, p.price, p.stock_quantity
FROM products p
JOIN product_categories pc ON p.category_id = pc.category_id;

-- Query to get all orders with their items
SELECT o.order_id, c.first_name, c.last_name, o.order_date, o.total_cost, oi.product_id, p.product_name, oi.quantity
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id;
```
