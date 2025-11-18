"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://calmartransport.ca
Prompt: Create a database schema to manage cross-docking operations, including efficient loading and unloading solutions like those described in Calmar Transport's lumper services.
Generated: DETERMINISTIC_e955172502e3f60d
Batch ID: 20250612_152405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing cross-docking operations

-- Create a table to store information about cross-docking facilities
CREATE TABLE CrossDockingFacilities (
    FacilityID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each facility
    FacilityName VARCHAR(255) NOT NULL,         -- Name of the facility
    Location VARCHAR(255) NOT NULL,              -- Physical location of the facility
    Capacity INT NOT NULL,                        -- Maximum capacity of the facility
    ContactNumber VARCHAR(15)                     -- Contact number for the facility
);

-- Create a table to store information about shipments
CREATE TABLE Shipments (
    ShipmentID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each shipment
    ShipmentDate DATETIME NOT NULL,               -- Date and time of the shipment
    Origin VARCHAR(255) NOT NULL,                 -- Origin of the shipment
    Destination VARCHAR(255) NOT NULL,            -- Destination of the shipment
    Status ENUM('Pending', 'In Transit', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Current status of the shipment
    FacilityID INT,                                -- Foreign key referencing CrossDockingFacilities
    FOREIGN KEY (FacilityID) REFERENCES CrossDockingFacilities(FacilityID)
);

-- Create a table to manage loading and unloading operations
CREATE TABLE LoadingUnloadingOperations (
    OperationID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each operation
    ShipmentID INT,                                -- Foreign key referencing Shipments
    OperationType ENUM('Loading', 'Unloading') NOT NULL, -- Type of operation
    StartTime DATETIME NOT NULL,                   -- Start time of the operation
    EndTime DATETIME,                              -- End time of the operation
    Status ENUM('Scheduled', 'In Progress', 'Completed', 'Failed') DEFAULT 'Scheduled', -- Current status of the operation
    FOREIGN KEY (ShipmentID) REFERENCES Shipments(ShipmentID)
);

-- Create a table to log lumper services used in the cross-docking process
CREATE TABLE LumperServices (
    LumperServiceID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each lumper service
    OperationID INT,                                 -- Foreign key referencing LoadingUnloadingOperations
    ServiceDate DATETIME NOT NULL,                   -- Date of the lumper service
    ServiceFee DECIMAL(10, 2) NOT NULL,             -- Fee charged for the lumper service
    Notes TEXT,                                      -- Additional notes regarding the service
    FOREIGN KEY (OperationID) REFERENCES LoadingUnloadingOperations(OperationID)
);

-- Ensure that all tables are created successfully
DELIMITER //
CREATE PROCEDURE InitializeSchema()
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Roll back the transaction in case of error
        ROLLBACK;
    END;

    -- Start a transaction
    START TRANSACTION;
    
    -- Create the tables
    CREATE TABLE IF NOT EXISTS CrossDockingFacilities (
        FacilityID INT PRIMARY KEY AUTO_INCREMENT,
        FacilityName VARCHAR(255) NOT NULL,
        Location VARCHAR(255) NOT NULL,
        Capacity INT NOT NULL,
        ContactNumber VARCHAR(15)
    );

    CREATE TABLE IF NOT EXISTS Shipments (
        ShipmentID INT PRIMARY KEY AUTO_INCREMENT,
        ShipmentDate DATETIME NOT NULL,
        Origin VARCHAR(255) NOT NULL,
        Destination VARCHAR(255) NOT NULL,
        Status ENUM('Pending', 'In Transit', 'Delivered', 'Cancelled') DEFAULT 'Pending',
        FacilityID INT,
        FOREIGN KEY (FacilityID) REFERENCES CrossDockingFacilities(FacilityID)
    );

    CREATE TABLE IF NOT EXISTS LoadingUnloadingOperations (
        OperationID INT PRIMARY KEY AUTO_INCREMENT,
        ShipmentID INT,
        OperationType ENUM('Loading', 'Unloading') NOT NULL,
        StartTime DATETIME NOT NULL,
        EndTime DATETIME,
        Status ENUM('Scheduled', 'In Progress', 'Completed', 'Failed') DEFAULT 'Scheduled',
        FOREIGN KEY (ShipmentID) REFERENCES Shipments(ShipmentID)
    );

    CREATE TABLE IF NOT EXISTS LumperServices (
        LumperServiceID INT PRIMARY KEY AUTO_INCREMENT,
        OperationID INT,
        ServiceDate DATETIME NOT NULL,
        ServiceFee DECIMAL(10, 2) NOT NULL,
        Notes TEXT,
        FOREIGN KEY (OperationID) REFERENCES LoadingUnloadingOperations(OperationID)
    );

    -- Commit the transaction
    COMMIT;
END //
DELIMITER ;

-- Call the procedure to initialize the schema
CALL InitializeSchema();
```
