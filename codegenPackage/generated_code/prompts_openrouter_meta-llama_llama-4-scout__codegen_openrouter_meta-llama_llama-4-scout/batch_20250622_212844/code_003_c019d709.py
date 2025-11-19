"""
Generated Code Metadata:
========================
Original URL: https://www.gardenpathquilts.com
Prompt: Design a database schema for storing quilt designs, including fields for quilt type, dimensions, and fabric requirements.
Generated: DETERMINISTIC_c019d709317c3838
Batch ID: 20250622_212844
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for quilt designs
CREATE DATABASE quilt_designs;

-- Use the quilt_designs database
USE quilt_designs;

-- Create a table for quilt types
CREATE TABLE quilt_types (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_quilt_type_name` (`name`)
);

-- Create a table for fabrics
CREATE TABLE fabrics (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `color` VARCHAR(255) NOT NULL,
  `fabric_type` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_fabric_name_color` (`name`, `color`)
);

-- Create a table for quilt designs
CREATE TABLE quilt_designs (
  `id` INT AUTO_INCREMENT,
  `quilt_type_id` INT NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `width` DECIMAL(10, 2) NOT NULL,
  `length` DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`quilt_type_id`) REFERENCES quilt_types(`id`)
);

-- Create a table for fabric requirements
CREATE TABLE fabric_requirements (
  `id` INT AUTO_INCREMENT,
  `quilt_design_id` INT NOT NULL,
  `fabric_id` INT NOT NULL,
  `quantity` DECIMAL(10, 2) NOT NULL,
  `units` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`quilt_design_id`) REFERENCES quilt_designs(`id`),
  FOREIGN KEY (`fabric_id`) REFERENCES fabrics(`id`)
);

-- Create a table for quilt design blocks
CREATE TABLE quilt_design_blocks (
  `id` INT AUTO_INCREMENT,
  `quilt_design_id` INT NOT NULL,
  `block_name` VARCHAR(255) NOT NULL,
  `block_description` TEXT,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`quilt_design_id`) REFERENCES quilt_designs(`id`)
);

-- Create a table for block fabric requirements
CREATE TABLE block_fabric_requirements (
  `id` INT AUTO_INCREMENT,
  `quilt_design_block_id` INT NOT NULL,
  `fabric_id` INT NOT NULL,
  `quantity` DECIMAL(10, 2) NOT NULL,
  `units` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`quilt_design_block_id`) REFERENCES quilt_design_blocks(`id`),
  FOREIGN KEY (`fabric_id`) REFERENCES fabrics(`id`)
);

-- Example data
INSERT INTO quilt_types (name, description)
VALUES 
('Lap Quilt', 'A small quilt for lap use'),
('Twin Quilt', 'A quilt for a twin-sized bed');

INSERT INTO fabrics (name, color, fabric_type)
VALUES 
('Cotton', 'Blue', 'Solid'),
('Cotton', 'Red', 'Print');

INSERT INTO quilt_designs (quilt_type_id, name, description, width, length)
VALUES 
(1, 'Simple Lap Quilt', 'A simple lap quilt', 30.00, 40.00),
(2, 'Striped Twin Quilt', 'A striped quilt for a twin bed', 60.00, 90.00);

INSERT INTO fabric_requirements (quilt_design_id, fabric_id, quantity, units)
VALUES 
(1, 1, 2.00, 'yards'),
(1, 2, 1.00, 'yards'),
(2, 1, 4.00, 'yards'),
(2, 2, 2.00, 'yards');

INSERT INTO quilt_design_blocks (quilt_design_id, block_name, block_description)
VALUES 
(1, 'Simple Block', 'A simple block'),
(2, 'Striped Block', 'A striped block');

INSERT INTO block_fabric_requirements (quilt_design_block_id, fabric_id, quantity, units)
VALUES 
(1, 1, 1.00, 'yards'),
(1, 2, 0.50, 'yards'),
(2, 1, 2.00, 'yards'),
(2, 2, 1.00, 'yards');
```
