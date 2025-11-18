"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecpowerlightingltd.com
Prompt: Develop a database schema for tracking traffic signal maintenance, inspired by E.C. Power & Lighting Ltd.'s expertise in traffic signal systems.
Generated: DETERMINISTIC_a9f827d200d6ad96
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for tracking traffic signal maintenance

-- Create a table to store traffic signal information
CREATE TABLE TrafficSignals (
    SignalID SERIAL PRIMARY KEY,         -- Unique identifier for each signal
    Location VARCHAR(255) NOT NULL,      -- Location description of the signal
    InstallationDate DATE NOT NULL,       -- Date the signal was installed
    LastMaintenanceDate DATE,              -- Date of the last maintenance performed
    Status VARCHAR(50) NOT NULL CHECK (Status IN ('Operational', 'Non-Operational', 'Under Maintenance')),  -- Status of the signal
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Create a table to store maintenance records
CREATE TABLE MaintenanceRecords (
    MaintenanceID SERIAL PRIMARY KEY,     -- Unique identifier for each maintenance record
    SignalID INT NOT NULL REFERENCES TrafficSignals(SignalID) ON DELETE CASCADE,  -- Foreign key linking to TrafficSignals table
    MaintenanceDate DATE NOT NULL,         -- Date maintenance was performed
    Description TEXT NOT NULL,             -- Description of the maintenance performed
    Cost DECIMAL(10, 2),                   -- Cost incurred during maintenance
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Create a table to store personnel information
CREATE TABLE Personnel (
    PersonnelID SERIAL PRIMARY KEY,        -- Unique identifier for each personnel
    Name VARCHAR(100) NOT NULL,            -- Name of the maintenance personnel
    Position VARCHAR(100) NOT NULL,        -- Position of the personnel
    ContactInfo VARCHAR(100)                -- Contact information for the personnel
);

-- Create a mapping table to associate personnel with maintenance records
CREATE TABLE MaintenancePersonnel (
    MaintenanceID INT NOT NULL REFERENCES MaintenanceRecords(MaintenanceID) ON DELETE CASCADE,  -- Foreign key to MaintenanceRecords
    PersonnelID INT NOT NULL REFERENCES Personnel(PersonnelID) ON DELETE CASCADE,  -- Foreign key to Personnel
    PRIMARY KEY (MaintenanceID, PersonnelID)   -- Composite primary key
);

-- Indexes for optimizing queries
CREATE INDEX idx_signal_status ON TrafficSignals(Status);
CREATE INDEX idx_maintenance_signal ON MaintenanceRecords(SignalID);
CREATE INDEX idx_personnel_name ON Personnel(Name);

-- Insert sample data for demonstration (optional)
INSERT INTO TrafficSignals (Location, InstallationDate, LastMaintenanceDate, Status) 
VALUES 
('Main St & 1st Ave', '2021-01-15', '2023-01-10', 'Operational'),
('2nd St & Maple Ave', '2019-05-20', '2023-02-20', 'Under Maintenance');

INSERT INTO Personnel (Name, Position, ContactInfo) 
VALUES 
('John Doe', 'Technician', '555-1234'),
('Jane Smith', 'Supervisor', '555-5678');

INSERT INTO MaintenanceRecords (SignalID, MaintenanceDate, Description, Cost) 
VALUES 
(1, '2023-01-10', 'Replaced bulbs and checked timers', 150.00),
(2, '2023-02-20', 'Routine maintenance and inspection', 200.00);

INSERT INTO MaintenancePersonnel (MaintenanceID, PersonnelID) 
VALUES 
(1, 1),
(2, 2);
```
