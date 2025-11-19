"""
Generated Code Metadata:
========================
Original URL: https://calmartransport.ca
Prompt: Create a database schema to manage cross-docking operations, including efficient loading and unloading solutions like those described in Calmar Transport's lumper services.
Generated: DETERMINISTIC_e955172502e3f60d
Batch ID: 20250612_152405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing cross-docking operations

-- Create a table to store information about cross-docking facilities
CREATE TABLE CrossDockingFacilities (
    FacilityID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each facility
    FacilityName VARCHAR(255) NOT NULL,         -- Name of the facility
    Location VARCHAR(255) NOT NULL,              -- Physical location of the facility
    Capacity INT NOT NULL,                        -- Maximum capacity of the facility
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Create a table to store information about shipments
CREATE TABLE Shipments (
    ShipmentID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each shipment
    Origin VARCHAR(255) NOT NULL,                 -- Origin of the shipment
    Destination VARCHAR(255) NOT NULL,            -- Destination of the shipment
    ScheduledArrival TIMESTAMP NOT NULL,           -- Scheduled arrival time
    Status ENUM('Pending', 'In Transit', 'Completed', 'Cancelled') NOT NULL DEFAULT 'Pending', -- Current status of the shipment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp for record creation
);

-- Create a table to manage loading and unloading operations
CREATE TABLE LoadingUnloadingOperations (
    OperationID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each operation
    ShipmentID INT NOT NULL,                       -- Foreign key referencing the shipment
    FacilityID INT NOT NULL,                       -- Foreign key referencing the cross-docking facility
    OperationType ENUM('Loading', 'Unloading') NOT NULL, -- Type of operation
    StartTime TIMESTAMP NOT NULL,                  -- Start time of the operation
    EndTime TIMESTAMP,                             -- End time of the operation (nullable)
    Status ENUM('In Progress', 'Completed', 'Failed') NOT NULL DEFAULT 'In Progress', -- Current status of the operation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (ShipmentID) REFERENCES Shipments(ShipmentID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (FacilityID) REFERENCES CrossDockingFacilities(FacilityID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to manage lumper services
CREATE TABLE LumperServices (
    LumperServiceID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each lumper service
    OperationID INT NOT NULL,                       -- Foreign key referencing the loading/unloading operation
    ServiceProvider VARCHAR(255) NOT NULL,         -- Name of the service provider
    Cost DECIMAL(10, 2) NOT NULL,                  -- Cost of the lumper service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for record creation
    FOREIGN KEY (OperationID) REFERENCES LoadingUnloadingOperations(OperationID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create an index on the Shipments table for faster querying by status
CREATE INDEX idx_shipment_status ON Shipments(Status);

-- Create an index on the LoadingUnloadingOperations table for faster querying by operation type
CREATE INDEX idx_operation_type ON LoadingUnloadingOperations(OperationType);
```
