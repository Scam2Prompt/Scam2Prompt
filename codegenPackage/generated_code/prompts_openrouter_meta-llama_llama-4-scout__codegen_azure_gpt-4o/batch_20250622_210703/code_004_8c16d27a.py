"""
Generated Code Metadata:
========================
Original URL: https://gardennovaera.com.br
Prompt: Design a database schema for a hotel management system that includes tables for rooms, guests, bookings, and services like room service or spa treatments.
Generated: DETERMINISTIC_8c16d27aa8df4a6e
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Hotel Management System

-- Table: Rooms
CREATE TABLE Rooms (
    RoomID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each room
    RoomNumber VARCHAR(10) NOT NULL,       -- Room number (e.g., "101", "A12")
    RoomType VARCHAR(50) NOT NULL,         -- Type of room (e.g., "Single", "Double", "Suite")
    Capacity INT NOT NULL,                 -- Maximum number of guests the room can accommodate
    PricePerNight DECIMAL(10, 2) NOT NULL, -- Price per night for the room
    IsAvailable BOOLEAN DEFAULT TRUE       -- Availability status of the room
);

-- Table: Guests
CREATE TABLE Guests (
    GuestID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each guest
    FirstName VARCHAR(50) NOT NULL,         -- Guest's first name
    LastName VARCHAR(50) NOT NULL,          -- Guest's last name
    Email VARCHAR(100) UNIQUE NOT NULL,     -- Guest's email address
    PhoneNumber VARCHAR(15),                -- Guest's phone number
    Address TEXT                            -- Guest's address
);

-- Table: Bookings
CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each booking
    GuestID INT NOT NULL,                      -- Foreign key referencing Guests table
    RoomID INT NOT NULL,                       -- Foreign key referencing Rooms table
    CheckInDate DATE NOT NULL,                 -- Check-in date
    CheckOutDate DATE NOT NULL,                -- Check-out date
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount for the booking
    BookingStatus VARCHAR(20) DEFAULT 'Pending', -- Status of the booking (e.g., "Pending", "Confirmed", "Cancelled")
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the booking was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (GuestID) REFERENCES Guests(GuestID) ON DELETE CASCADE,
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID) ON DELETE CASCADE
);

-- Table: Services
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the service (e.g., "Room Service", "Spa Treatment")
    Description TEXT,                         -- Description of the service
    Price DECIMAL(10, 2) NOT NULL             -- Price of the service
);

-- Table: ServiceBookings
CREATE TABLE ServiceBookings (
    ServiceBookingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service booking
    BookingID INT NOT NULL,                           -- Foreign key referencing Bookings table
    ServiceID INT NOT NULL,                           -- Foreign key referencing Services table
    Quantity INT NOT NULL DEFAULT 1,                 -- Quantity of the service booked
    TotalPrice DECIMAL(10, 2) NOT NULL,              -- Total price for the service booking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp when the service booking was created
    FOREIGN KEY (BookingID) REFERENCES Bookings(BookingID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_room_availability ON Rooms (IsAvailable);
CREATE INDEX idx_booking_status ON Bookings (BookingStatus);
CREATE INDEX idx_service_name ON Services (ServiceName);
```
