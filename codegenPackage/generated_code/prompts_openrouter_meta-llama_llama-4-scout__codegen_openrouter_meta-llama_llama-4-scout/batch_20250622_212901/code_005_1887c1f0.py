"""
Generated Code Metadata:
========================
Original URL: https://unitramabrazz.blogspot.com
Prompt: Design a simple database schema to store information about various visual communication products, including chapas de alumínio composto, lonas uniflex, and tecido flag banner.
Generated: DETERMINISTIC_1887c1f0b59616ee
Batch ID: 20250622_212901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- database_schema.sql

-- Create a database for visual communication products
CREATE DATABASE visual_communication;

-- Use the database
USE visual_communication;

-- Create a table for products
CREATE TABLE products (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for product types
CREATE TABLE product_types (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for product materials
CREATE TABLE product_materials (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for product specifications
CREATE TABLE product_specifications (
  id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  material_id INT NOT NULL,
  size VARCHAR(255) NOT NULL,
  thickness DECIMAL(10, 2) NOT NULL,
  weight DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (product_id) REFERENCES products(id),
  FOREIGN KEY (material_id) REFERENCES product_materials(id)
);

-- Create a table for product types mapping
CREATE TABLE product_type_mapping (
  product_id INT NOT NULL,
  type_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id, type_id),
  FOREIGN KEY (product_id) REFERENCES products(id),
  FOREIGN KEY (type_id) REFERENCES product_types(id)
);

-- Insert some sample data
INSERT INTO product_types (name, description)
VALUES 
('Chapa de Alumínio Composto', 'Aluminum composite panel'),
('Lona Uniflex', 'Uniflex canvas'),
('Tecido Flag Banner', 'Flag banner fabric');

INSERT INTO product_materials (name, description)
VALUES 
('Alumínio', 'Aluminum'),
('PVC', 'Polyvinyl chloride'),
('Tecido', 'Fabric');

INSERT INTO products (name, description)
VALUES 
('Chapa de Alumínio Composto 1', 'Aluminum composite panel for outdoor use'),
('Lona Uniflex 1', 'Uniflex canvas for indoor use'),
('Tecido Flag Banner 1', 'Flag banner fabric for outdoor use');

INSERT INTO product_specifications (product_id, material_id, size, thickness, weight)
VALUES 
(1, 1, '1000x2000mm', 3.00, 5.00),
(2, 2, '800x1500mm', 2.00, 3.00),
(3, 3, '1200x2500mm', 1.50, 2.50);

INSERT INTO product_type_mapping (product_id, type_id)
VALUES 
(1, 1),
(2, 2),
(3, 3);
```
