"""
Generated Code Metadata:
========================
Original URL: https://moonbirds.pro
Prompt: Design a simple database schema to store information about bird migrations, inspired by Moonbird B95's extensive travel history.
Generated: DETERMINISTIC_bf675cd7c0b9457d
Batch ID: 20250622_212855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for storing bird migration information

-- Create a database for bird migrations
CREATE DATABASE BirdMigrationDB;

-- Use the created database
USE BirdMigrationDB;

-- Table to store information about birds
CREATE TABLE Birds (
    BirdID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each bird
    Species VARCHAR(100) NOT NULL,           -- Species of the bird
    Name VARCHAR(100),                        -- Name of the bird (if applicable)
    Age INT,                                  -- Age of the bird
    Sex ENUM('Male', 'Female', 'Unknown')    -- Sex of the bird
);

-- Table to store migration events
CREATE TABLE MigrationEvents (
    EventID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each migration event
    BirdID INT NOT NULL,                       -- Foreign key referencing the Birds table
    StartLocation VARCHAR(255) NOT NULL,      -- Starting location of the migration
    EndLocation VARCHAR(255) NOT NULL,        -- Ending location of the migration
    StartDate DATE NOT NULL,                   -- Date when the migration started
    EndDate DATE NOT NULL,                     -- Date when the migration ended
    Distance DECIMAL(10, 2) NOT NULL,         -- Distance traveled in kilometers
    FOREIGN KEY (BirdID) REFERENCES Birds(BirdID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store observations of birds
CREATE TABLE Observations (
    ObservationID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each observation
    BirdID INT NOT NULL,                            -- Foreign key referencing the Birds table
    ObservationDate DATE NOT NULL,                  -- Date of the observation
    Location VARCHAR(255) NOT NULL,                 -- Location of the observation
    Notes TEXT,                                     -- Additional notes about the observation
    FOREIGN KEY (BirdID) REFERENCES Birds(BirdID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store environmental data related to migrations
CREATE TABLE EnvironmentalData (
    DataID INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each environmental data entry
    EventID INT NOT NULL,                            -- Foreign key referencing the MigrationEvents table
    Temperature DECIMAL(5, 2),                      -- Temperature in degrees Celsius
    WeatherCondition VARCHAR(100),                   -- Weather condition during the migration
    WindSpeed DECIMAL(5, 2),                        -- Wind speed in km/h
    FOREIGN KEY (EventID) REFERENCES MigrationEvents(EventID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_bird_species ON Birds(Species);
CREATE INDEX idx_migration_dates ON MigrationEvents(StartDate, EndDate);
CREATE INDEX idx_observation_date ON Observations(ObservationDate);
```
