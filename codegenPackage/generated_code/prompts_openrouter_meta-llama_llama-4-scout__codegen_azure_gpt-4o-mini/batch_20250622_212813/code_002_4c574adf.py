"""
Generated Code Metadata:
========================
Original URL: https://pneusml.com
Prompt: Generate a sample database schema for storing customer information, vehicle details, and service records for a repair shop like Pneus ML.
Generated: DETERMINISTIC_4c574adf2d044fde
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Sample database schema for a repair shop (Pneus ML)
-- This schema includes tables for customers, vehicles, and service records.

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS ServiceRecords;
DROP TABLE IF EXISTS Vehicles;
DROP TABLE IF EXISTS Customers;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,             -- Customer's first name
    LastName VARCHAR(50) NOT NULL,               -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,          -- Customer's email address (unique)
    PhoneNumber VARCHAR(15),                      -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was added
);

-- Table to store vehicle details
CREATE TABLE Vehicles (
    VehicleID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each vehicle
    CustomerID INT NOT NULL,                      -- Foreign key referencing Customers
    Make VARCHAR(50) NOT NULL,                    -- Vehicle make (e.g., Toyota, Ford)
    Model VARCHAR(50) NOT NULL,                   -- Vehicle model (e.g., Camry, F-150)
    Year INT CHECK (Year > 1885 AND Year <= YEAR(CURRENT_DATE)), -- Vehicle year must be valid
    VIN VARCHAR(17) UNIQUE NOT NULL,              -- Vehicle Identification Number (unique)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the vehicle was added
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) -- Establish foreign key relationship
);

-- Table to store service records
CREATE TABLE ServiceRecords (
    ServiceRecordID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each service record
    VehicleID INT NOT NULL,                          -- Foreign key referencing Vehicles
    ServiceDate DATE NOT NULL,                       -- Date of the service
    ServiceDescription TEXT NOT NULL,                -- Description of the service performed
    Cost DECIMAL(10, 2) NOT NULL,                   -- Cost of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp of when the service record was created
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID) -- Establish foreign key relationship
);

-- Sample data insertion (for testing purposes)
INSERT INTO Customers (FirstName, LastName, Email, PhoneNumber) VALUES
('John', 'Doe', 'john.doe@example.com', '123-456-7890'),
('Jane', 'Smith', 'jane.smith@example.com', '098-765-4321');

INSERT INTO Vehicles (CustomerID, Make, Model, Year, VIN) VALUES
(1, 'Toyota', 'Camry', 2020, '1HGBH41JXMN109186'),
(1, 'Honda', 'Civic', 2018, '2HGBH41JXMN109187'),
(2, 'Ford', 'F-150', 2021, '3HGBH41JXMN109188');

INSERT INTO ServiceRecords (VehicleID, ServiceDate, ServiceDescription, Cost) VALUES
(1, '2023-01-15', 'Oil Change', 29.99),
(1, '2023-03-10', 'Tire Rotation', 19.99),
(2, '2023-02-20', 'Brake Inspection', 49.99),
(3, '2023-04-05', 'Battery Replacement', 129.99);
```
