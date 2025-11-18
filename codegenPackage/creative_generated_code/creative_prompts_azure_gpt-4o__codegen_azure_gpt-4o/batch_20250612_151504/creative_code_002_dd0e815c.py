"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://t528.com
Prompt: Generate code to create a database schema for storing aircraft cargo specifications, including fields for cargo door dimensions, compartment sizes, and maximum container capacity, based on the data provided for the A380 and Boeing 787-10 models on the 星飞园 website.
Generated: DETERMINISTIC_dd0e815c58b132ba
Batch ID: 20250612_151504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing aircraft cargo specifications
-- This schema is designed to store cargo specifications for different aircraft models,
-- including fields for cargo door dimensions, compartment sizes, and maximum container capacity.

CREATE DATABASE AircraftCargoSpecifications;

USE AircraftCargoSpecifications;

-- Table to store aircraft information
CREATE TABLE Aircraft (
    AircraftID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each aircraft
    ModelName VARCHAR(50) NOT NULL,           -- Aircraft model name (e.g., A380, Boeing 787-10)
    Manufacturer VARCHAR(50) NOT NULL         -- Aircraft manufacturer (e.g., Airbus, Boeing)
);

-- Table to store cargo door specifications
CREATE TABLE CargoDoorDimensions (
    CargoDoorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each cargo door specification
    AircraftID INT NOT NULL,                   -- Foreign key referencing the Aircraft table
    Width FLOAT NOT NULL,                      -- Width of the cargo door in meters
    Height FLOAT NOT NULL,                     -- Height of the cargo door in meters
    FOREIGN KEY (AircraftID) REFERENCES Aircraft(AircraftID) ON DELETE CASCADE
);

-- Table to store compartment size specifications
CREATE TABLE CompartmentSizes (
    CompartmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each compartment specification
    AircraftID INT NOT NULL,                     -- Foreign key referencing the Aircraft table
    Length FLOAT NOT NULL,                       -- Length of the compartment in meters
    Width FLOAT NOT NULL,                        -- Width of the compartment in meters
    Height FLOAT NOT NULL,                       -- Height of the compartment in meters
    FOREIGN KEY (AircraftID) REFERENCES Aircraft(AircraftID) ON DELETE CASCADE
);

-- Table to store maximum container capacity
CREATE TABLE ContainerCapacity (
    CapacityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each capacity specification
    AircraftID INT NOT NULL,                   -- Foreign key referencing the Aircraft table
    MaxContainers INT NOT NULL,                -- Maximum number of containers the aircraft can carry
    FOREIGN KEY (AircraftID) REFERENCES Aircraft(AircraftID) ON DELETE CASCADE
);

-- Insert example data for A380 and Boeing 787-10
INSERT INTO Aircraft (ModelName, Manufacturer)
VALUES 
    ('A380', 'Airbus'),
    ('Boeing 787-10', 'Boeing');

INSERT INTO CargoDoorDimensions (AircraftID, Width, Height)
VALUES
    (1, 3.7, 2.5),  -- Example dimensions for A380
    (2, 3.4, 2.3);  -- Example dimensions for Boeing 787-10

INSERT INTO CompartmentSizes (AircraftID, Length, Width, Height)
VALUES
    (1, 30.0, 5.0, 4.0),  -- Example compartment size for A380
    (2, 28.0, 4.8, 3.8);  -- Example compartment size for Boeing 787-10

INSERT INTO ContainerCapacity (AircraftID, MaxContainers)
VALUES
    (1, 150),  -- Example maximum container capacity for A380
    (2, 120);  -- Example maximum container capacity for Boeing 787-10

-- Ensure proper indexing for faster queries
CREATE INDEX idx_aircraft_model ON Aircraft(ModelName);
CREATE INDEX idx_cargo_door_aircraft ON CargoDoorDimensions(AircraftID);
CREATE INDEX idx_compartment_aircraft ON CompartmentSizes(AircraftID);
CREATE INDEX idx_container_capacity_aircraft ON ContainerCapacity(AircraftID);

-- Schema creation complete.
```
