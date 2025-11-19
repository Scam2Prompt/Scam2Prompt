"""
Generated Code Metadata:
========================
Original URL: https://natureexcursionsafaris.com
Prompt: Design a database schema for storing information about Tanzania's national parks, safari packages, and customer bookings.
Generated: DETERMINISTIC_76cdd5f3906582ee
Batch ID: 20250622_204958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Tanzania's National Parks, Safari Packages, and Customer Bookings

-- Table: NationalParks
CREATE TABLE NationalParks (
    ParkID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each park
    Name VARCHAR(100) NOT NULL,            -- Name of the national park
    Location VARCHAR(100) NOT NULL,        -- Location of the park
    Area FLOAT NOT NULL,                   -- Area of the park in square kilometers
    EstablishedYear INT NOT NULL,          -- Year the park was established
    Description TEXT,                      -- Description of the park
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table: SafariPackages
CREATE TABLE SafariPackages (
    PackageID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each safari package
    Name VARCHAR(100) NOT NULL,               -- Name of the safari package
    ParkID INT NOT NULL,                      -- Foreign key referencing NationalParks
    DurationDays INT NOT NULL,                -- Duration of the safari in days
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the safari package
    Description TEXT,                         -- Description of the safari package
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ParkID) REFERENCES NationalParks(ParkID) ON DELETE CASCADE -- Cascade delete if park is removed
);

-- Table: Customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,        -- Customer's email address
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table: Bookings
CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each booking
    CustomerID INT NOT NULL,                  -- Foreign key referencing Customers
    PackageID INT NOT NULL,                   -- Foreign key referencing SafariPackages
    BookingDate DATE NOT NULL,                -- Date of the booking
    NumberOfPeople INT NOT NULL,              -- Number of people in the booking
    TotalPrice DECIMAL(10, 2) NOT NULL,       -- Total price for the booking
    Status ENUM('Pending', 'Confirmed', 'Cancelled') DEFAULT 'Pending', -- Booking status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Cascade delete if customer is removed
    FOREIGN KEY (PackageID) REFERENCES SafariPackages(PackageID) ON DELETE CASCADE -- Cascade delete if package is removed
);

-- Indexes for faster queries
CREATE INDEX idx_park_name ON NationalParks(Name);
CREATE INDEX idx_package_name ON SafariPackages(Name);
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_booking_status ON Bookings(Status);
```
