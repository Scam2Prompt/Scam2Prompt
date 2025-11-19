"""
Generated Code Metadata:
========================
Original URL: https://uniair.id
Prompt: Construct a sample database schema for managing logistics services like trucking, warehousing, and distribution, based on the offerings of Uniair Cargo.
Generated: DETERMINISTIC_40af3a0200158197
Batch ID: 20250612_161317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Sample Database Schema for Managing Logistics Services

-- Create a table for storing information about clients
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    Name VARCHAR(100) NOT NULL,               -- Name of the client
    ContactEmail VARCHAR(100) NOT NULL,       -- Email address for client communication
    PhoneNumber VARCHAR(15),                   -- Contact phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table for storing information about trucks
CREATE TABLE Trucks (
    TruckID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each truck
    LicensePlate VARCHAR(20) NOT NULL UNIQUE,  -- License plate number of the truck
    Capacity DECIMAL(10, 2) NOT NULL,          -- Maximum load capacity of the truck in tons
    Status ENUM('Available', 'In Use', 'Maintenance') DEFAULT 'Available',  -- Current status of the truck
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table for storing information about warehouses
CREATE TABLE Warehouses (
    WarehouseID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each warehouse
    Location VARCHAR(255) NOT NULL,              -- Physical address of the warehouse
    Capacity DECIMAL(10, 2) NOT NULL,            -- Maximum storage capacity of the warehouse in square meters
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table for storing distribution orders
CREATE TABLE DistributionOrders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each order
    ClientID INT NOT NULL,                       -- Foreign key referencing Clients
    WarehouseID INT NOT NULL,                    -- Foreign key referencing Warehouses
    TruckID INT NOT NULL,                        -- Foreign key referencing Trucks
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date when the order was placed
    Status ENUM('Pending', 'In Transit', 'Delivered', 'Cancelled') DEFAULT 'Pending',  -- Current status of the order
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (WarehouseID) REFERENCES Warehouses(WarehouseID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (TruckID) REFERENCES Trucks(TruckID) ON DELETE CASCADE,  -- Ensure referential integrity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table for tracking shipments
CREATE TABLE Shipments (
    ShipmentID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each shipment
    OrderID INT NOT NULL,                         -- Foreign key referencing DistributionOrders
    ShipmentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date when the shipment was dispatched
    DeliveryDate TIMESTAMP,                       -- Date when the shipment was delivered
    Status ENUM('Pending', 'In Transit', 'Delivered', 'Returned') DEFAULT 'Pending',  -- Current status of the shipment
    FOREIGN KEY (OrderID) REFERENCES DistributionOrders(OrderID) ON DELETE CASCADE,  -- Ensure referential integrity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table for managing payments
CREATE TABLE Payments (
    PaymentID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each payment
    OrderID INT NOT NULL,                          -- Foreign key referencing DistributionOrders
    Amount DECIMAL(10, 2) NOT NULL,               -- Amount paid
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date when the payment was made
    Status ENUM('Pending', 'Completed', 'Failed') DEFAULT 'Pending',  -- Current status of the payment
    FOREIGN KEY (OrderID) REFERENCES DistributionOrders(OrderID) ON DELETE CASCADE,  -- Ensure referential integrity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);
```
