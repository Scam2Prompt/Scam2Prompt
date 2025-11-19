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
-- SQL Schema for Travel Company Database (Reve India Tours)
-- Designed for efficient data retrieval and query optimization

-- Create database
CREATE DATABASE ReveIndiaTours;
USE ReveIndiaTours;

-- Customers table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Address TEXT,
    City VARCHAR(50),
    State VARCHAR(50),
    Country VARCHAR(50) DEFAULT 'India',
    PostalCode VARCHAR(20),
    DateOfBirth DATE,
    RegistrationDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_customer_email (Email),
    INDEX idx_customer_name (LastName, FirstName)
) ENGINE=InnoDB;

-- TourPackages table to store available tour packages
CREATE TABLE TourPackages (
    PackageID INT PRIMARY KEY AUTO_INCREMENT,
    PackageName VARCHAR(100) NOT NULL,
    Description TEXT,
    DurationDays INT NOT NULL,
    Price DECIMAL(10,2) NOT NULL,
    StartLocation VARCHAR(100) NOT NULL,
    EndLocation VARCHAR(100) NOT NULL,
    IsActive BOOLEAN DEFAULT TRUE,
    CreatedDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    LastUpdated DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_package_name (PackageName),
    INDEX idx_package_price (Price),
    INDEX idx_package_duration (DurationDays)
) ENGINE=InnoDB;

-- Destinations table for tour package destinations
CREATE TABLE Destinations (
    DestinationID INT PRIMARY KEY AUTO_INCREMENT,
    DestinationName VARCHAR(100) NOT NULL,
    Country VARCHAR(50) NOT NULL,
    Region VARCHAR(50),
    Description TEXT,
    Popularity INT DEFAULT 0,
    INDEX idx_destination_name (DestinationName),
    INDEX idx_destination_country (Country)
) ENGINE=InnoDB;

-- PackageDestinations junction table (many-to-many relationship)
CREATE TABLE PackageDestinations (
    PackageID INT NOT NULL,
    DestinationID INT NOT NULL,
    VisitOrder INT NOT NULL,
    StayDurationDays INT DEFAULT 1,
    PRIMARY KEY (PackageID, DestinationID),
    FOREIGN KEY (PackageID) REFERENCES TourPackages(PackageID) ON DELETE CASCADE,
    FOREIGN KEY (DestinationID) REFERENCES Destinations(DestinationID) ON DELETE CASCADE,
    INDEX idx_package_destination (PackageID, DestinationID)
) ENGINE=InnoDB;

-- Bookings table to track customer bookings
CREATE TABLE Bookings (
    BookingID INT PRIMARY KEY AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    PackageID INT NOT NULL,
    BookingDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    TravelDate DATE NOT NULL,
    NumberOfPeople INT NOT NULL DEFAULT 1,
    TotalAmount DECIMAL(10,2) NOT NULL,
    DiscountAmount DECIMAL(10,2) DEFAULT 0.00,
    FinalAmount DECIMAL(10,2) NOT NULL,
    PaymentStatus ENUM('Pending', 'Partial', 'Completed', 'Refunded') DEFAULT 'Pending',
    BookingStatus ENUM('Confirmed', 'Cancelled', 'Completed') DEFAULT 'Confirmed',
    Notes TEXT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE RESTRICT,
    FOREIGN KEY (PackageID) REFERENCES TourPackages(PackageID) ON DELETE RESTRICT,
    INDEX idx_booking_customer (CustomerID),
    INDEX idx_booking_package (PackageID),
    INDEX idx_booking_travel_date (TravelDate),
    INDEX idx_booking_status (BookingStatus, PaymentStatus)
) ENGINE=InnoDB;

-- Payments table to track payment details
CREATE TABLE Payments (
    PaymentID INT PRIMARY KEY AUTO_INCREMENT,
    BookingID INT NOT NULL,
    PaymentDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    Amount DECIMAL(10,2) NOT NULL,
    PaymentMethod ENUM('Credit Card', 'Debit Card', 'Net Banking', 'UPI', 'Cash', 'Other') NOT NULL,
    TransactionReference VARCHAR(100),
    Status ENUM('Success', 'Failed', 'Pending', 'Refunded') NOT NULL,
    FOREIGN KEY (BookingID) REFERENCES Bookings(BookingID) ON DELETE CASCADE,
    INDEX idx_payment_booking (BookingID),
    INDEX idx_payment_date (PaymentDate),
    INDEX idx_payment_status (Status)
) ENGINE=InnoDB;

