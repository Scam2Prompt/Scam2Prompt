"""
Generated Code Metadata:
========================
Original URL: https://vaperiyadh2.com
Prompt: "Design a simple database schema to store information about vape products, including devices, e-liquids, and coils."
Generated: DETERMINISTIC_6e8a0afcc7bf07e7
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for vape products
CREATE DATABASE vape_products;

-- Use the vape_products database
USE vape_products;

-- Create a table for manufacturers
CREATE TABLE manufacturers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for vape devices
CREATE TABLE devices (
  id INT AUTO_INCREMENT,
  manufacturer_id INT,
  model_name VARCHAR(255) NOT NULL,
  description TEXT,
  wattage_range VARCHAR(255),
  battery_capacity INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(id) ON DELETE CASCADE
);

-- Create a table for e-liquid flavors
CREATE TABLE e_liquid_flavors (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for e-liquid products
CREATE TABLE e_liquids (
  id INT AUTO_INCREMENT,
  manufacturer_id INT,
  flavor_id INT,
  name VARCHAR(255) NOT NULL,
  pg_percentage DECIMAL(5,2),
  vg_percentage DECIMAL(5,2),
  nicotine_level DECIMAL(5,2),
  bottle_size DECIMAL(5,2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(id) ON DELETE CASCADE,
  FOREIGN KEY (flavor_id) REFERENCES e_liquid_flavors(id) ON DELETE CASCADE
);

-- Create a table for coil types
CREATE TABLE coil_types (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for coils
CREATE TABLE coils (
  id INT AUTO_INCREMENT,
  manufacturer_id INT,
  coil_type_id INT,
  resistance DECIMAL(5,2),
  wattage_range VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(id) ON DELETE CASCADE,
  FOREIGN KEY (coil_type_id) REFERENCES coil_types(id) ON DELETE CASCADE
);
```

```sql
-- example_data.sql

-- Insert some example data into the database
INSERT INTO manufacturers (name, description) 
VALUES 
('NJOY', 'A well-known vape manufacturer'),
('Blu', 'Another popular vape brand');

INSERT INTO devices (manufacturer_id, model_name, description, wattage_range, battery_capacity) 
VALUES 
(1, 'NJOY Ace', 'A popular vape device', '10-20W', 2000),
(2, 'Blu Vape', 'A simple vape device', '5-15W', 1500);

INSERT INTO e_liquid_flavors (name, description) 
VALUES 
('Tobacco', 'A classic tobacco flavor'),
('Mango', 'A sweet and fruity flavor');

INSERT INTO e_liquids (manufacturer_id, flavor_id, name, pg_percentage, vg_percentage, nicotine_level, bottle_size) 
VALUES 
(1, 1, 'NJOY Tobacco', 50.00, 50.00, 12.00, 30.00),
(2, 2, 'Blu Mango', 30.00, 70.00, 18.00, 60.00);

INSERT INTO coil_types (name, description) 
VALUES 
('Single Coil', 'A basic single coil'),
('Dual Coil', 'A more powerful dual coil');

INSERT INTO coils (manufacturer_id, coil_type_id, resistance, wattage_range) 
VALUES 
(1, 1, 1.20, '10-20W'),
(2, 2, 0.80, '20-30W');
```
