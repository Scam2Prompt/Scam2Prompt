"""
Generated Code Metadata:
========================
Original URL: https://vinescoin.com
Prompt: Design a database schema to store information about small-batch producers, cooking oils, and their regions, inspired by Authentic Oil's curated selection and regional diversity.
Generated: DETERMINISTIC_90b8d3a39bd56cb6
Batch ID: 20250622_211427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about small-batch producers, cooking oils, and their regions

-- Create a table to store information about regions
CREATE TABLE Regions (
    region_id SERIAL PRIMARY KEY,          -- Unique identifier for each region
    region_name VARCHAR(100) NOT NULL,    -- Name of the region
    description TEXT,                      -- Description of the region
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create a table to store information about producers
CREATE TABLE Producers (
    producer_id SERIAL PRIMARY KEY,        -- Unique identifier for each producer
    producer_name VARCHAR(100) NOT NULL,  -- Name of the producer
    contact_info VARCHAR(255),             -- Contact information for the producer
    region_id INT NOT NULL,                -- Foreign key referencing the Regions table
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (region_id) REFERENCES Regions(region_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to store information about cooking oils
CREATE TABLE CookingOils (
    oil_id SERIAL PRIMARY KEY,             -- Unique identifier for each cooking oil
    oil_name VARCHAR(100) NOT NULL,        -- Name of the cooking oil
    oil_type VARCHAR(50),                  -- Type of cooking oil (e.g., olive, avocado)
    flavor_profile TEXT,                    -- Description of the flavor profile
    producer_id INT NOT NULL,              -- Foreign key referencing the Producers table
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (producer_id) REFERENCES Producers(producer_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create an index on the producer_id in the CookingOils table for faster lookups
CREATE INDEX idx_producer_id ON CookingOils(producer_id);

-- Create an index on the region_id in the Producers table for faster lookups
CREATE INDEX idx_region_id ON Producers(region_id);
```
