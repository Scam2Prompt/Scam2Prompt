"""
Generated Code Metadata:
========================
Original URL: https://wealthbhai.com
Prompt: Design a simple database schema for storing information about stainless steel clean tube products, including material, specification, and application industry.
Generated: DETERMINISTIC_1265f0d39ed805ee
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- stainless_steel_tube_schema.sql

-- Create a database schema for stainless steel clean tube products

CREATE DATABASE stainless_steel_tube;

USE stainless_steel_tube;

-- Material table to store information about different materials
CREATE TABLE materials (
  material_id INT AUTO_INCREMENT,
  material_name VARCHAR(255) NOT NULL,
  material_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (material_id)
);

-- Specification table to store information about different specifications
CREATE TABLE specifications (
  specification_id INT AUTO_INCREMENT,
  specification_name VARCHAR(255) NOT NULL,
  specification_description TEXT,
  diameter DECIMAL(10, 2),
  thickness DECIMAL(10, 2),
  length DECIMAL(10, 2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (specification_id)
);

-- Application industry table to store information about different industries
CREATE TABLE industries (
  industry_id INT AUTO_INCREMENT,
  industry_name VARCHAR(255) NOT NULL,
  industry_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (industry_id)
);

-- Stainless steel clean tube products table
CREATE TABLE stainless_steel_tubes (
  tube_id INT AUTO_INCREMENT,
  material_id INT,
  specification_id INT,
  industry_id INT,
  product_name VARCHAR(255) NOT NULL,
  product_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (tube_id),
  FOREIGN KEY (material_id) REFERENCES materials(material_id) ON DELETE CASCADE,
  FOREIGN KEY (specification_id) REFERENCES specifications(specification_id) ON DELETE CASCADE,
  FOREIGN KEY (industry_id) REFERENCES industries(industry_id) ON DELETE CASCADE
);

-- Indexing for better query performance
CREATE INDEX idx_material_id ON stainless_steel_tubes(material_id);
CREATE INDEX idx_specification_id ON stainless_steel_tubes(specification_id);
CREATE INDEX idx_industry_id ON stainless_steel_tubes(industry_id);

-- Example data insertion
INSERT INTO materials (material_name, material_description)
VALUES 
('304L', 'Low-carbon 304 stainless steel'),
('316L', 'Low-carbon 316 stainless steel');

INSERT INTO specifications (specification_name, diameter, thickness, length)
VALUES 
('Tube-1', 10.00, 1.00, 1000.00),
('Tube-2', 20.00, 2.00, 2000.00);

INSERT INTO industries (industry_name, industry_description)
VALUES 
('Pharmaceutical', 'Pharmaceutical industry'),
('Food Processing', 'Food processing industry');

INSERT INTO stainless_steel_tubes (material_id, specification_id, industry_id, product_name, product_description)
VALUES 
(1, 1, 1, '304L Tube', '304L stainless steel tube for pharmaceutical industry'),
(2, 2, 2, '316L Tube', '316L stainless steel tube for food processing industry');
```
