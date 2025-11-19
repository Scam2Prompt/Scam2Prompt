"""
Generated Code Metadata:
========================
Original URL: https://opcsas.com
Prompt: "Design a database schema to store information about cargo shipments, clients, and transportation services, inspired by the operations of OPC."
Generated: DETERMINISTIC_145ef0126e17c50f
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for cargo shipments, clients, and transportation services

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    Name VARCHAR(255) NOT NULL,              -- Name of the client
    Email VARCHAR(255) UNIQUE NOT NULL,      -- Email address of the client
    PhoneNumber VARCHAR(20),                 -- Contact phone number
    Address TEXT,                            -- Address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store transportation service information
CREATE TABLE TransportationServices (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(255) NOT NULL,        -- Name of the transportation service
    Description TEXT,                         -- Description of the service
    Cost DECIMAL(10, 2) NOT NULL,             -- Cost of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store cargo shipment information
CREATE TABLE Shipments (
    ShipmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each shipment
    ClientID INT NOT NULL,                     -- Foreign key referencing Clients table
    ServiceID INT NOT NULL,                    -- Foreign key referencing TransportationServices table
    CargoDescription TEXT NOT NULL,            -- Description of the cargo
    Weight DECIMAL(10, 2) NOT NULL,            -- Weight of the cargo in kilograms
    Origin VARCHAR(255) NOT NULL,              -- Origin location of the shipment
    Destination VARCHAR(255) NOT NULL,         -- Destination location of the shipment
    ShipmentDate DATE NOT NULL,                -- Date of the shipment
    DeliveryDate DATE,                         -- Expected delivery date
    Status ENUM('Pending', 'In Transit', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Status of the shipment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete for client
    FOREIGN KEY (ServiceID) REFERENCES TransportationServices(ServiceID) ON DELETE CASCADE -- Cascade delete for service
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_id ON Shipments(ClientID);
CREATE INDEX idx_service_id ON Shipments(ServiceID);
CREATE INDEX idx_status ON Shipments(Status);

-- Example of error handling: Ensure strict mode is enabled for better data integrity
SET sql_mode = 'STRICT_TRANS_TABLES';
```
