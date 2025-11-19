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
-- Database schema for storing MG car specifications

CREATE TABLE mg_car_specifications (
    id SERIAL PRIMARY KEY, -- Unique identifier for each car specification
    model_name VARCHAR(100) NOT NULL, -- Name of the car model
    engine_type VARCHAR(50) NOT NULL, -- Type of engine (e.g., petrol, diesel, electric)
    horsepower INT NOT NULL CHECK (horsepower > 0), -- Engine horsepower, must be a positive integer
    fuel_consumption DECIMAL(5, 2) NOT NULL CHECK (fuel_consumption >= 0), -- Fuel consumption in liters per 100 km
    emissions_standards VARCHAR(50) NOT NULL, -- Emissions standards (e.g., Euro 6, LEV III)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Index for faster querying by model name
CREATE INDEX idx_model_name ON mg_car_specifications (model_name);

-- Example of inserting a record into the table
-- INSERT INTO mg_car_specifications (model_name, engine_type, horsepower, fuel_consumption, emissions_standards)
-- VALUES ('MG ZS EV', 'Electric', 143, 0.00, 'Euro 6');

-- Note: Ensure to handle exceptions and errors in your application code when interacting with this database schema.
```
