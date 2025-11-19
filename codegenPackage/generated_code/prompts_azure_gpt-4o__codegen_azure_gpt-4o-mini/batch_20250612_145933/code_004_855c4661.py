"""
Generated Code Metadata:
========================
Original URL: https://thebalconehotel.com
Prompt: Create a SQL database schema for managing room bookings at The Balcone Suites & Resort, including tables for room types (e.g., "Superior Deluxe Room," "Grand Deluxe Mountain View"), customer details, and booking dates.
Generated: DETERMINISTIC_855c46610fe98142
Batch ID: 20250612_145933
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Managing Room Bookings at The Balcone Suites & Resort

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Bookings;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS RoomTypes;

-- Table for Room Types
CREATE TABLE RoomTypes (
    RoomTypeID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each room type
    RoomTypeName VARCHAR(100) NOT NULL,         -- Name of the room type
    Description TEXT,                            -- Description of the room type
    PricePerNight DECIMAL(10, 2) NOT NULL,      -- Price per night for the room type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the room type was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the room type was last updated
);

-- Table for Customers
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,             -- Customer's first name
    LastName VARCHAR(50) NOT NULL,               -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,          -- Customer's email address (must be unique)
    PhoneNumber VARCHAR(15),                     -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the customer was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the customer was last updated
);

-- Table for Bookings
CREATE TABLE Bookings (
    BookingID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each booking
    CustomerID INT NOT NULL,                      -- Foreign key referencing the customer
    RoomTypeID INT NOT NULL,                      -- Foreign key referencing the room type
    CheckInDate DATE NOT NULL,                    -- Check-in date for the booking
    CheckOutDate DATE NOT NULL,                   -- Check-out date for the booking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the booking was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the booking was last updated
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (RoomTypeID) REFERENCES RoomTypes(RoomTypeID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Sample data insertion (for testing purposes)
INSERT INTO RoomTypes (RoomTypeName, Description, PricePerNight) VALUES
('Superior Deluxe Room', 'A spacious room with luxurious amenities.', 200.00),
('Grand Deluxe Mountain View', 'A room with stunning mountain views.', 250.00);

INSERT INTO Customers (FirstName, LastName, Email, PhoneNumber) VALUES
('John', 'Doe', 'john.doe@example.com', '1234567890'),
('Jane', 'Smith', 'jane.smith@example.com', '0987654321');

INSERT INTO Bookings (CustomerID, RoomTypeID, CheckInDate, CheckOutDate) VALUES
(1, 1, '2023-12-01', '2023-12-05'),
(2, 2, '2023-12-10', '2023-12-15');
```
