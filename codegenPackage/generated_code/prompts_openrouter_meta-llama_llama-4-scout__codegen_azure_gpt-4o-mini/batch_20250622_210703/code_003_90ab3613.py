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
-- SQL script to create a database schema for storing information about electric vehicles

-- Create a database for electric vehicles
CREATE DATABASE ElectricVehiclesDB;

-- Use the created database
USE ElectricVehiclesDB;

-- Table to store information about electric vehicle models
CREATE TABLE ElectricVehicleModels (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each vehicle model
    model_name VARCHAR(100) NOT NULL, -- Name of the vehicle model
    mileage_per_charge DECIMAL(5, 2) NOT NULL, -- Mileage on a single charge in kilometers
    battery_capacity DECIMAL(5, 2) NOT NULL, -- Traction battery capacity in kWh
    price DECIMAL(10, 2) NOT NULL, -- Price of the vehicle in currency
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Index to improve search performance on model_name
CREATE INDEX idx_model_name ON ElectricVehicleModels(model_name);

-- Sample data insertion (uncomment to use)
-- INSERT INTO ElectricVehicleModels (model_name, mileage_per_charge, battery_capacity, price) VALUES
-- ('Model A', 400.00, 75.00, 35000.00),
-- ('Model B', 300.00, 50.00, 25000.00),
-- ('Model C', 500.00, 100.00, 45000.00);

-- Error handling can be implemented in application code when interacting with this database
-- Ensure to handle exceptions and validate data before insertion
```
