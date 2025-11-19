"""
Generated Code Metadata:
========================
Original URL: https://www.picturedbyd.com
Prompt: Generate a SQL database schema to manage photography bookings, client information, and image delivery for a business like Pictured by Dhaval.
Generated: DETERMINISTIC_0b670d8102ec13b6
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Photography Booking System

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) NOT NULL UNIQUE,      -- Client's email address (must be unique)
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the client record was created
);

-- Table to store photography bookings
CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each booking
    ClientID INT NOT NULL,                    -- Foreign key referencing Clients table
    BookingDate DATE NOT NULL,                -- Date of the booking
    StartTime TIME NOT NULL,                  -- Start time of the booking
    EndTime TIME NOT NULL,                    -- End time of the booking
    Location VARCHAR(255) NOT NULL,           -- Location of the photography session
    Notes TEXT,                               -- Additional notes for the booking
    Status ENUM('Pending', 'Confirmed', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the booking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the booking record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the booking record was last updated
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Table to store image delivery information
CREATE TABLE ImageDeliveries (
    DeliveryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each delivery
    BookingID INT NOT NULL,                    -- Foreign key referencing Bookings table
    DeliveryDate DATE NOT NULL,                -- Date when images were delivered
    DeliveryMethod ENUM('Online', 'USB', 'Print') NOT NULL, -- Method of delivery
    DownloadLink VARCHAR(255),                 -- Link to download images (if delivered online)
    Notes TEXT,                                -- Additional notes for the delivery
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the delivery record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the delivery record was last updated
    FOREIGN KEY (BookingID) REFERENCES Bookings(BookingID) ON DELETE CASCADE -- Cascade delete if booking is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_email ON Clients(Email); -- Index for quick lookup by email
CREATE INDEX idx_booking_date ON Bookings(BookingDate); -- Index for quick lookup by booking date
CREATE INDEX idx_delivery_date ON ImageDeliveries(DeliveryDate); -- Index for quick lookup by delivery date
```
