"""
Generated Code Metadata:
========================
Original URL: https://multiservicios3l.com
Prompt: Develop a simple database schema to store information about industrial machinery, including maintenance records and repair history, inspired by Multiservicios 3L's maintenance and repair services.
Generated: DETERMINISTIC_6ba20bd6b6223a7d
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about industrial machinery, maintenance records, and repair history.

-- Table to store information about machinery
CREATE TABLE Machinery (
    MachineryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each machinery
    Name VARCHAR(100) NOT NULL,                 -- Name of the machinery
    Model VARCHAR(50),                          -- Model of the machinery
    Manufacturer VARCHAR(100),                  -- Manufacturer of the machinery
    PurchaseDate DATE,                          -- Date the machinery was purchased
    SerialNumber VARCHAR(50) UNIQUE,            -- Unique serial number for the machinery
    Status ENUM('Active', 'Inactive', 'Under Maintenance') DEFAULT 'Active', -- Current status of the machinery
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store maintenance records
CREATE TABLE MaintenanceRecords (
    MaintenanceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each maintenance record
    MachineryID INT NOT NULL,                     -- Foreign key referencing Machinery table
    MaintenanceDate DATE NOT NULL,                -- Date of maintenance
    Description TEXT NOT NULL,                    -- Description of the maintenance performed
    PerformedBy VARCHAR(100),                     -- Name of the person or company performing the maintenance
    Cost DECIMAL(10, 2),                          -- Cost of the maintenance
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (MachineryID) REFERENCES Machinery(MachineryID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store repair history
CREATE TABLE RepairHistory (
    RepairID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each repair record
    MachineryID INT NOT NULL,                     -- Foreign key referencing Machinery table
    RepairDate DATE NOT NULL,                     -- Date of repair
    IssueDescription TEXT NOT NULL,               -- Description of the issue that was repaired
    RepairDescription TEXT NOT NULL,              -- Description of the repair performed
    RepairedBy VARCHAR(100),                      -- Name of the person or company performing the repair
    Cost DECIMAL(10, 2),                          -- Cost of the repair
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (MachineryID) REFERENCES Machinery(MachineryID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_machinery_status ON Machinery(Status); -- Index for machinery status
CREATE INDEX idx_maintenance_date ON MaintenanceRecords(MaintenanceDate); -- Index for maintenance date
CREATE INDEX idx_repair_date ON RepairHistory(RepairDate); -- Index for repair date
```
