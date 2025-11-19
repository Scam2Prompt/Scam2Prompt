"""
Generated Code Metadata:
========================
Original URL: https://koltinsuchitoto.com
Prompt: Design a database schema to store information about hotel rooms, guests, and reservations for a hostel like Hostal Koltin Suchitoto.
Generated: DETERMINISTIC_239c6aa8d7be01fe
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a hostel management system

-- Table to store information about hotel rooms
CREATE TABLE Rooms (
    RoomID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each room
    RoomNumber VARCHAR(10) NOT NULL,       -- Room number or identifier
    Capacity INT NOT NULL,                 -- Maximum number of guests the room can accommodate
    PricePerNight DECIMAL(10, 2) NOT NULL, -- Price per night for the room
    RoomType VARCHAR(50),                  -- Type of room (e.g., Single, Double, Dormitory)
    IsAvailable BOOLEAN DEFAULT TRUE       -- Availability status of the room
);

-- Table to store information about guests
CREATE TABLE Guests (
    GuestID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each guest
    FirstName VARCHAR(50) NOT NULL,         -- Guest's first name
    LastName VARCHAR(50) NOT NULL,          -- Guest's last name
    Email VARCHAR(100) UNIQUE,              -- Guest's email address
    PhoneNumber VARCHAR(15),                -- Guest's phone number
    DateOfBirth DATE,                       -- Guest's date of birth
    Address TEXT                            -- Guest's address
);

-- Table to store information about reservations
CREATE TABLE Reservations (
    ReservationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each reservation
    GuestID INT NOT NULL,                         -- Foreign key referencing Guests table
    RoomID INT NOT NULL,                          -- Foreign key referencing Rooms table
    CheckInDate DATE NOT NULL,                    -- Check-in date for the reservation
    CheckOutDate DATE NOT NULL,                   -- Check-out date for the reservation
    TotalPrice DECIMAL(10, 2) NOT NULL,           -- Total price for the reservation
    ReservationStatus VARCHAR(20) DEFAULT 'Pending', -- Status of the reservation (e.g., Pending, Confirmed, Cancelled)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the reservation was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update

    -- Foreign key constraints
    CONSTRAINT FK_Guest FOREIGN KEY (GuestID) REFERENCES Guests(GuestID) ON DELETE CASCADE,
    CONSTRAINT FK_Room FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX IDX_RoomAvailability ON Rooms (IsAvailable);
CREATE INDEX IDX_ReservationDates ON Reservations (CheckInDate, CheckOutDate);
CREATE INDEX IDX_GuestEmail ON Guests (Email);
```
