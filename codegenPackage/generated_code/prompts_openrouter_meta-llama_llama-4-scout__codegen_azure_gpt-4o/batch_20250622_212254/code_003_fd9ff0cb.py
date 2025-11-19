"""
Generated Code Metadata:
========================
Original URL: https://333club.xyz
Prompt: Design a simple database schema to store information about events, guests, and bookings for a nightclub like 333 CLUB, including fields for event type (e.g., Afrobeats, Amapiano, R&B).
Generated: DETERMINISTIC_fd9ff0cb3a0dee69
Batch ID: 20250622_212254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Nightclub Management System

-- Table to store information about events
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each event
    EventName VARCHAR(100) NOT NULL,        -- Name of the event
    EventType ENUM('Afrobeats', 'Amapiano', 'R&B', 'Other') NOT NULL, -- Type of event
    EventDate DATE NOT NULL,                -- Date of the event
    StartTime TIME NOT NULL,                -- Start time of the event
    EndTime TIME NOT NULL,                  -- End time of the event
    Description TEXT,                       -- Optional description of the event
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about guests
CREATE TABLE Guests (
    GuestID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each guest
    FirstName VARCHAR(50) NOT NULL,         -- Guest's first name
    LastName VARCHAR(50) NOT NULL,          -- Guest's last name
    Email VARCHAR(100) NOT NULL UNIQUE,     -- Guest's email address (must be unique)
    PhoneNumber VARCHAR(15),                -- Optional phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about bookings
CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each booking
    EventID INT NOT NULL,                     -- Foreign key referencing Events table
    GuestID INT NOT NULL,                     -- Foreign key referencing Guests table
    BookingDate DATE NOT NULL,                -- Date of the booking
    NumberOfGuests INT NOT NULL,              -- Number of guests included in the booking
    Status ENUM('Confirmed', 'Pending', 'Cancelled') DEFAULT 'Pending', -- Booking status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE, -- Cascade delete if event is deleted
    FOREIGN KEY (GuestID) REFERENCES Guests(GuestID) ON DELETE CASCADE  -- Cascade delete if guest is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_event_type ON Events(EventType); -- Index for EventType in Events table
CREATE INDEX idx_guest_email ON Guests(Email);    -- Index for Email in Guests table
CREATE INDEX idx_booking_status ON Bookings(Status); -- Index for Status in Bookings table
```
