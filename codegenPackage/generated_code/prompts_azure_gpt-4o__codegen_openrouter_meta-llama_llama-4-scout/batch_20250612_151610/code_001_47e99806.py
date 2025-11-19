"""
Generated Code Metadata:
========================
Original URL: https://trackdieselperu.com
Prompt: Generate a database schema in SQL to store and manage high-quality machinery parts and accessories, including fields for brand (e.g., FIATALLIS, KOMATSU), part type, quality certification, and supplier details.
Generated: DETERMINISTIC_47e998067eb6058e
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- machinery_parts_schema.sql

-- Create a database for machinery parts
CREATE DATABASE IF NOT EXISTS machinery_parts;

-- Use the machinery_parts database
USE machinery_parts;

-- Create a table for brands
CREATE TABLE IF NOT EXISTS brands (
  brand_id INT AUTO_INCREMENT,
  brand_name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (brand_id),
  UNIQUE KEY (brand_name)
);

-- Create a table for part types
CREATE TABLE IF NOT EXISTS part_types (
  part_type_id INT AUTO_INCREMENT,
  part_type_name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (part_type_id),
  UNIQUE KEY (part_type_name)
);

-- Create a table for quality certifications
CREATE TABLE IF NOT EXISTS quality_certifications (
  certification_id INT AUTO_INCREMENT,
  certification_name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (certification_id),
  UNIQUE KEY (certification_name)
);

-- Create a table for suppliers
CREATE TABLE IF NOT EXISTS suppliers (
  supplier_id INT AUTO_INCREMENT,
  supplier_name VARCHAR(255) NOT NULL,
  contact_name VARCHAR(255) NOT NULL,
  contact_email VARCHAR(255) NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (supplier_id)
);

-- Create a table for machinery parts
CREATE TABLE IF NOT EXISTS machinery_parts (
  part_id INT AUTO_INCREMENT,
  brand_id INT NOT NULL,
  part_type_id INT NOT NULL,
  part_number VARCHAR(255) NOT NULL,
  part_description TEXT,
  certification_id INT,
  supplier_id INT NOT NULL,
  unit_price DECIMAL(10, 2) NOT NULL,
  stock_quantity INT NOT NULL DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (part_id),
  FOREIGN KEY (brand_id) REFERENCES brands(brand_id),
  FOREIGN KEY (part_type_id) REFERENCES part_types(part_type_id),
  FOREIGN KEY (certification_id) REFERENCES quality_certifications(certification_id),
  FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

-- Create a table for part accessories
CREATE TABLE IF NOT EXISTS part_accessories (
  accessory_id INT AUTO_INCREMENT,
  part_id INT NOT NULL,
  accessory_name VARCHAR(255) NOT NULL,
  accessory_description TEXT,
  unit_price DECIMAL(10, 2) NOT NULL,
  stock_quantity INT NOT NULL DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (accessory_id),
  FOREIGN KEY (part_id) REFERENCES machinery_parts(part_id)
);

-- Create indexes for faster queries
CREATE INDEX idx_brand_name ON brands (brand_name);
CREATE INDEX idx_part_type_name ON part_types (part_type_name);
CREATE INDEX idx_certification_name ON quality_certifications (certification_name);
CREATE INDEX idx_supplier_name ON suppliers (supplier_name);
CREATE INDEX idx_part_number ON machinery_parts (part_number);
```

```sql
-- Example usage:
-- Insert some sample data
INSERT INTO brands (brand_name) VALUES ('FIATALLIS');
INSERT INTO brands (brand_name) VALUES ('KOMATSU');

INSERT INTO part_types (part_type_name) VALUES ('Engine');
INSERT INTO part_types (part_type_name) VALUES ('Transmission');

INSERT INTO quality_certifications (certification_name) VALUES ('ISO 9001');
INSERT INTO quality_certifications (certification_name) VALUES ('CE');

INSERT INTO suppliers (supplier_name, contact_name, contact_email, phone_number, address)
VALUES ('Supplier 1', 'John Doe', 'john.doe@example.com', '123-456-7890', '123 Main St');

INSERT INTO machinery_parts (brand_id, part_type_id, part_number, part_description, certification_id, supplier_id, unit_price, stock_quantity)
VALUES (1, 1, 'FIATALLIS-123', 'Engine part', 1, 1, 100.00, 10);

INSERT INTO part_accessories (part_id, accessory_name, accessory_description, unit_price, stock_quantity)
VALUES (1, 'Accessory 1', 'Accessory description', 20.00, 5);
```
