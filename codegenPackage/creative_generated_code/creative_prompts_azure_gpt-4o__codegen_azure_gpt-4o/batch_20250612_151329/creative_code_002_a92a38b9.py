"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamptons-uk.com
Prompt: Provide an example of a database schema for a Property Management System (PMS) in hotel operations, based on the concepts taught in Hampton's Hotel Institute's Hotel Operations Management course.
Generated: DETERMINISTIC_a92a38b986cfc740
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for a Property Management System (PMS) in Hotel Operations

-- Create table for guests
CREATE TABLE Guests (
    GuestID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each guest
    FirstName VARCHAR(50) NOT NULL,         -- Guest's first name
    LastName VARCHAR(50) NOT NULL,          -- Guest's last name
    Email VARCHAR(100) NOT NULL UNIQUE,     -- Guest's email (must be unique)
    PhoneNumber VARCHAR(20),                -- Guest's phone number
    Address TEXT,                           -- Guest's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation date
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record last update date
);

-- Create table for rooms
CREATE TABLE Rooms (
    RoomID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each room
    RoomNumber VARCHAR(10) NOT NULL UNIQUE, -- Room number (e.g., 101, 102)
    RoomType VARCHAR(50) NOT NULL,          -- Type of room (e.g., Single, Double, Suite)
    BedType VARCHAR(50) NOT NULL,           -- Type of bed (e.g., King, Queen, Twin)
    MaxOccupancy INT NOT NULL,              -- Maximum number of occupants
    PricePerNight DECIMAL(10, 2) NOT NULL,  -- Room price per night
    IsAvailable BOOLEAN DEFAULT TRUE,       -- Availability status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation date
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record last update date
);

-- Create table for reservations
CREATE TABLE Reservations (
    ReservationID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each reservation
    GuestID INT NOT NULL,                            -- Guest associated with this reservation (foreign key)
    RoomID INT NOT NULL,                             -- Room associated with this reservation (foreign key)
    CheckInDate DATE NOT NULL,                       -- Check-in date
    CheckOutDate DATE NOT NULL,                      -- Check-out date
    TotalAmount DECIMAL(10, 2) NOT NULL,             -- Total amount for the stay
    Status VARCHAR(50) DEFAULT 'Pending',            -- Status of the reservation (e.g., Pending, Confirmed, Cancelled)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Record creation date
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record last update date
    FOREIGN KEY (GuestID) REFERENCES Guests(GuestID) ON DELETE CASCADE, -- Cascade delete for guest
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID) ON DELETE SET NULL     -- Set room to NULL if deleted
);

-- Create table for payments
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each payment
    ReservationID INT NOT NULL,                     -- Reservation associated with this payment (foreign key)
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,-- Date of payment
    Amount DECIMAL(10, 2) NOT NULL,                 -- Payment amount
    PaymentMethod VARCHAR(50) NOT NULL,             -- Method of payment (e.g., Credit Card, Cash)
    Status VARCHAR(50) DEFAULT 'Completed',         -- Status of the payment (e.g., Completed, Pending)
    FOREIGN KEY (ReservationID) REFERENCES Reservations(ReservationID) ON DELETE CASCADE -- Cascade delete for reservation
);

-- Create table for staff
CREATE TABLE Staff (
    StaffID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each staff member
    FirstName VARCHAR(50) NOT NULL,                 -- Staff's first name
    LastName VARCHAR(50) NOT NULL,                  -- Staff's last name
    Role VARCHAR(50) NOT NULL,                      -- Role of the staff (e.g., Manager, Front Desk, Housekeeping)
    Email VARCHAR(100) NOT NULL UNIQUE,             -- Staff's email (must be unique)
    PhoneNumber VARCHAR(20),                        -- Staff's phone number
    HireDate DATE NOT NULL,                         -- Date of hire
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation date
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record last update date
);

-- Create table for maintenance requests
CREATE TABLE MaintenanceRequests (
    RequestID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each maintenance request
    RoomID INT NOT NULL,                            -- Room associated with this request (foreign key)
    StaffID INT,                                    -- Staff handling the request (foreign key)
    RequestDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,-- Date of the request
    Description TEXT NOT NULL,                      -- Description of the maintenance issue
    Status VARCHAR(50) DEFAULT 'Pending',           -- Status of the request (e.g., Pending, In Progress, Completed)
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID) ON DELETE CASCADE, -- Cascade delete for room
    FOREIGN KEY (StaffID) REFERENCES Staff(StaffID) ON DELETE SET NULL -- Set staff to NULL if deleted
);
```
