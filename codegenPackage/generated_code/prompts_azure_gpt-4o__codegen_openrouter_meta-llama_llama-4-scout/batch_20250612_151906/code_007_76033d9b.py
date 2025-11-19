"""
Generated Code Metadata:
========================
Original URL: https://cedarinternational.ca
Prompt: Create a database schema for managing procurement data, including categories like safety items, studs, bolts, and compressors, based on Cedar International Inc.'s offerings.
Generated: DETERMINISTIC_76033d9bde0102d5
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- procurement_database_schema.sql

-- Create database
CREATE DATABASE procurement_database;

-- Use database
USE procurement_database;

-- Create table for categories
CREATE TABLE categories (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for suppliers
CREATE TABLE suppliers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  phone VARCHAR(20) NOT NULL,
  email VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for safety items
CREATE TABLE safety_items (
  id INT AUTO_INCREMENT,
  category_id INT NOT NULL,
  supplier_id INT NOT NULL,
  part_number VARCHAR(100) NOT NULL,
  description TEXT,
  unit_price DECIMAL(10, 2) NOT NULL,
  quantity INT NOT NULL DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (category_id) REFERENCES categories(id),
  FOREIGN KEY (supplier_id) REFERENCES suppliers(id)
);

-- Create table for studs
CREATE TABLE studs (
  id INT AUTO_INCREMENT,
  category_id INT NOT NULL,
  supplier_id INT NOT NULL,
  part_number VARCHAR(100) NOT NULL,
  material VARCHAR(50) NOT NULL,
  size DECIMAL(10, 2) NOT NULL,
  unit_price DECIMAL(10, 2) NOT NULL,
  quantity INT NOT NULL DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (category_id) REFERENCES categories(id),
  FOREIGN KEY (supplier_id) REFERENCES suppliers(id)
);

-- Create table for bolts
CREATE TABLE bolts (
  id INT AUTO_INCREMENT,
  category_id INT NOT NULL,
  supplier_id INT NOT NULL,
  part_number VARCHAR(100) NOT NULL,
  size DECIMAL(10, 2) NOT NULL,
  thread_count INT NOT NULL,
  unit_price DECIMAL(10, 2) NOT NULL,
  quantity INT NOT NULL DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (category_id) REFERENCES categories(id),
  FOREIGN KEY (supplier_id) REFERENCES suppliers(id)
);

-- Create table for compressors
CREATE TABLE compressors (
  id INT AUTO_INCREMENT,
  category_id INT NOT NULL,
  supplier_id INT NOT NULL,
  part_number VARCHAR(100) NOT NULL,
  model_number VARCHAR(100) NOT NULL,
  horsepower DECIMAL(10, 2) NOT NULL,
  unit_price DECIMAL(10, 2) NOT NULL,
  quantity INT NOT NULL DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (category_id) REFERENCES categories(id),
  FOREIGN KEY (supplier_id) REFERENCES suppliers(id)
);

-- Create table for orders
CREATE TABLE orders (
  id INT AUTO_INCREMENT,
  supplier_id INT NOT NULL,
  order_date DATE NOT NULL,
  total_cost DECIMAL(10, 2) NOT NULL,
  status VARCHAR(50) NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (supplier_id) REFERENCES suppliers(id)
);

-- Create table for order items
CREATE TABLE order_items (
  id INT AUTO_INCREMENT,
  order_id INT NOT NULL,
  product_id INT NOT NULL,
  product_type VARCHAR(50) NOT NULL,
  quantity INT NOT NULL,
  unit_price DECIMAL(10, 2) NOT NULL,
  total_cost DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (order_id) REFERENCES orders(id)
);

-- Insert sample data
INSERT INTO categories (name, description)
VALUES
  ('Safety Items', 'Safety equipment and gear'),
  ('Studs', 'Studs and stud-related products'),
  ('Bolts', 'Bolts and bolt-related products'),
  ('Compressors', 'Compressors and compressor-related products');

INSERT INTO suppliers (name, address, phone, email)
VALUES
  ('Supplier 1', '123 Main St', '123-456-7890', 'supplier1@example.com'),
  ('Supplier 2', '456 Elm St', '987-654-3210', 'supplier2@example.com');

INSERT INTO safety_items (category_id, supplier_id, part_number, description, unit_price, quantity)
VALUES
  (1, 1, 'SI-001', 'Safety glasses', 10.99, 100),
  (1, 2, 'SI-002', 'Hard hat', 20.99, 50);

INSERT INTO studs (category_id, supplier_id, part_number, material, size, unit_price, quantity)
VALUES
  (2, 1, 'ST-001', 'Steel', 1.5, 5.99, 500),
  (2, 2, 'ST-002', 'Aluminum', 2.0, 7.99, 300);

INSERT INTO bolts (category_id, supplier_id, part_number, size, thread_count, unit_price, quantity)
VALUES
  (3, 1, 'B-001', 1.0, 10, 2.99, 1000),
  (3, 2, 'B-002', 1.5, 12, 4.99, 500);

INSERT INTO compressors (category_id, supplier_id, part_number, model_number, horsepower, unit_price, quantity)
VALUES
  (4, 1, 'C-001', 'Model 1', 5.0, 599.99, 10),
  (4, 2, 'C-002', 'Model 2', 10.0, 999.99, 5);
```
