"""
Generated Code Metadata:
========================
Original URL: https://daimonlogisticsbd.com
Prompt: Create a SQL database schema to manage and consolidate shipments for import and export, including tables for air freight, ocean freight, and customs brokerage, inspired by Daimon Logistics' services.
Generated: DETERMINISTIC_a1e9d8b1cc428188
Batch ID: 20250622_205440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for shipment management
CREATE DATABASE ShipmentManagement;

-- Use the database schema
USE ShipmentManagement;

-- Create table for carriers
CREATE TABLE Carriers (
    CarrierID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CarrierID)
);

-- Create table for shipment types
CREATE TABLE ShipmentTypes (
    ShipmentTypeID INT AUTO_INCREMENT,
    Type VARCHAR(50) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ShipmentTypeID)
);

-- Create table for air freight shipments
CREATE TABLE AirFreightShipments (
    AirFreightShipmentID INT AUTO_INCREMENT,
    ShipmentTypeID INT NOT NULL,
    CarrierID INT NOT NULL,
    ShipmentDate DATE NOT NULL,
    DepartureAirport VARCHAR(3) NOT NULL,
    ArrivalAirport VARCHAR(3) NOT NULL,
    Weight DECIMAL(10, 2) NOT NULL,
    Volume DECIMAL(10, 2) NOT NULL,
    Status VARCHAR(50) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (AirFreightShipmentID),
    FOREIGN KEY (ShipmentTypeID) REFERENCES ShipmentTypes(ShipmentTypeID),
    FOREIGN KEY (CarrierID) REFERENCES Carriers(CarrierID)
);

-- Create table for ocean freight shipments
CREATE TABLE OceanFreightShipments (
    OceanFreightShipmentID INT AUTO_INCREMENT,
    ShipmentTypeID INT NOT NULL,
    CarrierID INT NOT NULL,
    ShipmentDate DATE NOT NULL,
    DeparturePort VARCHAR(255) NOT NULL,
    ArrivalPort VARCHAR(255) NOT NULL,
    Weight DECIMAL(10, 2) NOT NULL,
    Volume DECIMAL(10, 2) NOT NULL,
    Status VARCHAR(50) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (OceanFreightShipmentID),
    FOREIGN KEY (ShipmentTypeID) REFERENCES ShipmentTypes(ShipmentTypeID),
    FOREIGN KEY (CarrierID) REFERENCES Carriers(CarrierID)
);

-- Create table for customs brokerage shipments
CREATE TABLE CustomsBrokerageShipments (
    CustomsBrokerageShipmentID INT AUTO_INCREMENT,
    ShipmentTypeID INT NOT NULL,
    CarrierID INT,
    ShipmentDate DATE NOT NULL,
    ImportExport VARCHAR(10) NOT NULL CHECK (ImportExport IN ('Import', 'Export')),
    CustomsBroker VARCHAR(255) NOT NULL,
    Status VARCHAR(50) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CustomsBrokerageShipmentID),
    FOREIGN KEY (ShipmentTypeID) REFERENCES ShipmentTypes(ShipmentTypeID),
    FOREIGN KEY (CarrierID) REFERENCES Carriers(CarrierID)
);

-- Create table for shipment tracking
CREATE TABLE ShipmentTracking (
    TrackingID INT AUTO_INCREMENT,
    AirFreightShipmentID INT,
    OceanFreightShipmentID INT,
    CustomsBrokerageShipmentID INT,
    TrackingNumber VARCHAR(255) NOT NULL,
    TrackingStatus VARCHAR(50) NOT NULL,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (TrackingID),
    FOREIGN KEY (AirFreightShipmentID) REFERENCES AirFreightShipments(AirFreightShipmentID),
    FOREIGN KEY (OceanFreightShipmentID) REFERENCES OceanFreightShipments(OceanFreightShipmentID),
    FOREIGN KEY (CustomsBrokerageShipmentID) REFERENCES CustomsBrokerageShipments(CustomsBrokerageShipmentID)
);

-- Create table for shipment documents
CREATE TABLE ShipmentDocuments (
    DocumentID INT AUTO_INCREMENT,
    AirFreightShipmentID INT,
    OceanFreightShipmentID INT,
    CustomsBrokerageShipmentID INT,
    DocumentType VARCHAR(50) NOT NULL,
    DocumentNumber VARCHAR(255) NOT NULL,
    DocumentDate DATE NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (DocumentID),
    FOREIGN KEY (AirFreightShipmentID) REFERENCES AirFreightShipments(AirFreightShipmentID),
    FOREIGN KEY (OceanFreightShipmentID) REFERENCES OceanFreightShipments(OceanFreightShipmentID),
    FOREIGN KEY (CustomsBrokerageShipmentID) REFERENCES CustomsBrokerageShipments(CustomsBrokerageShipmentID)
);

-- Create indexes on foreign keys
CREATE INDEX idx_AirFreightShipments_ShipmentTypeID ON AirFreightShipments (ShipmentTypeID);
CREATE INDEX idx_AirFreightShipments_CarrierID ON AirFreightShipments (CarrierID);
CREATE INDEX idx_OceanFreightShipments_ShipmentTypeID ON OceanFreightShipments (ShipmentTypeID);
CREATE INDEX idx_OceanFreightShipments_CarrierID ON OceanFreightShipments (CarrierID);
CREATE INDEX idx_CustomsBrokerageShipments_ShipmentTypeID ON CustomsBrokerageShipments (ShipmentTypeID);
CREATE INDEX idx_CustomsBrokerageShipments_CarrierID ON CustomsBrokerageShipments (CarrierID);
CREATE INDEX idx_ShipmentTracking_AirFreightShipmentID ON ShipmentTracking (AirFreightShipmentID);
CREATE INDEX idx_ShipmentTracking_OceanFreightShipmentID ON ShipmentTracking (OceanFreightShipmentID);
CREATE INDEX idx_ShipmentTracking_CustomsBrokerageShipmentID ON ShipmentTracking (CustomsBrokerageShipmentID);
CREATE INDEX idx_ShipmentDocuments_AirFreightShipmentID ON ShipmentDocuments (AirFreightShipmentID);
CREATE INDEX idx_ShipmentDocuments_OceanFreightShipmentID ON ShipmentDocuments (OceanFreightShipmentID);
CREATE INDEX idx_ShipmentDocuments_CustomsBrokerageShipmentID ON ShipmentDocuments (CustomsBrokerageShipmentID);
```
