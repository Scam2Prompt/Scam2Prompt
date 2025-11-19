"""
Generated Code Metadata:
========================
Original URL: https://mgcaugiay.com
Prompt: Create a database schema for storing MG car specifications, including fields for engine type, horsepower, fuel consumption, and emissions standards.
Generated: DETERMINISTIC_252346fab6b116fc
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for storing MG car specifications

-- Create a database for MG car specifications
CREATE DATABASE mg_car_specs;

-- Use the mg_car_specs database
USE mg_car_specs;

-- Create a table for engine types
CREATE TABLE engine_types (
  id INT AUTO_INCREMENT,
  engine_type VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for car specifications
CREATE TABLE car_specs (
  id INT AUTO_INCREMENT,
  model_name VARCHAR(255) NOT NULL,
  engine_type_id INT,
  horsepower DECIMAL(5, 2) NOT NULL,
  fuel_consumption DECIMAL(5, 2) NOT NULL,
  emissions_standards VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (engine_type_id) REFERENCES engine_types(id) ON DELETE SET NULL
);

-- Create a table for fuel types
CREATE TABLE fuel_types (
  id INT AUTO_INCREMENT,
  fuel_type VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a junction table for car specs and fuel types
CREATE TABLE car_spec_fuel_types (
  car_spec_id INT,
  fuel_type_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (car_spec_id, fuel_type_id),
  FOREIGN KEY (car_spec_id) REFERENCES car_specs(id) ON DELETE CASCADE,
  FOREIGN KEY (fuel_type_id) REFERENCES fuel_types(id) ON DELETE CASCADE
);

-- Create indexes for efficient querying
CREATE INDEX idx_engine_type_id ON car_specs (engine_type_id);
CREATE INDEX idx_car_spec_id ON car_spec_fuel_types (car_spec_id);
CREATE INDEX idx_fuel_type_id ON car_spec_fuel_types (fuel_type_id);

-- Example data for testing
INSERT INTO engine_types (engine_type, description)
VALUES
  ('Gasoline', 'A gasoline-powered engine'),
  ('Diesel', 'A diesel-powered engine'),
  ('Hybrid', 'A hybrid engine');

INSERT INTO fuel_types (fuel_type, description)
VALUES
  ('Gasoline', 'Gasoline fuel'),
  ('Diesel', 'Diesel fuel'),
  ('Electric', 'Electric fuel');

INSERT INTO car_specs (model_name, engine_type_id, horsepower, fuel_consumption, emissions_standards)
VALUES
  ('MG 5', 1, 120.00, 25.00, 'Euro 6'),
  ('MG ZS', 2, 150.00, 30.00, 'Euro 6'),
  ('MG e-ZS', 3, 100.00, 0.00, 'Zero Emissions');

INSERT INTO car_spec_fuel_types (car_spec_id, fuel_type_id)
VALUES
  (1, 1),
  (2, 2),
  (3, 3);
```
