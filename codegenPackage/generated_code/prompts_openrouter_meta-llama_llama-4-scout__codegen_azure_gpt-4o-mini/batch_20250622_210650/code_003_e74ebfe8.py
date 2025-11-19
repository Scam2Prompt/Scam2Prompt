"""
Generated Code Metadata:
========================
Original URL: https://thegujaratcalling.com
Prompt: "Design a database schema for storing information about tour packages, travel services, and customer bookings for a company like The Gujarat Calling, using a relational database management system."
Generated: DETERMINISTIC_e74ebfe872d945d4
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about tour packages, travel services, and customer bookings

-- Create a table for storing information about customers
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,             -- Customer's first name
    LastName VARCHAR(50) NOT NULL,               -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,          -- Customer's email address
    Phone VARCHAR(15),                           -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the customer was created
);

-- Create a table for storing information about tour packages
CREATE TABLE TourPackages (
    PackageID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each tour package
    PackageName VARCHAR(100) NOT NULL,           -- Name of the tour package
    Description TEXT,                             -- Description of the tour package
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the tour package
    Duration INT NOT NULL,                        -- Duration of the tour in days
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the package was created
);

-- Create a table for storing information about travel services
CREATE TABLE TravelServices (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each travel service
    ServiceName VARCHAR(100) NOT NULL,           -- Name of the travel service
    Description TEXT,                             -- Description of the travel service
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the travel service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the service was created
);

-- Create a table for storing customer bookings
CREATE TABLE Bookings (
    BookingID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each booking
    CustomerID INT NOT NULL,                      -- Foreign key referencing Customers
    PackageID INT NOT NULL,                       -- Foreign key referencing TourPackages
    ServiceID INT,                                -- Foreign key referencing TravelServices (optional)
    BookingDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the booking
    TotalAmount DECIMAL(10, 2) NOT NULL,         -- Total amount for the booking
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (PackageID) REFERENCES TourPackages(PackageID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ServiceID) REFERENCES TravelServices(ServiceID) ON DELETE SET NULL -- Optional service
);

-- Create an index on the email column in the Customers table for faster lookups
CREATE INDEX idx_email ON Customers(Email);

-- Create an index on the BookingDate column in the Bookings table for faster queries
CREATE INDEX idx_booking_date ON Bookings(BookingDate);
```
