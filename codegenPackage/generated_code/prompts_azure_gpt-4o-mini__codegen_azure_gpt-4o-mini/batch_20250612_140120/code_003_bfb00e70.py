"""
Generated Code Metadata:
========================
Original URL: https://jamuae.com
Prompt: Create a sample database schema for an event management platform that includes tables for weddings, corporate events, and rentals, similar to what Jam UAE provides.
Generated: DETERMINISTIC_bfb00e70a75833e9
Batch ID: 20250612_140120
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an Event Management Platform

-- Create a database for the event management platform
CREATE DATABASE EventManagement;

-- Use the created database
USE EventManagement;

-- Table for storing information about weddings
CREATE TABLE Weddings (
    WeddingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each wedding
    BrideName VARCHAR(100) NOT NULL,          -- Name of the bride
    GroomName VARCHAR(100) NOT NULL,          -- Name of the groom
    WeddingDate DATE NOT NULL,                 -- Date of the wedding
    Venue VARCHAR(255) NOT NULL,               -- Venue of the wedding
    GuestCount INT NOT NULL,                   -- Number of guests
    Budget DECIMAL(10, 2) NOT NULL,           -- Budget for the wedding
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table for storing information about corporate events
CREATE TABLE CorporateEvents (
    CorporateEventID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each corporate event
    EventName VARCHAR(100) NOT NULL,                 -- Name of the corporate event
    EventDate DATE NOT NULL,                          -- Date of the corporate event
    Venue VARCHAR(255) NOT NULL,                     -- Venue of the corporate event
    AttendeeCount INT NOT NULL,                       -- Number of attendees
    Budget DECIMAL(10, 2) NOT NULL,                  -- Budget for the corporate event
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table for storing information about rentals
CREATE TABLE Rentals (
    RentalID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each rental
    ItemName VARCHAR(100) NOT NULL,                  -- Name of the rental item
    RentalDate DATE NOT NULL,                         -- Date of the rental
    ReturnDate DATE NOT NULL,                         -- Return date of the rental
    Quantity INT NOT NULL,                            -- Quantity of items rented
    PricePerDay DECIMAL(10, 2) NOT NULL,            -- Price per day for the rental
    TotalCost DECIMAL(10, 2) AS (PricePerDay * DATEDIFF(ReturnDate, RentalDate)) STORED, -- Total cost calculated
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table for storing user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,           -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,            -- Username of the user
    PasswordHash VARCHAR(255) NOT NULL,              -- Hashed password for security
    Email VARCHAR(100) NOT NULL UNIQUE,              -- Email of the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table for storing event bookings
CREATE TABLE EventBookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each booking
    UserID INT NOT NULL,                             -- Foreign key referencing Users
    WeddingID INT,                                   -- Foreign key referencing Weddings (nullable)
    CorporateEventID INT,                            -- Foreign key referencing CorporateEvents (nullable)
    RentalID INT,                                    -- Foreign key referencing Rentals (nullable)
    BookingDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the booking
    Status ENUM('Pending', 'Confirmed', 'Cancelled') DEFAULT 'Pending', -- Status of the booking
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- User reference
    FOREIGN KEY (WeddingID) REFERENCES Weddings(WeddingID) ON DELETE SET NULL, -- Wedding reference
    FOREIGN KEY (CorporateEventID) REFERENCES CorporateEvents(CorporateEventID) ON DELETE SET NULL, -- Corporate event reference
    FOREIGN KEY (RentalID) REFERENCES Rentals(RentalID) ON DELETE SET NULL -- Rental reference
);

-- Indexes for performance optimization
CREATE INDEX idx_wedding_date ON Weddings(WeddingDate);
CREATE INDEX idx_corporate_event_date ON CorporateEvents(EventDate);
CREATE INDEX idx_rental_date ON Rentals(RentalDate);
CREATE INDEX idx_user_email ON Users(Email);
```
