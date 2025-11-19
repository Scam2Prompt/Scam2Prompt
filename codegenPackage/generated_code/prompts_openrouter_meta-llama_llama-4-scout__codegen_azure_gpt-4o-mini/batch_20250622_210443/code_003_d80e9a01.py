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
-- Database schema for a vacation rental property management system

-- Table to store information about properties
CREATE TABLE Properties (
    PropertyID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each property
    Name VARCHAR(255) NOT NULL,                 -- Name of the property
    Address VARCHAR(255) NOT NULL,              -- Address of the property
    City VARCHAR(100) NOT NULL,                  -- City where the property is located
    State VARCHAR(100) NOT NULL,                 -- State where the property is located
    ZipCode VARCHAR(10) NOT NULL,                -- Zip code of the property
    Description TEXT,                            -- Description of the property
    OwnerID INT NOT NULL,                        -- Foreign key to the Owners table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the property was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (OwnerID) REFERENCES Owners(OwnerID) -- Ensure OwnerID exists in Owners table
);

-- Table to store information about property owners
CREATE TABLE Owners (
    OwnerID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each owner
    Name VARCHAR(255) NOT NULL,                  -- Name of the owner
    Email VARCHAR(255) NOT NULL UNIQUE,          -- Email of the owner
    Phone VARCHAR(15)                            -- Phone number of the owner
);

-- Table to store information about rooms in each property
CREATE TABLE Rooms (
    RoomID INT PRIMARY KEY AUTO_INCREMENT,        -- Unique identifier for each room
    PropertyID INT NOT NULL,                      -- Foreign key to the Properties table
    RoomType VARCHAR(100) NOT NULL,              -- Type of room (e.g., bedroom, suite)
    Capacity INT NOT NULL,                        -- Maximum number of guests the room can accommodate
    Price DECIMAL(10, 2) NOT NULL,               -- Price per night for the room
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the room was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) -- Ensure PropertyID exists in Properties table
);

-- Table to store information about guests
CREATE TABLE Guests (
    GuestID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each guest
    Name VARCHAR(255) NOT NULL,                   -- Name of the guest
    Email VARCHAR(255) NOT NULL UNIQUE,           -- Email of the guest
    Phone VARCHAR(15)                             -- Phone number of the guest
);

-- Table to store information about bookings
CREATE TABLE Bookings (
    BookingID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each booking
    RoomID INT NOT NULL,                          -- Foreign key to the Rooms table
    GuestID INT NOT NULL,                         -- Foreign key to the Guests table
    CheckInDate DATE NOT NULL,                   -- Check-in date for the booking
    CheckOutDate DATE NOT NULL,                  -- Check-out date for the booking
    TotalPrice DECIMAL(10, 2) NOT NULL,         -- Total price for the booking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the booking was made
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID), -- Ensure RoomID exists in Rooms table
    FOREIGN KEY (GuestID) REFERENCES Guests(GuestID) -- Ensure GuestID exists in Guests table
);
```
