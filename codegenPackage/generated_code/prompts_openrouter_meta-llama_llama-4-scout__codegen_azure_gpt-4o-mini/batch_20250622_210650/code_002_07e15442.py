"""
Generated Code Metadata:
========================
Original URL: https://knitplusltd.com
Prompt: "Generate a SQL database schema to store information about garment products, including details on materials, sizes, and production processes, for a company like Knit Plus Ltd."
Generated: DETERMINISTIC_07e154423a0db38e
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Knit Plus Ltd Garment Products

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS ProductionProcesses;
DROP TABLE IF EXISTS Materials;
DROP TABLE IF EXISTS Sizes;
DROP TABLE IF EXISTS Garments;

-- Table to store information about materials used in garments
CREATE TABLE Materials (
    MaterialID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each material
    MaterialName VARCHAR(100) NOT NULL,         -- Name of the material
    Description TEXT,                            -- Description of the material
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the material was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store different sizes available for garments
CREATE TABLE Sizes (
    SizeID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each size
    SizeLabel VARCHAR(10) NOT NULL,             -- Label for the size (e.g., S, M, L, XL)
    Description TEXT,                            -- Description of the size
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the size was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store production processes for garments
CREATE TABLE ProductionProcesses (
    ProcessID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each production process
    ProcessName VARCHAR(100) NOT NULL,          -- Name of the production process
    Description TEXT,                            -- Description of the production process
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the process was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store information about garments
CREATE TABLE Garments (
    GarmentID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each garment
    GarmentName VARCHAR(100) NOT NULL,          -- Name of the garment
    MaterialID INT NOT NULL,                     -- Foreign key referencing Materials
    SizeID INT NOT NULL,                         -- Foreign key referencing Sizes
    ProcessID INT NOT NULL,                      -- Foreign key referencing ProductionProcesses
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the garment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the garment was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (SizeID) REFERENCES Sizes(SizeID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ProcessID) REFERENCES ProductionProcesses(ProcessID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes can be added for performance optimization if necessary
-- Example: CREATE INDEX idx_garment_name ON Garments(GarmentName);
```
