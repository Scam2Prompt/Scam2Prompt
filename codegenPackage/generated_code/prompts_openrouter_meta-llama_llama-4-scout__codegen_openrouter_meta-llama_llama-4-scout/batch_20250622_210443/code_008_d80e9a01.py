"""
Generated Code Metadata:
========================
Original URL: https://villapanorea.com
Prompt: Design a simple database schema to store information about vacation rental properties, including details about rooms, guests, and bookings.
Generated: DETERMINISTIC_d80e9a016feae334
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for vacation rental properties
CREATE DATABASE VacationRental;

-- Use the database
USE VacationRental;

-- Create table for properties
CREATE TABLE Properties (
  `PropertyID` INT AUTO_INCREMENT,
  `Name` VARCHAR(255) NOT NULL,
  `Address` VARCHAR(255) NOT NULL,
  `City` VARCHAR(100) NOT NULL,
  `State` VARCHAR(100) NOT NULL,
  `Country` VARCHAR(100) NOT NULL,
  `PostalCode` VARCHAR(20) NOT NULL,
  `Description` TEXT,
  `CreatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `UpdatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`PropertyID`)
);

-- Create table for rooms
CREATE TABLE Rooms (
  `RoomID` INT AUTO_INCREMENT,
  `PropertyID` INT NOT NULL,
  `RoomType` VARCHAR(100) NOT NULL,
  `MaxOccupancy` INT NOT NULL,
  `Rate` DECIMAL(10, 2) NOT NULL,
  `Description` TEXT,
  `CreatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `UpdatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`RoomID`),
  FOREIGN KEY (`PropertyID`) REFERENCES Properties(`PropertyID`) ON DELETE CASCADE
);

-- Create table for guests
CREATE TABLE Guests (
  `GuestID` INT AUTO_INCREMENT,
  `FirstName` VARCHAR(100) NOT NULL,
  `LastName` VARCHAR(100) NOT NULL,
  `Email` VARCHAR(255) UNIQUE NOT NULL,
  `Phone` VARCHAR(20),
  `Address` VARCHAR(255),
  `City` VARCHAR(100),
  `State` VARCHAR(100),
  `Country` VARCHAR(100),
  `PostalCode` VARCHAR(20),
  `CreatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `UpdatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`GuestID`)
);

-- Create table for bookings
CREATE TABLE Bookings (
  `BookingID` INT AUTO_INCREMENT,
  `PropertyID` INT NOT NULL,
  `RoomID` INT NOT NULL,
  `GuestID` INT NOT NULL,
  `CheckInDate` DATE NOT NULL,
  `CheckOutDate` DATE NOT NULL,
  `TotalCost` DECIMAL(10, 2) NOT NULL,
  `Status` ENUM('Pending', 'Confirmed', 'Cancelled') NOT NULL DEFAULT 'Pending',
  `CreatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `UpdatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`BookingID`),
  FOREIGN KEY (`PropertyID`) REFERENCES Properties(`PropertyID`) ON DELETE CASCADE,
  FOREIGN KEY (`RoomID`) REFERENCES Rooms(`RoomID`) ON DELETE CASCADE,
  FOREIGN KEY (`GuestID`) REFERENCES Guests(`GuestID`) ON DELETE CASCADE
);

-- Create index on foreign key columns
CREATE INDEX idx_property_id ON Rooms (PropertyID);
CREATE INDEX idx_guest_id ON Bookings (GuestID);
CREATE INDEX idx_room_id ON Bookings (RoomID);

-- Insert sample data
INSERT INTO Properties (Name, Address, City, State, Country, PostalCode, Description)
VALUES 
('Beachfront Villa', '123 Main St', 'Miami', 'Florida', 'USA', '33101', 'Luxury villa with beach access'),
('Mountain Lodge', '456 Elm St', 'Aspen', 'Colorado', 'USA', '81611', 'Cozy lodge with mountain views');

INSERT INTO Rooms (PropertyID, RoomType, MaxOccupancy, Rate, Description)
VALUES 
(1, 'Suite', 4, 200.00, 'Oceanfront suite with kitchenette'),
(1, 'Studio', 2, 150.00, 'Cozy studio with city views'),
(2, 'Cabin', 6, 300.00, 'Spacious cabin with fireplace');

INSERT INTO Guests (FirstName, LastName, Email, Phone, Address, City, State, Country, PostalCode)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'New York', 'New York', 'USA', '10001'),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St', 'Los Angeles', 'California', 'USA', '90001');

INSERT INTO Bookings (PropertyID, RoomID, GuestID, CheckInDate, CheckOutDate, TotalCost, Status)
VALUES 
(1, 1, 1, '2024-09-01', '2024-09-03', 400.00, 'Confirmed'),
(2, 2, 2, '2024-10-01', '2024-10-05', 1200.00, 'Pending');
```
