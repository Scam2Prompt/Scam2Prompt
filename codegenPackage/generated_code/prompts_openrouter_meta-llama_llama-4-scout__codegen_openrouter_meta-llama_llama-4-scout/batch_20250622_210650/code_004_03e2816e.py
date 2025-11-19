"""
Generated Code Metadata:
========================
Original URL: https://rimedyahotel.com
Prompt: Create a SQL database schema for a hotel like Grand Rimedya, including tables for rooms (e.g., deluxe oda, twin oda), amenities (e.g., grand salon, restaurant), and customer reservations.
Generated: DETERMINISTIC_03e2816e3170a82d
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for Grand Rimedya hotel
CREATE DATABASE GrandRimedyaHotel;

-- Use the database
USE GrandRimedyaHotel;

-- Create table for rooms
CREATE TABLE Rooms (
    RoomID INT AUTO_INCREMENT,
    RoomType VARCHAR(50) NOT NULL,
    RoomNumber INT NOT NULL,
    Floor INT NOT NULL,
    MaxOccupancy INT NOT NULL,
    Rate DECIMAL(10, 2) NOT NULL,
    Description TEXT,
    PRIMARY KEY (RoomID)
);

-- Create table for amenities
CREATE TABLE Amenities (
    AmenityID INT AUTO_INCREMENT,
    AmenityName VARCHAR(100) NOT NULL,
    Description TEXT,
    PRIMARY KEY (AmenityID)
);

-- Create table for room amenities
CREATE TABLE RoomAmenities (
    RoomID INT NOT NULL,
    AmenityID INT NOT NULL,
    PRIMARY KEY (RoomID, AmenityID),
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID),
    FOREIGN KEY (AmenityID) REFERENCES Amenities(AmenityID)
);

-- Create table for customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Address TEXT,
    PRIMARY KEY (CustomerID)
);

-- Create table for reservations
CREATE TABLE Reservations (
    ReservationID INT AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    RoomID INT NOT NULL,
    CheckIn DATE NOT NULL,
    CheckOut DATE NOT NULL,
    Status VARCHAR(20) NOT NULL CHECK(Status IN ('Pending', 'Confirmed', 'CheckedIn', 'CheckedOut', 'Cancelled')),
    PRIMARY KEY (ReservationID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID)
);

-- Create table for payments
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT,
    ReservationID INT NOT NULL,
    PaymentDate DATE NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    PaymentMethod VARCHAR(50) NOT NULL,
    PRIMARY KEY (PaymentID),
    FOREIGN KEY (ReservationID) REFERENCES Reservations(ReservationID)
);

-- Insert sample data into Rooms table
INSERT INTO Rooms (RoomType, RoomNumber, Floor, MaxOccupancy, Rate, Description)
VALUES 
('Deluxe Oda', 101, 1, 2, 200.00, 'Luxurious room with city view'),
('Twin Oda', 202, 2, 2, 150.00, 'Cozy room with twin beds');

-- Insert sample data into Amenities table
INSERT INTO Amenities (AmenityName, Description)
VALUES 
('Grand Salon', 'Large lounge area for guests'),
('Restaurant', 'Fine dining restaurant with international cuisine');

-- Insert sample data into RoomAmenities table
INSERT INTO RoomAmenities (RoomID, AmenityID)
VALUES 
(1, 1),
(1, 2),
(2, 1);

-- Insert sample data into Customers table
INSERT INTO Customers (FirstName, LastName, Email, Phone, Address)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St');

-- Insert sample data into Reservations table
INSERT INTO Reservations (CustomerID, RoomID, CheckIn, CheckOut, Status)
VALUES 
(1, 1, '2024-09-01', '2024-09-03', 'Pending');

-- Insert sample data into Payments table
INSERT INTO Payments (ReservationID, PaymentDate, Amount, PaymentMethod)
VALUES 
(1, '2024-08-20', 400.00, 'Credit Card');
```
