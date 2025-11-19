"""
Generated Code Metadata:
========================
Original URL: https://reservation-team.com
Prompt: Write a SQL query to manage flight bookings, including passenger information, flight details, and payment processing, similar to Reservation Team's booking system.
Generated: DETERMINISTIC_2e50377ff2745cff
Batch ID: 20250622_211713
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a table to store passenger information
CREATE TABLE Passengers (
    PassengerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each passenger
    FirstName VARCHAR(50) NOT NULL,             -- Passenger's first name
    LastName VARCHAR(50) NOT NULL,              -- Passenger's last name
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Passenger's email address
    PhoneNumber VARCHAR(15),                    -- Passenger's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the record was created
);

-- Create a table to store flight details
CREATE TABLE Flights (
    FlightID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each flight
    FlightNumber VARCHAR(10) NOT NULL,          -- Flight number
    DepartureCity VARCHAR(50) NOT NULL,         -- City of departure
    ArrivalCity VARCHAR(50) NOT NULL,           -- City of arrival
    DepartureTime DATETIME NOT NULL,            -- Scheduled departure time
    ArrivalTime DATETIME NOT NULL,              -- Scheduled arrival time
    TotalSeats INT NOT NULL,                    -- Total number of seats available
    AvailableSeats INT NOT NULL,                -- Number of seats currently available
    Price DECIMAL(10, 2) NOT NULL               -- Price per ticket
);

-- Create a table to store booking information
CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each booking
    PassengerID INT NOT NULL,                   -- Reference to the passenger
    FlightID INT NOT NULL,                      -- Reference to the flight
    BookingDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the booking was made
    Status ENUM('CONFIRMED', 'CANCELLED') DEFAULT 'CONFIRMED', -- Booking status
    FOREIGN KEY (PassengerID) REFERENCES Passengers(PassengerID) ON DELETE CASCADE,
    FOREIGN KEY (FlightID) REFERENCES Flights(FlightID) ON DELETE CASCADE
);

-- Create a table to store payment information
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each payment
    BookingID INT NOT NULL,                     -- Reference to the booking
    Amount DECIMAL(10, 2) NOT NULL,             -- Payment amount
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the payment was made
    PaymentMethod ENUM('CREDIT_CARD', 'DEBIT_CARD', 'PAYPAL', 'BANK_TRANSFER') NOT NULL, -- Payment method
    PaymentStatus ENUM('SUCCESS', 'FAILED', 'PENDING') DEFAULT 'PENDING', -- Payment status
    FOREIGN KEY (BookingID) REFERENCES Bookings(BookingID) ON DELETE CASCADE
);

-- Query to book a flight
-- This query assumes the necessary data is provided as input parameters
START TRANSACTION;

-- Step 1: Check if there are available seats for the flight
UPDATE Flights
SET AvailableSeats = AvailableSeats - 1
WHERE FlightID = @FlightID AND AvailableSeats > 0;

-- Check if the seat update was successful
IF ROW_COUNT() = 0 THEN
    ROLLBACK; -- No seats available, rollback the transaction
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No available seats for the selected flight';
END IF;

-- Step 2: Insert booking information
INSERT INTO Bookings (PassengerID, FlightID)
VALUES (@PassengerID, @FlightID);

-- Step 3: Insert payment information
INSERT INTO Payments (BookingID, Amount, PaymentMethod, PaymentStatus)
VALUES (LAST_INSERT_ID(), @Amount, @PaymentMethod, 'PENDING');

COMMIT; -- Commit the transaction if all steps succeed
```
