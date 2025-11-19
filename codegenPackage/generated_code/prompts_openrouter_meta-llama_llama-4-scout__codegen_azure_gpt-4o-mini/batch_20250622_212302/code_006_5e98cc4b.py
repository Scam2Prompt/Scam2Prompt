"""
Generated Code Metadata:
========================
Original URL: https://uniair.id
Prompt: Design a simple database schema to store and manage Uniair Cargo's global network of logistics services, including air freight, ocean freight, and trucking services.
Generated: DETERMINISTIC_5e98cc4bef87e551
Batch ID: 20250622_212302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Uniair Cargo's global logistics services

-- Create a database for Uniair Cargo
CREATE DATABASE UniairCargo;

-- Use the created database
USE UniairCargo;

-- Table to store information about logistics services
CREATE TABLE LogisticsServices (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceType ENUM('Air Freight', 'Ocean Freight', 'Trucking') NOT NULL, -- Type of logistics service
    Description TEXT, -- Description of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the service was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table to store information about locations
CREATE TABLE Locations (
    LocationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each location
    LocationName VARCHAR(255) NOT NULL, -- Name of the location
    Country VARCHAR(100) NOT NULL, -- Country of the location
    City VARCHAR(100) NOT NULL, -- City of the location
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the location was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table to store information about shipments
CREATE TABLE Shipments (
    ShipmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each shipment
    ServiceID INT NOT NULL, -- Foreign key referencing LogisticsServices
    OriginLocationID INT NOT NULL, -- Foreign key referencing Locations
    DestinationLocationID INT NOT NULL, -- Foreign key referencing Locations
    ShipmentDate DATE NOT NULL, -- Date of the shipment
    Status ENUM('Pending', 'In Transit', 'Delivered', 'Cancelled') NOT NULL, -- Current status of the shipment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the shipment was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (ServiceID) REFERENCES LogisticsServices(ServiceID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (OriginLocationID) REFERENCES Locations(LocationID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (DestinationLocationID) REFERENCES Locations(LocationID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    Name VARCHAR(255) NOT NULL, -- Name of the customer
    Email VARCHAR(255) UNIQUE NOT NULL, -- Email of the customer
    Phone VARCHAR(20), -- Phone number of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the customer was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table to store customer shipments
CREATE TABLE CustomerShipments (
    CustomerShipmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer shipment
    CustomerID INT NOT NULL, -- Foreign key referencing Customers
    ShipmentID INT NOT NULL, -- Foreign key referencing Shipments
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the customer shipment was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ShipmentID) REFERENCES Shipments(ShipmentID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_service_type ON LogisticsServices(ServiceType);
CREATE INDEX idx_location_name ON Locations(LocationName);
CREATE INDEX idx_shipment_status ON Shipments(Status);
CREATE INDEX idx_customer_email ON Customers(Email);
```
