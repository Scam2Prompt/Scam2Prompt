"""
Generated Code Metadata:
========================
Original URL: https://windscreensreplacementmelbourne.com.au
Prompt: Develop a simple database schema to store customer information, vehicle details, and service records for a windscreen repair and replacement company in Melbourne.
Generated: DETERMINISTIC_c203f5d5db628d84
Batch ID: 20250622_204944
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a windscreen repair and replacement company

-- Create a database for the company
CREATE DATABASE WindscreenRepair;

-- Use the created database
USE WindscreenRepair;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,             -- Customer's first name
    LastName VARCHAR(50) NOT NULL,              -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Customer's email address (unique)
    PhoneNumber VARCHAR(15),                     -- Customer's phone number
    Address VARCHAR(255),                        -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store vehicle details
CREATE TABLE Vehicles (
    VehicleID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each vehicle
    CustomerID INT NOT NULL,                     -- Foreign key referencing Customers
    Make VARCHAR(50) NOT NULL,                   -- Vehicle make (e.g., Toyota, Ford)
    Model VARCHAR(50) NOT NULL,                  -- Vehicle model (e.g., Camry, Focus)
    Year INT CHECK (Year > 1885 AND Year <= YEAR(CURDATE())), -- Vehicle year must be valid
    VIN VARCHAR(17) UNIQUE NOT NULL,             -- Vehicle Identification Number (unique)
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Ensure referential integrity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store service records
CREATE TABLE ServiceRecords (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each service record
    VehicleID INT NOT NULL,                       -- Foreign key referencing Vehicles
    ServiceDate DATE NOT NULL,                    -- Date of the service
    ServiceType ENUM('Repair', 'Replacement') NOT NULL, -- Type of service performed
    Cost DECIMAL(10, 2) NOT NULL,                -- Cost of the service
    Description TEXT,                             -- Description of the service performed
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID) ON DELETE CASCADE, -- Ensure referential integrity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_vehicle_vin ON Vehicles(VIN);
CREATE INDEX idx_service_vehicle ON ServiceRecords(VehicleID);
```
