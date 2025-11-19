"""
Generated Code Metadata:
========================
Original URL: https://olgadorks.com
Prompt: Design a database schema to store information about shipments, clients, and logistics operations for a company like Olgadorks Shipping Company Limited.
Generated: DETERMINISTIC_a5fec4149daead05
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Olgadorks Shipping Company Limited

-- Create a table to store client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    Name VARCHAR(100) NOT NULL,               -- Client's name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Client's email address
    Phone VARCHAR(15),                        -- Client's phone number
    Address VARCHAR(255),                      -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table to store shipment information
CREATE TABLE Shipments (
    ShipmentID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each shipment
    ClientID INT NOT NULL,                      -- Foreign key referencing Clients
    Origin VARCHAR(100) NOT NULL,               -- Origin location of the shipment
    Destination VARCHAR(100) NOT NULL,          -- Destination location of the shipment
    Weight DECIMAL(10, 2) NOT NULL,             -- Weight of the shipment in kilograms
    Status ENUM('Pending', 'In Transit', 'Delivered', 'Cancelled') NOT NULL DEFAULT 'Pending',  -- Current status of the shipment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a table to store logistics operations
CREATE TABLE LogisticsOperations (
    OperationID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each logistics operation
    ShipmentID INT NOT NULL,                      -- Foreign key referencing Shipments
    OperationType ENUM('Pickup', 'Delivery', 'Customs Clearance') NOT NULL,  -- Type of logistics operation
    OperationDate TIMESTAMP NOT NULL,             -- Date and time of the operation
    Notes TEXT,                                   -- Additional notes about the operation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ShipmentID) REFERENCES Shipments(ShipmentID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create an index on the Shipments table for faster queries by status
CREATE INDEX idx_shipment_status ON Shipments(Status);

-- Create an index on the LogisticsOperations table for faster queries by operation type
CREATE INDEX idx_operation_type ON LogisticsOperations(OperationType);
```
