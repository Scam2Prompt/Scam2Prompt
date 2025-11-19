"""
Generated Code Metadata:
========================
Original URL: https://trackdieselperu.com
Prompt: "Create a SQL database schema to store information about heavy machinery, their spare parts, and maintenance services offered by a company like Track Diesel Peru S.R.L."
Generated: DETERMINISTIC_0391f4c7bb75d285
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Heavy Machinery, Spare Parts, and Maintenance Services

-- Create a database for the company
CREATE DATABASE TrackDieselPeru;

-- Use the created database
USE TrackDieselPeru;

-- Table to store information about heavy machinery
CREATE TABLE HeavyMachinery (
    MachineryID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each machinery
    Name VARCHAR(100) NOT NULL,                   -- Name of the machinery
    Model VARCHAR(50) NOT NULL,                   -- Model of the machinery
    Year INT NOT NULL,                            -- Year of manufacture
    Manufacturer VARCHAR(100) NOT NULL,          -- Manufacturer of the machinery
    Description TEXT,                             -- Description of the machinery
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store information about spare parts
CREATE TABLE SpareParts (
    PartID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each spare part
    PartName VARCHAR(100) NOT NULL,               -- Name of the spare part
    PartNumber VARCHAR(50) NOT NULL,              -- Part number for identification
    MachineryID INT,                               -- Foreign key referencing HeavyMachinery
    QuantityInStock INT DEFAULT 0,                -- Quantity of spare part in stock
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the spare part
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (MachineryID) REFERENCES HeavyMachinery(MachineryID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store information about maintenance services
CREATE TABLE MaintenanceServices (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,            -- Name of the maintenance service
    Description TEXT,                              -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the maintenance service
    Duration INT NOT NULL,                         -- Duration of the service in hours
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to link heavy machinery with maintenance services
CREATE TABLE MachineryMaintenance (
    MachineryID INT,                               -- Foreign key referencing HeavyMachinery
    ServiceID INT,                                 -- Foreign key referencing MaintenanceServices
    PRIMARY KEY (MachineryID, ServiceID),         -- Composite primary key
    FOREIGN KEY (MachineryID) REFERENCES HeavyMachinery(MachineryID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ServiceID) REFERENCES MaintenanceServices(ServiceID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store maintenance records for heavy machinery
CREATE TABLE MaintenanceRecords (
    RecordID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each maintenance record
    MachineryID INT,                               -- Foreign key referencing HeavyMachinery
    ServiceID INT,                                 -- Foreign key referencing MaintenanceServices
    MaintenanceDate DATE NOT NULL,                 -- Date of maintenance
    Notes TEXT,                                    -- Additional notes about the maintenance
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    FOREIGN KEY (MachineryID) REFERENCES HeavyMachinery(MachineryID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ServiceID) REFERENCES MaintenanceServices(ServiceID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes can be added for performance optimization as needed
```
