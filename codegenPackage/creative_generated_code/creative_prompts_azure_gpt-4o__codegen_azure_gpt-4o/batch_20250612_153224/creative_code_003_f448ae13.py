"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://microrentacar.biz
Prompt: Create a database schema for managing car rental services, including categories like luxury cars, wedding cars, and trip vehicles, based on the offerings of Micro Rent a Car.
Generated: DETERMINISTIC_f448ae1321f8c406
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Schema for Car Rental Service managed by Micro Rent a Car

-- Create a database named 'CarRentalService'
CREATE DATABASE CarRentalService;

-- Switch to the 'CarRentalService' database
USE CarRentalService;

-- Table to hold information about car categories
CREATE TABLE CarCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(50) NOT NULL,         -- Name of the category (e.g., Luxury Cars, Wedding Cars, Trip Vehicles)
    Description TEXT                           -- Optional description of the category
);

-- Table to hold information about cars
CREATE TABLE Cars (
    CarID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each car
    CategoryID INT NOT NULL,                   -- Foreign key referencing CarCategories
    Make VARCHAR(50) NOT NULL,                 -- Car manufacturer (e.g., Toyota, BMW)
    Model VARCHAR(50) NOT NULL,                -- Car model (e.g., Camry, X5)
    Year INT NOT NULL,                         -- Year the car was manufactured
    LicensePlate VARCHAR(15) NOT NULL UNIQUE,  -- Unique license plate number
    IsAvailable BOOLEAN DEFAULT TRUE,          -- Availability status of the car (true = available, false = rented)
    DailyRate DECIMAL(10, 2) NOT NULL,         -- Daily rental price for the car
    FOREIGN KEY (CategoryID) REFERENCES CarCategories(CategoryID) ON DELETE CASCADE
);

-- Table to hold customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,        -- Customer's email address (must be unique)
    PhoneNumber VARCHAR(15),                   -- Contact phone number
    DriverLicenseNumber VARCHAR(30) NOT NULL UNIQUE -- Driver's license number for verification
);

-- Table to hold rental transactions
CREATE TABLE Rentals (
    RentalID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each rental transaction
    CarID INT NOT NULL,                        -- Foreign key referencing Cars
    CustomerID INT NOT NULL,                   -- Foreign key referencing Customers
    RentalStartDate DATE NOT NULL,             -- Date the rental starts
    RentalEndDate DATE NOT NULL,               -- Date the rental ends
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total rental cost for the transaction
    FOREIGN KEY (CarID) REFERENCES Cars(CarID) ON DELETE CASCADE,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);

-- Table to track payments for rentals
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each payment
    RentalID INT NOT NULL,                     -- Foreign key referencing Rentals
    PaymentDate DATE NOT NULL,                 -- Date the payment was made
    AmountPaid DECIMAL(10, 2) NOT NULL,        -- Amount paid
    PaymentMethod ENUM('Credit Card', 'Debit Card', 'Cash', 'Online Transfer') NOT NULL, -- Payment method used
    FOREIGN KEY (RentalID) REFERENCES Rentals(RentalID) ON DELETE CASCADE
);

-- Example indexes for optimizing queries
CREATE INDEX idx_car_availability ON Cars(IsAvailable); -- Index to quickly filter available cars
CREATE INDEX idx_rental_dates ON Rentals(RentalStartDate, RentalEndDate); -- Index to optimize date-based queries

-- Example constraints
ALTER TABLE Rentals
ADD CONSTRAINT chk_rental_dates CHECK (RentalEndDate > RentalStartDate); -- Ensure valid rental period
```
