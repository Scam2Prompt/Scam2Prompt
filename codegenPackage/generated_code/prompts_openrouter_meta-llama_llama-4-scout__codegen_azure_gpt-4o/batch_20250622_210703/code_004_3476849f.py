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
-- SQL Schema for Diesel Turbocharger Repairs Database

-- Create a database
CREATE DATABASE DieselTurboRepairDB;

-- Use the database
USE DieselTurboRepairDB;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    Address TEXT                               -- Customer's address
);

-- Table to store vehicle specifications
CREATE TABLE Vehicles (
    VehicleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each vehicle
    CustomerID INT NOT NULL,                  -- Foreign key linking to Customers table
    Make VARCHAR(50) NOT NULL,                -- Vehicle manufacturer
    Model VARCHAR(50) NOT NULL,               -- Vehicle model
    Year INT NOT NULL,                        -- Vehicle manufacturing year
    VIN VARCHAR(17) UNIQUE NOT NULL,          -- Vehicle Identification Number
    EngineType VARCHAR(50),                   -- Type of engine (e.g., diesel, petrol)
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);

-- Table to store repair details
CREATE TABLE Repairs (
    RepairID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each repair
    VehicleID INT NOT NULL,                   -- Foreign key linking to Vehicles table
    RepairDate DATE NOT NULL,                 -- Date of the repair
    Description TEXT NOT NULL,                -- Description of the repair
    Cost DECIMAL(10, 2) NOT NULL,             -- Cost of the repair
    TechnicianName VARCHAR(100),              -- Name of the technician who performed the repair
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID) ON DELETE CASCADE
);

-- Table to store warranty information
CREATE TABLE Warranties (
    WarrantyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each warranty
    RepairID INT NOT NULL,                     -- Foreign key linking to Repairs table
    WarrantyStartDate DATE NOT NULL,           -- Start date of the warranty
    WarrantyEndDate DATE NOT NULL,             -- End date of the warranty
    CoverageDetails TEXT NOT NULL,             -- Details of what the warranty covers
    FOREIGN KEY (RepairID) REFERENCES Repairs(RepairID) ON DELETE CASCADE
);

-- Indexes for faster queries
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_vehicle_vin ON Vehicles(VIN);
CREATE INDEX idx_repair_date ON Repairs(RepairDate);

-- Error handling: Ensure strict mode is enabled for better data integrity
SET sql_mode = 'STRICT_ALL_TABLES';
```
