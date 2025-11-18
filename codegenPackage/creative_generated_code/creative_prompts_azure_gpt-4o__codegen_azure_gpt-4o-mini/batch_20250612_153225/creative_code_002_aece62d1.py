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
-- SQL script to create a database schema for a Car Rental Service

-- Create Vehicle Details Table
CREATE TABLE VehicleDetails (
    VehicleID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique ID for each vehicle
    VehicleType VARCHAR(50) NOT NULL,          -- Type of vehicle (e.g., Sedan, SUV)
    FuelType VARCHAR(20) NOT NULL,             -- Fuel type (e.g., Gasoline, Diesel, Electric)
    Capacity INT NOT NULL,                      -- Seating capacity of the vehicle
    Status ENUM('Available', 'Rented', 'Maintenance') NOT NULL DEFAULT 'Available',  -- Current status of the vehicle
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create Customer Information Table
CREATE TABLE CustomerInformation (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique ID for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,              -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,         -- Customer's email (unique)
    PhoneNumber VARCHAR(15) NOT NULL,           -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create Booking Records Table
CREATE TABLE BookingRecords (
    BookingID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique ID for each booking
    VehicleID INT NOT NULL,                      -- Reference to the VehicleDetails table
    CustomerID INT NOT NULL,                     -- Reference to the CustomerInformation table
    StartDate DATETIME NOT NULL,                 -- Booking start date and time
    EndDate DATETIME NOT NULL,                   -- Booking end date and time
    TotalCost DECIMAL(10, 2) NOT NULL,          -- Total cost of the booking
    Status ENUM('Confirmed', 'Cancelled', 'Completed') NOT NULL DEFAULT 'Confirmed',  -- Current status of the booking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (VehicleID) REFERENCES VehicleDetails(VehicleID) ON DELETE CASCADE,  -- Ensuring referential integrity
    FOREIGN KEY (CustomerID) REFERENCES CustomerInformation(CustomerID) ON DELETE CASCADE -- Ensuring referential integrity
);

-- End of database schema creation
```
