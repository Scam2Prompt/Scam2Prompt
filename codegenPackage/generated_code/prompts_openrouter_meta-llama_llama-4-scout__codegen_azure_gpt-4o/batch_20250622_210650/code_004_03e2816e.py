"""
Generated Code Metadata:
========================
Original URL: https://rimedyahotel.com
Prompt: Create a SQL database schema for a hotel like Grand Rimedya, including tables for rooms (e.g., deluxe oda, twin oda), amenities (e.g., grand salon, restaurant), and customer reservations.
Generated: DETERMINISTIC_03e2816e3170a82d
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for a Hotel Database

-- Create a table for storing room information
CREATE TABLE Rooms (
    RoomID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each room
    RoomType VARCHAR(50) NOT NULL,         -- Type of the room (e.g., deluxe oda, twin oda)
    Capacity INT NOT NULL,                 -- Maximum number of occupants
    PricePerNight DECIMAL(10, 2) NOT NULL, -- Price per night for the room
    IsAvailable BOOLEAN DEFAULT TRUE       -- Availability status of the room
);

-- Create a table for storing amenities information
CREATE TABLE Amenities (
    AmenityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each amenity
    AmenityName VARCHAR(100) NOT NULL,        -- Name of the amenity (e.g., grand salon, restaurant)
    Description TEXT,                         -- Description of the amenity
    IsOperational BOOLEAN DEFAULT TRUE        -- Operational status of the amenity
);

-- Create a table for storing customer reservations
CREATE TABLE Reservations (
    ReservationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each reservation
    CustomerName VARCHAR(100) NOT NULL,           -- Name of the customer
    CustomerEmail VARCHAR(100) NOT NULL,          -- Email of the customer
    RoomID INT NOT NULL,                          -- Foreign key referencing the Rooms table
    CheckInDate DATE NOT NULL,                    -- Check-in date for the reservation
    CheckOutDate DATE NOT NULL,                   -- Check-out date for the reservation
    TotalPrice DECIMAL(10, 2) NOT NULL,           -- Total price for the reservation
    ReservationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time the reservation was made
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID) ON DELETE CASCADE -- Cascade delete if the room is deleted
);

-- Create a junction table for linking amenities to rooms
CREATE TABLE RoomAmenities (
    RoomAmenityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each room-amenity relationship
    RoomID INT NOT NULL,                          -- Foreign key referencing the Rooms table
    AmenityID INT NOT NULL,                       -- Foreign key referencing the Amenities table
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID) ON DELETE CASCADE, -- Cascade delete if the room is deleted
    FOREIGN KEY (AmenityID) REFERENCES Amenities(AmenityID) ON DELETE CASCADE -- Cascade delete if the amenity is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_room_type ON Rooms(RoomType);
CREATE INDEX idx_amenity_name ON Amenities(AmenityName);
CREATE INDEX idx_customer_email ON Reservations(CustomerEmail);

-- Error handling and constraints
-- Ensure check-out date is after check-in date
ALTER TABLE Reservations
ADD CONSTRAINT chk_dates CHECK (CheckOutDate > CheckInDate);

-- Ensure room capacity is a positive number
ALTER TABLE Rooms
ADD CONSTRAINT chk_capacity CHECK (Capacity > 0);

-- Ensure price per night and total price are positive numbers
ALTER TABLE Rooms
ADD CONSTRAINT chk_price_per_night CHECK (PricePerNight > 0);

ALTER TABLE Reservations
ADD CONSTRAINT chk_total_price CHECK (TotalPrice > 0);
```
