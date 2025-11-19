"""
Generated Code Metadata:
========================
Original URL: https://ecpowerlightingltd.com
Prompt: Develop a database schema for tracking traffic signal maintenance, inspired by E.C. Power & Lighting Ltd.'s expertise in traffic signal systems.
Generated: DETERMINISTIC_a9f827d200d6ad96
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for tracking traffic signal maintenance

-- Create a table to store information about traffic signals
CREATE TABLE TrafficSignals (
    SignalID SERIAL PRIMARY KEY,          -- Unique identifier for each traffic signal
    Location VARCHAR(255) NOT NULL,       -- Location description of the traffic signal
    InstallationDate DATE NOT NULL,        -- Date when the traffic signal was installed
    LastMaintenanceDate DATE,              -- Date of the last maintenance performed
    Status VARCHAR(50) NOT NULL CHECK (Status IN ('Active', 'Inactive', 'Under Maintenance')), -- Current status of the signal
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Create a table to store maintenance records for traffic signals
CREATE TABLE MaintenanceRecords (
    MaintenanceID SERIAL PRIMARY KEY,      -- Unique identifier for each maintenance record
    SignalID INT NOT NULL,                  -- Foreign key referencing the TrafficSignals table
    MaintenanceDate DATE NOT NULL,          -- Date when maintenance was performed
    Description TEXT NOT NULL,              -- Description of the maintenance performed
    Cost DECIMAL(10, 2) NOT NULL,          -- Cost of the maintenance
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (SignalID) REFERENCES TrafficSignals(SignalID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to store users who perform maintenance
CREATE TABLE MaintenanceTechnicians (
    TechnicianID SERIAL PRIMARY KEY,       -- Unique identifier for each technician
    Name VARCHAR(100) NOT NULL,            -- Name of the technician
    ContactInfo VARCHAR(255),               -- Contact information for the technician
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Create a junction table to associate technicians with maintenance records
CREATE TABLE TechnicianMaintenance (
    TechnicianID INT NOT NULL,             -- Foreign key referencing the MaintenanceTechnicians table
    MaintenanceID INT NOT NULL,             -- Foreign key referencing the MaintenanceRecords table
    PRIMARY KEY (TechnicianID, MaintenanceID), -- Composite primary key
    FOREIGN KEY (TechnicianID) REFERENCES MaintenanceTechnicians(TechnicianID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (MaintenanceID) REFERENCES MaintenanceRecords(MaintenanceID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_signal_status ON TrafficSignals(Status);
CREATE INDEX idx_maintenance_date ON MaintenanceRecords(MaintenanceDate);
CREATE INDEX idx_technician_name ON MaintenanceTechnicians(Name);
```
