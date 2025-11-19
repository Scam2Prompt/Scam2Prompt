"""
Generated Code Metadata:
========================
Original URL: https://hamptons-uk.com
Prompt: Design a database schema for storing hotel operations data, including sales, reservations, and customer information, using a hospitality management system.
Generated: DETERMINISTIC_6807f1020bc1622e
Batch ID: 20250622_204740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for hospitality management system
CREATE DATABASE HospitalityManagement;

-- Use the database
USE HospitalityManagement;

-- Create table for customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address VARCHAR(255),
    City VARCHAR(100),
    State VARCHAR(100),
    Country VARCHAR(100),
    PostalCode VARCHAR(20),
    PRIMARY KEY (CustomerID)
);

-- Create table for hotels
CREATE TABLE Hotels (
    HotelID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    State VARCHAR(100) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    PostalCode VARCHAR(20) NOT NULL,
    Rating TINYINT,
    PRIMARY KEY (HotelID)
);

-- Create table for rooms
CREATE TABLE Rooms (
    RoomID INT AUTO_INCREMENT,
    HotelID INT NOT NULL,
    RoomType VARCHAR(100) NOT NULL,
    RoomNumber INT NOT NULL,
    MaxOccupancy TINYINT NOT NULL,
    Rate DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (RoomID),
    FOREIGN KEY (HotelID) REFERENCES Hotels(HotelID)
);

-- Create table for reservations
CREATE TABLE Reservations (
    ReservationID INT AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    RoomID INT NOT NULL,
    ArrivalDate DATE NOT NULL,
    DepartureDate DATE NOT NULL,
    Status VARCHAR(50) NOT NULL CHECK (Status IN ('Pending', 'Confirmed', 'CheckedIn', 'CheckedOut', 'Cancelled')),
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
    PaymentMethod VARCHAR(100) NOT NULL,
    PRIMARY KEY (PaymentID),
    FOREIGN KEY (ReservationID) REFERENCES Reservations(ReservationID)
);

-- Create table for sales
CREATE TABLE Sales (
    SaleID INT AUTO_INCREMENT,
    ReservationID INT NOT NULL,
    SaleDate DATE NOT NULL,
    Item VARCHAR(255) NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (SaleID),
    FOREIGN KEY (ReservationID) REFERENCES Reservations(ReservationID)
);

-- Create table for services
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT,
    ReservationID INT NOT NULL,
    ServiceDate DATE NOT NULL,
    ServiceType VARCHAR(100) NOT NULL,
    Cost DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (ServiceID),
    FOREIGN KEY (ReservationID) REFERENCES Reservations(ReservationID)
);

-- Create indexes for faster queries
CREATE INDEX idx_Customers_Email ON Customers (Email);
CREATE INDEX idx_Reservations_CustomerID ON Reservations (CustomerID);
CREATE INDEX idx_Reservations_RoomID ON Reservations (RoomID);
CREATE INDEX idx_Payments_ReservationID ON Payments (ReservationID);
CREATE INDEX idx_Sales_ReservationID ON Sales (ReservationID);
CREATE INDEX idx_Services_ReservationID ON Services (ReservationID);
```
