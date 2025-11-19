"""
Generated Code Metadata:
========================
Original URL: https://viamare.com.gr
Prompt: "Design a database schema to store information about yacht charter services, VIP concierge services, and travel arrangements for a company like Viamare Yachting."
Generated: DETERMINISTIC_b5fcbe2ef7ec3bd7
Batch ID: 20250622_212046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for Viamare Yachting
CREATE DATABASE ViamareYachting;

-- Use the database
USE ViamareYachting;

-- Create table for yacht charter services
CREATE TABLE Yachts (
  `YachtID` INT AUTO_INCREMENT,
  `Name` VARCHAR(255) NOT NULL,
  `Type` ENUM('Sailing', 'Motor') NOT NULL,
  `Length` DECIMAL(5,2) NOT NULL,
  `Beam` DECIMAL(5,2) NOT NULL,
  `Draft` DECIMAL(5,2) NOT NULL,
  `Crew` INT NOT NULL,
  `Guests` INT NOT NULL,
  `Cabins` INT NOT NULL,
  `BasePrice` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`YachtID`)
);

-- Create table for VIP concierge services
CREATE TABLE ConciergeServices (
  `ServiceID` INT AUTO_INCREMENT,
  `Name` VARCHAR(255) NOT NULL,
  `Description` TEXT,
  `Price` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`ServiceID`)
);

-- Create table for travel arrangements
CREATE TABLE TravelArrangements (
  `ArrangementID` INT AUTO_INCREMENT,
  `Departure` VARCHAR(255) NOT NULL,
  `Destination` VARCHAR(255) NOT NULL,
  `DepartureDate` DATE NOT NULL,
  `ReturnDate` DATE,
  PRIMARY KEY (`ArrangementID`)
);

-- Create table for charter bookings
CREATE TABLE CharterBookings (
  `BookingID` INT AUTO_INCREMENT,
  `YachtID` INT NOT NULL,
  `ArrangementID` INT,
  `ClientName` VARCHAR(255) NOT NULL,
  `BookingDate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `StartDate` DATE NOT NULL,
  `EndDate` DATE NOT NULL,
  `TotalCost` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`BookingID`),
  FOREIGN KEY (`YachtID`) REFERENCES Yachts(`YachtID`),
  FOREIGN KEY (`ArrangementID`) REFERENCES TravelArrangements(`ArrangementID`)
);

-- Create table for concierge service bookings
CREATE TABLE ConciergeBookings (
  `BookingID` INT AUTO_INCREMENT,
  `ServiceID` INT NOT NULL,
  `ClientName` VARCHAR(255) NOT NULL,
  `BookingDate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `ServiceDate` DATE NOT NULL,
  `TotalCost` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`BookingID`),
  FOREIGN KEY (`ServiceID`) REFERENCES ConciergeServices(`ServiceID`)
);

-- Create table for payments
CREATE TABLE Payments (
  `PaymentID` INT AUTO_INCREMENT,
  `BookingID` INT,
  `PaymentMethod` ENUM('Cash', 'Credit Card', 'Bank Transfer') NOT NULL,
  `PaymentDate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `Amount` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`PaymentID`),
  FOREIGN KEY (`BookingID`) REFERENCES CharterBookings(`BookingID`)
);

-- Create table for payment invoices
CREATE TABLE Invoices (
  `InvoiceID` INT AUTO_INCREMENT,
  `BookingID` INT NOT NULL,
  `InvoiceDate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `DueDate` DATE NOT NULL,
  `TotalAmount` DECIMAL(10,2) NOT NULL,
  `Status` ENUM('Pending', 'Paid', 'Overdue') NOT NULL DEFAULT 'Pending',
  PRIMARY KEY (`InvoiceID`),
  FOREIGN KEY (`BookingID`) REFERENCES CharterBookings(`BookingID`)
);

-- Create indexes on foreign key columns
CREATE INDEX idx_YachtID ON CharterBookings(YachtID);
CREATE INDEX idx_ArrangementID ON CharterBookings(ArrangementID);
CREATE INDEX idx_ServiceID ON ConciergeBookings(ServiceID);
CREATE INDEX idx_BookingID ON Payments(BookingID);
CREATE INDEX idx_BookingID ON Invoices(BookingID);
```

```sql
-- sample_data.sql

-- Insert sample data into Yachts table
INSERT INTO Yachts (Name, Type, Length, Beam, Draft, Crew, Guests, Cabins, BasePrice)
VALUES 
('Sailing Yacht', 'Sailing', 20.00, 5.00, 2.00, 2, 6, 3, 1000.00),
('Motor Yacht', 'Motor', 30.00, 7.00, 3.00, 4, 8, 4, 2000.00);

-- Insert sample data into ConciergeServices table
INSERT INTO ConciergeServices (Name, Description, Price)
VALUES 
('Private Chef', 'Private chef for the day', 500.00),
('Personal Assistant', 'Personal assistant for the day', 300.00);

-- Insert sample data into TravelArrangements table
INSERT INTO TravelArrangements (Departure, Destination, DepartureDate, ReturnDate)
VALUES 
('Marina', 'Island', '2024-09-01', '2024-09-03'),
('City', 'Beach', '2024-09-05', '2024-09-07');

-- Insert sample data into CharterBookings table
INSERT INTO CharterBookings (YachtID, ArrangementID, ClientName, StartDate, EndDate, TotalCost)
VALUES 
(1, 1, 'John Doe', '2024-09-01', '2024-09-03', 2000.00),
(2, 2, 'Jane Doe', '2024-09-05', '2024-09-07', 4000.00);

-- Insert sample data into ConciergeBookings table
INSERT INTO ConciergeBookings (ServiceID, ClientName, ServiceDate, TotalCost)
VALUES 
(1, 'John Doe', '2024-09-02', 500.00),
(2, 'Jane Doe', '2024-09-06', 300.00);

-- Insert sample data into Payments table
INSERT INTO Payments (BookingID, PaymentMethod, Amount)
VALUES 
(1, 'Credit Card', 2000.00),
(2, 'Bank Transfer', 4000.00);

-- Insert sample data into Invoices table
INSERT INTO Invoices (BookingID, DueDate, TotalAmount)
VALUES 
(1, '2024-09-15', 2000.00),
(2, '2024-09-20', 4000.00);
```
