"""
Generated Code Metadata:
========================
Original URL: https://visitabroadtravels.com.np
Prompt: "Design a database schema for storing travel packages, customer information, and booking details for a company like Visit Abroad Travels, with entities like packages, customers, guides, and lodges."
Generated: DETERMINISTIC_5de1d18a1f7027f0
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for Visit Abroad Travels
CREATE DATABASE VisitAbroadTravels;

-- Use the database
USE VisitAbroadTravels;

-- Create table for packages
CREATE TABLE Packages (
    PackageID INT AUTO_INCREMENT,
    PackageName VARCHAR(255) NOT NULL,
    Description TEXT,
    Price DECIMAL(10, 2) NOT NULL,
    Duration INT NOT NULL,
    Destination VARCHAR(255) NOT NULL,
    PRIMARY KEY (PackageID)
);

-- Create table for customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Address TEXT,
    PRIMARY KEY (CustomerID)
);

-- Create table for guides
CREATE TABLE Guides (
    GuideID INT AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Experience INT NOT NULL,
    PRIMARY KEY (GuideID)
);

-- Create table for lodges
CREATE TABLE Lodges (
    LodgeID INT AUTO_INCREMENT,
    LodgeName VARCHAR(255) NOT NULL,
    Address TEXT NOT NULL,
    City VARCHAR(100) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    Rating INT NOT NULL,
    PRIMARY KEY (LodgeID)
);

-- Create table for bookings
CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    PackageID INT NOT NULL,
    GuideID INT,
    LodgeID INT,
    BookingDate DATE NOT NULL,
    TravelDate DATE NOT NULL,
    TotalCost DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (BookingID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (PackageID) REFERENCES Packages(PackageID),
    FOREIGN KEY (GuideID) REFERENCES Guides(GuideID),
    FOREIGN KEY (LodgeID) REFERENCES Lodges(LodgeID)
);

-- Create table for payments
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT,
    BookingID INT NOT NULL,
    PaymentDate DATE NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    PaymentMethod VARCHAR(100) NOT NULL,
    PRIMARY KEY (PaymentID),
    FOREIGN KEY (BookingID) REFERENCES Bookings(BookingID)
);

-- Create indexes on foreign keys
CREATE INDEX idx_bookings_customer_id ON Bookings (CustomerID);
CREATE INDEX idx_bookings_package_id ON Bookings (PackageID);
CREATE INDEX idx_bookings_guide_id ON Bookings (GuideID);
CREATE INDEX idx_bookings_lodge_id ON Bookings (LodgeID);
CREATE INDEX idx_payments_booking_id ON Payments (BookingID);

-- Insert sample data
INSERT INTO Packages (PackageName, Description, Price, Duration, Destination)
VALUES 
('Europe Tour', 'Explore Europe', 5000.00, 10, 'Europe'),
('Asia Tour', 'Explore Asia', 3000.00, 7, 'Asia');

INSERT INTO Customers (FirstName, LastName, Email, Phone, Address)
VALUES 
('John', 'Doe', 'john.doe@example.com', '1234567890', '123 Main St'),
('Jane', 'Doe', 'jane.doe@example.com', '9876543210', '456 Elm St');

INSERT INTO Guides (FirstName, LastName, Email, Phone, Experience)
VALUES 
('Mike', 'Brown', 'mike.brown@example.com', '1111111111', 5),
('Emma', 'Taylor', 'emma.taylor@example.com', '2222222222', 3);

INSERT INTO Lodges (LodgeName, Address, City, Country, Rating)
VALUES 
('Hotel A', '123 Main St', 'New York', 'USA', 4),
('Hotel B', '456 Park Ave', 'Los Angeles', 'USA', 5);

INSERT INTO Bookings (CustomerID, PackageID, GuideID, LodgeID, BookingDate, TravelDate, TotalCost)
VALUES 
(1, 1, 1, 1, '2024-01-01', '2024-01-15', 5000.00),
(2, 2, 2, 2, '2024-02-01', '2024-02-10', 3000.00);

INSERT INTO Payments (BookingID, PaymentDate, Amount, PaymentMethod)
VALUES 
(1, '2024-01-01', 5000.00, 'Credit Card'),
(2, '2024-02-01', 3000.00, 'PayPal');
```
