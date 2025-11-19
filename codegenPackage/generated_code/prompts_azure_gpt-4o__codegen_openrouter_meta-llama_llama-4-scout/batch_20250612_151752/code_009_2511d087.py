"""
Generated Code Metadata:
========================
Original URL: https://chandkalaco.com
Prompt: Design a database schema to store product details, including categories like "شیرآلات بهداشتی ساختمان" and "دوربین مدار بسته," for an e-commerce platform similar to chandkala.com.
Generated: DETERMINISTIC_2511d087065ae030
Batch ID: 20250612_151752
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/product1-image2.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/product2-image1.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/product1-image1.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```sql
-- database_schema.sql

-- Create database for e-commerce platform
CREATE DATABASE ecommerce_platform;

-- Use the created database
USE ecommerce_platform;

-- Create table for product categories
CREATE TABLE categories (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for products
CREATE TABLE products (
  id INT AUTO_INCREMENT,
  category_id INT,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  stock_quantity INT NOT NULL DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
);

-- Create table for product images
CREATE TABLE product_images (
  id INT AUTO_INCREMENT,
  product_id INT,
  image_url VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

-- Create table for product specifications
CREATE TABLE product_specs (
  id INT AUTO_INCREMENT,
  product_id INT,
  spec_name VARCHAR(255) NOT NULL,
  spec_value VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

-- Insert sample categories
INSERT INTO categories (name, description) 
VALUES 
('شیرآلات بهداشتی ساختمان', 'بهداشتی ساختمان مربوط به شیرآلات'),
('دوربین مدار بسته', 'دوربین های مدار بسته امنیتی');

-- Insert sample products
INSERT INTO products (category_id, title, description, price, stock_quantity) 
VALUES 
(1, 'شیرآلات بهداشتی ساختمان مدل A', 'مدل A شیرآلات بهداشتی ساختمان', 100.00, 10),
(2, 'دوربین مدار بسته مدل B', 'مدل B دوربین مدار بسته', 200.00, 5);

-- Insert sample product images
INSERT INTO product_images (product_id, image_url) 
VALUES 
(1, 'https://example.com/product1-image1.jpg'),
(1, 'https://example.com/product1-image2.jpg'),
(2, 'https://example.com/product2-image1.jpg');

-- Insert sample product specifications
INSERT INTO product_specs (product_id, spec_name, spec_value) 
VALUES 
(1, 'Material', 'Brass'),
(1, 'Color', 'Chrome'),
(2, 'Resolution', '1080p'),
(2, 'Field of View', '90 degrees');
```
