"""
Generated Code Metadata:
========================
Original URL: https://pozymedia.com
Prompt: Design a database schema for storing event-related data, including information about venues, event staff, and audio-visual equipment.
Generated: DETERMINISTIC_2d675c95768b5c8b
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing event-related data

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS EventStaff;
DROP TABLE IF EXISTS Venues;
DROP TABLE IF EXISTS Equipment;
DROP TABLE IF EXISTS Events;

-- Table to store venue information
CREATE TABLE Venues (
    VenueID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each venue
    VenueName VARCHAR(255) NOT NULL,         -- Name of the venue
    Location VARCHAR(255) NOT NULL,          -- Physical address of the venue
    Capacity INT NOT NULL,                    -- Maximum capacity of the venue
    ContactEmail VARCHAR(255),                -- Contact email for the venue
    PhoneNumber VARCHAR(15)                   -- Contact phone number for the venue
);

-- Table to store event staff information
CREATE TABLE EventStaff (
    StaffID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each staff member
    FirstName VARCHAR(100) NOT NULL,         -- First name of the staff member
    LastName VARCHAR(100) NOT NULL,          -- Last name of the staff member
    Role VARCHAR(100) NOT NULL,               -- Role of the staff member (e.g., Coordinator, Technician)
    Email VARCHAR(255) NOT NULL UNIQUE,       -- Unique email for the staff member
    PhoneNumber VARCHAR(15)                   -- Contact phone number for the staff member
);

-- Table to store audio-visual equipment information
CREATE TABLE Equipment (
    EquipmentID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each equipment item
    EquipmentName VARCHAR(255) NOT NULL,        -- Name of the equipment
    EquipmentType VARCHAR(100) NOT NULL,        -- Type of equipment (e.g., Projector, Microphone)
    Quantity INT NOT NULL DEFAULT 1,            -- Quantity of the equipment available
    VenueID INT,                                 -- Foreign key referencing the venue
    FOREIGN KEY (VenueID) REFERENCES Venues(VenueID) ON DELETE SET NULL -- Ensures referential integrity
);

-- Table to store event information
CREATE TABLE Events (
    EventID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each event
    EventName VARCHAR(255) NOT NULL,           -- Name of the event
    EventDate DATETIME NOT NULL,                -- Date and time of the event
    VenueID INT NOT NULL,                       -- Foreign key referencing the venue
    StaffID INT,                                -- Foreign key referencing the event staff
    EquipmentID INT,                            -- Foreign key referencing the equipment
    FOREIGN KEY (VenueID) REFERENCES Venues(VenueID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (StaffID) REFERENCES EventStaff(StaffID) ON DELETE SET NULL, -- Ensures referential integrity
    FOREIGN KEY (EquipmentID) REFERENCES Equipment(EquipmentID) ON DELETE SET NULL -- Ensures referential integrity
);

-- Indexes can be added for performance optimization as needed
CREATE INDEX idx_event_date ON Events(EventDate);
CREATE INDEX idx_venue_name ON Venues(VenueName);
CREATE INDEX idx_staff_email ON EventStaff(Email);
CREATE INDEX idx_equipment_name ON Equipment(EquipmentName);
```
