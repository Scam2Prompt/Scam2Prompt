"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniair.id
Prompt: Construct a sample database schema for managing logistics services like trucking, warehousing, and distribution, based on the offerings of Uniair Cargo.
Generated: DETERMINISTIC_40af3a0200158197
Batch ID: 20250612_161317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Logistics Services (Trucking, Warehousing, Distribution)
-- Designed for Uniair Cargo offerings

-- Table to store companies or clients using the logistics services
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each client
    Name VARCHAR(255) NOT NULL,              -- Name of the client
    Email VARCHAR(255) UNIQUE NOT NULL,      -- Contact email of the client
    Phone VARCHAR(15),                       -- Contact phone number
    Address TEXT NOT NULL,                   -- Address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store details of trucks used in trucking services
CREATE TABLE Trucks (
    TruckID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each truck
    LicensePlate VARCHAR(50) UNIQUE NOT NULL, -- License plate number
    Model VARCHAR(100),                       -- Model of the truck
    Capacity DECIMAL(10, 2) NOT NULL,         -- Maximum capacity in tons
    Status ENUM('Available', 'In Transit', 'Under Maintenance') DEFAULT 'Available', -- Current status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store warehousing facilities
CREATE TABLE Warehouses (
    WarehouseID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each warehouse
    Name VARCHAR(255) NOT NULL,                 -- Name of the warehouse
    Location TEXT NOT NULL,                     -- Physical address or location
    Capacity DECIMAL(12, 2) NOT NULL,           -- Maximum storage capacity in cubic meters
    Status ENUM('Active', 'Inactive') DEFAULT 'Active', -- Operational status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store distribution orders or shipments
CREATE TABLE Shipments (
    ShipmentID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each shipment
    ClientID INT NOT NULL,                     -- Reference to the client initiating the shipment
    TruckID INT NULL,                          -- Reference to the truck assigned (if applicable)
    WarehouseID INT NULL,                      -- Reference to the warehouse used (if applicable)
    Origin TEXT NOT NULL,                      -- Origin address of the shipment
    Destination TEXT NOT NULL,                 -- Destination address of the shipment
    Weight DECIMAL(10, 2) NOT NULL,            -- Weight of the shipment in tons
    Status ENUM('Pending', 'In Progress', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Shipment status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID), -- Enforce relationship with Clients table
    FOREIGN KEY (TruckID) REFERENCES Trucks(TruckID), -- Enforce relationship with Trucks table
    FOREIGN KEY (WarehouseID) REFERENCES Warehouses(WarehouseID) -- Enforce relationship with Warehouses table
);

-- Table to log activities for auditing purposes
CREATE TABLE ActivityLog (
    LogID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each log entry
    Entity VARCHAR(255) NOT NULL,         -- Entity affected (e.g., 'Shipment', 'Warehouse', etc.)
    EntityID INT NOT NULL,                -- ID of the affected entity
    Action VARCHAR(255) NOT NULL,         -- Action performed (e.g., 'Created', 'Updated', 'Deleted')
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Time of the action
    Details TEXT                          -- Additional details about the action
);

-- Indexes for performance optimization
CREATE INDEX idx_shipments_status ON Shipments(Status); -- Index on Shipment status
CREATE INDEX idx_clients_email ON Clients(Email);       -- Index on Client email
CREATE INDEX idx_trucks_status ON Trucks(Status);       -- Index on Truck status
CREATE INDEX idx_warehouses_status ON Warehouses(Status); -- Index on Warehouse status
```
