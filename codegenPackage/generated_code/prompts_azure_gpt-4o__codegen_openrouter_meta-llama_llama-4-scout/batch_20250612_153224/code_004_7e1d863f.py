"""
Generated Code Metadata:
========================
Original URL: https://dolphiniran.com
Prompt: Suggest a database schema for storing product information from Dolphin Iran, including fields for product name, category (e.g., "پرده حمام" or "جا ظرفی و آبچکان"), original price, discounted price, and stock status.
Generated: DETERMINISTIC_7e1d863f141ba309
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- dolphin_iran_products.sql

-- Create a database for storing product information
CREATE DATABASE dolphin_iran_products;

-- Use the created database
USE dolphin_iran_products;

-- Create a table for product categories
CREATE TABLE product_categories (
  category_id INT AUTO_INCREMENT,
  category_name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (category_id)
);

-- Create a table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  product_name VARCHAR(255) NOT NULL,
  category_id INT,
  original_price DECIMAL(10, 2) NOT NULL,
  discounted_price DECIMAL(10, 2),
  stock_status ENUM('in_stock', 'out_of_stock', 'low_stock') NOT NULL DEFAULT 'in_stock',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id),
  FOREIGN KEY (category_id) REFERENCES product_categories(category_id)
);

-- Create an index on category_id for efficient queries
CREATE INDEX idx_category_id ON products(category_id);

-- Example insert statements
INSERT INTO product_categories (category_name)
VALUES 
('پرده حمام'),
('جا ظرفی و آبچکان');

INSERT INTO products (product_name, category_id, original_price, discounted_price, stock_status)
VALUES 
('Product 1', 1, 100.00, 80.00, 'in_stock'),
('Product 2', 2, 200.00, NULL, 'out_of_stock'),
('Product 3', 1, 50.00, 40.00, 'low_stock');
```
