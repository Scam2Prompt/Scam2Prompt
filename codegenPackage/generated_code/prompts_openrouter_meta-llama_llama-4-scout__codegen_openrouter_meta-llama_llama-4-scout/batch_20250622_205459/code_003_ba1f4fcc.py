"""
Generated Code Metadata:
========================
Original URL: https://kalgatetechnology.com.ng
Prompt: Design a database schema for storing information about clients, drivers, and vehicles for a logistics company like Kalgate Technology that has 110 clients worldwide and 2340 tonnes transported.
Generated: DETERMINISTIC_ba1f4fcc2bbd17b5
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the logistics company
CREATE DATABASE LogisticsCompany;

-- Use the database
USE LogisticsCompany;

-- Create a table for clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT,
    CompanyName VARCHAR(255) NOT NULL,
    ContactPerson VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    PostalCode VARCHAR(20) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ClientID)
);

-- Create a table for drivers
CREATE TABLE Drivers (
    DriverID INT AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    LicenseNumber VARCHAR(50) NOT NULL,
    LicenseExpiry DATE NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (DriverID)
);

-- Create a table for vehicles
CREATE TABLE Vehicles (
    VehicleID INT AUTO_INCREMENT,
    VehicleType VARCHAR(100) NOT NULL,
    VehicleMake VARCHAR(100) NOT NULL,
    VehicleModel VARCHAR(100) NOT NULL,
    VehicleYear INT NOT NULL,
    LicensePlate VARCHAR(20) NOT NULL,
    Capacity DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (VehicleID)
);

-- Create a table for shipments
CREATE TABLE Shipments (
    ShipmentID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    DriverID INT,
    VehicleID INT,
    ShipmentDate DATE NOT NULL,
    Weight DECIMAL(10, 2) NOT NULL,
    Distance DECIMAL(10, 2) NOT NULL,
    Status VARCHAR(50) NOT NULL DEFAULT 'Pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ShipmentID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID),
    FOREIGN KEY (DriverID) REFERENCES Drivers(DriverID),
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID)
);

-- Create a table for shipment history
CREATE TABLE ShipmentHistory (
    HistoryID INT AUTO_INCREMENT,
    ShipmentID INT NOT NULL,
    Status VARCHAR(50) NOT NULL,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (HistoryID),
    FOREIGN KEY (ShipmentID) REFERENCES Shipments(ShipmentID)
);

-- Insert sample data
INSERT INTO Clients (CompanyName, ContactPerson, Email, Phone, Address, City, Country, PostalCode)
VALUES 
('Kalgate Technology', 'John Doe', 'john.doe@kalgate.com', '+1 123 456 7890', '123 Main St', 'New York', 'USA', '10001'),
('ABC Inc.', 'Jane Smith', 'jane.smith@abc.com', '+1 987 654 3210', '456 Park Ave', 'Los Angeles', 'USA', '90001');

INSERT INTO Drivers (FirstName, LastName, Email, Phone, LicenseNumber, LicenseExpiry)
VALUES 
('Michael', 'Brown', 'michael.brown@kalgate.com', '+1 111 222 3333', 'License123', '2025-01-01'),
('Emily', 'Chen', 'emily.chen@kalgate.com', '+1 444 555 6666', 'License456', '2026-01-01');

INSERT INTO Vehicles (VehicleType, VehicleMake, VehicleModel, VehicleYear, LicensePlate, Capacity)
VALUES 
('Truck', 'Ford', 'F-150', 2020, 'ABC123', 1000.00),
('Van', 'Toyota', 'Hiace', 2019, 'XYZ789', 500.00);

INSERT INTO Shipments (ClientID, DriverID, VehicleID, ShipmentDate, Weight, Distance)
VALUES 
(1, 1, 1, '2022-01-01', 100.00, 100.00),
(2, 2, 2, '2022-01-15', 200.00, 200.00);

-- Create views for easy data retrieval
CREATE VIEW ClientShipments AS
SELECT c.CompanyName, s.ShipmentDate, s.Weight, s.Distance
FROM Clients c
JOIN Shipments s ON c.ClientID = s.ClientID;

CREATE VIEW DriverShipments AS
SELECT d.FirstName, d.LastName, s.ShipmentDate, s.Weight, s.Distance
FROM Drivers d
JOIN Shipments s ON d.DriverID = s.DriverID;

CREATE VIEW VehicleShipments AS
SELECT v.VehicleMake, v.VehicleModel, s.ShipmentDate, s.Weight, s.Distance
FROM Vehicles v
JOIN Shipments s ON v.VehicleID = s.VehicleID;
```
