"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fealtyworldwide.com
Prompt: Create a database schema for managing ocean freight shipments, including container types (45', 40', 20') and import/export details, inspired by Fealty Worldwide's services.
Generated: DETERMINISTIC_58115ff10f2508a7
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Ocean Freight Shipments Database Schema
-- This schema is designed to manage ocean freight shipments, including container types and import/export details.

-- Table: ContainerTypes
-- Description: Stores container type information.
CREATE TABLE ContainerTypes (
    ContainerTypeID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for the container type
    TypeName VARCHAR(100) NOT NULL,                -- Name of the container type (e.g., '45', '40', '20')
    Description VARCHAR(255)                       -- Additional details about the container type
);

-- Table: Shipments
-- Description: Stores shipment information for import and export.
CREATE TABLE Shipments (
    ShipmentID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for the shipment
    ContainerTypeID INT NOT NULL,                  -- Foreign key referencing the container type
    ShipmentType ENUM('Import', 'Export') NOT NULL, -- Type of shipment: Import or Export
    OriginPort VARCHAR(100) NOT NULL,              -- Origin port of the shipment
    DestinationPort VARCHAR(100) NOT NULL,         -- Destination port of the shipment
    DepartureDate DATE NOT NULL,                   -- Departure date of the shipment
    ArrivalDate DATE NOT NULL,                     -- Expected arrival date of the shipment
    Status ENUM('Pending', 'In Transit', 'Delivered', 'Cancelled') NOT NULL, -- Current status of the shipment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the shipment record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (ContainerTypeID) REFERENCES ContainerTypes(ContainerTypeID) ON DELETE CASCADE -- Ensures data integrity
);

-- Table: ShipmentDetails
-- Description: Stores detailed information about each shipment.
CREATE TABLE ShipmentDetails (
    DetailID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for the shipment detail
    ShipmentID INT NOT NULL,                       -- Foreign key referencing the shipment
    Weight DECIMAL(10, 2) NOT NULL,                -- Weight of the shipment in metric tons
    Volume DECIMAL(10, 2) NOT NULL,                -- Volume of the shipment in cubic meters
    GoodsDescription VARCHAR(255) NOT NULL,        -- Description of goods being shipped
    AdditionalNotes TEXT,                          -- Optional additional notes about the shipment
    FOREIGN KEY (ShipmentID) REFERENCES Shipments(ShipmentID) ON DELETE CASCADE -- Ensures data integrity
);

-- Table: Ports
-- Description: Stores information about ports involved in shipments.
CREATE TABLE Ports (
    PortID INT PRIMARY KEY AUTO_INCREMENT,         -- Unique identifier for the port
    PortName VARCHAR(100) NOT NULL,                -- Name of the port
    Country VARCHAR(100) NOT NULL,                 -- Country where the port is located
    PortCode VARCHAR(10) NOT NULL UNIQUE,          -- Unique code for the port (e.g., "LAX" for Los Angeles)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the port record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Last update timestamp
);

-- Table: ShipmentTracking
-- Description: Tracks shipment progress and updates.
CREATE TABLE ShipmentTracking (
    TrackingID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for the tracking record
    ShipmentID INT NOT NULL,                       -- Foreign key referencing the shipment
    StatusUpdate ENUM('Pending', 'In Transit', 'Delivered', 'Delayed', 'Cancelled') NOT NULL, -- Status update
    UpdateTimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the status update
    Location VARCHAR(255) NOT NULL,                -- Current location of the shipment
    Notes TEXT,                                    -- Optional notes for the status update
    FOREIGN KEY (ShipmentID) REFERENCES Shipments(ShipmentID) ON DELETE CASCADE -- Ensures data integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_container_type_name ON ContainerTypes(TypeName);
CREATE INDEX idx_shipment_status ON Shipments(Status);
CREATE INDEX idx_shipment_dates ON Shipments(DepartureDate, ArrivalDate);
CREATE INDEX idx_port_code ON Ports(PortCode);

-- Error handling and rollback support is assumed to be managed at the application layer
-- using proper transaction management.
```
