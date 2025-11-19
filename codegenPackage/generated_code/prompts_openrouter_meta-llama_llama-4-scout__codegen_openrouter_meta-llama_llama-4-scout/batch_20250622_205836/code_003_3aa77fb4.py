"""
Generated Code Metadata:
========================
Original URL: https://binqutab.ae
Prompt: Design a database schema for a logistics company providing ground, air, and sea freight services, similar to Bin Qutab Logistics L.L.C's cargo services.
Generated: DETERMINISTIC_3aa77fb4df0fc534
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for logistics company
CREATE DATABASE LogisticsCompany;

-- Use the database
USE LogisticsCompany;

-- Create table for customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT,
    CompanyName VARCHAR(255) NOT NULL,
    ContactName VARCHAR(255) NOT NULL,
    ContactTitle VARCHAR(255),
    Address VARCHAR(255),
    City VARCHAR(100),
    Region VARCHAR(100),
    PostalCode VARCHAR(20),
    Country VARCHAR(100),
    Phone VARCHAR(20),
    Fax VARCHAR(20),
    Email VARCHAR(100) UNIQUE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CustomerID)
);

-- Create table for services
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT,
    ServiceType ENUM('Ground', 'Air', 'Sea') NOT NULL,
    ServiceDescription TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ServiceID)
);

-- Create table for shipments
CREATE TABLE Shipments (
    ShipmentID INT AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    ServiceID INT NOT NULL,
    ShipmentDate DATE NOT NULL,
    ExpectedDeliveryDate DATE,
    ActualDeliveryDate DATE,
    ShipmentStatus ENUM('Pending', 'In Transit', 'Delivered', 'Lost', 'Damaged') NOT NULL DEFAULT 'Pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ShipmentID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID)
);

-- Create table for shipment tracking
CREATE TABLE ShipmentTracking (
    TrackingID INT AUTO_INCREMENT,
    ShipmentID INT NOT NULL,
    TrackingDate DATE NOT NULL,
    TrackingStatus VARCHAR(255) NOT NULL,
    Location VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (TrackingID),
    FOREIGN KEY (ShipmentID) REFERENCES Shipments(ShipmentID)
);

-- Create table for warehouses
CREATE TABLE Warehouses (
    WarehouseID INT AUTO_INCREMENT,
    WarehouseName VARCHAR(255) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    Region VARCHAR(100) NOT NULL,
    PostalCode VARCHAR(20) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    Phone VARCHAR(20),
    Fax VARCHAR(20),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (WarehouseID)
);

-- Create table for shipment warehouse mapping
CREATE TABLE ShipmentWarehouses (
    ShipmentID INT NOT NULL,
    WarehouseID INT NOT NULL,
    ArrivalDate DATE,
    DepartureDate DATE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ShipmentID, WarehouseID),
    FOREIGN KEY (ShipmentID) REFERENCES Shipments(ShipmentID),
    FOREIGN KEY (WarehouseID) REFERENCES Warehouses(WarehouseID)
);

-- Create table for users
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT,
    Username VARCHAR(100) NOT NULL UNIQUE,
    PasswordHash VARCHAR(255) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    Role ENUM('Admin', 'Customer', 'Dispatcher') NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (UserID)
);

-- Create table for invoices
CREATE TABLE Invoices (
    InvoiceID INT AUTO_INCREMENT,
    ShipmentID INT NOT NULL,
    InvoiceDate DATE NOT NULL,
    InvoiceAmount DECIMAL(10, 2) NOT NULL,
    PaymentStatus ENUM('Pending', 'Paid') NOT NULL DEFAULT 'Pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (InvoiceID),
    FOREIGN KEY (ShipmentID) REFERENCES Shipments(ShipmentID)
);

-- Create indexes on foreign key columns
CREATE INDEX idx_CustomerID ON Shipments (CustomerID);
CREATE INDEX idx_ServiceID ON Shipments (ServiceID);
CREATE INDEX idx_ShipmentID ON ShipmentTracking (ShipmentID);
CREATE INDEX idx_ShipmentID ON ShipmentWarehouses (ShipmentID);
CREATE INDEX idx_WarehouseID ON ShipmentWarehouses (WarehouseID);
CREATE INDEX idx_ShipmentID ON Invoices (ShipmentID);
```

```sql
-- Example data insertion
INSERT INTO Customers (CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone, Fax, Email)
VALUES 
('ABC Inc.', 'John Doe', 'CEO', '123 Main St', 'New York', 'NY', '10001', 'USA', '123-456-7890', '123-456-7891', 'john.doe@example.com'),
('XYZ Corp.', 'Jane Smith', 'Manager', '456 Park Ave', 'Los Angeles', 'CA', '90001', 'USA', '987-654-3210', '987-654-3211', 'jane.smith@example.com');

INSERT INTO Services (ServiceType, ServiceDescription)
VALUES 
('Ground', 'Ground freight services'),
('Air', 'Air freight services'),
('Sea', 'Sea freight services');

INSERT INTO Shipments (CustomerID, ServiceID, ShipmentDate, ExpectedDeliveryDate)
VALUES 
(1, 1, '2022-01-01', '2022-01-15'),
(2, 2, '2022-01-05', '2022-01-20');

INSERT INTO ShipmentTracking (ShipmentID, TrackingDate, TrackingStatus, Location)
VALUES 
(1, '2022-01-05', 'In Transit', 'New York'),
(1, '2022-01-10', 'In Transit', 'Chicago'),
(2, '2022-01-10', 'In Transit', 'Los Angeles');

INSERT INTO Warehouses (WarehouseName, Address, City, Region, PostalCode, Country, Phone, Fax)
VALUES 
('New York Warehouse', '789 Broadway', 'New York', 'NY', '10001', 'USA', '123-456-7890', '123-456-7891'),
('Los Angeles Warehouse', '321 Hollywood Blvd', 'Los Angeles', 'CA', '90001', 'USA', '987-654-3210', '987-654-3211');

INSERT INTO ShipmentWarehouses (ShipmentID, WarehouseID, ArrivalDate, DepartureDate)
VALUES 
(1, 1, '2022-01-05', '2022-01-10'),
(2, 2, '2022-01-10', NULL);

INSERT INTO Users (Username, PasswordHash, Email, Role)
VALUES 
('admin', 'password_hash', 'admin@example.com', 'Admin'),
('customer', 'password_hash', 'customer@example.com', 'Customer'),
('dispatcher', 'password_hash', 'dispatcher@example.com', 'Dispatcher');

INSERT INTO Invoices (ShipmentID, InvoiceDate, InvoiceAmount)
VALUES 
(1, '2022-01-15', 1000.00),
(2, '2022-01-20', 2000.00);
```
