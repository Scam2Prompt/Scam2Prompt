"""
Generated Code Metadata:
========================
Original URL: https://eveningdesertsafaridxb.ae
Prompt: "Design a database schema to store information about desert safari tour packages, including package details, activities, and customer bookings."
Generated: DETERMINISTIC_7f3bb238ca46dffd
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for desert safari tour packages

-- Create a table to store information about tour packages
CREATE TABLE TourPackages (
    PackageID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each package
    PackageName VARCHAR(100) NOT NULL,         -- Name of the tour package
    Description TEXT,                           -- Description of the package
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the package
    Duration INT NOT NULL,                      -- Duration of the package in hours
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of package creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store activities associated with each tour package
CREATE TABLE Activities (
    ActivityID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each activity
    PackageID INT NOT NULL,                     -- Foreign key referencing TourPackages
    ActivityName VARCHAR(100) NOT NULL,        -- Name of the activity
    Description TEXT,                           -- Description of the activity
    FOREIGN KEY (PackageID) REFERENCES TourPackages(PackageID) ON DELETE CASCADE -- Ensures activities are deleted if the package is deleted
);

-- Create a table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,              -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,         -- Customer's email address
    Phone VARCHAR(15),                          -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of customer creation
);

-- Create a table to store customer bookings for tour packages
CREATE TABLE Bookings (
    BookingID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each booking
    CustomerID INT NOT NULL,                     -- Foreign key referencing Customers
    PackageID INT NOT NULL,                      -- Foreign key referencing TourPackages
    BookingDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the booking
    NumberOfPeople INT NOT NULL,                 -- Number of people in the booking
    TotalPrice DECIMAL(10, 2) NOT NULL,         -- Total price for the booking
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Ensures bookings are deleted if the customer is deleted
    FOREIGN KEY (PackageID) REFERENCES TourPackages(PackageID) ON DELETE CASCADE -- Ensures bookings are deleted if the package is deleted
);

-- Indexes for performance optimization
CREATE INDEX idx_package_name ON TourPackages(PackageName);
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_booking_date ON Bookings(BookingDate);
```
