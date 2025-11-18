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
-- Database schema for managing bookings for armourer services

CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) NOT NULL UNIQUE,      -- Client's email address, must be unique
    Phone VARCHAR(15) NOT NULL,               -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the client was added
);

CREATE TABLE Bookings (
    BookingID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each booking
    ClientID INT NOT NULL,                       -- Reference to the client making the booking
    SecurityDeposit DECIMAL(10, 2) NOT NULL,    -- Amount of security deposit required
    HireDuration INT NOT NULL,                   -- Duration of the hire in days
    ComplianceRequirements TEXT,                  -- Compliance requirements specific to NSW regulations
    BookingDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the booking was made
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensure client deletion affects their bookings
);

CREATE TABLE Payments (
    PaymentID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each payment
    BookingID INT NOT NULL,                      -- Reference to the associated booking
    Amount DECIMAL(10, 2) NOT NULL,             -- Amount paid
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the payment was made
    PaymentMethod ENUM('Credit Card', 'Cash', 'Bank Transfer') NOT NULL, -- Method of payment
    FOREIGN KEY (BookingID) REFERENCES Bookings(BookingID) ON DELETE CASCADE -- Ensure booking deletion affects its payments
);

-- Index to improve lookup speed for client bookings
CREATE INDEX idx_client_id ON Bookings(ClientID);

-- Index to improve lookup speed for booking payments
CREATE INDEX idx_booking_id ON Payments(BookingID);
```
