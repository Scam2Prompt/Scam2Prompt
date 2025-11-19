"""
Generated Code Metadata:
========================
Original URL: https://tdkco.ir
Prompt: "Design a database schema to store information about car bearings, including product codes, vehicle models, and technical specifications, as used by یاتاقان گلدن."
Generated: DETERMINISTIC_5b31b612a78f0f77
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about car bearings

CREATE TABLE VehicleModels (
    id SERIAL PRIMARY KEY, -- Unique identifier for each vehicle model
    make VARCHAR(50) NOT NULL, -- Manufacturer of the vehicle
    model VARCHAR(50) NOT NULL, -- Model of the vehicle
    year INT CHECK (year > 1885 AND year <= EXTRACT(YEAR FROM CURRENT_DATE)), -- Year of manufacture
    UNIQUE (make, model, year) -- Ensure no duplicate vehicle models for the same year
);

CREATE TABLE TechnicalSpecifications (
    id SERIAL PRIMARY KEY, -- Unique identifier for each technical specification
    bearing_code VARCHAR(50) NOT NULL, -- Unique product code for the bearing
    inner_diameter DECIMAL(10, 2) NOT NULL, -- Inner diameter of the bearing in mm
    outer_diameter DECIMAL(10, 2) NOT NULL, -- Outer diameter of the bearing in mm
    width DECIMAL(10, 2) NOT NULL, -- Width of the bearing in mm
    material VARCHAR(50) NOT NULL, -- Material of the bearing
    load_capacity DECIMAL(10, 2) NOT NULL, -- Load capacity in kg
    UNIQUE (bearing_code) -- Ensure unique product codes
);

CREATE TABLE CarBearings (
    id SERIAL PRIMARY KEY, -- Unique identifier for each car bearing entry
    bearing_code VARCHAR(50) NOT NULL, -- Foreign key referencing TechnicalSpecifications
    vehicle_model_id INT NOT NULL, -- Foreign key referencing VehicleModels
    FOREIGN KEY (bearing_code) REFERENCES TechnicalSpecifications(bearing_code) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (vehicle_model_id) REFERENCES VehicleModels(id) ON DELETE CASCADE, -- Ensure referential integrity
    UNIQUE (bearing_code, vehicle_model_id) -- Ensure a bearing is not duplicated for the same vehicle model
);

-- Indexes for performance optimization
CREATE INDEX idx_vehicle_model ON VehicleModels(make, model, year);
CREATE INDEX idx_bearing_code ON TechnicalSpecifications(bearing_code);
CREATE INDEX idx_car_bearings ON CarBearings(bearing_code, vehicle_model_id);
```
