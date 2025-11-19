"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galopinautomobile.fr
Prompt: Design a database schema for managing a collection of luxury vehicles, ensuring it captures essential details like model, condition, and investment value, reflecting the meticulous selection process at Galopin Automobile.
Generated: DETERMINISTIC_21acd81e7c29ac76
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing a collection of luxury vehicles
CREATE DATABASE GalopinAutomobile;

USE GalopinAutomobile;

-- Table to store details about luxury vehicles
CREATE TABLE Vehicles (
    VehicleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each vehicle
    Model VARCHAR(100) NOT NULL,               -- Model of the luxury vehicle
    Year INT CHECK (Year >= 1886 AND Year <= YEAR(CURDATE())), -- Year of manufacture, must be a valid year
    Condition ENUM('New', 'Like New', 'Used', 'Certified Pre-Owned', 'Vintage') NOT NULL, -- Condition of the vehicle
    InvestmentValue DECIMAL(15, 2) NOT NULL,   -- Investment value of the vehicle
    DateAdded TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the vehicle was added to the collection
    UNIQUE(Model, Year)                        -- Ensures that duplicate models and years are not allowed
);

-- Table to store maintenance records for vehicles
CREATE TABLE MaintenanceRecords (
    RecordID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each maintenance record
    VehicleID INT NOT NULL,                     -- Foreign key referring to the Vehicles table
    MaintenanceDate DATE NOT NULL,              -- Date when maintenance was performed
    Description TEXT NOT NULL,                  -- Description of the maintenance done
    Cost DECIMAL(10, 2) NOT NULL,               -- Cost of the maintenance performed
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each customer
    Name VARCHAR(100) NOT NULL,                 -- Name of the customer
    ContactInfo VARCHAR(255),                    -- Contact information (email, phone, etc.)
    DateRegistered TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the customer registered
);

-- Table to store sales records
CREATE TABLE Sales (
    SaleID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each sale
    VehicleID INT NOT NULL,                       -- Foreign key referring to the Vehicles table
    CustomerID INT NOT NULL,                      -- Foreign key referring to the Customers table
    SaleDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the sale occurred
    SalePrice DECIMAL(15, 2) NOT NULL,           -- Sale price of the vehicle
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);
```
