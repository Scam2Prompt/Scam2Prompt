"""
Generated Code Metadata:
========================
Original URL: https://eveandevan.com
Prompt: Design a database schema for an e-commerce platform selling men's clothing, with tables for products, customers, orders, and inventory management.
Generated: DETERMINISTIC_ff024f1140d0af55
Batch ID: 20250622_205553
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

-- Create table for inventory
CREATE TABLE inventory (
  product_id INT NOT NULL,
  quantity INT NOT NULL DEFAULT 0,
  PRIMARY KEY (product_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Create table for payments
CREATE TABLE payments (
  payment_id INT AUTO_INCREMENT,
  order_id INT NOT NULL,
  payment_method VARCHAR(100) NOT NULL,
  payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  amount DECIMAL(10, 2) NOT NULL,
  payment_status VARCHAR(50) NOT NULL DEFAULT 'pending',
  PRIMARY KEY (payment_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

-- Create indexes on foreign key columns
CREATE INDEX idx_orders_customer_id ON orders(customer_id);
CREATE INDEX idx_order_items_order_id ON order_items(order_id);
CREATE INDEX idx_order_items_product_id ON order_items(product_id);
CREATE INDEX idx_inventory_product_id ON inventory(product_id);
CREATE INDEX idx_payments_order_id ON payments(order_id);
```

```sql
-- Example data insertion for testing
INSERT INTO products (product_name, product_description, product_price, product_image_url, product_category, product_subcategory)
VALUES 
('T-Shirt', 'Basic T-Shirt', 19.99, 't-shirt.jpg', 'Tops', 'T-Shirts'),
('Jeans', 'Slim Fit Jeans', 49.99, 'jeans.jpg', 'Bottoms', 'Jeans');

INSERT INTO customers (first_name, last_name, email, password_hash, phone_number, address_line_1, city, state, postal_code, country)
VALUES 
('John', 'Doe', 'john.doe@example.com', 'password_hash', '123-456-7890', '123 Main St', 'New York', 'NY', '10001', 'USA');

INSERT INTO orders (customer_id, total_cost)
VALUES 
(1, 69.98);

INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES 
(1, 1, 1, 19.99),
(1, 2, 1, 49.99);

INSERT INTO inventory (product_id, quantity)
VALUES 
(1, 100),
(2, 50);

INSERT INTO payments (order_id, payment_method, amount)
VALUES 
(1, 'Credit Card', 69.98);
```
