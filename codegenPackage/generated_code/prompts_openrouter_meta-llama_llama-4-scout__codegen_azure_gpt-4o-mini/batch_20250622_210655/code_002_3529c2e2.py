"""
Generated Code Metadata:
========================
Original URL: https://lhotel-des-chats.com
Prompt: Generate a sample database schema for a cat hotel management system, including tables for rooms, bookings, and customer information.
Generated: DETERMINISTIC_3529c2e2b59df6a7
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Sample Database Schema for a Cat Hotel Management System

-- Drop existing tables if they exist (for re-creation during development)
DROP TABLE IF EXISTS Bookings;
DROP TABLE IF EXISTS Rooms;
DROP TABLE IF EXISTS Customers;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address (unique)
    PhoneNumber VARCHAR(15),                    -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was added
);

-- Table to store room information
CREATE TABLE Rooms (
    RoomID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each room
    RoomNumber VARCHAR(10) NOT NULL UNIQUE,    -- Room number (unique)
    RoomType VARCHAR(50) NOT NULL,              -- Type of room (e.g., standard, luxury)
    Capacity INT NOT NULL CHECK (Capacity > 0), -- Maximum number of cats allowed in the room
    Price DECIMAL(10, 2) NOT NULL,              -- Price per night for the room
    IsAvailable BOOLEAN DEFAULT TRUE,            -- Availability status of the room
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the room was added
);

-- Table to store booking information
CREATE TABLE Bookings (
    BookingID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each booking
    CustomerID INT NOT NULL,                     -- Foreign key referencing Customers
    RoomID INT NOT NULL,                         -- Foreign key referencing Rooms
    CheckInDate DATE NOT NULL,                   -- Check-in date for the booking
    CheckOutDate DATE NOT NULL,                  -- Check-out date for the booking
    TotalPrice DECIMAL(10, 2) NOT NULL,         -- Total price for the booking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the booking was made
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_room_availability ON Rooms(IsAvailable);
CREATE INDEX idx_booking_dates ON Bookings(CheckInDate, CheckOutDate);
```
