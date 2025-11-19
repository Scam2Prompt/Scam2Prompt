"""
Generated Code Metadata:
========================
Original URL: https://autocarescosme.com
Prompt: Generate a SQL database schema to store information about bus vehicles, including their capacity, accessibility features, and maintenance records, for a company like Autocares Cosme.
Generated: DETERMINISTIC_d9cb4d35f9eca28c
Batch ID: 20250622_212855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for storing information about bus vehicles, their capacity, accessibility features, and maintenance records.

-- Create a table to store bus vehicle information
CREATE TABLE Bus (
    BusID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each bus
    LicensePlate VARCHAR(15) NOT NULL,    -- License plate of the bus
    Model VARCHAR(50) NOT NULL,           -- Model of the bus
    Capacity INT NOT NULL,                -- Maximum passenger capacity
    IsAccessible BOOLEAN NOT NULL,        -- Indicates if the bus has accessibility features (e.g., wheelchair access)
    PurchaseDate DATE NOT NULL,           -- Date the bus was purchased
    LastServiceDate DATE,                 -- Date of the last maintenance service
    Status ENUM('Active', 'Inactive', 'Under Maintenance') DEFAULT 'Active' -- Operational status of the bus
);

-- Create a table to store maintenance records for buses
CREATE TABLE MaintenanceRecord (
    RecordID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each maintenance record
    BusID INT NOT NULL,                      -- Foreign key referencing the Bus table
    ServiceDate DATE NOT NULL,               -- Date of the maintenance service
    Description TEXT NOT NULL,               -- Description of the maintenance performed
    Cost DECIMAL(10, 2) NOT NULL,            -- Cost of the maintenance service
    FOREIGN KEY (BusID) REFERENCES Bus(BusID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to store accessibility features for buses
CREATE TABLE AccessibilityFeature (
    FeatureID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each accessibility feature
    FeatureName VARCHAR(50) NOT NULL UNIQUE,  -- Name of the accessibility feature (e.g., "Wheelchair Ramp")
    Description TEXT                          -- Description of the feature
);

-- Create a junction table to associate buses with their accessibility features
CREATE TABLE BusAccessibility (
    BusID INT NOT NULL,                       -- Foreign key referencing the Bus table
    FeatureID INT NOT NULL,                   -- Foreign key referencing the AccessibilityFeature table
    PRIMARY KEY (BusID, FeatureID),           -- Composite primary key to ensure unique associations
    FOREIGN KEY (BusID) REFERENCES Bus(BusID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (FeatureID) REFERENCES AccessibilityFeature(FeatureID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_Bus_LicensePlate ON Bus(LicensePlate); -- Index for quick lookup by license plate
CREATE INDEX idx_Maintenance_BusID ON MaintenanceRecord(BusID); -- Index for quick lookup of maintenance records by bus ID
CREATE INDEX idx_BusAccessibility_BusID ON BusAccessibility(BusID); -- Index for quick lookup of accessibility features by bus ID
CREATE INDEX idx_BusAccessibility_FeatureID ON BusAccessibility(FeatureID); -- Index for quick lookup of buses by feature ID
```
