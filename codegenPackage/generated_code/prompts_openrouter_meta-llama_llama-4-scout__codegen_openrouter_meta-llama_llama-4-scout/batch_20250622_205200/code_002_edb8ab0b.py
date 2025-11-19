"""
Generated Code Metadata:
========================
Original URL: https://compensadosscursel.blogspot.com
Prompt: Generate a SQL query to design a database schema for storing information about wood products, including product types (e.g., compensados resinados, portas), materials (e.g., Sucupira, Itauba), and production dates.
Generated: DETERMINISTIC_edb8ab0ba37d142c
Batch ID: 20250622_205200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for wood products
CREATE DATABASE wood_products;

-- Use the wood_products database
USE wood_products;

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

-- Create a table for materials
CREATE TABLE materials (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (name)
);

-- Create a table for wood products
CREATE TABLE wood_products (
  id INT AUTO_INCREMENT,
  product_type_id INT NOT NULL,
  material_id INT NOT NULL,
  product_name VARCHAR(255) NOT NULL,
  production_date DATE NOT NULL,
  quantity INT NOT NULL DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (product_type_id) REFERENCES product_types(id) ON DELETE CASCADE,
  FOREIGN KEY (material_id) REFERENCES materials(id) ON DELETE CASCADE
);

-- Create a table for product type materials (many-to-many relationship)
CREATE TABLE product_type_materials (
  product_type_id INT NOT NULL,
  material_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (product_type_id, material_id),
  FOREIGN KEY (product_type_id) REFERENCES product_types(id) ON DELETE CASCADE,
  FOREIGN KEY (material_id) REFERENCES materials(id) ON DELETE CASCADE
);

-- Insert some sample data
INSERT INTO product_types (name, description) 
VALUES 
('Compensados Resinados', 'Resin-coated plywood products'),
('Portas', 'Wooden doors');

INSERT INTO materials (name, description) 
VALUES 
('Sucupira', 'A type of wood'),
('Itauba', 'Another type of wood');

INSERT INTO wood_products (product_type_id, material_id, product_name, production_date, quantity) 
VALUES 
(1, 1, 'Sample Product 1', '2022-01-01', 100),
(1, 2, 'Sample Product 2', '2022-02-01', 50),
(2, 1, 'Sample Door', '2022-03-01', 20);

INSERT INTO product_type_materials (product_type_id, material_id) 
VALUES 
(1, 1),
(1, 2),
(2, 1);
```
