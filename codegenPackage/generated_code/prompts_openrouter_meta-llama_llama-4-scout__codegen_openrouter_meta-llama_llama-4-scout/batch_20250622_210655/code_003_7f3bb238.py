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
-- Create database schema for desert safari tour packages
CREATE DATABASE DesertSafari;

-- Use the database
USE DesertSafari;

-- Create table for tour packages
CREATE TABLE TourPackages (
    PackageID INT AUTO_INCREMENT,
    PackageName VARCHAR(255) NOT NULL,
    Description TEXT,
    Duration INT NOT NULL,  -- in days
    Price DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PackageID)
);

-- Create table for activities
CREATE TABLE Activities (
    ActivityID INT AUTO_INCREMENT,
    ActivityName VARCHAR(255) NOT NULL,
    Description TEXT,
    PRIMARY KEY (ActivityID)
);

-- Create table for package activities
CREATE TABLE PackageActivities (
    PackageID INT NOT NULL,
    ActivityID INT NOT NULL,
    PRIMARY KEY (PackageID, ActivityID),
    FOREIGN KEY (PackageID) REFERENCES TourPackages(PackageID),
    FOREIGN KEY (ActivityID) REFERENCES Activities(ActivityID)
);

-- Create table for customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CustomerID)
);

-- Create table for bookings
CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    PackageID INT NOT NULL,
    BookingDate DATE NOT NULL,
    TravelDate DATE NOT NULL,
    TotalCost DECIMAL(10, 2) NOT NULL,
    Status ENUM('Pending', 'Confirmed', 'Cancelled') DEFAULT 'Pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (BookingID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (PackageID) REFERENCES TourPackages(PackageID)
);

-- Create table for payments
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT,
    BookingID INT NOT NULL,
    PaymentMethod ENUM('Cash', 'Credit Card', 'Bank Transfer') NOT NULL,
    PaymentDate DATE NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    Status ENUM('Pending', 'Successful', 'Failed') DEFAULT 'Pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PaymentID),
    FOREIGN KEY (BookingID) REFERENCES Bookings(BookingID)
);

-- Insert sample data
INSERT INTO TourPackages (PackageName, Description, Duration, Price)
VALUES 
('Desert Adventure', 'Explore the desert with our expert guides.', 3, 500.00),
('Safari Tour', 'Experience the thrill of a desert safari.', 5, 800.00);

INSERT INTO Activities (ActivityName, Description)
VALUES 
('Dune Bashing', 'Experience the thrill of dune bashing in a 4x4 vehicle.'),
('Camel Riding', 'Explore the desert on camelback.');

INSERT INTO PackageActivities (PackageID, ActivityID)
VALUES 
(1, 1),
(1, 2),
(2, 1);

INSERT INTO Customers (FirstName, LastName, Email, Phone)
VALUES 
('John', 'Doe', 'john.doe@example.com', '1234567890'),
('Jane', 'Doe', 'jane.doe@example.com', '9876543210');

INSERT INTO Bookings (CustomerID, PackageID, BookingDate, TravelDate, TotalCost)
VALUES 
(1, 1, '2024-09-01', '2024-09-15', 500.00),
(2, 2, '2024-09-05', '2024-09-20', 800.00);

INSERT INTO Payments (BookingID, PaymentMethod, PaymentDate, Amount)
VALUES 
(1, 'Credit Card', '2024-09-01', 500.00),
(2, 'Bank Transfer', '2024-09-05', 800.00);
```
