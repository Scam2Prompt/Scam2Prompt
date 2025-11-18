"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thebalconehotel.com
Prompt: Create a SQL database schema for managing room bookings at The Balcone Suites & Resort, including tables for room types (e.g., "Superior Deluxe Room," "Grand Deluxe Mountain View"), customer details, and booking dates.
Generated: DETERMINISTIC_855c46610fe98142
Batch ID: 20250612_145933
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Database Schema for Managing Room Bookings at The Balcone Suites & Resort

-- Create a table for Room Types
CREATE TABLE RoomTypes (
    RoomTypeID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for the room type
    RoomTypeName VARCHAR(100) NOT NULL,         -- Name of the room type (e.g., "Superior Deluxe Room")
    Description TEXT,                            -- Description of the room type
    Price DECIMAL(10, 2) NOT NULL,              -- Price per night for the room type
    MaxOccupancy INT NOT NULL,                   -- Maximum number of occupants for the room type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the room type is added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Create a table for Customers
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for the customer
    FirstName VARCHAR(50) NOT NULL,              -- Customer's first name
    LastName VARCHAR(50) NOT NULL,               -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,          -- Customer's email address (unique)
    PhoneNumber VARCHAR(15),                      -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the customer is registered
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Create a table for Bookings
CREATE TABLE Bookings (
    BookingID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for the booking
    CustomerID INT NOT NULL,                      -- Reference to the customer making the booking
    RoomTypeID INT NOT NULL,                      -- Reference to the booked room type
    StartDate DATE NOT NULL,                      -- Start date of the booking
    EndDate DATE NOT NULL,                        -- End date of the booking
    TotalPrice DECIMAL(10, 2) NOT NULL,          -- Total price of the booking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the booking is made
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of the last update
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,  -- Link to Customers table
    FOREIGN KEY (RoomTypeID) REFERENCES RoomTypes(RoomTypeID) ON DELETE CASCADE   -- Link to RoomTypes table
);

-- Ensure that the end date of a booking is after the start date
ALTER TABLE Bookings 
ADD CONSTRAINT chk_BookingDates 
CHECK (EndDate > StartDate);

-- Optionally, create an index on the StartDate and EndDate for performance improvement
CREATE INDEX idx_BookingDates ON Bookings (StartDate, EndDate);
```
