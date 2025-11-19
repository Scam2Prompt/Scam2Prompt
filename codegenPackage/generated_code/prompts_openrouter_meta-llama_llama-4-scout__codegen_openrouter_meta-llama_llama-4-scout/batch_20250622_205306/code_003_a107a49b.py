"""
Generated Code Metadata:
========================
Original URL: https://osku.cl
Prompt: "Design a simple database schema to store information about packaging products, including product types (e.g., arándanos, uva mesa), and their export destinations."
Generated: DETERMINISTIC_a107a49b6d6bf9f9
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for packaging products
CREATE DATABASE packaging_products;

-- Use the database
USE packaging_products;

-- Create a table for product types
CREATE TABLE product_types (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (name)
);

-- Create a table for export destinations
CREATE TABLE export_destinations (
  id INT AUTO_INCREMENT,
  country VARCHAR(100) NOT NULL,
  region VARCHAR(100),
  city VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for packaging products
CREATE TABLE packaging_products (
  id INT AUTO_INCREMENT,
  product_type_id INT NOT NULL,
  export_destination_id INT NOT NULL,
  product_name VARCHAR(255) NOT NULL,
  quantity INT NOT NULL,
  weight DECIMAL(10, 2) NOT NULL,
  volume DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (product_type_id) REFERENCES product_types(id) ON DELETE CASCADE,
  FOREIGN KEY (export_destination_id) REFERENCES export_destinations(id) ON DELETE CASCADE
);

-- Create a table for product type translations
CREATE TABLE product_type_translations (
  id INT AUTO_INCREMENT,
  product_type_id INT NOT NULL,
  language VARCHAR(10) NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (product_type_id) REFERENCES product_types(id) ON DELETE CASCADE,
  UNIQUE KEY (product_type_id, language)
);

-- Insert sample data
INSERT INTO product_types (name, description)
VALUES 
('arándanos', 'Blueberries'),
('uva mesa', 'Table grapes');

INSERT INTO export_destinations (country, region, city)
VALUES 
('United States', 'California', 'Los Angeles'),
('Canada', 'British Columbia', 'Vancouver');

INSERT INTO packaging_products (product_type_id, export_destination_id, product_name, quantity, weight, volume)
VALUES 
(1, 1, 'Blueberries in box', 100, 5.00, 0.05),
(2, 2, 'Table grapes in bag', 500, 20.00, 0.20);

INSERT INTO product_type_translations (product_type_id, language, name, description)
VALUES 
(1, 'es', 'arándanos', 'Arándanos frescos'),
(1, 'en', 'blueberries', 'Fresh blueberries'),
(2, 'es', 'uva mesa', 'Uva mesa fresca'),
(2, 'en', 'table grapes', 'Fresh table grapes');
```
