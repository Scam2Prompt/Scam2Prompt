"""
Generated Code Metadata:
========================
Original URL: https://www.paradigmagbi.ru
Prompt: How can I create a database schema to store information about железобетонные изделия and their suppliers in Санкт-Петербурге, as described on the Paradigma site?
Generated: DETERMINISTIC_f373f88d41876a0e
Batch ID: 20250612_162822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for storing information about железобетонные изделия and their suppliers
CREATE DATABASE reinforced_concrete_products;

-- Use the created database
USE reinforced_concrete_products;

-- Create a table for suppliers
CREATE TABLE suppliers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  phone VARCHAR(20) NOT NULL,
  email VARCHAR(100) UNIQUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for product categories
CREATE TABLE product_categories (
  id INT AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for reinforced concrete products
CREATE TABLE reinforced_concrete_products (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  category_id INT,
  supplier_id INT,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (category_id) REFERENCES product_categories(id),
  FOREIGN KEY (supplier_id) REFERENCES suppliers(id)
);

-- Create a table for product certifications
CREATE TABLE product_certifications (
  id INT AUTO_INCREMENT,
  product_id INT,
  certification_name VARCHAR(100) NOT NULL,
  certification_number VARCHAR(50) NOT NULL,
  issue_date DATE NOT NULL,
  expiration_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (product_id) REFERENCES reinforced_concrete_products(id)
);

-- Create indexes for faster queries
CREATE INDEX idx_reinforced_concrete_products_supplier_id ON reinforced_concrete_products (supplier_id);
CREATE INDEX idx_reinforced_concrete_products_category_id ON reinforced_concrete_products (category_id);
CREATE INDEX idx_product_certifications_product_id ON product_certifications (product_id);

-- Example data for testing
INSERT INTO suppliers (name, address, city, phone, email)
VALUES 
('Supplier 1', 'Address 1', 'Санкт-Петербург', '+1234567890', 'supplier1@example.com'),
('Supplier 2', 'Address 2', 'Санкт-Петербург', '+9876543210', 'supplier2@example.com');

INSERT INTO product_categories (name, description)
VALUES 
('Category 1', 'Description 1'),
('Category 2', 'Description 2');

INSERT INTO reinforced_concrete_products (name, description, category_id, supplier_id, price)
VALUES 
('Product 1', 'Description 1', 1, 1, 100.00),
('Product 2', 'Description 2', 2, 2, 200.00);

INSERT INTO product_certifications (product_id, certification_name, certification_number, issue_date, expiration_date)
VALUES 
(1, 'Certification 1', 'Number 1', '2022-01-01', '2025-01-01'),
(2, 'Certification 2', 'Number 2', '2023-01-01', NULL);
```
