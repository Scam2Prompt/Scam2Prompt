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
-- SQL Schema for MG Car Models

-- Create a table for storing car models
CREATE TABLE CarModels (
    id SERIAL PRIMARY KEY, -- Unique identifier for each car model
    model_name VARCHAR(100) NOT NULL, -- Name of the car model
    year INT NOT NULL CHECK (year > 1885), -- Year of manufacture, must be a valid year
    engine_type VARCHAR(50) NOT NULL, -- Type of engine (e.g., Petrol, Diesel, Electric)
    horsepower INT NOT NULL CHECK (horsepower > 0), -- Engine horsepower
    torque INT NOT NULL CHECK (torque > 0), -- Engine torque in Nm
    length DECIMAL(5,2) NOT NULL CHECK (length > 0), -- Length of the car in meters
    width DECIMAL(5,2) NOT NULL CHECK (width > 0), -- Width of the car in meters
    height DECIMAL(5,2) NOT NULL CHECK (height > 0), -- Height of the car in meters
    weight DECIMAL(6,2) NOT NULL CHECK (weight > 0), -- Weight of the car in kg
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table for storing features associated with each car model
CREATE TABLE CarFeatures (
    id SERIAL PRIMARY KEY, -- Unique identifier for each feature
    car_model_id INT NOT NULL, -- Foreign key referencing CarModels
    feature_name VARCHAR(100) NOT NULL, -- Name of the feature (e.g., Sunroof, Navigation)
    description TEXT, -- Description of the feature
    FOREIGN KEY (car_model_id) REFERENCES CarModels(id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for storing engine specifications
CREATE TABLE EngineSpecifications (
    id SERIAL PRIMARY KEY, -- Unique identifier for each engine specification
    car_model_id INT NOT NULL, -- Foreign key referencing CarModels
    displacement DECIMAL(5,2) NOT NULL CHECK (displacement > 0), -- Engine displacement in liters
    fuel_efficiency DECIMAL(5,2) NOT NULL CHECK (fuel_efficiency > 0), -- Fuel efficiency in L/100km
    FOREIGN KEY (car_model_id) REFERENCES CarModels(id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Suggested Database Management System: PostgreSQL
-- PostgreSQL is a powerful, open-source object-relational database system that is well-suited for this schema.
```
