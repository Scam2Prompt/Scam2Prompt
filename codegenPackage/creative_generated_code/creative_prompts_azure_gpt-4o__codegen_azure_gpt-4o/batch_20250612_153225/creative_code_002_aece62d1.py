"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rentalcarelena.it
Prompt: Generate code to create a database schema for a car rental service that includes tables for vehicle details (e.g., type, fuel, capacity), customer information, and booking records.
Generated: DETERMINISTIC_aece62d1910a8f4c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for a car rental service

-- Create a table for vehicle details
CREATE TABLE Vehicle (
    VehicleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each vehicle
    Type VARCHAR(50) NOT NULL,                -- Type of vehicle (e.g., sedan, SUV, van)
    FuelType VARCHAR(20) NOT NULL,            -- Fuel type (e.g., petrol, diesel, electric)
    Capacity INT NOT NULL,                    -- Number of passengers the vehicle can accommodate
    RegistrationNumber VARCHAR(20) UNIQUE NOT NULL, -- Vehicle registration number
    DailyRate DECIMAL(10, 2) NOT NULL,        -- Daily rental rate for the vehicle
    Status ENUM('Available', 'Rented', 'Maintenance') NOT NULL DEFAULT 'Available' -- Current status of the vehicle
);

-- Create a table for customer information
CREATE TABLE Customer (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FullName VARCHAR(100) NOT NULL,            -- Full name of the customer
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Email address of the customer
    PhoneNumber VARCHAR(15) NOT NULL,          -- Contact phone number
    Address TEXT NOT NULL,                     -- Residential address
    DateOfBirth DATE NOT NULL                  -- Date of birth of the customer
);

-- Create a table for booking records
CREATE TABLE Booking (
    BookingID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each booking
    VehicleID INT NOT NULL,                    -- Foreign key referencing the Vehicle table
    CustomerID INT NOT NULL,                   -- Foreign key referencing the Customer table
    StartDate DATE NOT NULL,                   -- Start date of the rental period
    EndDate DATE NOT NULL,                     -- End date of the rental period
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount for the booking
    BookingStatus ENUM('Confirmed', 'Cancelled', 'Completed') NOT NULL DEFAULT 'Confirmed', -- Status of the booking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the booking was created
    FOREIGN KEY (VehicleID) REFERENCES Vehicle(VehicleID) ON DELETE CASCADE, -- Cascade deletion on vehicle removal
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID) ON DELETE CASCADE -- Cascade deletion on customer removal
);

-- Additional indexing for optimization
CREATE INDEX idx_vehicle_status ON Vehicle(Status);
CREATE INDEX idx_booking_status ON Booking(BookingStatus);
```
