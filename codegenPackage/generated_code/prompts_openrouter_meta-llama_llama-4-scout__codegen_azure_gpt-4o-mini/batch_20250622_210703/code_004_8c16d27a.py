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
-- Database schema for a Hotel Management System

-- Table to store information about hotel rooms
CREATE TABLE Rooms (
    RoomID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each room
    RoomNumber VARCHAR(10) NOT NULL,        -- Room number (e.g., '101', '202')
    RoomType VARCHAR(50) NOT NULL,          -- Type of room (e.g., 'Single', 'Double', 'Suite')
    Capacity INT NOT NULL,                   -- Maximum number of guests allowed in the room
    Price DECIMAL(10, 2) NOT NULL,          -- Price per night for the room
    Status ENUM('Available', 'Occupied', 'Maintenance') NOT NULL DEFAULT 'Available', -- Current status of the room
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the room was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the room was last updated
);

-- Table to store information about guests
CREATE TABLE Guests (
    GuestID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each guest
    FirstName VARCHAR(50) NOT NULL,         -- Guest's first name
    LastName VARCHAR(50) NOT NULL,          -- Guest's last name
    Email VARCHAR(100) UNIQUE NOT NULL,     -- Guest's email address (must be unique)
    Phone VARCHAR(15),                       -- Guest's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the guest was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the guest was last updated
);

-- Table to store booking information
CREATE TABLE Bookings (
    BookingID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each booking
    GuestID INT NOT NULL,                     -- Foreign key referencing the guest
    RoomID INT NOT NULL,                      -- Foreign key referencing the room
    CheckInDate DATE NOT NULL,                -- Check-in date for the booking
    CheckOutDate DATE NOT NULL,               -- Check-out date for the booking
    TotalAmount DECIMAL(10, 2) NOT NULL,     -- Total amount for the booking
    Status ENUM('Confirmed', 'CheckedIn', 'CheckedOut', 'Cancelled') NOT NULL DEFAULT 'Confirmed', -- Current status of the booking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the booking was made
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the booking was last updated
    FOREIGN KEY (GuestID) REFERENCES Guests(GuestID) ON DELETE CASCADE, -- Ensure guest deletion cascades
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID) ON DELETE CASCADE -- Ensure room deletion cascades
);

-- Table to store services offered by the hotel
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,       -- Name of the service (e.g., 'Room Service', 'Spa Treatment')
    Description TEXT,                         -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,           -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the service was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the service was last updated
);

-- Table to store service bookings related to guests
CREATE TABLE ServiceBookings (
    ServiceBookingID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each service booking
    BookingID INT NOT NULL,                          -- Foreign key referencing the booking
    ServiceID INT NOT NULL,                          -- Foreign key referencing the service
    Quantity INT NOT NULL DEFAULT 1,                 -- Quantity of the service booked
    TotalAmount DECIMAL(10, 2) NOT NULL,            -- Total amount for the service booking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp for when the service booking was made
    FOREIGN KEY (BookingID) REFERENCES Bookings(BookingID) ON DELETE CASCADE, -- Ensure booking deletion cascades
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Ensure service deletion cascades
);
```
