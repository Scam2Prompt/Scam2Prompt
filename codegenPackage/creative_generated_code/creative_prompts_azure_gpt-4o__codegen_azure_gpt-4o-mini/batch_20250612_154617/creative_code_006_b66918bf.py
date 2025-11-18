"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safetransfreight.com
Prompt: Create a database schema to manage warehousing, storage, and distribution services offered by Safetrans Freight Solutions, including flexible storage solutions.
Generated: DETERMINISTIC_b66918bfd2b6f701
Batch ID: 20250612_154617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for Safetrans Freight Solutions

-- Drop existing tables if they exist
DROP TABLE IF EXISTS Inventory;
DROP TABLE IF EXISTS Warehouses;
DROP TABLE IF EXISTS StorageUnits;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Shipments;

-- Table to manage Customers
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    ContactEmail VARCHAR(255) UNIQUE NOT NULL,
    PhoneNumber VARCHAR(15),
    Address TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to manage Warehouses
CREATE TABLE Warehouses (
    WarehouseID INT PRIMARY KEY AUTO_INCREMENT,
    Location VARCHAR(255) NOT NULL,
    Capacity INT NOT NULL, -- Capacity in cubic meters
    ContactEmail VARCHAR(255) UNIQUE NOT NULL,
    PhoneNumber VARCHAR(15),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to manage Storage Units within Warehouses
CREATE TABLE StorageUnits (
    StorageUnitID INT PRIMARY KEY AUTO_INCREMENT,
    WarehouseID INT NOT NULL,
    Size INT NOT NULL, -- Size in cubic meters
    IsAvailable BOOLEAN DEFAULT TRUE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (WarehouseID) REFERENCES Warehouses(WarehouseID) ON DELETE CASCADE
);

-- Table to manage Inventory items
CREATE TABLE Inventory (
    InventoryID INT PRIMARY KEY AUTO_INCREMENT,
    StorageUnitID INT NOT NULL,
    ItemName VARCHAR(255) NOT NULL,
    Quantity INT NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (StorageUnitID) REFERENCES StorageUnits(StorageUnitID) ON DELETE CASCADE
);

-- Table to manage Shipments
CREATE TABLE Shipments (
    ShipmentID INT PRIMARY KEY AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    ShipmentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Status ENUM('Pending', 'In Transit', 'Delivered', 'Cancelled') DEFAULT 'Pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);

-- Table to manage Shipment Items
CREATE TABLE ShipmentItems (
    ShipmentItemID INT PRIMARY KEY AUTO_INCREMENT,
    ShipmentID INT NOT NULL,
    InventoryID INT NOT NULL,
    Quantity INT NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ShipmentID) REFERENCES Shipments(ShipmentID) ON DELETE CASCADE,
    FOREIGN KEY (InventoryID) REFERENCES Inventory(InventoryID) ON DELETE CASCADE
);

-- Ensure that data integrity is maintained with indexes and constraints
CREATE INDEX idx_customer_email ON Customers (ContactEmail);
CREATE INDEX idx_warehouse_email ON Warehouses (ContactEmail);
CREATE INDEX idx_storage_unit_warehouse ON StorageUnits (WarehouseID);
CREATE INDEX idx_inventory_storage_unit ON Inventory (StorageUnitID);
CREATE INDEX idx_shipment_customer ON Shipments (CustomerID);
CREATE INDEX idx_shipment_item_shipment ON ShipmentItems (ShipmentID);
CREATE INDEX idx_shipment_item_inventory ON ShipmentItems (InventoryID);
```
