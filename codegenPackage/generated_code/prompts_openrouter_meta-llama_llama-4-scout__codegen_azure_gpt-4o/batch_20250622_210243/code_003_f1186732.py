"""
Generated Code Metadata:
========================
Original URL: https://plm.cr
Prompt: "Design a database schema to store information about logistics and distribution centers, inspired by PLM's business model, including entities such as clients, warehouses, and transportation units."
Generated: DETERMINISTIC_f1186732c9c26b8d
Batch ID: 20250622_210243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Logistics and Distribution Centers

-- Table to store information about clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    Name VARCHAR(255) NOT NULL,              -- Name of the client
    Email VARCHAR(255) UNIQUE NOT NULL,      -- Email address of the client
    PhoneNumber VARCHAR(20),                 -- Contact phone number
    Address TEXT,                            -- Address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the client was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about warehouses
CREATE TABLE Warehouses (
    WarehouseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each warehouse
    Name VARCHAR(255) NOT NULL,                 -- Name of the warehouse
    Location TEXT NOT NULL,                     -- Physical location of the warehouse
    Capacity INT NOT NULL,                      -- Maximum storage capacity of the warehouse
    ManagerName VARCHAR(255),                   -- Name of the warehouse manager
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the warehouse was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about transportation units
CREATE TABLE TransportationUnits (
    UnitID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each transportation unit
    Type VARCHAR(50) NOT NULL,                 -- Type of transportation unit (e.g., truck, van, etc.)
    LicensePlate VARCHAR(50) UNIQUE NOT NULL,  -- License plate number
    Capacity INT NOT NULL,                     -- Maximum carrying capacity of the unit
    Status ENUM('Available', 'In Transit', 'Under Maintenance') DEFAULT 'Available', -- Current status of the unit
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the unit was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about shipments
CREATE TABLE Shipments (
    ShipmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each shipment
    ClientID INT NOT NULL,                     -- Reference to the client who owns the shipment
    WarehouseID INT NOT NULL,                  -- Reference to the warehouse where the shipment is stored
    UnitID INT,                                -- Reference to the transportation unit used for the shipment
    Status ENUM('Pending', 'In Transit', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Current status of the shipment
    ShipmentDate DATE NOT NULL,                -- Date of the shipment
    DeliveryDate DATE,                         -- Expected or actual delivery date
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the shipment was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (WarehouseID) REFERENCES Warehouses(WarehouseID) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (UnitID) REFERENCES TransportationUnits(UnitID) ON DELETE SET NULL -- Foreign key constraint
);

-- Table to store logs for tracking shipment status changes
CREATE TABLE ShipmentLogs (
    LogID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each log entry
    ShipmentID INT NOT NULL,                   -- Reference to the shipment being tracked
    Status ENUM('Pending', 'In Transit', 'Delivered', 'Cancelled') NOT NULL, -- Status at the time of the log
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the log entry
    Notes TEXT,                                -- Additional notes about the status change
    FOREIGN KEY (ShipmentID) REFERENCES Shipments(ShipmentID) ON DELETE CASCADE -- Foreign key constraint
);

-- Indexes for optimizing queries
CREATE INDEX idx_clients_email ON Clients(Email); -- Index for quick lookup of clients by email
CREATE INDEX idx_warehouses_location ON Warehouses(Location); -- Index for quick lookup of warehouses by location
CREATE INDEX idx_transportation_units_status ON TransportationUnits(Status); -- Index for quick lookup of transportation units by status
CREATE INDEX idx_shipments_status ON Shipments(Status); -- Index for quick lookup of shipments by status
CREATE INDEX idx_shipment_logs_timestamp ON ShipmentLogs(Timestamp); -- Index for quick lookup of logs by timestamp
```
