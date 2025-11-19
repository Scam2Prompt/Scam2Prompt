"""
Generated Code Metadata:
========================
Original URL: https://innovarenting.com
Prompt: "Suggest an efficient database schema for managing vehicle inventory, customer information, and renting agreements for a company like Innova Renting, including relationships between entities and potential queries for reporting."
Generated: DETERMINISTIC_19e40044d9de1592
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for Innova Renting
CREATE DATABASE InnovaRenting;

-- Use InnovaRenting database
USE InnovaRenting;

-- Create table for Vehicle Types
CREATE TABLE VehicleTypes (
    VehicleTypeID INT AUTO_INCREMENT,
    VehicleTypeName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (VehicleTypeID)
);

-- Create table for Vehicles
CREATE TABLE Vehicles (
    VehicleID INT AUTO_INCREMENT,
    VehicleTypeID INT NOT NULL,
    LicensePlate VARCHAR(20) NOT NULL,
    Make VARCHAR(100) NOT NULL,
    Model VARCHAR(100) NOT NULL,
    Year INT NOT NULL,
    Color VARCHAR(50) NOT NULL,
    Mileage INT NOT NULL DEFAULT 0,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (VehicleID),
    FOREIGN KEY (VehicleTypeID) REFERENCES VehicleTypes(VehicleTypeID) ON DELETE CASCADE
);

-- Create table for Customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    State VARCHAR(100) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    PostalCode VARCHAR(20) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CustomerID)
);

-- Create table for Renting Agreements
CREATE TABLE RentingAgreements (
    AgreementID INT AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    VehicleID INT NOT NULL,
    RentalDate DATE NOT NULL,
    ReturnDate DATE,
    RentalDuration INT,
    TotalCost DECIMAL(10, 2) NOT NULL,
    Status ENUM('Active', 'Returned', 'Cancelled') NOT NULL DEFAULT 'Active',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (AgreementID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID) ON DELETE CASCADE
);

-- Create table for Payments
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT,
    AgreementID INT NOT NULL,
    PaymentDate DATE NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    PaymentMethod ENUM('Cash', 'Credit Card', 'Bank Transfer') NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PaymentID),
    FOREIGN KEY (AgreementID) REFERENCES RentingAgreements(AgreementID) ON DELETE CASCADE
);

-- Indexing for efficient querying
CREATE INDEX idx_VehicleTypeID ON Vehicles (VehicleTypeID);
CREATE INDEX idx_CustomerID ON RentingAgreements (CustomerID);
CREATE INDEX idx_VehicleID ON RentingAgreements (VehicleID);
CREATE INDEX idx_AgreementID ON Payments (AgreementID);

-- Example queries for reporting
-- Get all active renting agreements
SELECT * FROM RentingAgreements WHERE Status = 'Active';

-- Get total revenue by month
SELECT 
    YEAR(PaymentDate) AS Year,
    MONTH(PaymentDate) AS Month,
    SUM(Amount) AS TotalRevenue
FROM 
    Payments
GROUP BY 
    Year, Month
ORDER BY 
    Year, Month;

-- Get vehicle types with most rented vehicles
SELECT 
    vt.VehicleTypeName, 
    COUNT(ra.VehicleID) AS TotalRented
FROM 
    RentingAgreements ra
JOIN 
    Vehicles v ON ra.VehicleID = v.VehicleID
JOIN 
    VehicleTypes vt ON v.VehicleTypeID = vt.VehicleTypeID
GROUP BY 
    vt.VehicleTypeName
ORDER BY 
    TotalRented DESC;

-- Get customers with most renting agreements
SELECT 
    c.FirstName, 
    c.LastName, 
    COUNT(ra.AgreementID) AS TotalAgreements
FROM 
    RentingAgreements ra
JOIN 
    Customers c ON ra.CustomerID = c.CustomerID
GROUP BY 
    c.FirstName, c.LastName
ORDER BY 
    TotalAgreements DESC;
```
