"""
Generated Code Metadata:
========================
Original URL: https://thebalconehotel.com
Prompt: Design a database schema to store information about hotel rooms, guests, and reservations for a system like The Balcone Suites & Resort.
Generated: DETERMINISTIC_69c240913da56bfe
Batch ID: 20250622_204951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for The Balcone Suites & Resort

-- Table to store information about hotel rooms
CREATE TABLE Rooms (
    RoomID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each room
    RoomNumber VARCHAR(10) NOT NULL,       -- Room number (e.g., "101", "A1")
    RoomType VARCHAR(50) NOT NULL,         -- Type of room (e.g., "Single", "Double", "Suite")
    Capacity INT NOT NULL,                 -- Maximum number of guests the room can accommodate
    PricePerNight DECIMAL(10, 2) NOT NULL, -- Price per night for the room
    IsAvailable BOOLEAN DEFAULT TRUE       -- Availability status of the room
);

-- Table to store information about guests
CREATE TABLE Guests (
    GuestID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each guest
    FirstName VARCHAR(50) NOT NULL,         -- Guest's first name
    LastName VARCHAR(50) NOT NULL,          -- Guest's last name
    Email VARCHAR(100) NOT NULL UNIQUE,     -- Guest's email address (must be unique)
    PhoneNumber VARCHAR(15),                -- Guest's phone number
    Address TEXT                            -- Guest's address
);

-- Table to store information about reservations
CREATE TABLE Reservations (
    ReservationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each reservation
    GuestID INT NOT NULL,                         -- Foreign key referencing Guests table
    RoomID INT NOT NULL,                          -- Foreign key referencing Rooms table
    CheckInDate DATE NOT NULL,                    -- Check-in date for the reservation
    CheckOutDate DATE NOT NULL,                   -- Check-out date for the reservation
    TotalAmount DECIMAL(10, 2) NOT NULL,          -- Total amount for the reservation
    ReservationStatus VARCHAR(20) DEFAULT 'Pending', -- Status of the reservation (e.g., "Pending", "Confirmed", "Cancelled")
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the reservation was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last update

    -- Foreign key constraints
    CONSTRAINT FK_Guest FOREIGN KEY (GuestID) REFERENCES Guests(GuestID) ON DELETE CASCADE,
    CONSTRAINT FK_Room FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID) ON DELETE CASCADE
);

-- Indexes for faster lookups
CREATE INDEX IDX_RoomAvailability ON Rooms (IsAvailable);
CREATE INDEX IDX_ReservationStatus ON Reservations (ReservationStatus);
CREATE INDEX IDX_CheckInDate ON Reservations (CheckInDate);
CREATE INDEX IDX_CheckOutDate ON Reservations (CheckOutDate);
```
