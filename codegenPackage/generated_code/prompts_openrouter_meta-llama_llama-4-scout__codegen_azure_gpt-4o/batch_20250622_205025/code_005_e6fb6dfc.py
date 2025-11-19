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

-- Table: Customers
-- Stores information about customers who book properties
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,        -- Customer's email address (must be unique)
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the customer record was created
);

-- Table: Rooms
-- Stores information about rooms available for booking
CREATE TABLE Rooms (
    RoomID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each room
    RoomName VARCHAR(100) NOT NULL,            -- Name or description of the room
    Capacity INT NOT NULL,                     -- Maximum number of people the room can accommodate
    PricePerNight DECIMAL(10, 2) NOT NULL,     -- Price per night for the room
    IsAvailable BOOLEAN DEFAULT TRUE,          -- Availability status of the room
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the room record was created
);

-- Table: Bookings
-- Stores information about bookings made by customers
CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each booking
    CustomerID INT NOT NULL,                   -- Foreign key referencing Customers table
    RoomID INT NOT NULL,                       -- Foreign key referencing Rooms table
    CheckInDate DATE NOT NULL,                 -- Check-in date for the booking
    CheckOutDate DATE NOT NULL,                -- Check-out date for the booking
    TotalPrice DECIMAL(10, 2) NOT NULL,        -- Total price for the booking
    BookingStatus ENUM('Pending', 'Confirmed', 'Cancelled') DEFAULT 'Pending', -- Status of the booking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the booking record was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Cascade delete if customer is removed
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID) ON DELETE CASCADE -- Cascade delete if room is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_customer_email ON Customers(Email); -- Index for quick lookup by email
CREATE INDEX idx_room_availability ON Rooms(IsAvailable); -- Index for quick lookup of available rooms
CREATE INDEX idx_booking_dates ON Bookings(CheckInDate, CheckOutDate); -- Index for quick lookup of booking dates
```
