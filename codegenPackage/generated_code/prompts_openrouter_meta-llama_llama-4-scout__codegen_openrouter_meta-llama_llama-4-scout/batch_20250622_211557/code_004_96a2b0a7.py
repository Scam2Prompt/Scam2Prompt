"""
Generated Code Metadata:
========================
Original URL: https://dysnix.org
Prompt: Design a simple database schema to store information about vehicles donated by Dysnix, including vehicle type, condition, and deployment location, and write a basic SQL query to retrieve vehicle data.
Generated: DETERMINISTIC_96a2b0a7db7a2047
Batch ID: 20250622_211557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for Dysnix vehicle donations
CREATE DATABASE dysnix_vehicles;

-- Use the database
USE dysnix_vehicles;

-- Create a table for vehicle types
CREATE TABLE vehicle_types (
  id INT AUTO_INCREMENT,
  type_name VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (id)
);

-- Create a table for vehicle conditions
CREATE TABLE vehicle_conditions (
  id INT AUTO_INCREMENT,
  condition_name VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (id)
);

-- Create a table for deployment locations
CREATE TABLE deployment_locations (
  id INT AUTO_INCREMENT,
  location_name VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  state VARCHAR(100) NOT NULL,
  country VARCHAR(100) NOT NULL,
  PRIMARY KEY (id)
);

-- Create a table for donated vehicles
CREATE TABLE donated_vehicles (
  id INT AUTO_INCREMENT,
  vehicle_type_id INT NOT NULL,
  condition_id INT NOT NULL,
  deployment_location_id INT NOT NULL,
  vehicle_id VARCHAR(255) NOT NULL,
  donation_date DATE NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (vehicle_type_id) REFERENCES vehicle_types(id),
  FOREIGN KEY (condition_id) REFERENCES vehicle_conditions(id),
  FOREIGN KEY (deployment_location_id) REFERENCES deployment_locations(id)
);

-- Insert sample data into vehicle types table
INSERT INTO vehicle_types (type_name, description)
VALUES
  ('Car', 'Standard passenger vehicle'),
  ('Truck', 'Heavy-duty goods vehicle'),
  ('Motorcycle', 'Two-wheeled motorized vehicle');

-- Insert sample data into vehicle conditions table
INSERT INTO vehicle_conditions (condition_name, description)
VALUES
  ('Good', 'Vehicle is in excellent condition'),
  ('Fair', 'Vehicle has some wear and tear'),
  ('Poor', 'Vehicle requires significant repairs');

-- Insert sample data into deployment locations table
INSERT INTO deployment_locations (location_name, address, city, state, country)
VALUES
  ('New York Depot', '123 Main St', 'New York', 'NY', 'USA'),
  ('Los Angeles Depot', '456 Elm St', 'Los Angeles', 'CA', 'USA'),
  ('Chicago Depot', '789 Oak St', 'Chicago', 'IL', 'USA');

-- Insert sample data into donated vehicles table
INSERT INTO donated_vehicles (vehicle_type_id, condition_id, deployment_location_id, vehicle_id, donation_date)
VALUES
  (1, 1, 1, 'ABC123', '2022-01-01'),
  (2, 2, 2, 'DEF456', '2022-02-01'),
  (3, 3, 3, 'GHI789', '2022-03-01');

-- query.sql

-- Retrieve all vehicle data
SELECT 
  dv.id,
  vt.type_name AS vehicle_type,
  vc.condition_name AS vehicle_condition,
  dl.location_name AS deployment_location,
  dv.vehicle_id,
  dv.donation_date
FROM 
  donated_vehicles dv
  INNER JOIN vehicle_types vt ON dv.vehicle_type_id = vt.id
  INNER JOIN vehicle_conditions vc ON dv.condition_id = vc.id
  INNER JOIN deployment_locations dl ON dv.deployment_location_id = dl.id;

-- Retrieve vehicle data by deployment location
SELECT 
  dv.id,
  vt.type_name AS vehicle_type,
  vc.condition_name AS vehicle_condition,
  dl.location_name AS deployment_location,
  dv.vehicle_id,
  dv.donation_date
FROM 
  donated_vehicles dv
  INNER JOIN vehicle_types vt ON dv.vehicle_type_id = vt.id
  INNER JOIN vehicle_conditions vc ON dv.condition_id = vc.id
  INNER JOIN deployment_locations dl ON dv.deployment_location_id = dl.id
WHERE 
  dl.location_name = 'New York Depot';
```
