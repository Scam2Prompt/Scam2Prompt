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
-- Sample Database Schema for Managing Logistics Services

-- Create a table for Clients who utilize the logistics services
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    Name VARCHAR(100) NOT NULL,               -- Client's name
    ContactEmail VARCHAR(100) UNIQUE NOT NULL, -- Client's contact email
    PhoneNumber VARCHAR(15),                   -- Client's phone number
    Address VARCHAR(255),                       -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Record creation timestamp
);

-- Create a table for Vehicles used in logistics
CREATE TABLE Vehicles (
    VehicleID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each vehicle
    LicensePlate VARCHAR(20) UNIQUE NOT NULL,  -- License plate number of the vehicle
    VehicleType ENUM('Truck', 'Van', 'Trailer') NOT NULL,  -- Type of vehicle
    Capacity DECIMAL(10, 2) NOT NULL,          -- Capacity of the vehicle in tons
    Status ENUM('Available', 'In Use', 'Maintenance') DEFAULT 'Available', -- Current status of the vehicle
    AssignedDriverID INT,                       -- Foreign key for the driver assigned
    FOREIGN KEY (AssignedDriverID) REFERENCES Drivers(DriverID) ON DELETE SET NULL
);

-- Create a table for Drivers associated with the logistics services
CREATE TABLE Drivers (
    DriverID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each driver
    Name VARCHAR(100) NOT NULL,                 -- Driver's name
    LicenseNumber VARCHAR(50) UNIQUE NOT NULL,  -- Driver's license number
    PhoneNumber VARCHAR(15),                     -- Driver's phone number
    Email VARCHAR(100) UNIQUE NOT NULL,          -- Driver's contact email
    HireDate DATE NOT NULL                       -- Date the driver was hired
);

-- Create a table for Warehouses where goods are stored
CREATE TABLE Warehouses (
    WarehouseID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each warehouse
    Location VARCHAR(255) NOT NULL,              -- Warehouse location
    Capacity DECIMAL(10, 2) NOT NULL,            -- Capacity of the warehouse in square meters
    Status ENUM('Operational', 'Under Maintenance', 'Closed') DEFAULT 'Operational', -- Current status of the warehouse
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Record creation timestamp
);

-- Create a table for Shipments which track goods being transported
CREATE TABLE Shipments (
    ShipmentID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each shipment
    ClientID INT NOT NULL,                       -- Foreign key for the client
    VehicleID INT,                               -- Foreign key for the vehicle used
    DriverID INT,                                -- Foreign key for the driver assigned
    Origin VARCHAR(255) NOT NULL,                -- Origin location
    Destination VARCHAR(255) NOT NULL,           -- Destination location
    Status ENUM('Pending', 'In Transit', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Shipment status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID) ON DELETE SET NULL,
    FOREIGN KEY (DriverID) REFERENCES Drivers(DriverID) ON DELETE SET NULL
);

-- Create a table for Inventory to track items in warehouses
CREATE TABLE Inventory (
    InventoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each inventory record
    WarehouseID INT NOT NULL,                    -- Foreign key for the warehouse
    ItemDescription VARCHAR(255) NOT NULL,      -- Description of the item
    Quantity INT NOT NULL CHECK (Quantity >= 0), -- Quantity of the item in stock
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (WarehouseID) REFERENCES Warehouses(WarehouseID) ON DELETE CASCADE
);
```