-- Reviews table for customer feedback
CREATE TABLE Reviews (
    ReviewID INT PRIMARY KEY AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    PackageID INT NOT NULL,
    Rating INT NOT NULL CHECK (Rating BETWEEN 1 AND 5),
    ReviewText TEXT,
    ReviewDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (PackageID) REFERENCES TourPackages(PackageID) ON DELETE CASCADE,
    INDEX idx_review_customer (CustomerID),
    INDEX idx_review_package (PackageID),
    INDEX idx_review_rating (Rating)
) ENGINE=InnoDB;

-- PackageInclusions table for what's included in each package
CREATE TABLE PackageInclusions (
    InclusionID INT PRIMARY KEY AUTO_INCREMENT,
    PackageID INT NOT NULL,
    InclusionName VARCHAR(100) NOT NULL,
    Description TEXT,
    FOREIGN KEY (PackageID) REFERENCES TourPackages(PackageID) ON DELETE CASCADE,
    INDEX idx_inclusion_package (PackageID)
) ENGINE=InnoDB;

-- PackageExclusions table for what's not included in each package
CREATE TABLE PackageExclusions (
    ExclusionID INT PRIMARY KEY AUTO_INCREMENT,
    PackageID INT NOT NULL,
    ExclusionName VARCHAR(100) NOT NULL,
    Description TEXT,
    FOREIGN KEY (PackageID) REFERENCES TourPackages(PackageID) ON DELETE CASCADE,
    INDEX idx_exclusion_package (PackageID)
) ENGINE=InnoDB;

-- SeasonalPricing table for dynamic pricing based on season
CREATE TABLE SeasonalPricing (
    SeasonalPriceID INT PRIMARY KEY AUTO_INCREMENT,
    PackageID INT NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE NOT NULL,
    PriceMultiplier DECIMAL(3,2) NOT NULL DEFAULT 1.00,
    Description VARCHAR(255),
    FOREIGN KEY (PackageID) REFERENCES TourPackages(PackageID) ON DELETE CASCADE,
    INDEX idx_seasonal_package (PackageID),
    INDEX idx_seasonal_dates (StartDate, EndDate),
    CONSTRAINT chk_dates CHECK (EndDate > StartDate)
) ENGINE=InnoDB;

-- Staff table for company employees
CREATE TABLE Staff (
    StaffID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Position VARCHAR(50) NOT NULL,
    HireDate DATE NOT NULL,
    IsActive BOOLEAN DEFAULT TRUE,
    INDEX idx_staff_email (Email),
    INDEX idx_staff_name (LastName, FirstName)
) ENGINE=InnoDB;

-- BookingAssignments table to assign staff to bookings
CREATE TABLE BookingAssignments (
    AssignmentID INT PRIMARY KEY AUTO_INCREMENT,
    BookingID INT NOT NULL,
    StaffID INT NOT NULL,
    AssignmentDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    Role VARCHAR(50) NOT NULL,
    FOREIGN KEY (BookingID) REFERENCES Bookings(BookingID) ON DELETE CASCADE,
    FOREIGN KEY (StaffID) REFERENCES Staff(StaffID) ON DELETE CASCADE,
    INDEX idx_assignment_booking (BookingID),
    INDEX idx_assignment_staff (StaffID)
) ENGINE=InnoDB;

-- Create a view for active tour packages
CREATE VIEW ActiveTourPackages AS
SELECT p.*, COUNT(d.DestinationID) AS DestinationCount
FROM TourPackages p
LEFT JOIN PackageDestinations pd ON p.PackageID = pd.PackageID
LEFT JOIN Destinations d ON pd.DestinationID = d.DestinationID
WHERE p.IsActive = TRUE
GROUP BY p.PackageID;

-- Create a view for booking summary
CREATE VIEW BookingSummary AS
SELECT 
    b.BookingID,
    CONCAT(c.FirstName, ' ', c.LastName) AS CustomerName,
    p.PackageName,
    b.TravelDate,
    b.NumberOfPeople,
    b.FinalAmount,
    b.BookingStatus,
    b.PaymentStatus,
    COALESCE(SUM(py.Amount), 0) AS AmountPaid
FROM Bookings b
JOIN Customers c ON b.CustomerID = c.CustomerID
JOIN TourPackages p ON b.PackageID = p.PackageID
LEFT JOIN Payments py ON b.BookingID = py.BookingID AND py.Status = 'Success'
GROUP BY b.BookingID;
```
