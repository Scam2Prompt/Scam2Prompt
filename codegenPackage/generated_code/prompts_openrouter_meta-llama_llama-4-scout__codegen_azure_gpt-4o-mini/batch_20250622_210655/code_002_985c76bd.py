"""
Generated Code Metadata:
========================
Original URL: https://microrentacar.biz
Prompt: Generate a sample database schema for a car rental system like Micro Rent a Car, including tables for vehicles, customers, bookings, and payments.
Generated: DETERMINISTIC_985c76bd34e894b0
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Sample Database Schema for a Car Rental System

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Payments;
DROP TABLE IF EXISTS Bookings;
DROP TABLE IF EXISTS Vehicles;
DROP TABLE IF EXISTS Customers;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,              -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Customer's email address
    Phone VARCHAR(15),                          -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was created
);

-- Table to store vehicle information
CREATE TABLE Vehicles (
    VehicleID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each vehicle
    Make VARCHAR(50) NOT NULL,                  -- Vehicle manufacturer
    Model VARCHAR(50) NOT NULL,                 -- Vehicle model
    Year INT NOT NULL,                          -- Year of manufacture
    LicensePlate VARCHAR(20) UNIQUE NOT NULL,   -- Vehicle license plate number
    DailyRate DECIMAL(10, 2) NOT NULL,         -- Daily rental rate
    IsAvailable BOOLEAN DEFAULT TRUE,           -- Availability status of the vehicle
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the vehicle was added
);

-- Table to store booking information
CREATE TABLE Bookings (
    BookingID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each booking
    CustomerID INT NOT NULL,                     -- Foreign key referencing Customers
    VehicleID INT NOT NULL,                      -- Foreign key referencing Vehicles
    StartDate DATE NOT NULL,                     -- Start date of the booking
    EndDate DATE NOT NULL,                       -- End date of the booking
    TotalAmount DECIMAL(10, 2) NOT NULL,        -- Total amount for the booking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the booking was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Cascade delete for customer
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID) ON DELETE CASCADE  -- Cascade delete for vehicle
);

-- Table to store payment information
CREATE TABLE Payments (
    PaymentID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each payment
    BookingID INT NOT NULL,                      -- Foreign key referencing Bookings
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the payment
    Amount DECIMAL(10, 2) NOT NULL,             -- Amount paid
    PaymentMethod ENUM('Credit Card', 'Debit Card', 'Cash', 'Online') NOT NULL, -- Method of payment
    FOREIGN KEY (BookingID) REFERENCES Bookings(BookingID) ON DELETE CASCADE  -- Cascade delete for booking
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_vehicle_license_plate ON Vehicles(LicensePlate);
CREATE INDEX idx_booking_dates ON Bookings(StartDate, EndDate);
```
