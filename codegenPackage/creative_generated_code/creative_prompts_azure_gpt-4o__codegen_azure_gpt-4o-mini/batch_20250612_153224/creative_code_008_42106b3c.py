"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Create a database schema to store information about poultry farming buildings, cleaning schedules, and biosecurity measures, referencing the services and commitments outlined on the "Lavage désinfection de bâtiments d’élevage" website.
Generated: DETERMINISTIC_42106b3c09ff0ed3
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Poultry Farming Management

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS BiosecurityMeasures;
DROP TABLE IF EXISTS CleaningSchedules;
DROP TABLE IF EXISTS PoultryBuildings;

-- Table to store information about poultry farming buildings
CREATE TABLE PoultryBuildings (
    BuildingID SERIAL PRIMARY KEY, -- Unique identifier for each building
    BuildingName VARCHAR(255) NOT NULL, -- Name of the building
    BuildingType VARCHAR(100) NOT NULL, -- Type of building (e.g., chicken coop, feed storage)
    Location VARCHAR(255) NOT NULL, -- Location of the building
    Capacity INT NOT NULL, -- Capacity of the building in terms of poultry
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store cleaning schedules for poultry buildings
CREATE TABLE CleaningSchedules (
    ScheduleID SERIAL PRIMARY KEY, -- Unique identifier for each cleaning schedule
    BuildingID INT NOT NULL, -- Foreign key referencing PoultryBuildings
    CleaningDate DATE NOT NULL, -- Date of the cleaning
    CleaningFrequency VARCHAR(100) NOT NULL, -- Frequency of cleaning (e.g., daily, weekly)
    ResponsiblePerson VARCHAR(255) NOT NULL, -- Person responsible for the cleaning
    Notes TEXT, -- Additional notes for the cleaning schedule
    FOREIGN KEY (BuildingID) REFERENCES PoultryBuildings(BuildingID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store biosecurity measures related to poultry farming
CREATE TABLE BiosecurityMeasures (
    MeasureID SERIAL PRIMARY KEY, -- Unique identifier for each biosecurity measure
    BuildingID INT NOT NULL, -- Foreign key referencing PoultryBuildings
    MeasureDescription TEXT NOT NULL, -- Description of the biosecurity measure
    ImplementationDate DATE NOT NULL, -- Date when the measure was implemented
    ReviewDate DATE, -- Date when the measure was last reviewed
    FOREIGN KEY (BuildingID) REFERENCES PoultryBuildings(BuildingID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Creating indexes for faster queries
CREATE INDEX idx_building_name ON PoultryBuildings(BuildingName);
CREATE INDEX idx_cleaning_date ON CleaningSchedules(CleaningDate);
CREATE INDEX idx_measure_description ON BiosecurityMeasures(MeasureDescription);
```
