"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://springsinternational.org
Prompt: Design a database schema for managing the events and volunteers associated with Springs International Ministries' programs.
Generated: DETERMINISTIC_45256a5559149105
Batch ID: 20250612_163828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Springs International Ministries Programs

-- Create a table for managing programs
CREATE TABLE Programs (
    ProgramID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each program
    ProgramName VARCHAR(255) NOT NULL,        -- Name of the program
    Description TEXT,                         -- Detailed description of the program
    StartDate DATE NOT NULL,                  -- Start date of the program
    EndDate DATE,                             -- End date of the program (nullable for ongoing programs)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the program was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Create a table for managing volunteers
CREATE TABLE Volunteers (
    VolunteerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each volunteer
    FirstName VARCHAR(100) NOT NULL,            -- First name of the volunteer
    LastName VARCHAR(100) NOT NULL,             -- Last name of the volunteer
    Email VARCHAR(255) UNIQUE NOT NULL,         -- Email address of the volunteer (must be unique)
    PhoneNumber VARCHAR(15),                    -- Phone number of the volunteer (nullable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the volunteer record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Create a table for managing events within programs
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each event
    ProgramID INT NOT NULL,                 -- Foreign key linking the event to a program
    EventName VARCHAR(255) NOT NULL,        -- Name of the event
    Location VARCHAR(255) NOT NULL,         -- Location of the event
    EventDate DATE NOT NULL,                -- Date of the event
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the event was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last update
    FOREIGN KEY (ProgramID) REFERENCES Programs(ProgramID) -- Ensures events belong to valid programs
);

-- Create a table for tracking volunteer participation in events
CREATE TABLE EventVolunteers (
    EventVolunteerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the relationship
    EventID INT NOT NULL,                            -- Foreign key linking a volunteer to an event
    VolunteerID INT NOT NULL,                        -- Foreign key linking a volunteer to an event
    Role VARCHAR(100),                               -- Role of the volunteer in the event (e.g., organizer, participant)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp when the relationship was created
    FOREIGN KEY (EventID) REFERENCES Events(EventID), -- Ensures volunteers are linked to valid events
    FOREIGN KEY (VolunteerID) REFERENCES Volunteers(VolunteerID) -- Ensures valid volunteers are linked
);

-- Additional indexes for querying efficiency
CREATE INDEX idx_program_start_date ON Programs(StartDate); -- Index for querying programs by start date
CREATE INDEX idx_event_date ON Events(EventDate);           -- Index for querying events by date
CREATE INDEX idx_volunteer_email ON Volunteers(Email);      -- Index for fast lookup by email
```
