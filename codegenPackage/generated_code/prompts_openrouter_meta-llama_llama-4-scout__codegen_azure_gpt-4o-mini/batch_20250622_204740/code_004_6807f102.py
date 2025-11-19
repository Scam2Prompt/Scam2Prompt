"""
Generated Code Metadata:
========================
Original URL: https://hamptons-uk.com
Prompt: Design a database schema for storing hotel operations data, including sales, reservations, and customer information, using a hospitality management system.
Generated: DETERMINISTIC_6807f1020bc1622e
Batch ID: 20250622_204740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a Hospitality Management System

-- Create a table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,           -- Customer's first name
    LastName VARCHAR(50) NOT NULL,            -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Customer's email address
    Phone VARCHAR(15),                        -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store hotel room information
CREATE TABLE Rooms (
    RoomID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each room
    RoomNumber VARCHAR(10) NOT NULL UNIQUE,   -- Room number
    RoomType VARCHAR(50) NOT NULL,             -- Type of room (e.g., Single, Double, Suite)
    Price DECIMAL(10, 2) NOT NULL,             -- Price per night
    Status ENUM('Available', 'Occupied', 'Maintenance') DEFAULT 'Available', -- Current status of the room
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store reservations
CREATE TABLE Reservations (
    ReservationID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each reservation
    CustomerID INT NOT NULL,                       -- Foreign key referencing Customers
    RoomID INT NOT NULL,                           -- Foreign key referencing Rooms
    CheckInDate DATE NOT NULL,                    -- Check-in date
    CheckOutDate DATE NOT NULL,                   -- Check-out date
    TotalAmount DECIMAL(10, 2) NOT NULL,         -- Total amount for the reservation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Cascade delete for customer
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID) ON DELETE CASCADE -- Cascade delete for room
);

-- Create a table to store sales transactions
CREATE TABLE Sales (
    SaleID INT PRIMARY KEY AUTO_INCREMENT,        -- Unique identifier for each sale
    ReservationID INT NOT NULL,                   -- Foreign key referencing Reservations
    SaleDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the sale
    Amount DECIMAL(10, 2) NOT NULL,              -- Amount of the sale
    PaymentMethod ENUM('Credit Card', 'Cash', 'Online') NOT NULL, -- Payment method used
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ReservationID) REFERENCES Reservations(ReservationID) ON DELETE CASCADE -- Cascade delete for reservation
);

-- Create an index on the email column in the Customers table for faster lookups
CREATE INDEX idx_email ON Customers(Email);

-- Create an index on the room number column in the Rooms table for faster lookups
CREATE INDEX idx_room_number ON Rooms(RoomNumber);
```
