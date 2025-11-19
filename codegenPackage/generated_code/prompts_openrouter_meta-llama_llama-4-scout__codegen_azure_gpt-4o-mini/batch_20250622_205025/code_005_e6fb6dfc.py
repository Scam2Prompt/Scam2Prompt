"""
Generated Code Metadata:
========================
Original URL: https://haus-alpenrose.com
Prompt: Design a simple database schema for a vacation rental property management system, including tables for rooms, bookings, and customers, inspired by the Haus Alpenrose website.
Generated: DETERMINISTIC_e6fb6dfccfdb6385
Batch ID: 20250622_205025
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a vacation rental property management system

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,             -- Customer's first name
    LastName VARCHAR(50) NOT NULL,              -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,         -- Customer's email address (must be unique)
    Phone VARCHAR(15),                          -- Customer's phone number (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was created
);

-- Table to store room information
CREATE TABLE Rooms (
    RoomID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each room
    RoomNumber VARCHAR(10) NOT NULL UNIQUE,     -- Room number (must be unique)
    RoomType VARCHAR(50) NOT NULL,              -- Type of room (e.g., Single, Double, Suite)
    Capacity INT NOT NULL,                       -- Maximum number of guests allowed in the room
    Price DECIMAL(10, 2) NOT NULL,              -- Price per night for the room
    Description TEXT,                            -- Description of the room (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the room was created
);

-- Table to store booking information
CREATE TABLE Bookings (
    BookingID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each booking
    CustomerID INT NOT NULL,                     -- Foreign key referencing the customer
    RoomID INT NOT NULL,                         -- Foreign key referencing the room
    CheckInDate DATE NOT NULL,                   -- Check-in date for the booking
    CheckOutDate DATE NOT NULL,                  -- Check-out date for the booking
    TotalPrice DECIMAL(10, 2) NOT NULL,         -- Total price for the booking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the booking was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_room_number ON Rooms(RoomNumber);
CREATE INDEX idx_booking_dates ON Bookings(CheckInDate, CheckOutDate);
```
