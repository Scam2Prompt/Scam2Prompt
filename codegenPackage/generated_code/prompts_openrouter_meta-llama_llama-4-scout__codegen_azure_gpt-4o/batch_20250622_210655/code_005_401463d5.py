"""
Generated Code Metadata:
========================
Original URL: https://jusoor.ch
Prompt: "Create a database schema to store information about humanitarian interventions, including details about affected regions, displaced persons, and medical aid, as described in Jusoor International's work."
Generated: DETERMINISTIC_401463d59ecf17ca
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about humanitarian interventions

-- Table to store information about regions affected by humanitarian interventions
CREATE TABLE Regions (
    RegionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the region
    RegionName VARCHAR(255) NOT NULL,        -- Name of the region
    Country VARCHAR(255) NOT NULL,           -- Country where the region is located
    Description TEXT,                        -- Additional details about the region
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about displaced persons
CREATE TABLE DisplacedPersons (
    PersonID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the displaced person
    FullName VARCHAR(255) NOT NULL,          -- Full name of the displaced person
    Age INT,                                 -- Age of the displaced person
    Gender ENUM('Male', 'Female', 'Other'),  -- Gender of the displaced person
    RegionID INT NOT NULL,                   -- Foreign key linking to the affected region
    DisplacementDate DATE,                   -- Date of displacement
    Notes TEXT,                              -- Additional notes about the person
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (RegionID) REFERENCES Regions(RegionID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store information about medical aid provided
CREATE TABLE MedicalAid (
    AidID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for the medical aid record
    AidType VARCHAR(255) NOT NULL,          -- Type of medical aid (e.g., vaccines, first aid kits)
    Quantity INT NOT NULL,                  -- Quantity of aid provided
    RegionID INT NOT NULL,                  -- Foreign key linking to the affected region
    AidDate DATE NOT NULL,                  -- Date when the aid was provided
    Notes TEXT,                             -- Additional notes about the aid
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (RegionID) REFERENCES Regions(RegionID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store information about humanitarian interventions
CREATE TABLE Interventions (
    InterventionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the intervention
    InterventionName VARCHAR(255) NOT NULL,        -- Name of the intervention
    Description TEXT,                              -- Detailed description of the intervention
    StartDate DATE NOT NULL,                       -- Start date of the intervention
    EndDate DATE,                                  -- End date of the intervention (nullable if ongoing)
    RegionID INT NOT NULL,                         -- Foreign key linking to the affected region
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (RegionID) REFERENCES Regions(RegionID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_region_name ON Regions(RegionName);
CREATE INDEX idx_displacement_date ON DisplacedPersons(DisplacementDate);
CREATE INDEX idx_aid_date ON MedicalAid(AidDate);
CREATE INDEX idx_intervention_dates ON Interventions(StartDate, EndDate);
```
