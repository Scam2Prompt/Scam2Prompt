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
    PackageID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each tour package
    PackageName VARCHAR(255) NOT NULL,        -- Name of the tour package
    Description TEXT,                         -- Detailed description of the tour package
    Destination VARCHAR(255) NOT NULL,       -- Destination of the tour package
    DurationDays INT NOT NULL,               -- Duration of the tour package in days
    Price DECIMAL(10, 2) NOT NULL,           -- Price of the tour package
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the package was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(100) NOT NULL,           -- First name of the customer
    LastName VARCHAR(100) NOT NULL,            -- Last name of the customer
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Email address of the customer (must be unique)
    PhoneNumber VARCHAR(15),                   -- Phone number of the customer
    Address TEXT,                              -- Address of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the customer was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about bookings
CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each booking
    CustomerID INT NOT NULL,                  -- Foreign key referencing Customers table
    PackageID INT NOT NULL,                   -- Foreign key referencing TourPackages table
    BookingDate DATE NOT NULL,                -- Date when the booking was made
    NumberOfPeople INT NOT NULL,              -- Number of people included in the booking
    TotalAmount DECIMAL(10, 2) NOT NULL,      -- Total amount for the booking
    Status ENUM('Pending', 'Confirmed', 'Cancelled') DEFAULT 'Pending', -- Status of the booking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the booking was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Cascade delete for customer
    FOREIGN KEY (PackageID) REFERENCES TourPackages(PackageID) ON DELETE CASCADE -- Cascade delete for package
);

-- Indexes for optimizing queries
CREATE INDEX idx_customer_email ON Customers(Email); -- Index for quick lookup by email
CREATE INDEX idx_booking_status ON Bookings(Status); -- Index for quick lookup by booking status
```
