"""
Generated Code Metadata:
========================
Original URL: https://skyline-ia.com
Prompt: "Suggest a suitable database schema for storing information about tour packages, customers, and bookings for a company like Skyline International Agent."
Generated: DETERMINISTIC_98820e7b0411a15b
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Skyline International Agent

-- Table to store information about tour packages
CREATE TABLE TourPackages (
    PackageID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each tour package
    PackageName VARCHAR(255) NOT NULL,         -- Name of the tour package
    Description TEXT,                           -- Description of the tour package
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the tour package
    Duration INT NOT NULL,                      -- Duration of the tour in days
    Destination VARCHAR(255) NOT NULL,         -- Destination of the tour
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the package was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(100) NOT NULL,           -- Customer's first name
    LastName VARCHAR(100) NOT NULL,            -- Customer's last name
    Email VARCHAR(255) NOT NULL UNIQUE,        -- Customer's email address (must be unique)
    Phone VARCHAR(15),                         -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the customer was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store booking information
CREATE TABLE Bookings (
    BookingID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each booking
    CustomerID INT NOT NULL,                    -- Foreign key referencing Customers
    PackageID INT NOT NULL,                     -- Foreign key referencing TourPackages
    BookingDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date when the booking was made
    NumberOfPeople INT NOT NULL,                -- Number of people in the booking
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount for the booking
    Status ENUM('Pending', 'Confirmed', 'Cancelled') DEFAULT 'Pending',  -- Status of the booking
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (PackageID) REFERENCES TourPackages(PackageID) ON DELETE CASCADE,  -- Ensures referential integrity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the booking was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);
```
