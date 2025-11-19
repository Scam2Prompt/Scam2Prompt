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
-- Create database schema for logistics services
CREATE DATABASE LogisticsDB;

-- Use the created database
USE LogisticsDB;

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
    Email VARCHAR(100) UNIQUE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CustomerID)
);

-- Create table for carriers (trucking companies, warehouses, etc.)
CREATE TABLE Carriers (
    CarrierID INT AUTO_INCREMENT,
    CompanyName VARCHAR(255) NOT NULL,
    ContactName VARCHAR(255) NOT NULL,
    ContactTitle VARCHAR(255),
    Address VARCHAR(255),
    City VARCHAR(100),
    Region VARCHAR(100),
    PostalCode VARCHAR(20),
    Country VARCHAR(100),
    Phone VARCHAR(20),
    Email VARCHAR(100) UNIQUE,
    ServiceType ENUM('trucking', 'warehousing', 'distribution') NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CarrierID)
);

-- Create table for shipments
CREATE TABLE Shipments (
    ShipmentID INT AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    CarrierID INT NOT NULL,
    ShipmentDate DATE NOT NULL,
    ExpectedDeliveryDate DATE,
    ActualDeliveryDate DATE,
    ShipmentStatus ENUM('pending', 'in_transit', 'delivered', 'lost', 'damaged') DEFAULT 'pending',
    PackageType VARCHAR(100) NOT NULL,
    PackageDescription TEXT,
    Weight DECIMAL(10, 2) NOT NULL,
    Dimensions VARCHAR(255),
    SpecialInstructions TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ShipmentID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (CarrierID) REFERENCES Carriers(CarrierID)
);

-- Create table for warehouse management
CREATE TABLE Warehouses (
    WarehouseID INT AUTO_INCREMENT,
    CarrierID INT NOT NULL,
    WarehouseAddress VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    Region VARCHAR(100) NOT NULL,
    PostalCode VARCHAR(20) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    Capacity DECIMAL(10, 2) NOT NULL,
    CurrentOccupancy DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (WarehouseID),
    FOREIGN KEY (CarrierID) REFERENCES Carriers(CarrierID)
);

-- Create table for inventory management
CREATE TABLE Inventory (
    InventoryID INT AUTO_INCREMENT,
    WarehouseID INT NOT NULL,
    ProductName VARCHAR(255) NOT NULL,
    ProductDescription TEXT,
    Quantity INT NOT NULL,
    UnitPrice DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (InventoryID),
    FOREIGN KEY (WarehouseID) REFERENCES Warehouses(WarehouseID)
);

-- Create table for distribution management
CREATE TABLE Distributions (
    DistributionID INT AUTO_INCREMENT,
    ShipmentID INT NOT NULL,
    WarehouseID INT NOT NULL,
    DistributionDate DATE NOT NULL,
    DistributionStatus ENUM('pending', 'in_progress', 'completed') DEFAULT 'pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (DistributionID),
    FOREIGN KEY (ShipmentID) REFERENCES Shipments(ShipmentID),
    FOREIGN KEY (WarehouseID) REFERENCES Warehouses(WarehouseID)
);

-- Create table for tracking and tracing
CREATE TABLE Tracking (
    TrackingID INT AUTO_INCREMENT,
    ShipmentID INT NOT NULL,
    TrackingNumber VARCHAR(255) NOT NULL,
    TrackingStatus ENUM('pending', 'scanned', 'delivered') DEFAULT 'pending',
    ScanDate DATE,
    ScanLocation VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (TrackingID),
    FOREIGN KEY (ShipmentID) REFERENCES Shipments(ShipmentID)
);
```
