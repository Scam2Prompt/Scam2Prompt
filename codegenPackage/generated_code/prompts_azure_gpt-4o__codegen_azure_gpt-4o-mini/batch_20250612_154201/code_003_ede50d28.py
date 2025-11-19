"""
Generated Code Metadata:
========================
Original URL: https://enfock.com
Prompt: Develop a database schema for managing assets, fiscal data, and distribution center operations for a fuel station ERP system, as outlined by Enfock.
Generated: DETERMINISTIC_ede50d28eb2b2865
Batch ID: 20250612_154201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Fuel Station ERP System

-- Create a schema for the Fuel Station ERP
CREATE SCHEMA FuelStationERP;

-- Table to store information about assets
CREATE TABLE FuelStationERP.Assets (
    AssetID SERIAL PRIMARY KEY, -- Unique identifier for each asset
    AssetName VARCHAR(255) NOT NULL, -- Name of the asset
    AssetType VARCHAR(100) NOT NULL, -- Type of asset (e.g., Tank, Pump, etc.)
    PurchaseDate DATE NOT NULL, -- Date when the asset was purchased
    Cost DECIMAL(10, 2) NOT NULL, -- Cost of the asset
    Status VARCHAR(50) NOT NULL CHECK (Status IN ('Active', 'Inactive', 'Maintenance')), -- Current status of the asset
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store fiscal data
CREATE TABLE FuelStationERP.FiscalData (
    FiscalID SERIAL PRIMARY KEY, -- Unique identifier for each fiscal record
    FiscalYear INT NOT NULL CHECK (FiscalYear > 2000), -- Fiscal year
    Revenue DECIMAL(15, 2) NOT NULL, -- Total revenue for the year
    Expenses DECIMAL(15, 2) NOT NULL, -- Total expenses for the year
    Profit DECIMAL(15, 2) AS (Revenue - Expenses) STORED, -- Calculated profit
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about distribution centers
CREATE TABLE FuelStationERP.DistributionCenters (
    CenterID SERIAL PRIMARY KEY, -- Unique identifier for each distribution center
    CenterName VARCHAR(255) NOT NULL, -- Name of the distribution center
    Location VARCHAR(255) NOT NULL, -- Physical location of the center
    Capacity INT NOT NULL CHECK (Capacity > 0), -- Maximum capacity of the center
    ContactNumber VARCHAR(15), -- Contact number for the center
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to manage inventory of fuel types
CREATE TABLE FuelStationERP.FuelInventory (
    InventoryID SERIAL PRIMARY KEY, -- Unique identifier for each inventory record
    FuelType VARCHAR(100) NOT NULL, -- Type of fuel (e.g., Gasoline, Diesel)
    Quantity DECIMAL(10, 2) NOT NULL CHECK (Quantity >= 0), -- Quantity available
    CenterID INT NOT NULL, -- Foreign key referencing DistributionCenters
    FOREIGN KEY (CenterID) REFERENCES FuelStationERP.DistributionCenters(CenterID) ON DELETE CASCADE, -- Ensures referential integrity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to log transactions related to fuel sales
CREATE TABLE FuelStationERP.FuelSales (
    SaleID SERIAL PRIMARY KEY, -- Unique identifier for each sale
    SaleDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the sale
    FuelType VARCHAR(100) NOT NULL, -- Type of fuel sold
    Quantity DECIMAL(10, 2) NOT NULL CHECK (Quantity > 0), -- Quantity sold
    SaleAmount DECIMAL(15, 2) NOT NULL, -- Total sale amount
    CenterID INT NOT NULL, -- Foreign key referencing DistributionCenters
    FOREIGN KEY (CenterID) REFERENCES FuelStationERP.DistributionCenters(CenterID) ON DELETE CASCADE, -- Ensures referential integrity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Indexes for performance optimization
CREATE INDEX idx_fuel_type ON FuelStationERP.FuelInventory(FuelType);
CREATE INDEX idx_sale_date ON FuelStationERP.FuelSales(SaleDate);
```
