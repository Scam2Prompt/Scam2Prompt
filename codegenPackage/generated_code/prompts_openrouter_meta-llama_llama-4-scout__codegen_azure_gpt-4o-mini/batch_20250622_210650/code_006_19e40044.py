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
-- Database schema for Innova Renting

-- Table to store vehicle information
CREATE TABLE Vehicles (
    VehicleID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each vehicle
    Make VARCHAR(50) NOT NULL,                 -- Manufacturer of the vehicle
    Model VARCHAR(50) NOT NULL,                -- Model of the vehicle
    Year INT NOT NULL,                         -- Year of manufacture
    VIN VARCHAR(17) UNIQUE NOT NULL,           -- Vehicle Identification Number
    Status ENUM('Available', 'Rented', 'Maintenance') NOT NULL DEFAULT 'Available', -- Current status of the vehicle
    DailyRate DECIMAL(10, 2) NOT NULL          -- Daily rental rate
);

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,              -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Customer's email address
    Phone VARCHAR(15),                          -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was added
);

-- Table to store renting agreements
CREATE TABLE Rentals (
    RentalID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each rental agreement
    VehicleID INT NOT NULL,                      -- Foreign key referencing Vehicles
    CustomerID INT NOT NULL,                     -- Foreign key referencing Customers
    StartDate DATE NOT NULL,                     -- Start date of the rental
    EndDate DATE NOT NULL,                       -- End date of the rental
    TotalAmount DECIMAL(10, 2) NOT NULL,        -- Total amount for the rental
    Status ENUM('Active', 'Completed', 'Cancelled') NOT NULL DEFAULT 'Active', -- Current status of the rental
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID) ON DELETE CASCADE, -- Ensures vehicle is deleted if rental is deleted
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures customer is deleted if rental is deleted
);

-- Example query to get all active rentals with customer and vehicle details
SELECT 
    r.RentalID,
    c.FirstName,
    c.LastName,
    v.Make,
    v.Model,
    r.StartDate,
    r.EndDate,
    r.TotalAmount
FROM 
    Rentals r
JOIN 
    Customers c ON r.CustomerID = c.CustomerID
JOIN 
    Vehicles v ON r.VehicleID = v.VehicleID
WHERE 
    r.Status = 'Active';

-- Example query to get total revenue generated from rentals
SELECT 
    SUM(TotalAmount) AS TotalRevenue
FROM 
    Rentals
WHERE 
    Status = 'Completed';

-- Example query to get available vehicles
SELECT 
    VehicleID, 
    Make, 
    Model, 
    Year, 
    DailyRate 
FROM 
    Vehicles 
WHERE 
    Status = 'Available';
```
