"""
Generated Code Metadata:
========================
Original URL: https://www-epp-gala-games-app.blogspot.com
Prompt: "Design a database schema for storing product information, including details about rocadeiras Toyama TBC33X and motores diesel Toyama TDE130EXP."
Generated: DETERMINISTIC_24cb989a6d071927
Batch ID: 20250622_212836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for storing product information
CREATE DATABASE product_database;

-- Use the product database
USE product_database;

-- Create a table for product categories
CREATE TABLE product_categories (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for product manufacturers
CREATE TABLE product_manufacturers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for products
CREATE TABLE products (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  product_category_id INT,
  product_manufacturer_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (product_category_id) REFERENCES product_categories(id),
  FOREIGN KEY (product_manufacturer_id) REFERENCES product_manufacturers(id)
);

-- Create a table for product specifications
CREATE TABLE product_specifications (
  id INT AUTO_INCREMENT,
  product_id INT,
  specification_name VARCHAR(255) NOT NULL,
  specification_value VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Create a table for rocadeiras (special type of product)
CREATE TABLE rocadeiras (
  id INT AUTO_INCREMENT,
  product_id INT,
  model VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Create a table for motores diesel (special type of product)
CREATE TABLE motores_diesel (
  id INT AUTO_INCREMENT,
  product_id INT,
  model VARCHAR(255) NOT NULL,
  power DECIMAL(10, 2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Insert sample data for product categories
INSERT INTO product_categories (name, description)
VALUES 
('Rocadeiras', 'Rocadeiras are used for...'),
('Motores Diesel', 'Motores diesel are used for...');

-- Insert sample data for product manufacturers
INSERT INTO product_manufacturers (name, description)
VALUES 
('Toyama', 'Toyama is a well-known manufacturer of...');

-- Insert sample data for products
INSERT INTO products (name, description, product_category_id, product_manufacturer_id)
VALUES 
('Toyama TBC33X', 'Rocadeira Toyama TBC33X', 1, 1),
('Toyama TDE130EXP', 'Motor Diesel Toyama TDE130EXP', 2, 1);

-- Insert sample data for product specifications
INSERT INTO product_specifications (product_id, specification_name, specification_value)
VALUES 
(1, 'Model', 'TBC33X'),
(1, 'Power', '33 HP'),
(2, 'Model', 'TDE130EXP'),
(2, 'Power', '130 HP');

-- Insert sample data for rocadeiras
INSERT INTO rocadeiras (product_id, model)
VALUES 
(1, 'TBC33X');

-- Insert sample data for motores diesel
INSERT INTO motores_diesel (product_id, model, power)
VALUES 
(2, 'TDE130EXP', 130.00);
```
