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
-- Database Schema for Cross-Docking Operations with Loading and Unloading Solutions

-- Create a table for storing information about facilities where cross-docking takes place
CREATE TABLE Facilities (
    FacilityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each facility
    FacilityName VARCHAR(255) NOT NULL, -- Name of the facility
    Location VARCHAR(255), -- Location of the facility (city, state, etc.)
    Capacity INT NOT NULL, -- Maximum capacity of the facility
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the facility was added
);

-- Create a table for storing information about incoming shipments
CREATE TABLE IncomingShipments (
    ShipmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each shipment
    FacilityID INT NOT NULL, -- Associated facility
    CarrierName VARCHAR(255) NOT NULL, -- Name of the carrier transporting the shipment
    ArrivalDate DATETIME NOT NULL, -- Scheduled date and time of shipment arrival
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Current status of the shipment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the shipment was recorded
    FOREIGN KEY (FacilityID) REFERENCES Facilities(FacilityID) ON DELETE CASCADE
);

-- Create a table for storing information about outgoing shipments
CREATE TABLE OutgoingShipments (
    ShipmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each shipment
    FacilityID INT NOT NULL, -- Associated facility
    Destination VARCHAR(255) NOT NULL, -- Destination of the outgoing shipment
    DepartureDate DATETIME NOT NULL, -- Scheduled date and time of shipment departure
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Current status of the shipment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the shipment was recorded
    FOREIGN KEY (FacilityID) REFERENCES Facilities(FacilityID) ON DELETE CASCADE
);

-- Create a table for managing lumper services (loading and unloading operations)
CREATE TABLE LumperServices (
    LumperServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for lumper service
    ShipmentID INT NOT NULL, -- Associated shipment (can be incoming or outgoing)
    ServiceType ENUM('Loading', 'Unloading') NOT NULL, -- Type of lumper service
    StartTime DATETIME NOT NULL, -- Start time of the service
    EndTime DATETIME NULL, -- End time of the service (NULL if not completed)
    AssignedWorker VARCHAR(255) NOT NULL, -- Name of the worker assigned to the service
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Current status of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the service was initiated
    FOREIGN KEY (ShipmentID) REFERENCES IncomingShipments(ShipmentID) ON DELETE CASCADE
);

-- Create a table for tracking workers involved in cross-docking operations
CREATE TABLE Workers (
    WorkerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each worker
    WorkerName VARCHAR(255) NOT NULL, -- Name of the worker
    ContactInfo VARCHAR(255), -- Contact information (phone, email, etc.)
    Role ENUM('Lumper', 'Supervisor', 'Manager') NOT NULL, -- Role of the worker
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the worker was added
);

-- Create a table for logging errors and issues during operations
CREATE TABLE ErrorLogs (
    ErrorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each error log
    FacilityID INT NOT NULL, -- Associated facility
    ErrorMessage TEXT NOT NULL, -- Detailed error message
    ErrorDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the error occurred
    FOREIGN KEY (FacilityID) REFERENCES Facilities(FacilityID) ON DELETE CASCADE
);

-- Best-practice indexes for performance optimization
CREATE INDEX idx_facility_location ON Facilities(Location);
CREATE INDEX idx_incoming_arrival_date ON IncomingShipments(ArrivalDate);
CREATE INDEX idx_outgoing_departure_date ON OutgoingShipments(DepartureDate);
CREATE INDEX idx_lumper_start_time ON LumperServices(StartTime);

-- Example stored procedure for assigning a lumper service to a worker
DELIMITER $$
CREATE PROCEDURE AssignLumperService(
    IN lumperServiceID INT,
    IN workerName VARCHAR(255)
)
BEGIN
    -- Update the AssignedWorker field for the specified lumper service
    UPDATE LumperServices
    SET AssignedWorker = workerName, Status = 'In Progress'
    WHERE LumperServiceID = lumperServiceID AND Status = 'Pending';

    -- Log an error if no rows are updated
    IF ROW_COUNT() = 0 THEN
        INSERT INTO ErrorLogs (FacilityID, ErrorMessage)
        SELECT FacilityID, CONCAT('Failed to assign lumper service ID ', lumperServiceID)
        FROM LumperServices
        WHERE LumperServiceID = lumperServiceID;
    END IF;
END$$
DELIMITER ;

-- Ensure proper cleanup when deleting related data
CREATE TRIGGER trg_delete_facility_cleanup
AFTER DELETE ON Facilities
FOR EACH ROW
BEGIN
    DELETE FROM IncomingShipments WHERE FacilityID = OLD.FacilityID;
    DELETE FROM OutgoingShipments WHERE FacilityID = OLD.FacilityID;
    DELETE FROM LumperServices WHERE ShipmentID IN (
        SELECT ShipmentID FROM IncomingShipments WHERE FacilityID = OLD.FacilityID
    );
END;
```
