"""
Generated Code Metadata:
========================
Original URL: https://www.hostalcasadelmar.es
Prompt: Create a SQL database schema for managing room reservations at a boutique hostel like Hostal Casa del Mar, including tables for rooms, guests, and reservations.
Generated: DETERMINISTIC_268ded61a23b4a4c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Managing Room Reservations at a Boutique Hostel

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Reservations;
DROP TABLE IF EXISTS Guests;
DROP TABLE IF EXISTS Rooms;

-- Table to store information about rooms
CREATE TABLE Rooms (
    RoomID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each room
    RoomNumber VARCHAR(10) NOT NULL UNIQUE, -- Room number (e.g., "101", "102")
    RoomType VARCHAR(50) NOT NULL,           -- Type of room (e.g., "Single", "Double", "Suite")
    Capacity INT NOT NULL,                    -- Maximum number of guests allowed in the room
    Price DECIMAL(10, 2) NOT NULL,           -- Price per night for the room
    Description TEXT,                         -- Description of the room
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the room was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store information about guests
CREATE TABLE Guests (
    GuestID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each guest
    FirstName VARCHAR(50) NOT NULL,          -- Guest's first name
    LastName VARCHAR(50) NOT NULL,            -- Guest's last name
    Email VARCHAR(100) NOT NULL UNIQUE,       -- Guest's email address
    PhoneNumber VARCHAR(15),                  -- Guest's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the guest was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store reservations
CREATE TABLE Reservations (
    ReservationID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each reservation
    GuestID INT NOT NULL,                         -- Foreign key referencing Guests
    RoomID INT NOT NULL,                          -- Foreign key referencing Rooms
    CheckInDate DATE NOT NULL,                    -- Check-in date for the reservation
    CheckOutDate DATE NOT NULL,                   -- Check-out date for the reservation
    NumberOfGuests INT NOT NULL,                 -- Number of guests for the reservation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the reservation was made
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (GuestID) REFERENCES Guests(GuestID) ON DELETE CASCADE, -- Ensure guest deletion cascades
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID) ON DELETE CASCADE,     -- Ensure room deletion cascades
    CHECK (CheckInDate < CheckOutDate)          -- Ensure check-in date is before check-out date
);

-- Indexes for performance optimization
CREATE INDEX idx_guest_email ON Guests(Email);
CREATE INDEX idx_room_number ON Rooms(RoomNumber);
CREATE INDEX idx_reservation_dates ON Reservations(CheckInDate, CheckOutDate);
```
