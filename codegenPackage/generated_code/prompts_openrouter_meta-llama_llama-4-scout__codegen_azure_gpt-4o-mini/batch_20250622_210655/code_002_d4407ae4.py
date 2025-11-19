"""
Generated Code Metadata:
========================
Original URL: https://galopinautomobile.fr
Prompt: Generate a SQL database schema to store information about sports cars, including make, model, year, and condition, inspired by Galopin Automobile's vehicle listings.
Generated: DETERMINISTIC_d4407ae4b46bf64e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Sports Cars

-- Drop the table if it already exists to avoid conflicts during creation
DROP TABLE IF EXISTS SportsCars;

-- Create the SportsCars table to store information about sports cars
CREATE TABLE SportsCars (
    id SERIAL PRIMARY KEY, -- Unique identifier for each sports car
    make VARCHAR(50) NOT NULL, -- Manufacturer of the sports car
    model VARCHAR(50) NOT NULL, -- Model of the sports car
    year INT CHECK (year >= 1886 AND year <= EXTRACT(YEAR FROM CURRENT_DATE)), -- Year of manufacture, must be valid
    condition VARCHAR(20) CHECK (condition IN ('New', 'Used', 'Certified Pre-Owned')), -- Condition of the car
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Index on make and model for faster search queries
CREATE INDEX idx_make_model ON SportsCars (make, model);

-- Sample data insertion (uncomment to use)
-- INSERT INTO SportsCars (make, model, year, condition) VALUES
-- ('Ferrari', '488 GTB', 2019, 'Used'),
-- ('Porsche', '911 Carrera', 2020, 'New'),
-- ('Lamborghini', 'Huracan', 2021, 'Certified Pre-Owned');
```
