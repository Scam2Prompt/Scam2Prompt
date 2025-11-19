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
-- Create database schema for Reve India Tours
CREATE DATABASE ReveIndiaTours;

-- Use the database schema
USE ReveIndiaTours;

-- Create table for tour packages
CREATE TABLE TourPackages (
    PackageID INT AUTO_INCREMENT,
    PackageName VARCHAR(255) NOT NULL,
    Description TEXT,
    Duration INT,
    Price DECIMAL(10, 2),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PackageID)
);

-- Create table for customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CustomerID)
);

-- Create table for booking details
CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT,
    CustomerID INT,
    PackageID INT,
    BookingDate DATE NOT NULL,
    TravelDate DATE NOT NULL,
    TotalCost DECIMAL(10, 2) NOT NULL,
    Status ENUM('Pending', 'Confirmed', 'Cancelled') DEFAULT 'Pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (BookingID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (PackageID) REFERENCES TourPackages(PackageID) ON DELETE CASCADE
);

-- Create table for payment details
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT,
    BookingID INT,
    PaymentMethod ENUM('Cash', 'Credit Card', 'Online Banking') NOT NULL,
    PaymentDate DATE NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    Status ENUM('Pending', 'Successful', 'Failed') DEFAULT 'Pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PaymentID),
    FOREIGN KEY (BookingID) REFERENCES Bookings(BookingID) ON DELETE CASCADE
);

-- Create indexes for efficient data retrieval
CREATE INDEX idx_CustomerID ON Bookings (CustomerID);
CREATE INDEX idx_PackageID ON Bookings (PackageID);
CREATE INDEX idx_BookingID ON Payments (BookingID);
CREATE INDEX idx_Email ON Customers (Email);

-- Create views for query optimization
CREATE VIEW CustomerBookings AS
SELECT c.CustomerID, c.FirstName, c.LastName, b.BookingID, b.PackageID, b.TravelDate
FROM Customers c
JOIN Bookings b ON c.CustomerID = b.CustomerID;

CREATE VIEW PackageBookings AS
SELECT tp.PackageID, tp.PackageName, b.BookingID, b.CustomerID, b.TravelDate
FROM TourPackages tp
JOIN Bookings b ON tp.PackageID = b.PackageID;

-- Create stored procedures for common queries
DELIMITER //
CREATE PROCEDURE GetCustomerBookings(IN customerID INT)
BEGIN
    SELECT * FROM CustomerBookings WHERE CustomerID = customerID;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE GetPackageBookings(IN packageID INT)
BEGIN
    SELECT * FROM PackageBookings WHERE PackageID = packageID;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE UpdateBookingStatus(IN bookingID INT, IN status ENUM('Pending', 'Confirmed', 'Cancelled'))
BEGIN
    UPDATE Bookings SET Status = status WHERE BookingID = bookingID;
END//
DELIMITER ;
```
