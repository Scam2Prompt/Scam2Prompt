"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.airlines-reservation.com
Prompt: Create a database schema in SQL to store flight booking information, including fields for departure, return dates, passenger details, and preferred airline, modeled after the booking process on airlines-reservation.com.
Generated: DETERMINISTIC_8cb75db1f3b98965
Batch ID: 20250612_154846
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL schema for flight booking information

-- Create the table to store passenger information
CREATE TABLE Passengers (
    PassengerID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each passenger
    FirstName VARCHAR(50) NOT NULL,                     -- First name of the passenger
    LastName VARCHAR(50) NOT NULL,                      -- Last name of the passenger
    Email VARCHAR(100) NOT NULL UNIQUE,                 -- Email address of the passenger (must be unique)
    PhoneNumber VARCHAR(15),                            -- Contact phone number of the passenger
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP       -- Timestamp for when the passenger record was created
);

-- Create the table to store flight booking information
CREATE TABLE FlightBookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY,           -- Unique identifier for each booking
    PassengerID INT NOT NULL,                           -- Foreign key referencing the Passengers table
    DepartureDate DATE NOT NULL,                        -- Departure date of the flight
    ReturnDate DATE,                                    -- Return date of the flight (optional for one-way trips)
    PreferredAirline VARCHAR(100) NOT NULL,             -- Name of the passenger's preferred airline
    BookingStatus ENUM('Pending', 'Confirmed', 'Cancelled') DEFAULT 'Pending', -- Status of the booking
    TotalPrice DECIMAL(10, 2) NOT NULL,                 -- Total price of the flight booking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,      -- Timestamp for when the booking record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last update to the booking record
    FOREIGN KEY (PassengerID) REFERENCES Passengers(PassengerID) ON DELETE CASCADE -- Ensure bookings are deleted if the passenger is deleted
);

-- Create the table to store flight details
CREATE TABLE FlightDetails (
    FlightID INT AUTO_INCREMENT PRIMARY KEY,            -- Unique identifier for each flight
    BookingID INT NOT NULL,                             -- Foreign key referencing the FlightBookings table
    FlightNumber VARCHAR(20) NOT NULL,                  -- Flight number assigned by the airline
    Airline VARCHAR(100) NOT NULL,                      -- Name of the airline operating the flight
    DepartureAirport VARCHAR(100) NOT NULL,             -- Code or name of the departure airport
    ArrivalAirport VARCHAR(100) NOT NULL,               -- Code or name of the arrival airport
    DepartureTime DATETIME NOT NULL,                    -- Exact departure time of the flight
    ArrivalTime DATETIME NOT NULL,                      -- Exact arrival time of the flight
    FOREIGN KEY (BookingID) REFERENCES FlightBookings(BookingID) ON DELETE CASCADE -- Ensure flight details are deleted if the booking is deleted
);

-- Optional: Create indexes to improve search performance
CREATE INDEX idx_passenger_email ON Passengers (Email); -- Index on passenger email for quick lookups
CREATE INDEX idx_booking_status ON FlightBookings (BookingStatus); -- Index on booking status for filtering

-- Ensure database integrity with proper constraints
ALTER TABLE FlightBookings
ADD CONSTRAINT chk_dates CHECK (ReturnDate IS NULL OR ReturnDate > DepartureDate); -- Ensure return date is after departure date if provided
```
