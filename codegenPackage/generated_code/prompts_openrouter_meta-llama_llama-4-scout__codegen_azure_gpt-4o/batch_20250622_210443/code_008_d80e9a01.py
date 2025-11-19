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
-- Database schema for vacation rental properties

-- Table to store information about properties
CREATE TABLE Properties (
    PropertyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each property
    Name VARCHAR(255) NOT NULL,                -- Name of the property
    Address VARCHAR(255) NOT NULL,             -- Address of the property
    City VARCHAR(100) NOT NULL,                -- City where the property is located
    State VARCHAR(100) NOT NULL,               -- State where the property is located
    Country VARCHAR(100) NOT NULL,             -- Country where the property is located
    ZipCode VARCHAR(20),                       -- Zip code of the property
    Description TEXT,                          -- Description of the property
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the property was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about rooms in a property
CREATE TABLE Rooms (
    RoomID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each room
    PropertyID INT NOT NULL,                   -- Foreign key referencing the property
    Name VARCHAR(255) NOT NULL,                -- Name or identifier for the room
    Capacity INT NOT NULL,                     -- Maximum number of guests the room can accommodate
    PricePerNight DECIMAL(10, 2) NOT NULL,     -- Price per night for the room
    Description TEXT,                          -- Description of the room
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the room was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE -- Cascade delete if property is deleted
);

-- Table to store information about guests
CREATE TABLE Guests (
    GuestID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each guest
    FirstName VARCHAR(100) NOT NULL,           -- First name of the guest
    LastName VARCHAR(100) NOT NULL,            -- Last name of the guest
    Email VARCHAR(255) NOT NULL UNIQUE,        -- Email address of the guest
    PhoneNumber VARCHAR(20),                   -- Phone number of the guest
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the guest was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about bookings
CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each booking
    RoomID INT NOT NULL,                       -- Foreign key referencing the room
    GuestID INT NOT NULL,                      -- Foreign key referencing the guest
    CheckInDate DATE NOT NULL,                 -- Check-in date for the booking
    CheckOutDate DATE NOT NULL,                -- Check-out date for the booking
    TotalPrice DECIMAL(10, 2) NOT NULL,        -- Total price for the booking
    Status ENUM('Pending', 'Confirmed', 'Cancelled') DEFAULT 'Pending', -- Status of the booking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the booking was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID) ON DELETE CASCADE, -- Cascade delete if room is deleted
    FOREIGN KEY (GuestID) REFERENCES Guests(GuestID) ON DELETE CASCADE -- Cascade delete if guest is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_property_city ON Properties(City);
CREATE INDEX idx_room_property ON Rooms(PropertyID);
CREATE INDEX idx_booking_dates ON Bookings(CheckInDate, CheckOutDate);
```
