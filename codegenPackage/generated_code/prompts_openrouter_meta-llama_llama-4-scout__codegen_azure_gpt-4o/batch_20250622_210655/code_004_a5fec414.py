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

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    Name VARCHAR(255) NOT NULL,              -- Full name of the client
    Email VARCHAR(255) UNIQUE NOT NULL,      -- Email address of the client
    PhoneNumber VARCHAR(20),                 -- Contact phone number
    Address TEXT,                            -- Physical address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the client was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store shipment information
CREATE TABLE Shipments (
    ShipmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each shipment
    ClientID INT NOT NULL,                     -- Foreign key referencing the client
    Origin VARCHAR(255) NOT NULL,              -- Origin location of the shipment
    Destination VARCHAR(255) NOT NULL,         -- Destination location of the shipment
    Weight DECIMAL(10, 2) NOT NULL,            -- Weight of the shipment in kilograms
    Status ENUM('Pending', 'In Transit', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Current status of the shipment
    EstimatedDeliveryDate DATE,                -- Estimated delivery date
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the shipment was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Table to store logistics operations
CREATE TABLE LogisticsOperations (
    OperationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each operation
    ShipmentID INT NOT NULL,                    -- Foreign key referencing the shipment
    OperationType ENUM('Pickup', 'Transit', 'Delivery', 'Inspection') NOT NULL, -- Type of logistics operation
    OperationDate TIMESTAMP NOT NULL,           -- Date and time of the operation
    Location VARCHAR(255) NOT NULL,             -- Location where the operation occurred
    Notes TEXT,                                 -- Additional notes about the operation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the operation was recorded
    FOREIGN KEY (ShipmentID) REFERENCES Shipments(ShipmentID) ON DELETE CASCADE -- Cascade delete if shipment is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_email ON Clients(Email); -- Index for quick lookup by email
CREATE INDEX idx_shipment_status ON Shipments(Status); -- Index for filtering by shipment status
CREATE INDEX idx_operation_date ON LogisticsOperations(OperationDate); -- Index for sorting/filtering by operation date
```
