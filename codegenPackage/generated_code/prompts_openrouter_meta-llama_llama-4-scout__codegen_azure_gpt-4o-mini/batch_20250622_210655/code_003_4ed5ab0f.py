"""
Generated Code Metadata:
========================
Original URL: https://indpfire.com
Prompt: "Design a simple database schema for storing fire safety equipment inspection and maintenance records."
Generated: DETERMINISTIC_4ed5ab0f73ae2376
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing fire safety equipment inspection and maintenance records

-- Create a table for storing information about fire safety equipment
CREATE TABLE FireSafetyEquipment (
    EquipmentID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each equipment
    EquipmentType VARCHAR(100) NOT NULL,         -- Type of the equipment (e.g., Fire Extinguisher, Smoke Detector)
    Location VARCHAR(255) NOT NULL,              -- Location where the equipment is installed
    PurchaseDate DATE NOT NULL,                   -- Date when the equipment was purchased
    LastInspectionDate DATE,                      -- Date of the last inspection
    NextInspectionDate DATE,                      -- Date of the next scheduled inspection
    Status ENUM('Active', 'Inactive') NOT NULL DEFAULT 'Active'  -- Status of the equipment
);

-- Create a table for storing inspection records
CREATE TABLE InspectionRecords (
    InspectionID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each inspection record
    EquipmentID INT NOT NULL,                     -- Foreign key referencing FireSafetyEquipment
    InspectionDate DATE NOT NULL,                 -- Date when the inspection was conducted
    InspectorName VARCHAR(100) NOT NULL,         -- Name of the inspector
    InspectionResult ENUM('Pass', 'Fail') NOT NULL,  -- Result of the inspection
    Comments TEXT,                                -- Additional comments regarding the inspection
    FOREIGN KEY (EquipmentID) REFERENCES FireSafetyEquipment(EquipmentID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create a table for storing maintenance records
CREATE TABLE MaintenanceRecords (
    MaintenanceID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each maintenance record
    EquipmentID INT NOT NULL,                      -- Foreign key referencing FireSafetyEquipment
    MaintenanceDate DATE NOT NULL,                 -- Date when maintenance was performed
    MaintenancePerformed VARCHAR(255) NOT NULL,   -- Description of maintenance performed
    TechnicianName VARCHAR(100) NOT NULL,         -- Name of the technician who performed the maintenance
    FOREIGN KEY (EquipmentID) REFERENCES FireSafetyEquipment(EquipmentID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_equipment_location ON FireSafetyEquipment(Location);
CREATE INDEX idx_inspection_equipment ON InspectionRecords(EquipmentID);
CREATE INDEX idx_maintenance_equipment ON MaintenanceRecords(EquipmentID);
```
