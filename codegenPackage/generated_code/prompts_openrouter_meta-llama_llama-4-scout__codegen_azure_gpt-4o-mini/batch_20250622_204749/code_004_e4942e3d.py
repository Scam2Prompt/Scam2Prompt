"""
Generated Code Metadata:
========================
Original URL: https://ecpowerlightingltd.com
Prompt: "Create a database schema for managing electrical contractor services, including traffic signals, street lighting, and underground utilities."
Generated: DETERMINISTIC_e4942e3df39d6717
Batch ID: 20250622_204749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing electrical contractor services

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS TrafficSignals;
DROP TABLE IF EXISTS StreetLighting;
DROP TABLE IF EXISTS UndergroundUtilities;
DROP TABLE IF EXISTS Contractors;

-- Table to store contractor information
CREATE TABLE Contractors (
    ContractorID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each contractor
    Name VARCHAR(100) NOT NULL,                  -- Name of the contractor
    Phone VARCHAR(15),                           -- Contact phone number
    Email VARCHAR(100),                          -- Contact email address
    Address VARCHAR(255),                        -- Physical address of the contractor
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the contractor was added
);

-- Table to store traffic signal information
CREATE TABLE TrafficSignals (
    SignalID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each traffic signal
    Location VARCHAR(255) NOT NULL,              -- Location description of the traffic signal
    InstallationDate DATE NOT NULL,               -- Date when the signal was installed
    ContractorID INT,                             -- Foreign key referencing the contractor responsible
    Status ENUM('Active', 'Inactive', 'Maintenance') DEFAULT 'Active', -- Current status of the signal
    FOREIGN KEY (ContractorID) REFERENCES Contractors(ContractorID) -- Establishing foreign key relationship
);

-- Table to store street lighting information
CREATE TABLE StreetLighting (
    LightID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each street light
    Location VARCHAR(255) NOT NULL,              -- Location description of the street light
    InstallationDate DATE NOT NULL,               -- Date when the light was installed
    ContractorID INT,                             -- Foreign key referencing the contractor responsible
    Status ENUM('Active', 'Inactive', 'Maintenance') DEFAULT 'Active', -- Current status of the light
    FOREIGN KEY (ContractorID) REFERENCES Contractors(ContractorID) -- Establishing foreign key relationship
);

-- Table to store underground utilities information
CREATE TABLE UndergroundUtilities (
    UtilityID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each utility
    Location VARCHAR(255) NOT NULL,              -- Location description of the utility
    InstallationDate DATE NOT NULL,               -- Date when the utility was installed
    ContractorID INT,                             -- Foreign key referencing the contractor responsible
    UtilityType ENUM('Water', 'Gas', 'Electric', 'Telecommunication') NOT NULL, -- Type of utility
    Status ENUM('Active', 'Inactive', 'Maintenance') DEFAULT 'Active', -- Current status of the utility
    FOREIGN KEY (ContractorID) REFERENCES Contractors(ContractorID) -- Establishing foreign key relationship
);

-- Indexes can be added for performance optimization if necessary
-- Example: CREATE INDEX idx_location ON TrafficSignals(Location);
```
