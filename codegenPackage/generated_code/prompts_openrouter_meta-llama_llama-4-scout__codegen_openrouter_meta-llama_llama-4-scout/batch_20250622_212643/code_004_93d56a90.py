"""
Generated Code Metadata:
========================
Original URL: https://anywhere-adventure.com
Prompt: "Create a sample database schema to store information about travel destinations, tour packages, and customer reviews for a company like Anywhere Adventures."
Generated: DETERMINISTIC_93d56a9082e97077
Batch ID: 20250622_212643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for Anywhere Adventures

-- Create database
CREATE DATABASE AnywhereAdventures;

-- Use database
USE AnywhereAdventures;

-- Create table for destinations
CREATE TABLE Destinations (
    DestinationID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Description TEXT,
    Location VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (DestinationID)
);

-- Create table for tour packages
CREATE TABLE TourPackages (
    PackageID INT AUTO_INCREMENT,
    DestinationID INT,
    PackageName VARCHAR(255) NOT NULL,
    Description TEXT,
    Price DECIMAL(10, 2) NOT NULL,
    Duration INT NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PackageID),
    FOREIGN KEY (DestinationID) REFERENCES Destinations(DestinationID) ON DELETE CASCADE
);

-- Create table for customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CustomerID)
);

-- Create table for reviews
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT,
    CustomerID INT,
    PackageID INT,
    Rating TINYINT NOT NULL CHECK (Rating BETWEEN 1 AND 5),
    Review TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ReviewID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (PackageID) REFERENCES TourPackages(PackageID) ON DELETE CASCADE
);

-- Create table for bookings
CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT,
    CustomerID INT,
    PackageID INT,
    BookingDate DATE NOT NULL,
    TravelDate DATE NOT NULL,
    Status ENUM('Pending', 'Confirmed', 'Cancelled') DEFAULT 'Pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (BookingID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (PackageID) REFERENCES TourPackages(PackageID) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO Destinations (Name, Description, Location)
VALUES 
('Paris', 'The city of love and lights', 'France'),
('Rome', 'The eternal city', 'Italy'),
('New York', 'The city that never sleeps', 'USA');

INSERT INTO TourPackages (DestinationID, PackageName, Description, Price, Duration)
VALUES 
(1, 'Parisian Getaway', 'Explore the romantic city of Paris', 1000.00, 5),
(2, 'Roman Holiday', 'Discover the ancient ruins of Rome', 800.00, 4),
(3, 'New York Adventure', 'Experience the vibrant city of New York', 1200.00, 6);

INSERT INTO Customers (FirstName, LastName, Email, Phone)
VALUES 
('John', 'Doe', 'john.doe@example.com', '1234567890'),
('Jane', 'Doe', 'jane.doe@example.com', '9876543210');

INSERT INTO Reviews (CustomerID, PackageID, Rating, Review)
VALUES 
(1, 1, 5, 'Amazing experience in Paris!'),
(2, 2, 4, 'Great tour package, but could be improved');

INSERT INTO Bookings (CustomerID, PackageID, BookingDate, TravelDate)
VALUES 
(1, 1, '2024-09-01', '2024-09-15'),
(2, 2, '2024-08-01', '2024-08-20');
```
