"""
Generated Code Metadata:
========================
Original URL: https://balticasopot.pl
Prompt: Design a basic database schema for storing hotel information, including rooms, guests, and reservations, and provide SQL code to create the schema.
Generated: DETERMINISTIC_425d0a17722588e2
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for hotel information
CREATE DATABASE HotelManagement;

-- Use the HotelManagement database
USE HotelManagement;

-- Create table for hotels
CREATE TABLE Hotels (
    HotelID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    State VARCHAR(100) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    PostalCode VARCHAR(20) NOT NULL,
    Phone VARCHAR(20),
    Email VARCHAR(100) UNIQUE,
    PRIMARY KEY (HotelID)
);

-- Create table for rooms
CREATE TABLE Rooms (
    RoomID INT AUTO_INCREMENT,
    HotelID INT NOT NULL,
    RoomNumber INT NOT NULL,
    RoomType VARCHAR(50) NOT NULL,
    MaxOccupancy INT NOT NULL,
    Rate DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (RoomID),
    FOREIGN KEY (HotelID) REFERENCES Hotels(HotelID) ON DELETE CASCADE
);

-- Create table for guests
CREATE TABLE Guests (
    GuestID INT AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    State VARCHAR(100) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    PostalCode VARCHAR(20) NOT NULL,
    PRIMARY KEY (GuestID)
);

-- Create table for reservations
CREATE TABLE Reservations (
    ReservationID INT AUTO_INCREMENT,
    GuestID INT NOT NULL,
    HotelID INT NOT NULL,
    RoomID INT NOT NULL,
    ArrivalDate DATE NOT NULL,
    DepartureDate DATE NOT NULL,
    Status VARCHAR(50) NOT NULL CHECK (Status IN ('Pending', 'Confirmed', 'CheckedIn', 'CheckedOut', 'Cancelled')),
    PRIMARY KEY (ReservationID),
    FOREIGN KEY (GuestID) REFERENCES Guests(GuestID) ON DELETE CASCADE,
    FOREIGN KEY (HotelID) REFERENCES Hotels(HotelID) ON DELETE CASCADE,
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID) ON DELETE CASCADE,
    CHECK (ArrivalDate < DepartureDate)
);

-- Create table for payments
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT,
    ReservationID INT NOT NULL,
    PaymentDate DATE NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    PaymentMethod VARCHAR(50) NOT NULL,
    PRIMARY KEY (PaymentID),
    FOREIGN KEY (ReservationID) REFERENCES Reservations(ReservationID) ON DELETE CASCADE
);
```
