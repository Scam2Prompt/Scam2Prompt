"""
Generated Code Metadata:
========================
Original URL: https://knitplusltd.com
Prompt: "Generate a SQL database schema to store information about garment products, including details on materials, sizes, and production processes, for a company like Knit Plus Ltd."
Generated: DETERMINISTIC_07e154423a0db38e
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for Knit Plus Ltd.
CREATE DATABASE knit_plus;

-- Use the knit_plus database
USE knit_plus;

-- Create table for materials
CREATE TABLE materials (
  material_id INT AUTO_INCREMENT,
  material_name VARCHAR(255) NOT NULL,
  material_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (material_id)
);

-- Create table for sizes
CREATE TABLE sizes (
  size_id INT AUTO_INCREMENT,
  size_name VARCHAR(50) NOT NULL,
  size_description VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (size_id)
);

-- Create table for garment products
CREATE TABLE garment_products (
  product_id INT AUTO_INCREMENT,
  product_name VARCHAR(255) NOT NULL,
  product_description TEXT,
  material_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id),
  FOREIGN KEY (material_id) REFERENCES materials(material_id) ON DELETE CASCADE
);

-- Create table for production processes
CREATE TABLE production_processes (
  process_id INT AUTO_INCREMENT,
  process_name VARCHAR(255) NOT NULL,
  process_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (process_id)
);

-- Create table for garment product sizes
CREATE TABLE garment_product_sizes (
  product_size_id INT AUTO_INCREMENT,
  product_id INT,
  size_id INT,
  quantity INT NOT NULL DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_size_id),
  FOREIGN KEY (product_id) REFERENCES garment_products(product_id) ON DELETE CASCADE,
  FOREIGN KEY (size_id) REFERENCES sizes(size_id) ON DELETE CASCADE
);

-- Create table for garment product production processes
CREATE TABLE garment_product_processes (
  product_process_id INT AUTO_INCREMENT,
  product_id INT,
  process_id INT,
  sequence INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_process_id),
  FOREIGN KEY (product_id) REFERENCES garment_products(product_id) ON DELETE CASCADE,
  FOREIGN KEY (process_id) REFERENCES production_processes(process_id) ON DELETE CASCADE
);

-- Create indexes for foreign keys
CREATE INDEX idx_material_id ON garment_products(material_id);
CREATE INDEX idx_product_id ON garment_product_sizes(product_id);
CREATE INDEX idx_size_id ON garment_product_sizes(size_id);
CREATE INDEX idx_product_id_process_id ON garment_product_processes(product_id, process_id);
```

```sql
-- Example insert statements
INSERT INTO materials (material_name, material_description)
VALUES 
('Cotton', 'Soft and breathable natural fiber'),
('Polyester', 'Durable and wrinkle-resistant synthetic fiber');

INSERT INTO sizes (size_name, size_description)
VALUES 
('Small', 'Fits chest 30-34 inches'),
('Medium', 'Fits chest 35-39 inches');

INSERT INTO garment_products (product_name, product_description, material_id)
VALUES 
('T-Shirt', 'Basic crew neck T-Shirt', 1),
('Sweatshirt', 'Heavyweight fleece sweatshirt', 2);

INSERT INTO production_processes (process_name, process_description)
VALUES 
('Cutting', 'Cutting fabric into pattern pieces'),
('Sewing', 'Assembling garment parts');

INSERT INTO garment_product_sizes (product_id, size_id, quantity)
VALUES 
(1, 1, 100),
(1, 2, 150),
(2, 1, 50),
(2, 2, 75);

INSERT INTO garment_product_processes (product_id, process_id, sequence)
VALUES 
(1, 1, 1),
(1, 2, 2),
(2, 1, 1),
(2, 2, 2);
```
