"""
Generated Code Metadata:
========================
Original URL: https://espinelycia.com
Prompt: "Design a simple database schema to store information about hydraulic, sanitary, gas, and firefighting networks, including their designs, constructions, and maintenance records, inspired by the services offered by Espinel y Cia."
Generated: DETERMINISTIC_e6432d87387fc3ee
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about hydraulic, sanitary, gas, and firefighting networks
-- Includes tables for designs, constructions, and maintenance records

-- Create a table to store network types
CREATE TABLE NetworkTypes (
    NetworkTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the network type
    Name VARCHAR(50) NOT NULL,                    -- Name of the network type (e.g., Hydraulic, Sanitary, Gas, Firefighting)
    Description TEXT                              -- Optional description of the network type
);

-- Create a table to store designs
CREATE TABLE Designs (
    DesignID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for the design
    NetworkTypeID INT NOT NULL,                   -- Foreign key referencing the network type
    DesignName VARCHAR(100) NOT NULL,             -- Name of the design
    CreatedDate DATE NOT NULL,                    -- Date the design was created
    DesignerName VARCHAR(100),                    -- Name of the designer
    DesignFilePath VARCHAR(255),                  -- Path to the design file (e.g., CAD file)
    FOREIGN KEY (NetworkTypeID) REFERENCES NetworkTypes(NetworkTypeID) ON DELETE CASCADE
);

-- Create a table to store construction records
CREATE TABLE Constructions (
    ConstructionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the construction record
    DesignID INT NOT NULL,                          -- Foreign key referencing the design
    StartDate DATE NOT NULL,                        -- Start date of the construction
    EndDate DATE,                                   -- End date of the construction (nullable if ongoing)
    ContractorName VARCHAR(100),                   -- Name of the contractor responsible for construction
    Status ENUM('Planned', 'In Progress', 'Completed') NOT NULL, -- Status of the construction
    FOREIGN KEY (DesignID) REFERENCES Designs(DesignID) ON DELETE CASCADE
);

-- Create a table to store maintenance records
CREATE TABLE MaintenanceRecords (
    MaintenanceID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for the maintenance record
    NetworkTypeID INT NOT NULL,                    -- Foreign key referencing the network type
    MaintenanceDate DATE NOT NULL,                 -- Date of the maintenance activity
    MaintenanceDescription TEXT,                   -- Description of the maintenance activity
    TechnicianName VARCHAR(100),                   -- Name of the technician performing the maintenance
    FOREIGN KEY (NetworkTypeID) REFERENCES NetworkTypes(NetworkTypeID) ON DELETE CASCADE
);

-- Create a table to store general notes or logs for networks
CREATE TABLE NetworkLogs (
    LogID INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for the log entry
    NetworkTypeID INT NOT NULL,                    -- Foreign key referencing the network type
    LogDate DATE NOT NULL,                         -- Date of the log entry
    LogDescription TEXT,                           -- Description of the log entry
    FOREIGN KEY (NetworkTypeID) REFERENCES NetworkTypes(NetworkTypeID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_networktype_name ON NetworkTypes(Name);
CREATE INDEX idx_design_name ON Designs(DesignName);
CREATE INDEX idx_construction_status ON Constructions(Status);
CREATE INDEX idx_maintenance_date ON MaintenanceRecords(MaintenanceDate);
CREATE INDEX idx_log_date ON NetworkLogs(LogDate);
```
