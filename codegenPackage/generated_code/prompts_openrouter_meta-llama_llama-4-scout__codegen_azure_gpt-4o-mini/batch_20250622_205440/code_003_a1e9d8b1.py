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
-- SQL Database Schema for Managing Shipments for Import and Export

-- Create a database for the logistics management system
CREATE DATABASE LogisticsManagement;

-- Use the created database
USE LogisticsManagement;

-- Table for Air Freight shipments
CREATE TABLE AirFreight (
    AirFreightID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each air freight shipment
    ShipmentDate DATETIME NOT NULL,              -- Date and time of the shipment
    Origin VARCHAR(255) NOT NULL,                -- Origin location of the shipment
    Destination VARCHAR(255) NOT NULL,           -- Destination location of the shipment
    Weight DECIMAL(10, 2) NOT NULL,              -- Weight of the shipment in kilograms
    Volume DECIMAL(10, 2) NOT NULL,              -- Volume of the shipment in cubic meters
    Carrier VARCHAR(255) NOT NULL,               -- Carrier handling the air freight
    Status ENUM('Pending', 'In Transit', 'Delivered', 'Cancelled') NOT NULL DEFAULT 'Pending', -- Current status of the shipment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Table for Ocean Freight shipments
CREATE TABLE OceanFreight (
    OceanFreightID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each ocean freight shipment
    ShipmentDate DATETIME NOT NULL,                 -- Date and time of the shipment
    Origin VARCHAR(255) NOT NULL,                   -- Origin location of the shipment
    Destination VARCHAR(255) NOT NULL,              -- Destination location of the shipment
    Weight DECIMAL(10, 2) NOT NULL,                 -- Weight of the shipment in kilograms
    Volume DECIMAL(10, 2) NOT NULL,                 -- Volume of the shipment in cubic meters
    VesselName VARCHAR(255) NOT NULL,               -- Name of the vessel transporting the shipment
    Status ENUM('Pending', 'In Transit', 'Delivered', 'Cancelled') NOT NULL DEFAULT 'Pending', -- Current status of the shipment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Table for Customs Brokerage
CREATE TABLE CustomsBrokerage (
    CustomsBrokerageID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customs brokerage record
    ShipmentID INT NOT NULL,                            -- Foreign key referencing the shipment
    ShipmentType ENUM('Air', 'Ocean') NOT NULL,        -- Type of shipment (Air or Ocean)
    CustomsStatus ENUM('Pending', 'Cleared', 'Rejected') NOT NULL DEFAULT 'Pending', -- Current customs status
    BrokerName VARCHAR(255) NOT NULL,                  -- Name of the customs broker
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,      -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the record was last updated
    FOREIGN KEY (ShipmentID) REFERENCES AirFreight(AirFreightID) ON DELETE CASCADE, -- Foreign key constraint for air freight
    FOREIGN KEY (ShipmentID) REFERENCES OceanFreight(OceanFreightID) ON DELETE CASCADE -- Foreign key constraint for ocean freight
);

-- Indexes for performance optimization
CREATE INDEX idx_air_freight_status ON AirFreight(Status);
CREATE INDEX idx_ocean_freight_status ON OceanFreight(Status);
CREATE INDEX idx_customs_brokerage_status ON CustomsBrokerage(CustomsStatus);
```
