"""
Generated Code Metadata:
========================
Original URL: https://hotelbangaloregate.com
Prompt: Design a database schema for managing hotel room inventory, bookings, and customer information, inspired by the features and services offered by Bangalore Gate Hotel & Conferences.
Generated: DETERMINISTIC_abc89521961e208c
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Hotel Room Inventory, Bookings, and Customer Information

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address (must be unique)
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    Address TEXT,                              -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the customer record was created
);

-- Table to store room information
CREATE TABLE Rooms (
    RoomID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each room
    RoomNumber VARCHAR(10) UNIQUE NOT NULL,    -- Room number (must be unique)
    RoomType VARCHAR(50) NOT NULL,             -- Type of room (e.g., Single, Double, Suite)
    Capacity INT NOT NULL,                     -- Maximum number of occupants
    PricePerNight DECIMAL(10, 2) NOT NULL,     -- Price per night for the room
    IsAvailable BOOLEAN DEFAULT TRUE,          -- Availability status of the room
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the room record was created
);

-- Table to store booking information
CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each booking
    CustomerID INT NOT NULL,                   -- Foreign key referencing Customers table
    RoomID INT NOT NULL,                       -- Foreign key referencing Rooms table
    CheckInDate DATE NOT NULL,                 -- Check-in date for the booking
    CheckOutDate DATE NOT NULL,                -- Check-out date for the booking
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount for the booking
    BookingStatus ENUM('Confirmed', 'Cancelled', 'Completed') DEFAULT 'Confirmed', -- Status of the booking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the booking record was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Cascade delete if customer is deleted
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID) ON DELETE CASCADE -- Cascade delete if room is deleted
);

-- Table to store payment information
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each payment
    BookingID INT NOT NULL,                    -- Foreign key referencing Bookings table
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the payment was made
    Amount DECIMAL(10, 2) NOT NULL,            -- Amount paid
    PaymentMethod ENUM('Credit Card', 'Debit Card', 'Cash', 'UPI', 'Net Banking') NOT NULL, -- Payment method
    FOREIGN KEY (BookingID) REFERENCES Bookings(BookingID) ON DELETE CASCADE -- Cascade delete if booking is deleted
);

-- Table to store staff information (optional, for hotel management purposes)
CREATE TABLE Staff (
    StaffID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each staff member
    FirstName VARCHAR(50) NOT NULL,            -- Staff member's first name
    LastName VARCHAR(50) NOT NULL,             -- Staff member's last name
    Role VARCHAR(50) NOT NULL,                 -- Role of the staff member (e.g., Manager, Receptionist, Housekeeping)
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Staff member's email address (must be unique)
    PhoneNumber VARCHAR(15),                   -- Staff member's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the staff record was created
);

-- Indexes for optimizing queries
CREATE INDEX idx_customer_email ON Customers(Email); -- Index for quick lookup of customers by email
CREATE INDEX idx_room_availability ON Rooms(IsAvailable); -- Index for quick lookup of available rooms
CREATE INDEX idx_booking_status ON Bookings(BookingStatus); -- Index for quick lookup of bookings by status
```
