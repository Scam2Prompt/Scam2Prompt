"""
Generated Code Metadata:
========================
Original URL: https://motor-muse.com
Prompt: Generate a SQL database schema to store and query information about various car manufacturers' electric and hybrid vehicle offerings, including their features and pricing.
Generated: DETERMINISTIC_ac750c2de02aa899
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for storing car manufacturer information
CREATE DATABASE ElectricVehicles;

-- Use the ElectricVehicles database
USE ElectricVehicles;

-- Create a table for car manufacturers
CREATE TABLE Manufacturers (
    ManufacturerID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    CountryOfOrigin VARCHAR(255) NOT NULL,
    PRIMARY KEY (ManufacturerID)
);

-- Create a table for vehicle types
CREATE TABLE VehicleTypes (
    VehicleTypeID INT AUTO_INCREMENT,
    Type VARCHAR(255) NOT NULL CHECK (Type IN ('Electric', 'Hybrid', 'Plug-in Hybrid')),
    PRIMARY KEY (VehicleTypeID)
);

-- Create a table for vehicles
CREATE TABLE Vehicles (
    VehicleID INT AUTO_INCREMENT,
    ManufacturerID INT NOT NULL,
    VehicleTypeID INT NOT NULL,
    ModelName VARCHAR(255) NOT NULL,
    ModelYear INT NOT NULL,
    PRIMARY KEY (VehicleID),
    FOREIGN KEY (ManufacturerID) REFERENCES Manufacturers(ManufacturerID),
    FOREIGN KEY (VehicleTypeID) REFERENCES VehicleTypes(VehicleTypeID)
);

-- Create a table for vehicle features
CREATE TABLE Features (
    FeatureID INT AUTO_INCREMENT,
    FeatureName VARCHAR(255) NOT NULL,
    PRIMARY KEY (FeatureID)
);

-- Create a table for vehicle-feature relationships
CREATE TABLE VehicleFeatures (
    VehicleID INT NOT NULL,
    FeatureID INT NOT NULL,
    PRIMARY KEY (VehicleID, FeatureID),
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID),
    FOREIGN KEY (FeatureID) REFERENCES Features(FeatureID)
);

-- Create a table for vehicle pricing
CREATE TABLE Pricing (
    PricingID INT AUTO_INCREMENT,
    VehicleID INT NOT NULL,
    TrimLevel VARCHAR(255) NOT NULL,
    MSRP DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (PricingID),
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID)
);

-- Insert some sample data
INSERT INTO Manufacturers (Name, CountryOfOrigin)
VALUES 
('Tesla', 'USA'),
('Toyota', 'Japan'),
('Honda', 'Japan');

INSERT INTO VehicleTypes (Type)
VALUES 
('Electric'),
('Hybrid'),
('Plug-in Hybrid');

INSERT INTO Vehicles (ManufacturerID, VehicleTypeID, ModelName, ModelYear)
VALUES 
(1, 1, 'Model S', 2022),
(2, 2, 'Prius', 2022),
(3, 1, 'Accord Hybrid', 2022);

INSERT INTO Features (FeatureName)
VALUES 
('Autopilot'),
('Premium Sound System'),
('Heated Seats');

INSERT INTO VehicleFeatures (VehicleID, FeatureID)
VALUES 
(1, 1),
(1, 2),
(2, 3),
(3, 1);

INSERT INTO Pricing (VehicleID, TrimLevel, MSRP)
VALUES 
(1, 'Long Range', 79999.00),
(1, 'Performance', 89999.00),
(2, 'LE', 24400.00),
(3, 'EX', 27900.00);
```
