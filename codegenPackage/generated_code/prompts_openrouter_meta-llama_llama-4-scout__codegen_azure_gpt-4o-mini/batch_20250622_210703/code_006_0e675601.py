"""
Generated Code Metadata:
========================
Original URL: https://refrigeratortransport.com
Prompt: Develop a simple database schema to manage refrigerated vehicle rentals, customer information, and delivery records for a company like Refrigerator Transport in Dubai.
Generated: DETERMINISTIC_0e675601d1fd6e27
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Refrigerator Transport

-- Create a database for the application
CREATE DATABASE RefrigeratorTransport;

-- Use the created database
USE RefrigeratorTransport;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,             -- Customer's first name
    LastName VARCHAR(50) NOT NULL,              -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Customer's email address (unique)
    PhoneNumber VARCHAR(15),                     -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was added
);

-- Table to store refrigerated vehicle information
CREATE TABLE Vehicles (
    VehicleID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each vehicle
    LicensePlate VARCHAR(20) UNIQUE NOT NULL,   -- Vehicle's license plate (unique)
    Model VARCHAR(50) NOT NULL,                  -- Vehicle model
    Capacity INT NOT NULL,                       -- Vehicle capacity in cubic meters
    Status ENUM('Available', 'Rented', 'Maintenance') DEFAULT 'Available', -- Current status of the vehicle
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the vehicle was added
);

-- Table to store rental records
CREATE TABLE Rentals (
    RentalID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each rental
    CustomerID INT NOT NULL,                     -- Foreign key referencing Customers
    VehicleID INT NOT NULL,                      -- Foreign key referencing Vehicles
    RentalStart DATETIME NOT NULL,               -- Start date and time of the rental
    RentalEnd DATETIME NOT NULL,                 -- End date and time of the rental
    TotalCost DECIMAL(10, 2) NOT NULL,          -- Total cost of the rental
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the rental was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store delivery records
CREATE TABLE Deliveries (
    DeliveryID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each delivery
    RentalID INT NOT NULL,                       -- Foreign key referencing Rentals
    DeliveryAddress VARCHAR(255) NOT NULL,      -- Address where the delivery is to be made
    DeliveryDate DATETIME NOT NULL,              -- Date and time of the delivery
    Status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Current status of the delivery
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the delivery was created
    FOREIGN KEY (RentalID) REFERENCES Rentals(RentalID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_vehicle_status ON Vehicles(Status);
CREATE INDEX idx_rental_dates ON Rentals(RentalStart, RentalEnd);
CREATE INDEX idx_delivery_status ON Deliveries(Status);
```
