"""
Generated Code Metadata:
========================
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Create a database schema to store information about poultry farming buildings, cleaning schedules, and biosecurity measures, referencing the services and commitments outlined on the "Lavage désinfection de bâtiments d’élevage" website.
Generated: DETERMINISTIC_42106b3c09ff0ed3
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for poultry farming management

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS BiosecurityMeasures;
DROP TABLE IF EXISTS CleaningSchedules;
DROP TABLE IF EXISTS PoultryBuildings;

-- Table to store information about poultry farming buildings
CREATE TABLE PoultryBuildings (
    BuildingID SERIAL PRIMARY KEY, -- Unique identifier for each building
    BuildingName VARCHAR(255) NOT NULL, -- Name of the building
    BuildingType VARCHAR(100) NOT NULL, -- Type of building (e.g., broiler, layer)
    Capacity INT NOT NULL, -- Capacity of the building (number of birds)
    Location VARCHAR(255), -- Location of the building
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store cleaning schedules for poultry buildings
CREATE TABLE CleaningSchedules (
    ScheduleID SERIAL PRIMARY KEY, -- Unique identifier for each cleaning schedule
    BuildingID INT NOT NULL, -- Foreign key referencing the building
    CleaningDate DATE NOT NULL, -- Date of the cleaning
    CleaningType VARCHAR(100) NOT NULL, -- Type of cleaning (e.g., deep clean, routine)
    Notes TEXT, -- Additional notes about the cleaning
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (BuildingID) REFERENCES PoultryBuildings(BuildingID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store biosecurity measures implemented in poultry buildings
CREATE TABLE BiosecurityMeasures (
    MeasureID SERIAL PRIMARY KEY, -- Unique identifier for each biosecurity measure
    BuildingID INT NOT NULL, -- Foreign key referencing the building
    MeasureDescription TEXT NOT NULL, -- Description of the biosecurity measure
    ImplementationDate DATE NOT NULL, -- Date when the measure was implemented
    EffectivenessRating INT CHECK (EffectivenessRating BETWEEN 1 AND 5), -- Effectiveness rating (1-5 scale)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (BuildingID) REFERENCES PoultryBuildings(BuildingID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_building_name ON PoultryBuildings(BuildingName);
CREATE INDEX idx_cleaning_date ON CleaningSchedules(CleaningDate);
CREATE INDEX idx_measure_description ON BiosecurityMeasures(MeasureDescription);
```
