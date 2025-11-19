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
-- Database schema for storing information about industrial machinery, maintenance records, and repair history

-- Create a database for the machinery management system
CREATE DATABASE IF NOT EXISTS MachineryManagement;

-- Use the created database
USE MachineryManagement;

-- Table to store information about industrial machinery
CREATE TABLE IF NOT EXISTS Machinery (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each machine
    name VARCHAR(255) NOT NULL,        -- Name of the machine
    type VARCHAR(100) NOT NULL,        -- Type of the machine (e.g., lathe, drill press)
    manufacturer VARCHAR(100),          -- Manufacturer of the machine
    model VARCHAR(100),                 -- Model number of the machine
    purchase_date DATE,                 -- Date when the machine was purchased
    warranty_expiration DATE,           -- Expiration date of the warranty
    status ENUM('Operational', 'Under Maintenance', 'Decommissioned') DEFAULT 'Operational', -- Current status of the machine
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store maintenance records for each machine
CREATE TABLE IF NOT EXISTS MaintenanceRecords (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each maintenance record
    machinery_id INT NOT NULL,          -- Foreign key referencing the Machinery table
    maintenance_date DATE NOT NULL,     -- Date when maintenance was performed
    description TEXT NOT NULL,          -- Description of the maintenance performed
    performed_by VARCHAR(100),          -- Name of the technician who performed the maintenance
    next_due_date DATE,                 -- Next scheduled maintenance date
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (machinery_id) REFERENCES Machinery(id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store repair history for each machine
CREATE TABLE IF NOT EXISTS RepairHistory (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each repair record
    machinery_id INT NOT NULL,          -- Foreign key referencing the Machinery table
    repair_date DATE NOT NULL,          -- Date when the repair was performed
    issue_description TEXT NOT NULL,    -- Description of the issue that required repair
    repair_description TEXT NOT NULL,    -- Description of the repair performed
    cost DECIMAL(10, 2),                -- Cost of the repair
    performed_by VARCHAR(100),          -- Name of the technician who performed the repair
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (machinery_id) REFERENCES Machinery(id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_machinery_name ON Machinery(name);
CREATE INDEX idx_maintenance_machinery_id ON MaintenanceRecords(machinery_id);
CREATE INDEX idx_repair_machinery_id ON RepairHistory(machinery_id);
```
