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
-- Database Schema for Vehicle Inventory, Customer Information, and Renting Agreements

-- Table: Vehicles
CREATE TABLE Vehicles (
    VehicleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each vehicle
    Make VARCHAR(50) NOT NULL,                -- Manufacturer of the vehicle
    Model VARCHAR(50) NOT NULL,               -- Model of the vehicle
    Year INT NOT NULL,                        -- Year of manufacture
    LicensePlate VARCHAR(20) UNIQUE NOT NULL, -- Unique license plate number
    Status ENUM('Available', 'Rented', 'Maintenance') NOT NULL DEFAULT 'Available', -- Current status of the vehicle
    DailyRate DECIMAL(10, 2) NOT NULL,        -- Daily rental rate for the vehicle
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table: Customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address
    PhoneNumber VARCHAR(15) NOT NULL,          -- Customer's phone number
    Address TEXT,                              -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table: Rentals
CREATE TABLE Rentals (
    RentalID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each rental agreement
    VehicleID INT NOT NULL,                  -- Foreign key referencing Vehicles table
    CustomerID INT NOT NULL,                 -- Foreign key referencing Customers table
    RentalStartDate DATE NOT NULL,           -- Start date of the rental
    RentalEndDate DATE NOT NULL,             -- End date of the rental
    TotalAmount DECIMAL(10, 2) NOT NULL,     -- Total amount for the rental
    Status ENUM('Active', 'Completed', 'Cancelled') NOT NULL DEFAULT 'Active', -- Status of the rental agreement
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID) ON DELETE CASCADE, -- Cascade delete if vehicle is removed
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Cascade delete if customer is removed
);

-- Example Queries for Reporting

-- Query: List all available vehicles
SELECT * FROM Vehicles
WHERE Status = 'Available';

-- Query: Get rental history for a specific customer
SELECT Rentals.RentalID, Vehicles.Make, Vehicles.Model, Rentals.RentalStartDate, Rentals.RentalEndDate, Rentals.TotalAmount
FROM Rentals
JOIN Vehicles ON Rentals.VehicleID = Vehicles.VehicleID
WHERE Rentals.CustomerID = ?; -- Replace '?' with the specific CustomerID

-- Query: Calculate total revenue from completed rentals
SELECT SUM(TotalAmount) AS TotalRevenue
FROM Rentals
WHERE Status = 'Completed';

-- Query: List all rentals that are currently active
SELECT Rentals.RentalID, Customers.FirstName, Customers.LastName, Vehicles.Make, Vehicles.Model, Rentals.RentalStartDate, Rentals.RentalEndDate
FROM Rentals
JOIN Customers ON Rentals.CustomerID = Customers.CustomerID
JOIN Vehicles ON Rentals.VehicleID = Vehicles.VehicleID
WHERE Rentals.Status = 'Active';
```
