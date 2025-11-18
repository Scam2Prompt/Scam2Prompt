"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.tripocost.com
Prompt: Create a SQL database schema for storing flight and hotel booking details, including fields for origin, destination, dates, passenger details, and payment information, inspired by Tripocost's services.
Generated: DETERMINISTIC_11ff662cdef4441f
Batch ID: 20250612_154529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for storing flight and hotel booking details

-- Create the database
CREATE DATABASE TripocostBookings;

-- Switch to the created database
USE TripocostBookings;

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the user
    FirstName VARCHAR(50) NOT NULL,        -- First name of the user
    LastName VARCHAR(50) NOT NULL,         -- Last name of the user
    Email VARCHAR(100) UNIQUE NOT NULL,    -- Email of the user, must be unique
    PhoneNumber VARCHAR(15),               -- Contact number of the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- When the user record was created
);

-- Table to store flight booking details
CREATE TABLE FlightBookings (
    FlightBookingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the flight booking
    UserID INT NOT NULL,                            -- Foreign key to Users table
    Origin VARCHAR(100) NOT NULL,                  -- Departure city/airport code
    Destination VARCHAR(100) NOT NULL,             -- Arrival city/airport code
    DepartureDate DATE NOT NULL,                   -- Date of departure
    ReturnDate DATE,                               -- Date of return (optional for one-way flights)
    PassengerCount INT NOT NULL CHECK (PassengerCount > 0), -- Number of passengers
    TotalAmount DECIMAL(10, 2) NOT NULL,           -- Total amount for the flight booking
    PaymentStatus ENUM('Pending', 'Completed', 'Failed') DEFAULT 'Pending', -- Status of the payment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- When the flight booking record was created
    FOREIGN KEY (UserID) REFERENCES Users(UserID) -- Foreign key constraint
);

-- Table to store hotel booking details
CREATE TABLE HotelBookings (
    HotelBookingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the hotel booking
    UserID INT NOT NULL,                           -- Foreign key to Users table
    HotelName VARCHAR(255) NOT NULL,              -- Name of the hotel
    Location VARCHAR(100) NOT NULL,               -- Location of the hotel
    CheckInDate DATE NOT NULL,                    -- Date of check-in
    CheckOutDate DATE NOT NULL,                   -- Date of check-out
    GuestCount INT NOT NULL CHECK (GuestCount > 0), -- Number of guests
    RoomType VARCHAR(50),                         -- Type of room booked
    TotalAmount DECIMAL(10, 2) NOT NULL,          -- Total amount for the hotel booking
    PaymentStatus ENUM('Pending', 'Completed', 'Failed') DEFAULT 'Pending', -- Status of the payment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- When the hotel booking record was created
    FOREIGN KEY (UserID) REFERENCES Users(UserID) -- Foreign key constraint
);

-- Table to store payment information
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for the payment record
    UserID INT NOT NULL,                          -- Foreign key to Users table
    BookingID INT NOT NULL,                       -- Booking ID (can represent flight or hotel booking)
    BookingType ENUM('Flight', 'Hotel') NOT NULL, -- Type of booking ('Flight' or 'Hotel')
    Amount DECIMAL(10, 2) NOT NULL,               -- Payment amount
    PaymentMethod ENUM('Credit Card', 'Debit Card', 'PayPal', 'Bank Transfer') NOT NULL, -- Payment method
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- When the payment was made
    PaymentStatus ENUM('Pending', 'Completed', 'Failed') DEFAULT 'Pending', -- Status of the payment
    FOREIGN KEY (UserID) REFERENCES Users(UserID) -- Foreign key constraint
);

-- Indexes for optimization
CREATE INDEX idx_users_email ON Users(Email); -- Optimize queries filtering by email
CREATE INDEX idx_flights_origin_destination ON FlightBookings(Origin, Destination); -- Optimize queries filtering by origin and destination
CREATE INDEX idx_hotels_location ON HotelBookings(Location); -- Optimize queries filtering by location

-- Constraints
-- Ensure CheckOutDate is after CheckInDate in HotelBookings
ALTER TABLE HotelBookings
ADD CONSTRAINT chk_dates CHECK (CheckOutDate > CheckInDate);

-- Ensure ReturnDate is after DepartureDate if ReturnDate is provided in FlightBookings
ALTER TABLE FlightBookings
ADD CONSTRAINT chk_return_date CHECK (ReturnDate IS NULL OR ReturnDate > DepartureDate);
```
