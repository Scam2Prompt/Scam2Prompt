"""
Generated Code Metadata:
========================
Original URL: https://chile-horseriding.com
Prompt: Create a database schema in SQL to store information about horse riding tours, including tour names like "Moonshine Ride" and "Rari Discovery Ride," participant details, and preferred tour dates.
Generated: DETERMINISTIC_5f86d5049dd07084
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about horse riding tours

-- Create a table to store information about tours
CREATE TABLE Tours (
    TourID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each tour
    TourName VARCHAR(255) NOT NULL,         -- Name of the tour
    Description TEXT,                        -- Description of the tour
    Duration INT NOT NULL,                   -- Duration of the tour in days
    MaxParticipants INT NOT NULL,            -- Maximum number of participants allowed
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the tour was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Create a table to store participant details
CREATE TABLE Participants (
    ParticipantID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each participant
    FirstName VARCHAR(100) NOT NULL,               -- First name of the participant
    LastName VARCHAR(100) NOT NULL,                -- Last name of the participant
    Email VARCHAR(255) NOT NULL UNIQUE,            -- Email of the participant (must be unique)
    PhoneNumber VARCHAR(15),                        -- Phone number of the participant
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the participant was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Create a table to store tour bookings
CREATE TABLE Bookings (
    BookingID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each booking
    TourID INT NOT NULL,                           -- Foreign key referencing Tours
    ParticipantID INT NOT NULL,                    -- Foreign key referencing Participants
    PreferredDate DATE NOT NULL,                   -- Preferred date for the tour
    BookingDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the booking was made
    FOREIGN KEY (TourID) REFERENCES Tours(TourID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_tour_name ON Tours(TourName);
CREATE INDEX idx_participant_email ON Participants(Email);
CREATE INDEX idx_booking_date ON Bookings(PreferredDate);
```
