"""
Generated Code Metadata:
========================
Original URL: https://enlconsortium.com
Prompt: "Design a database schema to store equipment profiles and performance indicators for a logistics company with diverse operations like ENL Consortium."
Generated: DETERMINISTIC_40769b532252e231
Batch ID: 20250622_204704
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing equipment profiles and performance indicators
-- Designed for a logistics company with diverse operations

-- Table to store equipment profiles
CREATE TABLE Equipment (
    EquipmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each equipment
    Name VARCHAR(255) NOT NULL,                 -- Name of the equipment
    Type VARCHAR(100) NOT NULL,                 -- Type/category of the equipment (e.g., truck, crane, etc.)
    Manufacturer VARCHAR(255),                  -- Manufacturer of the equipment
    Model VARCHAR(100),                         -- Model of the equipment
    SerialNumber VARCHAR(100) UNIQUE,           -- Unique serial number for the equipment
    PurchaseDate DATE,                          -- Date the equipment was purchased
    Status ENUM('Active', 'Inactive', 'Under Maintenance') DEFAULT 'Active', -- Current status of the equipment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Table to store performance indicators for equipment
CREATE TABLE PerformanceIndicators (
    IndicatorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each performance indicator
<<<<<<< HEAD
    EquipmentID INT NOT NULL,                   -- Foreign key referencing the Equipment table
=======
    EquipmentID INT NOT NULL,                   -- Foreign key referencing Equipment table
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    IndicatorName VARCHAR(255) NOT NULL,        -- Name of the performance indicator (e.g., fuel efficiency, uptime, etc.)
    Value DECIMAL(10, 2) NOT NULL,              -- Value of the performance indicator
    Unit VARCHAR(50),                           -- Unit of measurement for the indicator (e.g., liters/hour, hours, etc.)
    RecordedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the indicator was recorded
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the record was last updated
    FOREIGN KEY (EquipmentID) REFERENCES Equipment(EquipmentID) ON DELETE CASCADE -- Ensures data integrity
);

-- Table to store maintenance records for equipment
CREATE TABLE MaintenanceRecords (
    MaintenanceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each maintenance record
<<<<<<< HEAD
    EquipmentID INT NOT NULL,                     -- Foreign key referencing the Equipment table
=======
    EquipmentID INT NOT NULL,                     -- Foreign key referencing Equipment table
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    MaintenanceDate DATE NOT NULL,                -- Date of maintenance
    Description TEXT NOT NULL,                    -- Description of the maintenance performed
    Cost DECIMAL(10, 2),                          -- Cost of the maintenance
    PerformedBy VARCHAR(255),                     -- Name of the person or company performing the maintenance
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the record was last updated
    FOREIGN KEY (EquipmentID) REFERENCES Equipment(EquipmentID) ON DELETE CASCADE -- Ensures data integrity
);

-- Table to store operational logs for equipment
CREATE TABLE OperationalLogs (
    LogID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each operational log
<<<<<<< HEAD
    EquipmentID INT NOT NULL,                     -- Foreign key referencing the Equipment table
    OperationDate DATE NOT NULL,                  -- Date of the operation
    Description TEXT NOT NULL,                    -- Description of the operation
=======
    EquipmentID INT NOT NULL,                     -- Foreign key referencing Equipment table
    OperationDate DATE NOT NULL,                  -- Date of the operation
    OperationType VARCHAR(100) NOT NULL,          -- Type of operation (e.g., transport, loading, etc.)
    Description TEXT,                             -- Description of the operation
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    Duration DECIMAL(10, 2),                      -- Duration of the operation (e.g., hours)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the record was last updated
    FOREIGN KEY (EquipmentID) REFERENCES Equipment(EquipmentID) ON DELETE CASCADE -- Ensures data integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_equipment_type ON Equipment(Type); -- Index for querying equipment by type
CREATE INDEX idx_performance_equipment ON PerformanceIndicators(EquipmentID); -- Index for querying performance indicators by equipment
CREATE INDEX idx_maintenance_equipment ON MaintenanceRecords(EquipmentID); -- Index for querying maintenance records by equipment
CREATE INDEX idx_logs_equipment ON OperationalLogs(EquipmentID); -- Index for querying operational logs by equipment
```
