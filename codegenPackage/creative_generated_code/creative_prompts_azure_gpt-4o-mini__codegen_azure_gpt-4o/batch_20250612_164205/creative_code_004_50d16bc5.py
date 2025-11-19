"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://t528.com
Prompt: Illustrate how to use the data from 星飞园 to create a database schema for storing aircraft cargo specifications, including fields for aircraft type, cargo dimensions, and container capacity.
Generated: DETERMINISTIC_50d16bc5c9ca975e
Batch ID: 20250612_164205
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for storing aircraft cargo specifications
-- The database schema includes tables for aircraft types, cargo dimensions, and container capacity.

-- Create a table to store aircraft types
CREATE TABLE Aircraft (
    AircraftID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each aircraft type
    AircraftType VARCHAR(100) NOT NULL,        -- Name or model of the aircraft
    Manufacturer VARCHAR(100),                 -- Manufacturer's name
    MaxPayload INT,                            -- Maximum payload capacity in kilograms
    Range INT                                  -- Maximum range of the aircraft in kilometers
);

-- Create a table to store cargo dimensions for each aircraft
CREATE TABLE CargoDimensions (
    DimensionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for dimensions
    AircraftID INT NOT NULL,                    -- Foreign key referencing the Aircraft table
    Length DECIMAL(10, 2) NOT NULL,             -- Length of cargo space in meters
    Width DECIMAL(10, 2) NOT NULL,              -- Width of cargo space in meters
    Height DECIMAL(10, 2) NOT NULL,             -- Height of cargo space in meters
    Volume DECIMAL(15, 2) GENERATED ALWAYS AS (Length * Width * Height), -- Automatically calculated volume in cubic meters
    FOREIGN KEY (AircraftID) REFERENCES Aircraft(AircraftID)             -- Enforces relationship between CargoDimensions and Aircraft
);

-- Create a table to store container capacity specifications
CREATE TABLE ContainerCapacity (
    ContainerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each container type
    AircraftID INT NOT NULL,                    -- Foreign key referencing the Aircraft table
    ContainerType VARCHAR(50) NOT NULL,         -- Type or category of the container
    MaxContainers INT NOT NULL,                 -- Maximum number of containers the aircraft can carry
    MaxWeightPerContainer INT NOT NULL,         -- Maximum weight per container in kilograms
    FOREIGN KEY (AircraftID) REFERENCES Aircraft(AircraftID)             -- Enforces relationship between ContainerCapacity and Aircraft
);

-- Ensure the database adheres to best practices:
-- Use transactions for critical operations on this schema to maintain integrity.
-- Index AircraftID fields for faster lookups in related tables.
-- Avoid storing redundant data by normalizing the schema.

-- Example indices for faster queries
CREATE INDEX idx_aircraft_type ON Aircraft(AircraftType);
CREATE INDEX idx_cargo_aircraft ON CargoDimensions(AircraftID);
CREATE INDEX idx_container_aircraft ON ContainerCapacity(AircraftID);
```
