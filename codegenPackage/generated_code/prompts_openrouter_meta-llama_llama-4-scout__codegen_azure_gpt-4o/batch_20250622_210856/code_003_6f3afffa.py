"""
Generated Code Metadata:
========================
Original URL: https://mgcaugiay.com
Prompt: Design a data schema for storing information about MG car models, including their engine specifications, dimensions, and features, and suggest a suitable database management system.
Generated: DETERMINISTIC_6f3afffa3066c511
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Suggested Database Management System: PostgreSQL

-- Create a schema for storing MG car models information
CREATE TABLE mg_car_models (
    id SERIAL PRIMARY KEY, -- Unique identifier for each car model
    model_name VARCHAR(100) NOT NULL, -- Name of the car model
    year INT NOT NULL, -- Year of manufacture
    engine_type VARCHAR(50) NOT NULL, -- Type of engine (e.g., petrol, diesel, electric)
    engine_capacity DECIMAL(5, 2) NOT NULL, -- Engine capacity in liters (e.g., 1.5, 2.0)
    horsepower INT NOT NULL, -- Engine horsepower
    torque INT NOT NULL, -- Engine torque in Nm
    length_mm INT NOT NULL, -- Length of the car in millimeters
    width_mm INT NOT NULL, -- Width of the car in millimeters
    height_mm INT NOT NULL, -- Height of the car in millimeters
    features JSONB NOT NULL, -- JSON object to store additional features (e.g., {"sunroof": true, "bluetooth": true})
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Indexes for faster querying
CREATE INDEX idx_model_name ON mg_car_models(model_name);
CREATE INDEX idx_year ON mg_car_models(year);

-- Example of inserting data into the table
INSERT INTO mg_car_models (
    model_name, year, engine_type, engine_capacity, horsepower, torque, 
    length_mm, width_mm, height_mm, features
) VALUES (
    'MG Hector', 2023, 'Petrol', 1.5, 143, 250, 
    4655, 1835, 1760, '{"sunroof": true, "bluetooth": true, "airbags": 6}'
);

-- Example of querying data
SELECT * FROM mg_car_models WHERE year = 2023;

-- Example of updating data
UPDATE mg_car_models
SET features = '{"sunroof": true, "bluetooth": true, "airbags": 6, "navigation_system": true}'
WHERE model_name = 'MG Hector';

-- Example of deleting data
DELETE FROM mg_car_models WHERE model_name = 'MG Hector';
```
