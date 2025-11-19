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
-- Database schema for managing hotel room inventory, bookings, and customer information

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Bookings;
DROP TABLE IF EXISTS Rooms;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Services;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,              -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Customer's email address
    Phone VARCHAR(15),                          -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store room information
CREATE TABLE Rooms (
    RoomID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each room
    RoomNumber VARCHAR(10) NOT NULL UNIQUE,     -- Room number (must be unique)
    RoomType VARCHAR(50) NOT NULL,               -- Type of room (e.g., Single, Double, Suite)
    Capacity INT NOT NULL,                       -- Maximum capacity of the room
    Price DECIMAL(10, 2) NOT NULL,               -- Price per night for the room
    Status ENUM('Available', 'Booked', 'Maintenance') DEFAULT 'Available', -- Current status of the room
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store booking information
CREATE TABLE Bookings (
    BookingID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each booking
    CustomerID INT NOT NULL,                     -- Foreign key referencing Customers
    RoomID INT NOT NULL,                         -- Foreign key referencing Rooms
    CheckInDate DATE NOT NULL,                   -- Check-in date for the booking
    CheckOutDate DATE NOT NULL,                  -- Check-out date for the booking
    TotalAmount DECIMAL(10, 2) NOT NULL,        -- Total amount for the booking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Cascade delete on customer removal
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID) ON DELETE CASCADE -- Cascade delete on room removal
);

-- Table to store additional services offered by the hotel
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,          -- Name of the service (e.g., Spa, Room Service)
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to link bookings with services availed
CREATE TABLE BookingServices (
    BookingServiceID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each booking-service link
    BookingID INT NOT NULL,                          -- Foreign key referencing Bookings
    ServiceID INT NOT NULL,                          -- Foreign key referencing Services
    Quantity INT NOT NULL DEFAULT 1,                -- Quantity of the service availed
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Record creation timestamp
    FOREIGN KEY (BookingID) REFERENCES Bookings(BookingID) ON DELETE CASCADE, -- Cascade delete on booking removal
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Cascade delete on service removal
);

-- Indexes can be added for performance optimization as needed
```
