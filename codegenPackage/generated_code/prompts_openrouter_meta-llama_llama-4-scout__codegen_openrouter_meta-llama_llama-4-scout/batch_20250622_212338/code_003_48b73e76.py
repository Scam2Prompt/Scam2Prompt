"""
Generated Code Metadata:
========================
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Design a database schema to store product information, customer data, and order details for an e-commerce website like ebrasilbrazz, which sells various products, including equipment, supplies, and home decor items.
Generated: DETERMINISTIC_48b73e76ed86557a
Batch ID: 20250622_212338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for e-commerce website
CREATE DATABASE ecommerce_website;

-- Use the created database
USE ecommerce_website;

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

-- Create table for payments
CREATE TABLE payments (
  payment_id INT AUTO_INCREMENT,
  order_id INT NOT NULL,
  payment_method VARCHAR(100) NOT NULL,
  payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  payment_amount DECIMAL(10, 2) NOT NULL,
  payment_status VARCHAR(50) NOT NULL DEFAULT 'pending',
  PRIMARY KEY (payment_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

-- Create indexes on foreign key columns
CREATE INDEX idx_orders_customer_id ON orders (customer_id);
CREATE INDEX idx_order_items_order_id ON order_items (order_id);
CREATE INDEX idx_order_items_product_id ON order_items (product_id);
CREATE INDEX idx_payments_order_id ON payments (order_id);
```

```sql
-- Example data insertion
INSERT INTO products (product_name, product_description, product_price, product_image_url, product_category, product_subcategory)
VALUES 
('Product 1', 'This is product 1', 10.99, 'product1.jpg', 'Equipment', 'Tools'),
('Product 2', 'This is product 2', 5.99, 'product2.jpg', 'Supplies', 'Materials'),
('Product 3', 'This is product 3', 7.99, 'product3.jpg', 'Home Decor', 'Furniture');

INSERT INTO customers (first_name, last_name, email, password_hash, phone_number, address_line_1, city, state, postal_code, country)
VALUES 
('John', 'Doe', 'john.doe@example.com', 'password_hash', '123-456-7890', '123 Main St', 'Anytown', 'CA', '12345', 'USA');

INSERT INTO orders (customer_id, total_cost)
VALUES 
(1, 10.99);

INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES 
(1, 1, 1, 10.99);

INSERT INTO payments (order_id, payment_method, payment_amount)
VALUES 
(1, 'Credit Card', 10.99);
```
