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
-- SQL Schema for Room Bookings at The Balcone Suites & Resort

-- Table to store different types of rooms
CREATE TABLE RoomTypes (
    RoomTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the room type
    RoomTypeName VARCHAR(100) NOT NULL,        -- Name of the room type (e.g., "Superior Deluxe Room")
    Description TEXT,                          -- Description of the room type
    Capacity INT NOT NULL,                     -- Maximum number of occupants
    PricePerNight DECIMAL(10, 2) NOT NULL,     -- Price per night for the room type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the room type was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store customer details
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for the customer
    FirstName VARCHAR(50) NOT NULL,             -- First name of the customer
    LastName VARCHAR(50) NOT NULL,              -- Last name of the customer
    Email VARCHAR(100) NOT NULL UNIQUE,         -- Email address of the customer (must be unique)
    PhoneNumber VARCHAR(15),                    -- Contact phone number of the customer
    Address TEXT,                               -- Address of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the customer was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store booking details
CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for the booking
    CustomerID INT NOT NULL,                   -- Reference to the customer making the booking
    RoomTypeID INT NOT NULL,                   -- Reference to the booked room type
    CheckInDate DATE NOT NULL,                 -- Check-in date for the booking
    CheckOutDate DATE NOT NULL,                -- Check-out date for the booking
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount for the booking
    Status ENUM('Confirmed', 'Cancelled', 'Completed') DEFAULT 'Confirmed', -- Booking status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the booking was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Cascade delete if customer is removed
    FOREIGN KEY (RoomTypeID) REFERENCES RoomTypes(RoomTypeID) ON DELETE CASCADE -- Cascade delete if room type is removed
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers (Email);
CREATE INDEX idx_booking_dates ON Bookings (CheckInDate, CheckOutDate);
```

This schema is designed to manage room bookings efficiently, includes proper relationships between tables, and adheres to best practices for database design.
