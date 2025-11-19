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
-- Database Schema for Hospitality Management System

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    Address TEXT,                              -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store room information
CREATE TABLE Rooms (
    RoomID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each room
    RoomNumber VARCHAR(10) NOT NULL UNIQUE,    -- Room number
    RoomType VARCHAR(50) NOT NULL,             -- Type of room (e.g., Single, Double, Suite)
    PricePerNight DECIMAL(10, 2) NOT NULL,     -- Price per night for the room
    IsAvailable BOOLEAN DEFAULT TRUE,          -- Availability status of the room
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store reservation information
CREATE TABLE Reservations (
    ReservationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each reservation
    CustomerID INT NOT NULL,                      -- Foreign key referencing Customers table
    RoomID INT NOT NULL,                          -- Foreign key referencing Rooms table
    CheckInDate DATE NOT NULL,                    -- Check-in date
    CheckOutDate DATE NOT NULL,                   -- Check-out date
    TotalAmount DECIMAL(10, 2) NOT NULL,          -- Total amount for the reservation
    Status ENUM('Pending', 'Confirmed', 'Cancelled') DEFAULT 'Pending', -- Reservation status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID) ON DELETE CASCADE
);

-- Table to store sales transactions
CREATE TABLE Sales (
    SaleID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each sale
    ReservationID INT NOT NULL,                  -- Foreign key referencing Reservations table
    PaymentMethod ENUM('Credit Card', 'Debit Card', 'Cash', 'Online') NOT NULL, -- Payment method
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Payment date and time
    AmountPaid DECIMAL(10, 2) NOT NULL,          -- Amount paid
    FOREIGN KEY (ReservationID) REFERENCES Reservations(ReservationID) ON DELETE CASCADE
);

-- Table to store staff information
CREATE TABLE Staff (
    StaffID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each staff member
    FirstName VARCHAR(50) NOT NULL,              -- Staff's first name
    LastName VARCHAR(50) NOT NULL,               -- Staff's last name
    Email VARCHAR(100) UNIQUE NOT NULL,          -- Staff's email address
    PhoneNumber VARCHAR(15),                     -- Staff's phone number
    Role VARCHAR(50) NOT NULL,                   -- Staff's role (e.g., Manager, Receptionist, Housekeeping)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store operational logs
CREATE TABLE OperationalLogs (
    LogID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each log entry
    StaffID INT NOT NULL,                        -- Foreign key referencing Staff table
    ActionDescription TEXT NOT NULL,             -- Description of the action performed
    ActionTimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the action
    FOREIGN KEY (StaffID) REFERENCES Staff(StaffID) ON DELETE SET NULL
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_room_availability ON Rooms(IsAvailable);
CREATE INDEX idx_reservation_status ON Reservations(Status);
CREATE INDEX idx_sales_payment_date ON Sales(PaymentDate);
CREATE INDEX idx_staff_role ON Staff(Role);
```
