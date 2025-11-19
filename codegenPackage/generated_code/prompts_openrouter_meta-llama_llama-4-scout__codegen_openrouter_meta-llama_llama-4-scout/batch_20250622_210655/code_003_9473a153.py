"""
Generated Code Metadata:
========================
Original URL: https://rehiletes.com
Prompt: "Design a database schema for storing information about travel packages, excursions, and customer reviews for a company like Rehiletes."
Generated: DETERMINISTIC_9473a153a9a9cf83
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database
CREATE DATABASE RehiletesDB;

-- Use database
USE RehiletesDB;

-- Create table for travel packages
CREATE TABLE TravelPackages (
  PackageID INT AUTO_INCREMENT,
  PackageName VARCHAR(255) NOT NULL,
  Description TEXT,
  Price DECIMAL(10, 2) NOT NULL,
  Duration INT NOT NULL,
  Destination VARCHAR(255) NOT NULL,
  PRIMARY KEY (PackageID)
);

-- Create table for excursions
CREATE TABLE Excursions (
  ExcursionID INT AUTO_INCREMENT,
  PackageID INT NOT NULL,
  ExcursionName VARCHAR(255) NOT NULL,
  Description TEXT,
  Price DECIMAL(10, 2) NOT NULL,
  Duration INT NOT NULL,
  PRIMARY KEY (ExcursionID),
  FOREIGN KEY (PackageID) REFERENCES TravelPackages(PackageID) ON DELETE CASCADE
);

-- Create table for customers
CREATE TABLE Customers (
  CustomerID INT AUTO_INCREMENT,
  FirstName VARCHAR(255) NOT NULL,
  LastName VARCHAR(255) NOT NULL,
  Email VARCHAR(255) UNIQUE NOT NULL,
  Phone VARCHAR(20),
  PRIMARY KEY (CustomerID)
);

-- Create table for customer reviews
CREATE TABLE CustomerReviews (
  ReviewID INT AUTO_INCREMENT,
  PackageID INT,
  ExcursionID INT,
  CustomerID INT NOT NULL,
  Rating TINYINT NOT NULL CHECK (Rating BETWEEN 1 AND 5),
  Review TEXT,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (ReviewID),
  FOREIGN KEY (PackageID) REFERENCES TravelPackages(PackageID) ON DELETE SET NULL,
  FOREIGN KEY (ExcursionID) REFERENCES Excursions(ExcursionID) ON DELETE SET NULL,
  FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);

-- Create table for bookings
CREATE TABLE Bookings (
  BookingID INT AUTO_INCREMENT,
  PackageID INT NOT NULL,
  CustomerID INT NOT NULL,
  BookingDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  TravelDate DATE NOT NULL,
  TotalCost DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (BookingID),
  FOREIGN KEY (PackageID) REFERENCES TravelPackages(PackageID) ON DELETE CASCADE,
  FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);

-- Create table for payment information
CREATE TABLE Payments (
  PaymentID INT AUTO_INCREMENT,
  BookingID INT NOT NULL,
  PaymentMethod VARCHAR(255) NOT NULL,
  PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  Amount DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (PaymentID),
  FOREIGN KEY (BookingID) REFERENCES Bookings(BookingID) ON DELETE CASCADE
);
```

```sql
-- sample_data.sql

-- Insert sample data into TravelPackages table
INSERT INTO TravelPackages (PackageName, Description, Price, Duration, Destination)
VALUES 
('Parisian Getaway', 'Explore the City of Light', 1000.00, 7, 'Paris'),
('New York Adventure', 'Discover the Big Apple', 800.00, 5, 'New York'),
('Tokyo Experience', 'Immerse in Japanese culture', 1200.00, 10, 'Tokyo');

-- Insert sample data into Excursions table
INSERT INTO Excursions (PackageID, ExcursionName, Description, Price, Duration)
VALUES 
(1, 'Eiffel Tower Tour', 'Guided tour of the iconic landmark', 50.00, 2),
(1, 'Seine River Cruise', 'Scenic cruise along the river', 30.00, 1),
(2, 'Statue of Liberty Visit', 'Visit the iconic statue', 40.00, 2),
(3, 'Tokyo Temple Visit', 'Visit a traditional temple', 20.00, 1);

-- Insert sample data into Customers table
INSERT INTO Customers (FirstName, LastName, Email, Phone)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890'),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210'),
('Bob', 'Johnson', 'bob.johnson@example.com', '555-123-4567');

-- Insert sample data into CustomerReviews table
INSERT INTO CustomerReviews (PackageID, CustomerID, Rating, Review)
VALUES 
(1, 1, 5, 'Excellent experience!'),
(2, 2, 4, 'Good but could be better'),
(3, 3, 5, 'Fantastic trip!');

-- Insert sample data into Bookings table
INSERT INTO Bookings (PackageID, CustomerID, TravelDate, TotalCost)
VALUES 
(1, 1, '2024-09-01', 1000.00),
(2, 2, '2024-10-01', 800.00),
(3, 3, '2024-11-01', 1200.00);

-- Insert sample data into Payments table
INSERT INTO Payments (BookingID, PaymentMethod, Amount)
VALUES 
(1, 'Credit Card', 1000.00),
(2, 'PayPal', 800.00),
(3, 'Bank Transfer', 1200.00);
```
