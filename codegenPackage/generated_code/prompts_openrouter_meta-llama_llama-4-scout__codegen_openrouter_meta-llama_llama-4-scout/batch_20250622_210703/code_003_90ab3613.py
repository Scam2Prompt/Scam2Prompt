"""
Generated Code Metadata:
========================
Original URL: https://econtrolsa.ch
Prompt: "Design a simple database schema to store information about electric vehicles, including their mileage on a single charge, traction battery capacity, and price, inspired by the car models listed on eControl SA's website."
Generated: DETERMINISTIC_90ab361378e6b8b5
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- electric_vehicle_schema.sql

-- Create a database schema for electric vehicles
CREATE DATABASE electric_vehicle_db;

-- Use the electric vehicle database
USE electric_vehicle_db;

-- Create a table for electric vehicle manufacturers
CREATE TABLE manufacturers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY (name)
);

-- Create a table for electric vehicle models
CREATE TABLE models (
  id INT AUTO_INCREMENT,
  manufacturer_id INT NOT NULL,
  model_name VARCHAR(255) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(id)
);

-- Create a table for electric vehicle specifications
CREATE TABLE specifications (
  id INT AUTO_INCREMENT,
  model_id INT NOT NULL,
  mileage_on_single_charge DECIMAL(5, 2) NOT NULL,  -- in km
  traction_battery_capacity DECIMAL(10, 2) NOT NULL,  -- in kWh
  price DECIMAL(15, 2) NOT NULL,  -- in local currency
  PRIMARY KEY (id),
  FOREIGN KEY (model_id) REFERENCES models(id)
);

-- Create a table for electric vehicle variants
CREATE TABLE variants (
  id INT AUTO_INCREMENT,
  specification_id INT NOT NULL,
  trim_level VARCHAR(255) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (specification_id) REFERENCES specifications(id)
);

-- Insert sample data
INSERT INTO manufacturers (name)
VALUES
  ('Tesla'),
  ('Nissan'),
  ('BMW');

INSERT INTO models (manufacturer_id, model_name)
VALUES
  (1, 'Model 3'),
  (1, 'Model S'),
  (2, 'Leaf'),
  (3, 'i3');

INSERT INTO specifications (model_id, mileage_on_single_charge, traction_battery_capacity, price)
VALUES
  (1, 560.00, 60.00, 45000.00),
  (2, 610.00, 100.00, 80000.00),
  (3, 320.00, 40.00, 30000.00),
  (4, 310.00, 42.20, 35000.00);

INSERT INTO variants (specification_id, trim_level)
VALUES
  (1, 'Standard Range'),
  (1, 'Long Range'),
  (2, 'Long Range'),
  (3, 'Base'),
  (4, 'Base');

-- Example query to retrieve electric vehicle information
SELECT 
  m.model_name,
  s.mileage_on_single_charge,
  s.traction_battery_capacity,
  s.price,
  v.trim_level
FROM 
  models m
  JOIN specifications s ON m.id = s.model_id
  JOIN variants v ON s.id = v.specification_id;
```
