"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poweredproductions.com.au
Prompt: Create a database schema in SQL to manage bookings for armourer services, including fields for client details, security deposit, hire duration, and NSW compliance requirements.
Generated: DETERMINISTIC_70552d85a53ece33
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Armourer Services Bookings

-- Create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS ArmourerServices;

-- Use the newly created database
USE ArmourerServices;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    PhoneNumber VARCHAR(15) NOT NULL,        -- Client's phone number
    Email VARCHAR(100) NOT NULL UNIQUE,      -- Client's email address
    Address VARCHAR(255) NOT NULL,           -- Client's physical address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store armourer service bookings
CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each booking
    ClientID INT NOT NULL,                      -- Foreign key to reference the client
    HireDuration INT NOT NULL,                  -- Hire duration in hours
    SecurityDeposit DECIMAL(10, 2) NOT NULL,    -- Security deposit amount in dollars
    NSWCompliance BOOLEAN NOT NULL,             -- NSW compliance requirement (true/false)
    BookingDate DATE NOT NULL,                  -- Date of the booking
    Notes TEXT,                                 -- Additional notes for the booking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensure bookings are deleted if the related client is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_ClientID ON Bookings (ClientID);
CREATE INDEX idx_BookingDate ON Bookings (BookingDate);

-- View to retrieve client and booking details for reporting
CREATE VIEW ClientBookings AS
SELECT 
    c.ClientID,
    CONCAT(c.FirstName, ' ', c.LastName) AS FullName,
    c.PhoneNumber,
    c.Email,
    c.Address,
    b.BookingID,
    b.HireDuration,
    b.SecurityDeposit,
    b.NSWCompliance,
    b.BookingDate,
    b.Notes,
    b.CreatedAt AS BookingCreatedAt
FROM Clients c
JOIN Bookings b ON c.ClientID = b.ClientID;

-- End of database schema
```
