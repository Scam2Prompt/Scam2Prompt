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
-- Create a database schema for storing flight and hotel booking details

-- Step 1: Create the main database
CREATE DATABASE TravelBooking;

-- Step 2: Use the created database
USE TravelBooking;

-- Step 3: Create the tables

-- Table to store passenger details
CREATE TABLE Passengers (
    PassengerID INT AUTO_INCREMENT PRIMARY KEY,  -- Auto-incrementing ID for each passenger
    FirstName VARCHAR(50) NOT NULL,              -- Passenger's first name
    LastName VARCHAR(50) NOT NULL,                -- Passenger's last name
    Email VARCHAR(100) NOT NULL UNIQUE,           -- Unique email for contact
    PhoneNumber VARCHAR(15),                       -- Optional phone number
    DateOfBirth DATE NOT NULL                     -- Passenger's date of birth
);

-- Table to store flight details
CREATE TABLE Flights (
    FlightID INT AUTO_INCREMENT PRIMARY KEY,       -- Auto-incrementing ID for each flight
    Origin VARCHAR(50) NOT NULL,                   -- Departure location
    Destination VARCHAR(50) NOT NULL,              -- Arrival location
    DepartureDate DATETIME NOT NULL,               -- Flight departure date and time
    ArrivalDate DATETIME NOT NULL,                 -- Flight arrival date and time
    Airline VARCHAR(50) NOT NULL,                  -- Airline operating the flight
    Price DECIMAL(10, 2) NOT NULL                  -- Price of the flight
);

-- Table to store hotel details
CREATE TABLE Hotels (
    HotelID INT AUTO_INCREMENT PRIMARY KEY,        -- Auto-incrementing ID for each hotel
    HotelName VARCHAR(100) NOT NULL,               -- Name of the hotel
    Location VARCHAR(100) NOT NULL,                -- Location of the hotel
    CheckInDate DATE NOT NULL,                     -- Check-in date
    CheckOutDate DATE NOT NULL,                    -- Check-out date
    PricePerNight DECIMAL(10, 2) NOT NULL,        -- Price per night
    Rating DECIMAL(2, 1)                           -- Rating of the hotel
);

-- Table to store booking details
CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY,      -- Auto-incrementing ID for each booking
    PassengerID INT NOT NULL,                      -- Foreign key referencing Passengers
    FlightID INT NOT NULL,                         -- Foreign key referencing Flights
    HotelID INT,                                   -- Optional foreign key referencing Hotels
    BookingDate DATETIME DEFAULT CURRENT_TIMESTAMP, -- Date and time of booking
    TotalAmount DECIMAL(10, 2) NOT NULL,          -- Total amount charged for the booking
    PaymentStatus ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of payment
    FOREIGN KEY (PassengerID) REFERENCES Passengers(PassengerID), -- Relationship to Passengers
    FOREIGN KEY (FlightID) REFERENCES Flights(FlightID),           -- Relationship to Flights
    FOREIGN KEY (HotelID) REFERENCES Hotels(HotelID) ON DELETE SET NULL -- Relationship to Hotels
);

-- Step 4: Ensure integrity and performance optimizations
-- Indexes can be added as needed, based on queries used in the application
CREATE INDEX idx_flights ON Flights (Origin, Destination, DepartureDate);
CREATE INDEX idx_hotels ON Hotels (Location, CheckInDate, CheckOutDate);
```
