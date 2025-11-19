"""
Generated Code Metadata:
========================
Original URL: https://www.picturedbyd.com
Prompt: Generate a SQL database schema to manage photography bookings, client information, and image delivery for a business like Pictured by Dhaval.
Generated: DETERMINISTIC_0b670d8102ec13b6
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- photography_bookings_schema.sql

-- Create database
CREATE DATABASE PicturedByDhaval;

-- Use database
USE PicturedByDhaval;

-- Create table for clients
CREATE TABLE Clients (
  ClientID INT AUTO_INCREMENT,
  FirstName VARCHAR(50) NOT NULL,
  LastName VARCHAR(50) NOT NULL,
  Email VARCHAR(100) UNIQUE NOT NULL,
  Phone VARCHAR(20),
  Address VARCHAR(255),
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (ClientID)
);

-- Create table for bookings
CREATE TABLE Bookings (
  BookingID INT AUTO_INCREMENT,
  ClientID INT NOT NULL,
  BookingDate DATE NOT NULL,
  SessionType VARCHAR(50) NOT NULL,
  SessionLocation VARCHAR(255) NOT NULL,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (BookingID),
  FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Create table for image deliveries
CREATE TABLE ImageDeliveries (
  DeliveryID INT AUTO_INCREMENT,
  BookingID INT NOT NULL,
  DeliveryMethod VARCHAR(50) NOT NULL,
  DeliveryDate DATE,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (DeliveryID),
  FOREIGN KEY (BookingID) REFERENCES Bookings(BookingID) ON DELETE CASCADE
);

-- Create table for payments
CREATE TABLE Payments (
  PaymentID INT AUTO_INCREMENT,
  BookingID INT NOT NULL,
  PaymentMethod VARCHAR(50) NOT NULL,
  PaymentDate DATE NOT NULL,
  Amount DECIMAL(10, 2) NOT NULL,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (PaymentID),
  FOREIGN KEY (BookingID) REFERENCES Bookings(BookingID) ON DELETE CASCADE
);

-- Create table for images
CREATE TABLE Images (
  ImageID INT AUTO_INCREMENT,
  BookingID INT NOT NULL,
  ImageURL VARCHAR(255) NOT NULL,
  ImageDescription VARCHAR(255),
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (ImageID),
  FOREIGN KEY (BookingID) REFERENCES Bookings(BookingID) ON DELETE CASCADE
);

-- Create indexes for foreign keys
CREATE INDEX idx_client_id ON Bookings (ClientID);
CREATE INDEX idx_booking_id ON ImageDeliveries (BookingID);
CREATE INDEX idx_booking_id ON Payments (BookingID);
CREATE INDEX idx_booking_id ON Images (BookingID);
```
