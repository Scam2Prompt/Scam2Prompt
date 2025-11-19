"""
Generated Code Metadata:
========================
Original URL: https://reparaciondeturbo.cl
Prompt: Create a SQL database schema to store information about diesel turbocharger repairs, including customer data, vehicle specifications, repair details, and warranty information.
Generated: DETERMINISTIC_3476849f9a4504e9
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Diesel Turbocharger Repairs

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Warranty;
DROP TABLE IF EXISTS Repair;
DROP TABLE IF EXISTS Vehicle;
DROP TABLE IF EXISTS Customer;

-- Table to store customer information
CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address
    Phone VARCHAR(15),                         -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store vehicle specifications
CREATE TABLE Vehicle (
    VehicleID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each vehicle
    CustomerID INT NOT NULL,                    -- Foreign key referencing Customer
    Make VARCHAR(50) NOT NULL,                  -- Vehicle make (e.g., Ford, Toyota)
    Model VARCHAR(50) NOT NULL,                 -- Vehicle model
    Year INT CHECK (Year > 1885 AND Year <= YEAR(CURRENT_DATE)), -- Vehicle year
    VIN VARCHAR(17) UNIQUE NOT NULL,            -- Vehicle Identification Number
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store repair details
CREATE TABLE Repair (
    RepairID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each repair
    VehicleID INT NOT NULL,                      -- Foreign key referencing Vehicle
    RepairDate DATE NOT NULL,                    -- Date of the repair
    Description TEXT NOT NULL,                   -- Description of the repair work done
    Cost DECIMAL(10, 2) NOT NULL,                -- Cost of the repair
    FOREIGN KEY (VehicleID) REFERENCES Vehicle(VehicleID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store warranty information
CREATE TABLE Warranty (
    WarrantyID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each warranty
    RepairID INT NOT NULL,                        -- Foreign key referencing Repair
    WarrantyPeriod INT NOT NULL,                  -- Warranty period in months
    StartDate DATE NOT NULL,                      -- Start date of the warranty
    EndDate DATE NOT NULL,                        -- End date of the warranty
    FOREIGN KEY (RepairID) REFERENCES Repair(RepairID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customer(Email);
CREATE INDEX idx_vehicle_vin ON Vehicle(VIN);
CREATE INDEX idx_repair_date ON Repair(RepairDate);
CREATE INDEX idx_warranty_end_date ON Warranty(EndDate);
```
