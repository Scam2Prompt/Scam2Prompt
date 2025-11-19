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
-- SQL Schema for managing and consolidating shipments for import and export

-- Create a database for the logistics system
CREATE DATABASE LogisticsManagement;

-- Use the newly created database
USE LogisticsManagement;

-- Table to store general shipment information
CREATE TABLE Shipments (
    ShipmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each shipment
    ShipmentType ENUM('Air Freight', 'Ocean Freight', 'Customs Brokerage') NOT NULL, -- Type of shipment
    Origin VARCHAR(255) NOT NULL, -- Origin location
    Destination VARCHAR(255) NOT NULL, -- Destination location
    ShipmentDate DATE NOT NULL, -- Date of shipment
    Status ENUM('Pending', 'In Transit', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Current status of the shipment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store air freight-specific details
CREATE TABLE AirFreight (
    AirFreightID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for air freight
    ShipmentID INT NOT NULL, -- Foreign key referencing Shipments table
    Airline VARCHAR(255) NOT NULL, -- Airline used for shipment
    FlightNumber VARCHAR(50) NOT NULL, -- Flight number
    Weight DECIMAL(10, 2) NOT NULL, -- Weight of the shipment in kilograms
    Volume DECIMAL(10, 2) NOT NULL, -- Volume of the shipment in cubic meters
    FOREIGN KEY (ShipmentID) REFERENCES Shipments(ShipmentID) ON DELETE CASCADE -- Cascade delete when shipment is deleted
);

-- Table to store ocean freight-specific details
CREATE TABLE OceanFreight (
    OceanFreightID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for ocean freight
    ShipmentID INT NOT NULL, -- Foreign key referencing Shipments table
    VesselName VARCHAR(255) NOT NULL, -- Name of the vessel
    ContainerNumber VARCHAR(50) NOT NULL, -- Container number
    Weight DECIMAL(10, 2) NOT NULL, -- Weight of the shipment in kilograms
    Volume DECIMAL(10, 2) NOT NULL, -- Volume of the shipment in cubic meters
    FOREIGN KEY (ShipmentID) REFERENCES Shipments(ShipmentID) ON DELETE CASCADE -- Cascade delete when shipment is deleted
);

-- Table to store customs brokerage-specific details
CREATE TABLE CustomsBrokerage (
    CustomsBrokerageID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for customs brokerage
    ShipmentID INT NOT NULL, -- Foreign key referencing Shipments table
    BrokerName VARCHAR(255) NOT NULL, -- Name of the customs broker
    CustomsFee DECIMAL(10, 2) NOT NULL, -- Fee for customs clearance
    ClearanceDate DATE NOT NULL, -- Date of customs clearance
    FOREIGN KEY (ShipmentID) REFERENCES Shipments(ShipmentID) ON DELETE CASCADE -- Cascade delete when shipment is deleted
);

-- Table to store audit logs for tracking changes
CREATE TABLE AuditLogs (
    AuditID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for audit log
    TableName VARCHAR(255) NOT NULL, -- Name of the table where the change occurred
    Operation ENUM('INSERT', 'UPDATE', 'DELETE') NOT NULL, -- Type of operation performed
    RecordID INT NOT NULL, -- ID of the record affected
    ChangedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the change
    ChangedBy VARCHAR(255) NOT NULL -- User or system that made the change
);

-- Indexes for optimizing queries
CREATE INDEX idx_ShipmentType ON Shipments(ShipmentType);
CREATE INDEX idx_Status ON Shipments(Status);
CREATE INDEX idx_AirFreight_ShipmentID ON AirFreight(ShipmentID);
CREATE INDEX idx_OceanFreight_ShipmentID ON OceanFreight(ShipmentID);
CREATE INDEX idx_CustomsBrokerage_ShipmentID ON CustomsBrokerage(ShipmentID);

-- Error handling and constraints are built into the schema using foreign keys, data types, and ENUMs.
```
