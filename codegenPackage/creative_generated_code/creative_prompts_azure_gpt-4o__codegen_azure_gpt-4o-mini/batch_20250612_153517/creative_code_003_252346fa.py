"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mgcaugiay.com
Prompt: Create a database schema for storing MG car specifications, including fields for engine type, horsepower, fuel consumption, and emissions standards.
Generated: DETERMINISTIC_252346fab6b116fc
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing MG car specifications
CREATE TABLE mg_car_specifications (
    id SERIAL PRIMARY KEY, -- Unique identifier for each car specification
    model_name VARCHAR(100) NOT NULL, -- Name of the car model
    engine_type VARCHAR(50) NOT NULL, -- Type of engine (e.g., Petrol, Diesel, Electric)
    horsepower INT CHECK (horsepower > 0), -- Horsepower of the engine, must be a positive integer
    fuel_consumption DECIMAL(5,2) CHECK (fuel_consumption >= 0), -- Fuel consumption in liters per 100km, must be non-negative
    emissions_standards VARCHAR(50) NOT NULL, -- Emission standards met by the car (e.g., Euro 6, LEV)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Index for quick lookups by model name
CREATE INDEX idx_model_name ON mg_car_specifications(model_name);

-- Sample insert statement for adding a new MG car specification
-- INSERT INTO mg_car_specifications (model_name, engine_type, horsepower, fuel_consumption, emissions_standards)
-- VALUES ('MG ZS', 'Petrol', 120, 6.5, 'Euro 6');
```
