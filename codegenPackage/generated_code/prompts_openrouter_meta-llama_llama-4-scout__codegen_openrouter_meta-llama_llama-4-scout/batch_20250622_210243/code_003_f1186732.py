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
-- logistics_distribution_centers_schema.sql

-- Create a database for logistics and distribution centers
CREATE DATABASE LogisticsDistributionCenters;

-- Use the database
USE LogisticsDistributionCenters;

-- Create a table for clients
CREATE TABLE Clients (
  ClientID INT AUTO_INCREMENT,
  Name VARCHAR(255) NOT NULL,
  Address VARCHAR(255) NOT NULL,
  City VARCHAR(100) NOT NULL,
  State VARCHAR(100) NOT NULL,
  Country VARCHAR(100) NOT NULL,
  PostalCode VARCHAR(20) NOT NULL,
  Email VARCHAR(255) UNIQUE NOT NULL,
  Phone VARCHAR(20) NOT NULL,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (ClientID)
);

-- Create a table for warehouses
CREATE TABLE Warehouses (
  WarehouseID INT AUTO_INCREMENT,
  ClientID INT NOT NULL,
  Name VARCHAR(255) NOT NULL,
  Address VARCHAR(255) NOT NULL,
  City VARCHAR(100) NOT NULL,
  State VARCHAR(100) NOT NULL,
  Country VARCHAR(100) NOT NULL,
  PostalCode VARCHAR(20) NOT NULL,
  Capacity DECIMAL(10, 2) NOT NULL,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (WarehouseID),
  FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Create a table for transportation units
CREATE TABLE TransportationUnits (
  TransportationUnitID INT AUTO_INCREMENT,
  ClientID INT NOT NULL,
  Type VARCHAR(100) NOT NULL,
  Description VARCHAR(255),
  Capacity DECIMAL(10, 2) NOT NULL,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (TransportationUnitID),
  FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Create a table for warehouse inventory
CREATE TABLE WarehouseInventory (
  WarehouseInventoryID INT AUTO_INCREMENT,
  WarehouseID INT NOT NULL,
  ProductName VARCHAR(255) NOT NULL,
  Quantity DECIMAL(10, 2) NOT NULL,
  UnitCost DECIMAL(10, 2) NOT NULL,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (WarehouseInventoryID),
  FOREIGN KEY (WarehouseID) REFERENCES Warehouses(WarehouseID) ON DELETE CASCADE
);

-- Create a table for shipments
CREATE TABLE Shipments (
  ShipmentID INT AUTO_INCREMENT,
  ClientID INT NOT NULL,
  WarehouseID INT NOT NULL,
  TransportationUnitID INT NOT NULL,
  ShipmentDate DATE NOT NULL,
  ExpectedDeliveryDate DATE NOT NULL,
  ActualDeliveryDate DATE,
  Status VARCHAR(100) NOT NULL,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (ShipmentID),
  FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,
  FOREIGN KEY (WarehouseID) REFERENCES Warehouses(WarehouseID) ON DELETE CASCADE,
  FOREIGN KEY (TransportationUnitID) REFERENCES TransportationUnits(TransportationUnitID) ON DELETE CASCADE
);

-- Create a table for shipment items
CREATE TABLE ShipmentItems (
  ShipmentItemID INT AUTO_INCREMENT,
  ShipmentID INT NOT NULL,
  ProductName VARCHAR(255) NOT NULL,
  Quantity DECIMAL(10, 2) NOT NULL,
  UnitCost DECIMAL(10, 2) NOT NULL,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (ShipmentItemID),
  FOREIGN KEY (ShipmentID) REFERENCES Shipments(ShipmentID) ON DELETE CASCADE
);

-- Create indexes on foreign key columns
CREATE INDEX idx_warehouses_client_id ON Warehouses (ClientID);
CREATE INDEX idx_transportation_units_client_id ON TransportationUnits (ClientID);
CREATE INDEX idx_warehouse_inventory_warehouse_id ON WarehouseInventory (WarehouseID);
CREATE INDEX idx_shipments_client_id ON Shipments (ClientID);
CREATE INDEX idx_shipments_warehouse_id ON Shipments (WarehouseID);
CREATE INDEX idx_shipments_transportation_unit_id ON Shipments (TransportationUnitID);
CREATE INDEX idx_shipment_items_shipment_id ON ShipmentItems (ShipmentID);
```

```sql
-- Example usage:

-- Insert a client
INSERT INTO Clients (Name, Address, City, State, Country, PostalCode, Email, Phone)
VALUES ('Example Client', '123 Main St', 'Anytown', 'CA', 'USA', '12345', 'client@example.com', '123-456-7890');

-- Insert a warehouse
INSERT INTO Warehouses (ClientID, Name, Address, City, State, Country, PostalCode, Capacity)
VALUES (1, 'Example Warehouse', '456 Elm St', 'Othertown', 'NY', 'USA', '67890', 10000.00);

-- Insert a transportation unit
INSERT INTO TransportationUnits (ClientID, Type, Description, Capacity)
VALUES (1, 'Truck', 'Example truck', 5000.00);

-- Insert a warehouse inventory item
INSERT INTO WarehouseInventory (WarehouseID, ProductName, Quantity, UnitCost)
VALUES (1, 'Example Product', 100.00, 10.00);

-- Insert a shipment
INSERT INTO Shipments (ClientID, WarehouseID, TransportationUnitID, ShipmentDate, ExpectedDeliveryDate, Status)
VALUES (1, 1, 1, '2022-01-01', '2022-01-15', 'In Transit');

-- Insert a shipment item
INSERT INTO ShipmentItems (ShipmentID, ProductName, Quantity, UnitCost)
VALUES (1, 'Example Product', 50.00, 10.00);
```
