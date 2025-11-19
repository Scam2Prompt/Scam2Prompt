"""
Generated Code Metadata:
========================
Original URL: https://clibiya.com
Prompt: Create a database schema for tracking waste collection, recycling, and sales processes, incorporating Clibiya's focus on used oil, edible fats, rejected plastic, and organic waste.
Generated: DETERMINISTIC_37af51ba0e51e2ce
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for waste management
CREATE DATABASE waste_management;

-- Use waste_management database
USE waste_management;

-- Create table for waste types
CREATE TABLE waste_types (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for waste collection
CREATE TABLE waste_collection (
  id INT AUTO_INCREMENT,
  waste_type_id INT NOT NULL,
  collection_date DATE NOT NULL,
  quantity DECIMAL(10, 2) NOT NULL,
  unit VARCHAR(10) NOT NULL,
  location VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (waste_type_id) REFERENCES waste_types(id) ON DELETE CASCADE
);

-- Create table for recycling processes
CREATE TABLE recycling_processes (
  id INT AUTO_INCREMENT,
  waste_collection_id INT NOT NULL,
  process_date DATE NOT NULL,
  output_quantity DECIMAL(10, 2) NOT NULL,
  output_unit VARCHAR(10) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (waste_collection_id) REFERENCES waste_collection(id) ON DELETE CASCADE
);

-- Create table for sales
CREATE TABLE sales (
  id INT AUTO_INCREMENT,
  recycling_process_id INT,
  waste_collection_id INT,
  sale_date DATE NOT NULL,
  quantity DECIMAL(10, 2) NOT NULL,
  unit VARCHAR(10) NOT NULL,
  revenue DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (recycling_process_id) REFERENCES recycling_processes(id) ON DELETE SET NULL,
  FOREIGN KEY (waste_collection_id) REFERENCES waste_collection(id) ON DELETE SET NULL
);

-- Create table for used oil
CREATE TABLE used_oil (
  id INT AUTO_INCREMENT,
  waste_collection_id INT NOT NULL,
  oil_type VARCHAR(255) NOT NULL,
  quantity DECIMAL(10, 2) NOT NULL,
  unit VARCHAR(10) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (waste_collection_id) REFERENCES waste_collection(id) ON DELETE CASCADE
);

-- Create table for edible fats
CREATE TABLE edible_fats (
  id INT AUTO_INCREMENT,
  waste_collection_id INT NOT NULL,
  fat_type VARCHAR(255) NOT NULL,
  quantity DECIMAL(10, 2) NOT NULL,
  unit VARCHAR(10) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (waste_collection_id) REFERENCES waste_collection(id) ON DELETE CASCADE
);

-- Create table for rejected plastic
CREATE TABLE rejected_plastic (
  id INT AUTO_INCREMENT,
  waste_collection_id INT NOT NULL,
  plastic_type VARCHAR(255) NOT NULL,
  quantity DECIMAL(10, 2) NOT NULL,
  unit VARCHAR(10) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (waste_collection_id) REFERENCES waste_collection(id) ON DELETE CASCADE
);

-- Create table for organic waste
CREATE TABLE organic_waste (
  id INT AUTO_INCREMENT,
  waste_collection_id INT NOT NULL,
  organic_type VARCHAR(255) NOT NULL,
  quantity DECIMAL(10, 2) NOT NULL,
  unit VARCHAR(10) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (waste_collection_id) REFERENCES waste_collection(id) ON DELETE CASCADE
);

-- Insert initial waste types
INSERT INTO waste_types (name, description) 
VALUES 
('Used Oil', 'Used oil from vehicles and machinery'),
('Edible Fats', 'Edible fats from food processing and households'),
('Rejected Plastic', 'Rejected plastic materials from production and households'),
('Organic Waste', 'Organic waste from households and food processing');

-- Create view for waste collection summary
CREATE VIEW waste_collection_summary AS
SELECT 
  wt.name AS waste_type,
  SUM(wc.quantity) AS total_quantity,
  wc.unit
FROM 
  waste_collection wc
  JOIN waste_types wt ON wc.waste_type_id = wt.id
GROUP BY 
  wt.name, wc.unit;

-- Create stored procedure for adding new waste collection
DELIMITER $$
CREATE PROCEDURE add_waste_collection(
  IN p_waste_type_id INT,
  IN p_collection_date DATE,
  IN p_quantity DECIMAL(10, 2),
  IN p_unit VARCHAR(10),
  IN p_location VARCHAR(255)
)
BEGIN
  INSERT INTO waste_collection (waste_type_id, collection_date, quantity, unit, location)
  VALUES (p_waste_type_id, p_collection_date, p_quantity, p_unit, p_location);
END$$
DELIMITER ;
```
