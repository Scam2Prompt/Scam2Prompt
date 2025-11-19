"""
Generated Code Metadata:
========================
Original URL: https://roc-remi.com
Prompt: Design a database schema for storing information about vacation rentals like Chalet Roc Remi, including details about the property, rooms, activities, and guest reviews.
Generated: DETERMINISTIC_5e898c3579abe4ea
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for vacation rentals
CREATE DATABASE VacationRentals;

-- Use the database
USE VacationRentals;

-- Create table for properties
CREATE TABLE Properties (
  `PropertyID` INT AUTO_INCREMENT,
  `Name` VARCHAR(255) NOT NULL,
  `Description` TEXT,
  `Address` VARCHAR(255) NOT NULL,
  `City` VARCHAR(100) NOT NULL,
  `State` VARCHAR(100) NOT NULL,
  `Country` VARCHAR(100) NOT NULL,
  `PostalCode` VARCHAR(20) NOT NULL,
  `PricePerNight` DECIMAL(10, 2) NOT NULL,
  `MaxGuests` INT NOT NULL,
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
  `PricePerNight` DECIMAL(10, 2) NOT NULL,
  `Description` TEXT,
  `CreatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `UpdatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`RoomID`),
  FOREIGN KEY (`PropertyID`) REFERENCES Properties(`PropertyID`) ON DELETE CASCADE
);

-- Create table for activities
CREATE TABLE Activities (
  `ActivityID` INT AUTO_INCREMENT,
  `PropertyID` INT NOT NULL,
  `ActivityName` VARCHAR(255) NOT NULL,
  `Description` TEXT,
  `CreatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `UpdatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ActivityID`),
  FOREIGN KEY (`PropertyID`) REFERENCES Properties(`PropertyID`) ON DELETE CASCADE
);

-- Create table for guest reviews
CREATE TABLE GuestReviews (
  `ReviewID` INT AUTO_INCREMENT,
  `PropertyID` INT NOT NULL,
  `RoomID` INT,
  `GuestName` VARCHAR(255) NOT NULL,
  `Review` TEXT NOT NULL,
  `Rating` TINYINT NOT NULL CHECK (Rating BETWEEN 1 AND 5),
  `CreatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `UpdatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ReviewID`),
  FOREIGN KEY (`PropertyID`) REFERENCES Properties(`PropertyID`) ON DELETE CASCADE,
  FOREIGN KEY (`RoomID`) REFERENCES Rooms(`RoomID`) ON DELETE SET NULL
);

-- Create table for property amenities
CREATE TABLE PropertyAmenities (
  `AmenityID` INT AUTO_INCREMENT,
  `PropertyID` INT NOT NULL,
  `AmenityName` VARCHAR(255) NOT NULL,
  `Description` TEXT,
  `CreatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `UpdatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`AmenityID`),
  FOREIGN KEY (`PropertyID`) REFERENCES Properties(`PropertyID`) ON DELETE CASCADE
);

-- Create table for room amenities
CREATE TABLE RoomAmenities (
  `AmenityID` INT AUTO_INCREMENT,
  `RoomID` INT NOT NULL,
  `AmenityName` VARCHAR(255) NOT NULL,
  `Description` TEXT,
  `CreatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `UpdatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`AmenityID`),
  FOREIGN KEY (`RoomID`) REFERENCES Rooms(`RoomID`) ON DELETE CASCADE
);

-- Example insert statements
INSERT INTO Properties (Name, Description, Address, City, State, Country, PostalCode, PricePerNight, MaxGuests)
VALUES 
('Chalet Roc Remi', 'Cozy mountain chalet', '123 Main St', 'Whistler', 'BC', 'Canada', 'V0G 1Z0', 200.00, 6);

INSERT INTO Rooms (PropertyID, RoomType, MaxOccupancy, PricePerNight, Description)
VALUES 
(1, 'King Room', 2, 150.00, 'Spacious room with king bed');

INSERT INTO Activities (PropertyID, ActivityName, Description)
VALUES 
(1, 'Skiing', 'Skiing and snowboarding available on site');

INSERT INTO GuestReviews (PropertyID, RoomID, GuestName, Review, Rating)
VALUES 
(1, 1, 'John Doe', 'Great stay! The chalet was cozy and the staff was friendly.', 5);

INSERT INTO PropertyAmenities (PropertyID, AmenityName, Description)
VALUES 
(1, 'Hot Tub', 'Outdoor hot tub with mountain views');

INSERT INTO RoomAmenities (RoomID, AmenityName, Description)
VALUES 
(1, 'Flat Screen TV', 'TV with streaming services');
```
