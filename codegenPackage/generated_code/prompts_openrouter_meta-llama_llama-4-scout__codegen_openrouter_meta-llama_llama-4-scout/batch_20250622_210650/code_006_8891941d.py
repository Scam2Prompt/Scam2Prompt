"""
Generated Code Metadata:
========================
Original URL: https://medpointye.com
Prompt: Design a database schema to store information about Medpointye's products, including Elisa Kits, and their respective product categories.
Generated: DETERMINISTIC_8891941d79fdb45d
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for Medpointye's products
CREATE DATABASE medpointye_products;

-- Use the medpointye_products database
USE medpointye_products;

-- Create a table for product categories
CREATE TABLE product_categories (
  `category_id` INT AUTO_INCREMENT,
  `category_name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`category_id`),
  UNIQUE KEY `category_name` (`category_name`)
);

-- Create a table for Elisa Kits
CREATE TABLE elisa_kits (
  `kit_id` INT AUTO_INCREMENT,
  `product_name` VARCHAR(255) NOT NULL,
  `product_code` VARCHAR(50) NOT NULL,
  `category_id` INT,
  `description` TEXT,
  `price` DECIMAL(10, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`kit_id`),
  UNIQUE KEY `product_code` (`product_code`),
  FOREIGN KEY (`category_id`) REFERENCES product_categories(`category_id`) ON DELETE SET NULL
);

-- Create a table for other products
CREATE TABLE products (
  `product_id` INT AUTO_INCREMENT,
  `product_name` VARCHAR(255) NOT NULL,
  `product_code` VARCHAR(50) NOT NULL,
  `category_id` INT,
  `description` TEXT,
  `price` DECIMAL(10, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`product_id`),
  UNIQUE KEY `product_code` (`product_code`),
  FOREIGN KEY (`category_id`) REFERENCES product_categories(`category_id`) ON DELETE SET NULL
);

-- Create a view to retrieve all products
CREATE VIEW all_products AS
SELECT 
  'Elisa Kit' AS product_type,
  kit_id AS product_id,
  product_name,
  product_code,
  category_id,
  description,
  price
FROM 
  elisa_kits
UNION ALL
SELECT 
  'Other Product' AS product_type,
  product_id,
  product_name,
  product_code,
  category_id,
  description,
  price
FROM 
  products;

-- Insert sample data into product categories
INSERT INTO product_categories (category_name, description)
VALUES 
('Elisa Kits', 'Enzyme-linked immunosorbent assay kits'),
('Antibodies', 'Antibodies for research and development'),
('Reagents', 'Reagents for laboratory use');

-- Insert sample data into Elisa Kits
INSERT INTO elisa_kits (product_name, product_code, category_id, description, price)
VALUES 
('Human ELISA Kit', 'MED-001', 1, 'Human ELISA kit for research', 100.00),
('Mouse ELISA Kit', 'MED-002', 1, 'Mouse ELISA kit for research', 120.00);

-- Insert sample data into other products
INSERT INTO products (product_name, product_code, category_id, description, price)
VALUES 
('Rabbit Antibody', 'MED-003', 2, 'Rabbit antibody for research', 50.00),
('Lab Reagent', 'MED-004', 3, 'Lab reagent for research', 20.00);

-- Retrieve all products
SELECT * FROM all_products;
```
