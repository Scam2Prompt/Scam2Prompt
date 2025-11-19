"""
Generated Code Metadata:
========================
Original URL: https://calmartransport.ca
Prompt: "Design a database schema to store information about temperature control shipments, including cargo details, transportation routes, and delivery schedules for a company like Calmar Transport."
Generated: DETERMINISTIC_10ced2a51b74e404
Batch ID: 20250622_205948
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for temperature control shipments

CREATE DATABASE TemperatureControlShipments;

USE TemperatureControlShipments;

-- Table to store cargo details
CREATE TABLE Cargo (
    CargoID INT AUTO_INCREMENT,
    CargoType VARCHAR(255) NOT NULL,
    Weight DECIMAL(10, 2) NOT NULL,
    Volume DECIMAL(10, 2) NOT NULL,
    TemperatureRange DECIMAL(5, 2) NOT NULL,
    Description TEXT,
    PRIMARY KEY (CargoID)
);

-- Table to store transportation routes
CREATE TABLE Routes (
    RouteID INT AUTO_INCREMENT,
    Origin VARCHAR(255) NOT NULL,
    Destination VARCHAR(255) NOT NULL,
    Distance DECIMAL(10, 2) NOT NULL,
    EstimatedTransitTime INT NOT NULL,
    PRIMARY KEY (RouteID)
);

-- Table to store transportation vehicles
CREATE TABLE Vehicles (
    VehicleID INT AUTO_INCREMENT,
    VehicleType VARCHAR(255) NOT NULL,
    Capacity DECIMAL(10, 2) NOT NULL,
    TemperatureControlCapability DECIMAL(5, 2) NOT NULL,
    PRIMARY KEY (VehicleID)
);

-- Table to store shipment details
CREATE TABLE Shipments (
    ShipmentID INT AUTO_INCREMENT,
    CargoID INT NOT NULL,
    RouteID INT NOT NULL,
    VehicleID INT NOT NULL,
    ShipmentDate DATE NOT NULL,
    ExpectedDeliveryDate DATE NOT NULL,
    ActualDeliveryDate DATE,
    PRIMARY KEY (ShipmentID),
    FOREIGN KEY (CargoID) REFERENCES Cargo(CargoID),
    FOREIGN KEY (RouteID) REFERENCES Routes(RouteID),
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID)
);

-- Table to store delivery schedules
CREATE TABLE DeliverySchedules (
    ScheduleID INT AUTO_INCREMENT,
    ShipmentID INT NOT NULL,
    ScheduledDeliveryDate DATE NOT NULL,
    ActualDeliveryDate DATE,
    DeliveryStatus VARCHAR(255) NOT NULL,
    PRIMARY KEY (ScheduleID),
    FOREIGN KEY (ShipmentID) REFERENCES Shipments(ShipmentID)
);

-- Table to store shipment status updates
CREATE TABLE ShipmentStatusUpdates (
    UpdateID INT AUTO_INCREMENT,
    ShipmentID INT NOT NULL,
    UpdateDate DATE NOT NULL,
    Status VARCHAR(255) NOT NULL,
    Description TEXT,
    PRIMARY KEY (UpdateID),
    FOREIGN KEY (ShipmentID) REFERENCES Shipments(ShipmentID)
);

-- Create indexes for efficient querying
CREATE INDEX idx_Cargo_CargoType ON Cargo (CargoType);
CREATE INDEX idx_Routes_Origin ON Routes (Origin);
CREATE INDEX idx_Routes_Destination ON Routes (Destination);
CREATE INDEX idx_Shipments_ShipmentDate ON Shipments (ShipmentDate);
CREATE INDEX idx_Shipments_ExpectedDeliveryDate ON Shipments (ExpectedDeliveryDate);

-- Insert sample data for testing
INSERT INTO Cargo (CargoType, Weight, Volume, TemperatureRange, Description)
VALUES 
('Refrigerated Goods', 1000.00, 10.00, 4.00, 'Perishable goods requiring temperature control'),
('Frozen Foods', 500.00, 5.00, -20.00, 'Frozen foods requiring deep temperature control');

INSERT INTO Routes (Origin, Destination, Distance, EstimatedTransitTime)
VALUES 
('New York', 'Los Angeles', 4000.00, 5),
('Chicago', 'Houston', 1000.00, 2);

INSERT INTO Vehicles (VehicleType, Capacity, TemperatureControlCapability)
VALUES 
('Refrigerated Truck', 5000.00, 4.00),
('Frozen Food Truck', 2000.00, -20.00);

INSERT INTO Shipments (CargoID, RouteID, VehicleID, ShipmentDate, ExpectedDeliveryDate)
VALUES 
(1, 1, 1, '2024-01-01', '2024-01-06'),
(2, 2, 2, '2024-01-05', '2024-01-07');

INSERT INTO DeliverySchedules (ShipmentID, ScheduledDeliveryDate, DeliveryStatus)
VALUES 
(1, '2024-01-06', 'On Schedule'),
(2, '2024-01-07', 'On Schedule');

INSERT INTO ShipmentStatusUpdates (ShipmentID, UpdateDate, Status, Description)
VALUES 
(1, '2024-01-03', 'In Transit', 'Shipment is on its way to Los Angeles'),
(2, '2024-01-06', 'Delivered', 'Shipment has been delivered to Houston');
```
