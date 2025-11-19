"""
Generated Code Metadata:
========================
Original URL: https://www.apos.cl
Prompt: "Design a database schema for an e-commerce platform specializing in paper roll distribution, with tables for products, customers, orders, and pricing information specific to the Chilean market."
Generated: DETERMINISTIC_6caa336d734af67a
Batch ID: 20250622_205138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for e-commerce platform
CREATE DATABASE paper_roll_distribution;

-- Use database
USE paper_roll_distribution;

-- Create table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  product_name VARCHAR(255) NOT NULL,
  product_description TEXT,
  product_code VARCHAR(50) UNIQUE NOT NULL,
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
  phone_number VARCHAR(20),
  address VARCHAR(255),
  city VARCHAR(100),
  region VARCHAR(100),
  country VARCHAR(100) DEFAULT 'Chile',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (customer_id)
);

-- Create table for orders
CREATE TABLE orders (
  order_id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  total DECIMAL(10, 2) NOT NULL,
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
  unit_price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (order_item_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Create table for pricing information
CREATE TABLE pricing (
  pricing_id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  currency VARCHAR(10) NOT NULL DEFAULT 'CLP',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (pricing_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Create table for taxes and discounts (Chilean market specific)
CREATE TABLE taxes_discounts (
  taxes_discounts_id INT AUTO_INCREMENT,
  product_id INT,
  customer_id INT,
  tax_rate DECIMAL(5, 2),
  discount_rate DECIMAL(5, 2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (taxes_discounts_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Create indexes for performance optimization
CREATE INDEX idx_orders_customer_id ON orders(customer_id);
CREATE INDEX idx_order_items_order_id ON order_items(order_id);
CREATE INDEX idx_order_items_product_id ON order_items(product_id);
CREATE INDEX idx_pricing_product_id ON pricing(product_id);
```

```sql
-- sample_data.sql

-- Insert sample data into products table
INSERT INTO products (product_name, product_description, product_code)
VALUES 
('Standard Paper Roll', 'Standard paper roll for printing', 'PR-001'),
('Large Paper Roll', 'Large paper roll for industrial use', 'PR-002'),
('Custom Paper Roll', 'Custom paper roll for specific needs', 'PR-003');

-- Insert sample data into customers table
INSERT INTO customers (first_name, last_name, email, phone_number, address, city, region)
VALUES 
('John', 'Doe', 'john.doe@example.com', '+56 9 1234 5678', 'Calle 123', 'Santiago', 'Metropolitana'),
('Jane', 'Smith', 'jane.smith@example.com', '+56 9 9012 3456', 'Calle 456', 'Valparaíso', 'Valparaíso');

-- Insert sample data into orders table
INSERT INTO orders (customer_id, total)
VALUES 
(1, 10000.00),
(2, 5000.00);

-- Insert sample data into order_items table
INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES 
(1, 1, 2, 2000.00),
(1, 2, 1, 8000.00),
(2, 3, 1, 5000.00);

-- Insert sample data into pricing table
INSERT INTO pricing (product_id, price)
VALUES 
(1, 1500.00),
(2, 6000.00),
(3, 4000.00);

-- Insert sample data into taxes_discounts table
INSERT INTO taxes_discounts (product_id, customer_id, tax_rate, discount_rate)
VALUES 
(1, 1, 0.19, 0.05),
(2, 2, 0.19, 0.10);
```
