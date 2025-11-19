"""
Generated Code Metadata:
========================
Original URL: https://reveindiatours.com
Prompt: "Create a SQL database schema to manage tour packages, customer information, and booking details for a travel company like Reve India Tours, with a focus on efficient data retrieval and query optimization."
Generated: DETERMINISTIC_640dbb1eaf97f5d7
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Reve India Tours

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Bookings;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS TourPackages;

-- Create a table to store information about tour packages
CREATE TABLE TourPackages (
    PackageID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each tour package
    PackageName VARCHAR(255) NOT NULL,         -- Name of the tour package
    Description TEXT,                           -- Description of the tour package
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the tour package
    Duration INT NOT NULL,                      -- Duration of the tour in days
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the package was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Create a table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(100) NOT NULL,           -- Customer's first name
    LastName VARCHAR(100) NOT NULL,            -- Customer's last name
    Email VARCHAR(255) NOT NULL UNIQUE,        -- Customer's email address (must be unique)
    Phone VARCHAR(15),                          -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the customer was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Create a table to store booking details
CREATE TABLE Bookings (
    BookingID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each booking
    CustomerID INT NOT NULL,                    -- Foreign key referencing Customers
    PackageID INT NOT NULL,                     -- Foreign key referencing TourPackages
    BookingDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date and time of the booking
    NumberOfPeople INT NOT NULL,                -- Number of people in the booking
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount for the booking
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (PackageID) REFERENCES TourPackages(PackageID) ON DELETE CASCADE   -- Ensure referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_package_name ON TourPackages(PackageName);
CREATE INDEX idx_booking_date ON Bookings(BookingDate);
```
