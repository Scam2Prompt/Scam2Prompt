"""
Generated Code Metadata:
========================
Original URL: https://rentalcarelena.it
Prompt: Create a SQL database schema for a car rental company like Rental Car Elena, including tables for vehicles, customers, bookings, and payments.
Generated: DETERMINISTIC_16eeaded85383343
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for a Car Rental Company

-- Table: Vehicles
CREATE TABLE Vehicles (
    VehicleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each vehicle
    Make VARCHAR(50) NOT NULL,                -- Manufacturer of the vehicle (e.g., Toyota, Ford)
    Model VARCHAR(50) NOT NULL,               -- Model of the vehicle (e.g., Corolla, Mustang)
    Year INT NOT NULL,                        -- Year of manufacture
    LicensePlate VARCHAR(20) UNIQUE NOT NULL, -- Unique license plate number
    Status ENUM('Available', 'Rented', 'Maintenance') DEFAULT 'Available', -- Current status of the vehicle
    DailyRate DECIMAL(10, 2) NOT NULL         -- Daily rental rate for the vehicle
);

-- Table: Customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address
    PhoneNumber VARCHAR(15) NOT NULL,          -- Customer's phone number
    DriverLicenseNumber VARCHAR(50) UNIQUE NOT NULL, -- Customer's driver license number
    Address TEXT                               -- Customer's address
);

-- Table: Bookings
CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each booking
    CustomerID INT NOT NULL,                  -- Foreign key referencing Customers table
    VehicleID INT NOT NULL,                   -- Foreign key referencing Vehicles table
    StartDate DATE NOT NULL,                  -- Start date of the rental
    EndDate DATE NOT NULL,                    -- End date of the rental
    TotalAmount DECIMAL(10, 2) NOT NULL,      -- Total amount for the booking
    Status ENUM('Pending', 'Confirmed', 'Cancelled', 'Completed') DEFAULT 'Pending', -- Booking status
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID) ON DELETE CASCADE
);

-- Table: Payments
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each payment
    BookingID INT NOT NULL,                   -- Foreign key referencing Bookings table
    PaymentDate DATE NOT NULL,                -- Date of payment
    Amount DECIMAL(10, 2) NOT NULL,           -- Amount paid
    PaymentMethod ENUM('Credit Card', 'Debit Card', 'Cash', 'Bank Transfer') NOT NULL, -- Payment method
    FOREIGN KEY (BookingID) REFERENCES Bookings(BookingID) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_vehicle_status ON Vehicles(Status);
CREATE INDEX idx_booking_status ON Bookings(Status);
CREATE INDEX idx_payment_date ON Payments(PaymentDate);
```
