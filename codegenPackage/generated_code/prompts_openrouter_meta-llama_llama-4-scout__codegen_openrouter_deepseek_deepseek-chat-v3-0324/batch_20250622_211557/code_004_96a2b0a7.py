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
-- Database schema for Dysnix vehicle donations

-- Create the database
CREATE DATABASE IF NOT EXISTS dysnix_vehicle_donations;
USE dysnix_vehicle_donations;

-- Table to store vehicle types
CREATE TABLE IF NOT EXISTS vehicle_types (
    id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store vehicle conditions
CREATE TABLE IF NOT EXISTS vehicle_conditions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    condition_name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store deployment locations
CREATE TABLE IF NOT EXISTS deployment_locations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    location_name VARCHAR(100) NOT NULL,
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(50) DEFAULT 'USA',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Main table to store vehicle information
CREATE TABLE IF NOT EXISTS vehicles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    vin VARCHAR(17) UNIQUE NOT NULL,
    make VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year INT NOT NULL,
    type_id INT NOT NULL,
    condition_id INT NOT NULL,
    location_id INT,
    donation_date DATE NOT NULL,
    notes TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (type_id) REFERENCES vehicle_types(id),
    FOREIGN KEY (condition_id) REFERENCES vehicle_conditions(id),
    FOREIGN KEY (location_id) REFERENCES deployment_locations(id)
);

-- Sample data insertion
INSERT INTO vehicle_types (type_name, description) VALUES
('Sedan', 'Standard passenger car'),
('SUV', 'Sport utility vehicle'),
('Truck', 'Pickup truck'),
('Van', 'Passenger or cargo van');

INSERT INTO vehicle_conditions (condition_name, description) VALUES
('New', 'Brand new vehicle'),
('Excellent', 'Like new condition'),
('Good', 'Minor wear and tear'),
('Fair', 'Needs some repairs'),
('Poor', 'Needs significant work');

INSERT INTO deployment_locations (location_name, city, state) VALUES
('Headquarters', 'San Francisco', 'CA'),
('Regional Office', 'Austin', 'TX'),
('Field Office', 'Denver', 'CO');

-- Basic SQL query to retrieve vehicle data
SELECT 
    v.id,
    v.vin,
    v.make,
    v.model,
    v.year,
    vt.type_name AS vehicle_type,
    vc.condition_name AS condition,
    dl.location_name AS deployment_location,
    dl.city,
    dl.state,
    v.donation_date,
    v.notes,
    v.is_active
FROM 
    vehicles v
JOIN 
    vehicle_types vt ON v.type_id = vt.id
JOIN 
    vehicle_conditions vc ON v.condition_id = vc.id
LEFT JOIN 
    deployment_locations dl ON v.location_id = dl.id
WHERE 
    v.is_active = TRUE
ORDER BY 
    v.donation_date DESC;
```
