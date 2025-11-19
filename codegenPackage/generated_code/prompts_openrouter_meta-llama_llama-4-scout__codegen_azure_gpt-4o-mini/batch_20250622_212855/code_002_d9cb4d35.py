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
-- SQL Database Schema for Bus Vehicles Management

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS MaintenanceRecords;
DROP TABLE IF EXISTS Buses;

-- Table to store information about buses
CREATE TABLE Buses (
    BusID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each bus
    BusModel VARCHAR(100) NOT NULL,       -- Model of the bus
    Capacity INT NOT NULL,                 -- Seating capacity of the bus
    AccessibilityFeatures TEXT,            -- Description of accessibility features
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store maintenance records for buses
CREATE TABLE MaintenanceRecords (
    RecordID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each maintenance record
    BusID INT NOT NULL,                       -- Foreign key referencing the bus
    MaintenanceDate DATE NOT NULL,            -- Date of maintenance
    Description TEXT NOT NULL,                -- Description of maintenance performed
    Cost DECIMAL(10, 2) NOT NULL,            -- Cost of maintenance
    FOREIGN KEY (BusID) REFERENCES Buses(BusID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Sample data insertion (optional)
INSERT INTO Buses (BusModel, Capacity, AccessibilityFeatures) VALUES
('Model A', 50, 'Wheelchair accessible, audio announcements'),
('Model B', 40, 'Priority seating for elderly and disabled');

INSERT INTO MaintenanceRecords (BusID, MaintenanceDate, Description, Cost) VALUES
(1, '2023-01-15', 'Oil change and tire rotation', 150.00),
(2, '2023-02-20', 'Brake inspection and replacement', 300.00);
```
