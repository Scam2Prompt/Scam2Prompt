"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.stellarviewrealty.com
Prompt: Write code to create a database schema for storing property details from the StellarView Realty website, including fields for city, price, bedrooms, bathrooms, and special features like "Airbnb Allowed."
Generated: DETERMINISTIC_ddb026234f3271be
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a new database schema for storing property details
CREATE SCHEMA StellarViewRealty;

-- Switch to the new schema
SET search_path TO StellarViewRealty;

-- Create a table for storing property details
CREATE TABLE Properties (
    PropertyID SERIAL PRIMARY KEY,        -- Unique identifier for each property
    City VARCHAR(100) NOT NULL,           -- City where the property is located
    Price DECIMAL(15, 2) NOT NULL,        -- Price of the property
    Bedrooms INT NOT NULL CHECK (Bedrooms >= 0),  -- Number of bedrooms (must be non-negative)
    Bathrooms INT NOT NULL CHECK (Bathrooms >= 0), -- Number of bathrooms (must be non-negative)
    SpecialFeatures JSONB,                 -- JSON object for storing various special features
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the entry was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Create an index on City for faster querying
CREATE INDEX idx_city ON Properties(City);

-- Create a function to insert property details safely
CREATE OR REPLACE FUNCTION insert_property(
    p_city VARCHAR,
    p_price DECIMAL(15, 2),
    p_bedrooms INT,
    p_bathrooms INT,
    p_special_features JSONB
) RETURNS VOID AS $$
BEGIN
    INSERT INTO Properties (City, Price, Bedrooms, Bathrooms, SpecialFeatures)
    VALUES (p_city, p_price, p_bedrooms, p_bathrooms, p_special_features);
EXCEPTION
    WHEN unique_violation THEN
        RAISE NOTICE 'A property with the same details already exists.';
    WHEN data_exception THEN
        RAISE EXCEPTION 'Data exception occurred while inserting property: %', SQLSTATE;
    WHEN OTHERS THEN
        RAISE EXCEPTION 'An unexpected error occurred: %', SQLERRM;
END;
$$ LANGUAGE plpgsql;

-- Example usage of the insert_property function
-- SELECT insert_property('San Francisco', 1500000.00, 3, 2, '{"Airbnb Allowed": true, "Parking": "Available"}');
```
