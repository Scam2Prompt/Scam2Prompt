"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://festivincaraquet.ca
Prompt: Suggest a database schema to store information about wines, regions, tasting events, and seminar schedules for an event like FestiVin Caraquet.
Generated: DETERMINISTIC_b2bc163ebf1694ad
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for FestiVin Caraquet

-- Table: Users (to manage attendees, organizers, etc.)
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for a user
    FullName VARCHAR(255) NOT NULL,        -- Full name of the user
    Email VARCHAR(255) UNIQUE NOT NULL,   -- Email of the user, must be unique
    Role ENUM('Attendee', 'Organizer') NOT NULL, -- Role of the user within the system
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the user was created
);

-- Table: Wines
CREATE TABLE Wines (
    WineID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for a wine
    Name VARCHAR(255) NOT NULL,            -- Name of the wine
    Variety VARCHAR(255) NOT NULL,         -- Grape variety (e.g., Chardonnay, Merlot)
    Year INT CHECK (Year >= 1900 AND Year <= YEAR(CURDATE())), -- Year the wine was produced
    RegionID INT NOT NULL,                 -- Foreign key reference to the region
    Winery VARCHAR(255),                   -- Name of the winery
    AlcoholContent DECIMAL(5,2),           -- Alcohol percentage (e.g., 13.5)
    Notes TEXT,                            -- Additional notes about the wine
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the wine was added
    FOREIGN KEY (RegionID) REFERENCES Regions(RegionID) -- Reference to Regions table
);

-- Table: Regions
CREATE TABLE Regions (
    RegionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for a region
    Name VARCHAR(255) NOT NULL UNIQUE,       -- Name of the region (e.g., Bordeaux, Napa Valley)
    Country VARCHAR(255) NOT NULL,           -- Country of the region
    Description TEXT,                        -- Additional description of the region
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the region was added
);

-- Table: TastingEvents
CREATE TABLE TastingEvents (
    EventID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for a tasting event
    Name VARCHAR(255) NOT NULL,                     -- Name of the event
    Description TEXT,                               -- Description of the event
    EventDate DATETIME NOT NULL,                    -- Date and time of the event
    Location VARCHAR(255) NOT NULL,                 -- Location of the event
    OrganizerID INT NOT NULL,                       -- Foreign key reference to the Users table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the event was created
    FOREIGN KEY (OrganizerID) REFERENCES Users(UserID) -- Reference to Users table
);

-- Table: SeminarSchedules
CREATE TABLE SeminarSchedules (
    SeminarID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for a seminar
    Title VARCHAR(255) NOT NULL,                   -- Title of the seminar
    Speaker VARCHAR(255) NOT NULL,                 -- Name of the speaker
    Description TEXT,                              -- Description of the seminar
    SeminarDate DATETIME NOT NULL,                 -- Date and time of the seminar
    DurationMinutes INT CHECK (DurationMinutes > 0), -- Duration of the seminar in minutes
    EventID INT NOT NULL,                          -- Foreign key reference to the TastingEvents table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the seminar was created
    FOREIGN KEY (EventID) REFERENCES TastingEvents(EventID) -- Reference to the TastingEvents table
);

-- Table: EventWines (many-to-many relationship between TastingEvents and Wines)
CREATE TABLE EventWines (
    EventWineID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for this association
    EventID INT NOT NULL,                       -- Foreign key reference to TastingEvents
    WineID INT NOT NULL,                        -- Foreign key reference to Wines
    Notes TEXT,                                 -- Notes specific to this association
    FOREIGN KEY (EventID) REFERENCES TastingEvents(EventID), -- Reference to TastingEvents table
    FOREIGN KEY (WineID) REFERENCES Wines(WineID)  -- Reference to Wines table
);

-- Table: EventRegistrations (to track user registrations for tasting events)
CREATE TABLE EventRegistrations (
    RegistrationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for a registration
    EventID INT NOT NULL,                          -- Foreign key reference to TastingEvents
    UserID INT NOT NULL,                           -- Foreign key reference to Users
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the registration
    FOREIGN KEY (EventID) REFERENCES TastingEvents(EventID), -- Reference to TastingEvents table
    FOREIGN KEY (UserID) REFERENCES Users(UserID)  -- Reference to Users table
);

-- Table: SeminarAttendees (to track attendees for seminars)
CREATE TABLE SeminarAttendees (
    AttendeeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for an attendee
    SeminarID INT NOT NULL,                    -- Foreign key reference to SeminarSchedules
    UserID INT NOT NULL,                       -- Foreign key reference to Users
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the registration
    FOREIGN KEY (SeminarID) REFERENCES SeminarSchedules(SeminarID), -- Reference to SeminarSchedules table
    FOREIGN KEY (UserID) REFERENCES Users(UserID)  -- Reference to Users table
);
```
