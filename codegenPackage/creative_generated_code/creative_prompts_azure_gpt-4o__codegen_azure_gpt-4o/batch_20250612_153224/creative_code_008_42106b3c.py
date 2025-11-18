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
-- Database schema for poultry farming buildings, cleaning schedules, and biosecurity measures.

-- Create a table to store information about the poultry farming buildings.
CREATE TABLE PoultryBuildings (
    BuildingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each building
    Name VARCHAR(255) NOT NULL,                -- Name/label of the building
    Location VARCHAR(255) NOT NULL,            -- Location of the building
    Capacity INT NOT NULL,                     -- Maximum capacity of the building (e.g., number of birds)
    Description TEXT,                          -- Additional details about the building
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the building record was created
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Create a table to store cleaning schedules for the buildings.
CREATE TABLE CleaningSchedules (
    ScheduleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each cleaning schedule
    BuildingID INT NOT NULL,                   -- Foreign key referencing PoultryBuildings.BuildingID
    CleaningDate DATE NOT NULL,                -- Scheduled cleaning date
    CleaningType ENUM('Washing', 'Disinfection', 'Both') NOT NULL, -- Type of cleaning
    Notes TEXT,                                -- Additional notes about the cleaning schedule
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the schedule record was created
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the record was last updated
    FOREIGN KEY (BuildingID) REFERENCES PoultryBuildings(BuildingID) ON DELETE CASCADE
);

-- Create a table to store biosecurity measures implemented for the buildings.
CREATE TABLE BiosecurityMeasures (
    MeasureID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each biosecurity measure
    BuildingID INT NOT NULL,                   -- Foreign key referencing PoultryBuildings.BuildingID
    MeasureName VARCHAR(255) NOT NULL,         -- Name of the biosecurity measure (e.g., "Footbath", "Rodent Control")
    Description TEXT NOT NULL,                 -- Detailed description of the measure
    ImplementationDate DATE NOT NULL,          -- Date the measure was implemented
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the measure record was created
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the record was last updated
    FOREIGN KEY (BuildingID) REFERENCES PoultryBuildings(BuildingID) ON DELETE CASCADE
);

-- Create a table to store services related to cleaning and disinfection.
CREATE TABLE CleaningServices (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each cleaning service
    ServiceName VARCHAR(255) NOT NULL,         -- Name of the cleaning service (e.g., "High-Pressure Washing")
    Description TEXT NOT NULL,                 -- Detailed description of the service
    ServiceProvider VARCHAR(255),              -- Name of the service provider company
    Cost DECIMAL(10, 2) NOT NULL,              -- Cost of the service
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the service record was created
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Create a table to link cleaning schedules with cleaning services used.
CREATE TABLE CleaningScheduleServices (
    ScheduleServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each entry
    ScheduleID INT NOT NULL,                          -- Foreign key referencing CleaningSchedules.ScheduleID
    ServiceID INT NOT NULL,                           -- Foreign key referencing CleaningServices.ServiceID
    UsageDate DATE NOT NULL,                          -- Date the service was used
    Notes TEXT,                                       -- Additional notes about the service usage
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,     -- Timestamp when the entry was created
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the record was last updated
    FOREIGN KEY (ScheduleID) REFERENCES CleaningSchedules(ScheduleID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceID) REFERENCES CleaningServices(ServiceID) ON DELETE CASCADE
);

-- Ensure proper indexing for efficient querying.
CREATE INDEX idx_building_location ON PoultryBuildings(Location);
CREATE INDEX idx_cleaning_date ON CleaningSchedules(CleaningDate);
CREATE INDEX idx_measure_implementation_date ON BiosecurityMeasures(ImplementationDate);
CREATE INDEX idx_service_provider ON CleaningServices(ServiceProvider);
```
