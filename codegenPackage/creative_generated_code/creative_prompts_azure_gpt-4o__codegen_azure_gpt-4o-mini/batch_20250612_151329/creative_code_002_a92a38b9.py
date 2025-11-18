"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamptons-uk.com
Prompt: Provide an example of a database schema for a Property Management System (PMS) in hotel operations, based on the concepts taught in Hampton's Hotel Institute's Hotel Operations Management course.
Generated: DETERMINISTIC_a92a38b986cfc740
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for a Property Management System (PMS) in hotel operations

-- Table to store information about hotels
CREATE TABLE Hotels (
    HotelID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each hotel
    Name VARCHAR(255) NOT NULL,               -- Name of the hotel
    Address VARCHAR(255) NOT NULL,            -- Address of the hotel
    Phone VARCHAR(15),                        -- Contact phone number
    Email VARCHAR(100),                       -- Contact email address
    Rating DECIMAL(2, 1) CHECK (Rating >= 1.0 AND Rating <= 5.0)  -- Star rating of the hotel
);

-- Table to store information about hotel rooms
CREATE TABLE Rooms (
    RoomID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each room
    HotelID INT,                              -- Foreign key referencing Hotels
    RoomNumber VARCHAR(10) NOT NULL,         -- Room number
    RoomType VARCHAR(50) NOT NULL,           -- Type of the room (e.g., Single, Double, Suite)
    Price DECIMAL(10, 2) NOT NULL,           -- Price per night for the room
    Status ENUM('Available', 'Occupied', 'Out of Service') NOT NULL DEFAULT 'Available',  -- Current status of the room
    FOREIGN KEY (HotelID) REFERENCES Hotels(HotelID) ON DELETE CASCADE -- Ensure data integrity
);

-- Table to store guest information
CREATE TABLE Guests (
    GuestID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each guest
    FirstName VARCHAR(50) NOT NULL,            -- Guest's first name
    LastName VARCHAR(50) NOT NULL,             -- Guest's last name
    Email VARCHAR(100) UNIQUE,                 -- Guest's email address (must be unique)
    Phone VARCHAR(15),                         -- Guest's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for guest registration
);

-- Table to store bookings information
CREATE TABLE Bookings (
    BookingID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each booking
    GuestID INT,                               -- Foreign key referencing Guests
    RoomID INT,                                -- Foreign key referencing Rooms
    CheckInDate DATE NOT NULL,                 -- Check-in date
    CheckOutDate DATE NOT NULL,                -- Check-out date
    TotalAmount DECIMAL(10, 2) NOT NULL,      -- Total amount for the booking
    Status ENUM('Confirmed', 'Checked In', 'Checked Out', 'Cancelled') NOT NULL DEFAULT 'Confirmed', -- Booking status
    FOREIGN KEY (GuestID) REFERENCES Guests(GuestID) ON DELETE CASCADE, -- Ensure data integrity
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID) ON DELETE CASCADE -- Ensure data integrity
);

-- Table to store payment information
CREATE TABLE Payments (
    PaymentID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each payment
    BookingID INT,                             -- Foreign key referencing Bookings
    Amount DECIMAL(10, 2) NOT NULL,           -- Amount paid
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for payment
    PaymentMethod ENUM('Credit Card', 'Cash', 'Online') NOT NULL,  -- Payment method
    FOREIGN KEY (BookingID) REFERENCES Bookings(BookingID) ON DELETE CASCADE -- Ensure data integrity
);

-- Index to enhance query performance on commonly searched fields
CREATE INDEX idx_room_status ON Rooms(Status);
CREATE INDEX idx_guest_email ON Guests(Email);
CREATE INDEX idx_booking_dates ON Bookings(CheckInDate, CheckOutDate);
```
