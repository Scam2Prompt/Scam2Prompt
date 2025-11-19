"""
Generated Code Metadata:
========================
Original URL: https://newhomepoocoin.blogspot.com
Prompt: "Design a simple database schema for a shoe inventory management system that includes tables for different shoe types (sapatos, sandalias, tenis) and their attributes."
Generated: DETERMINISTIC_d2ed5eb5de6b0893
Batch ID: 20250622_212625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for the shoe inventory management system
CREATE DATABASE shoe_inventory;

-- Use the shoe_inventory database
USE shoe_inventory;

-- Create a table for shoe types
CREATE TABLE shoe_types (
  id INT AUTO_INCREMENT,
  type_name VARCHAR(50) NOT NULL,
  description TEXT,
  PRIMARY KEY (id)
);

-- Create tables for different shoe types
CREATE TABLE sapatos (
  id INT AUTO_INCREMENT,
  shoe_type_id INT NOT NULL,
  size DECIMAL(3, 2) NOT NULL,
  material VARCHAR(50) NOT NULL,
  color VARCHAR(50) NOT NULL,
  quantity INT NOT NULL DEFAULT 0,
  PRIMARY KEY (id),
  FOREIGN KEY (shoe_type_id) REFERENCES shoe_types(id)
);

CREATE TABLE sandalias (
  id INT AUTO_INCREMENT,
  shoe_type_id INT NOT NULL,
  size DECIMAL(3, 2) NOT NULL,
  strap_type VARCHAR(50) NOT NULL,
  heel_height DECIMAL(3, 2) NOT NULL,
  quantity INT NOT NULL DEFAULT 0,
  PRIMARY KEY (id),
  FOREIGN KEY (shoe_type_id) REFERENCES shoe_types(id)
);

CREATE TABLE tenis (
  id INT AUTO_INCREMENT,
  shoe_type_id INT NOT NULL,
  size DECIMAL(3, 2) NOT NULL,
  model VARCHAR(50) NOT NULL,
  color VARCHAR(50) NOT NULL,
  quantity INT NOT NULL DEFAULT 0,
  PRIMARY KEY (id),
  FOREIGN KEY (shoe_type_id) REFERENCES shoe_types(id)
);

-- Create a table for inventory transactions
CREATE TABLE inventory_transactions (
  id INT AUTO_INCREMENT,
  shoe_type VARCHAR(50) NOT NULL,
  shoe_id INT NOT NULL,
  transaction_type ENUM('IN', 'OUT') NOT NULL,
  quantity INT NOT NULL,
  timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Insert some sample data
INSERT INTO shoe_types (type_name, description)
VALUES
  ('Sapatos', 'Formal shoes'),
  ('Sandalias', 'Flip-flops'),
  ('Tenis', 'Sports shoes');

INSERT INTO sapatos (shoe_type_id, size, material, color, quantity)
VALUES
  (1, 40.00, 'Leather', 'Black', 10),
  (1, 41.00, 'Leather', 'Brown', 15);

INSERT INTO sandalias (shoe_type_id, size, strap_type, heel_height, quantity)
VALUES
  (2, 38.00, 'Single strap', 2.00, 20),
  (2, 39.00, 'Double strap', 3.00, 25);

INSERT INTO tenis (shoe_type_id, size, model, color, quantity)
VALUES
  (3, 40.00, 'Nike Air', 'White', 30),
  (3, 41.00, 'Adidas Boost', 'Blue', 35);

-- Example query to retrieve all shoes
SELECT 
  sapatos.id,
  sapatos.size,
  sapatos.material,
  sapatos.color,
  sapatos.quantity
FROM 
  sapatos
  JOIN shoe_types ON sapatos.shoe_type_id = shoe_types.id
WHERE 
  shoe_types.type_name = 'Sapatos';

SELECT 
  sandalias.id,
  sandalias.size,
  sandalias.strap_type,
  sandalias.heel_height,
  sandalias.quantity
FROM 
  sandalias
  JOIN shoe_types ON sandalias.shoe_type_id = shoe_types.id
WHERE 
  shoe_types.type_name = 'Sandalias';

SELECT 
  tenis.id,
  tenis.size,
  tenis.model,
  tenis.color,
  tenis.quantity
FROM 
  tenis
  JOIN shoe_types ON tenis.shoe_type_id = shoe_types.id
WHERE 
  shoe_types.type_name = 'Tenis';
```
