"""
Generated Code Metadata:
========================
Original URL: https://trackdieselperu.com
Prompt: "Create a SQL database schema to store information about heavy machinery, their spare parts, and maintenance services offered by a company like Track Diesel Peru S.R.L."
Generated: DETERMINISTIC_0391f4c7bb75d285
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Heavy Machinery, Spare Parts, and Maintenance Services

-- Create a database
CREATE DATABASE HeavyMachineryDB;

-- Use the created database
USE HeavyMachineryDB;

-- Table to store information about heavy machinery
CREATE TABLE Machinery (
    MachineryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each machinery
    Name VARCHAR(100) NOT NULL,                 -- Name of the machinery
    Model VARCHAR(50) NOT NULL,                 -- Model of the machinery
    Manufacturer VARCHAR(100) NOT NULL,         -- Manufacturer of the machinery
    YearOfManufacture INT NOT NULL,             -- Year the machinery was manufactured
    SerialNumber VARCHAR(50) UNIQUE NOT NULL,   -- Unique serial number for the machinery
    PurchaseDate DATE NOT NULL,                 -- Date the machinery was purchased
    Status ENUM('Active', 'Inactive', 'Under Maintenance') DEFAULT 'Active', -- Current status of the machinery
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about spare parts
CREATE TABLE SpareParts (
    SparePartID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each spare part
    Name VARCHAR(100) NOT NULL,                 -- Name of the spare part
    PartNumber VARCHAR(50) UNIQUE NOT NULL,     -- Unique part number
    Manufacturer VARCHAR(100) NOT NULL,         -- Manufacturer of the spare part
    CompatibleMachineryModel VARCHAR(50),       -- Compatible machinery model(s)
    StockQuantity INT NOT NULL DEFAULT 0,       -- Quantity of spare parts in stock
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the spare part
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about maintenance services
CREATE TABLE MaintenanceServices (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each service
    MachineryID INT NOT NULL,                   -- Foreign key referencing Machinery table
    ServiceDate DATE NOT NULL,                  -- Date the service was performed
    Description TEXT NOT NULL,                  -- Description of the service performed
    Cost DECIMAL(10, 2) NOT NULL,               -- Cost of the service
    TechnicianName VARCHAR(100) NOT NULL,       -- Name of the technician who performed the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (MachineryID) REFERENCES Machinery(MachineryID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store information about spare parts used in maintenance services
CREATE TABLE MaintenanceSpareParts (
    MaintenanceSparePartID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    ServiceID INT NOT NULL,                                -- Foreign key referencing MaintenanceServices table
    SparePartID INT NOT NULL,                              -- Foreign key referencing SpareParts table
    QuantityUsed INT NOT NULL,                             -- Quantity of spare parts used
    FOREIGN KEY (ServiceID) REFERENCES MaintenanceServices(ServiceID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (SparePartID) REFERENCES SpareParts(SparePartID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for faster queries
CREATE INDEX idx_machinery_status ON Machinery(Status);
CREATE INDEX idx_spareparts_stock ON SpareParts(StockQuantity);
CREATE INDEX idx_maintenance_service_date ON MaintenanceServices(ServiceDate);

-- End of schema
```
