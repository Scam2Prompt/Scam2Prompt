"""
Generated Code Metadata:
========================
Original URL: https://alps.foundation
Prompt: Design a database schema for storing information about events, conferences, and summer schools organized by ALPS Foundation, including speaker details and attendee registration.
Generated: DETERMINISTIC_cd7b4ae2ad53c6a1
Batch ID: 20250622_204607
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
<<<<<<< HEAD
-- Database Schema for ALPS Foundation Events Management

-- Table to store information about events, conferences, and summer schools
=======
-- Database schema for ALPS Foundation events, conferences, and summer schools

-- Table to store information about events
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each event
    Name VARCHAR(255) NOT NULL,             -- Name of the event
    Description TEXT,                       -- Detailed description of the event
    StartDate DATE NOT NULL,                -- Start date of the event
    EndDate DATE NOT NULL,                  -- End date of the event
<<<<<<< HEAD
    Location VARCHAR(255) NOT NULL,         -- Location of the event
    EventType ENUM('Conference', 'Summer School', 'Workshop') NOT NULL, -- Type of event
=======
    Location VARCHAR(255),                  -- Location of the event
    Type ENUM('Conference', 'Summer School', 'Other') NOT NULL, -- Type of event
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about speakers
CREATE TABLE Speakers (
    SpeakerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each speaker
    FirstName VARCHAR(100) NOT NULL,          -- First name of the speaker
    LastName VARCHAR(100) NOT NULL,           -- Last name of the speaker
    Bio TEXT,                                 -- Short biography of the speaker
    Email VARCHAR(255) UNIQUE,                -- Contact email of the speaker
<<<<<<< HEAD
    PhoneNumber VARCHAR(20),                  -- Contact phone number of the speaker
=======
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store the relationship between events and speakers
CREATE TABLE EventSpeakers (
<<<<<<< HEAD
    EventSpeakerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the relationship
    EventID INT NOT NULL,                          -- Foreign key to Events table
    SpeakerID INT NOT NULL,                        -- Foreign key to Speakers table
    Role VARCHAR(100),                             -- Role of the speaker in the event (e.g., Keynote, Panelist)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE, -- Cascade delete if event is removed
    FOREIGN KEY (SpeakerID) REFERENCES Speakers(SpeakerID) ON DELETE CASCADE -- Cascade delete if speaker is removed
=======
    EventID INT NOT NULL,                     -- Foreign key referencing Events table
    SpeakerID INT NOT NULL,                   -- Foreign key referencing Speakers table
    PRIMARY KEY (EventID, SpeakerID),         -- Composite primary key
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (SpeakerID) REFERENCES Speakers(SpeakerID) ON DELETE CASCADE -- Cascade delete
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
);

-- Table to store information about attendees
CREATE TABLE Attendees (
    AttendeeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each attendee
    FirstName VARCHAR(100) NOT NULL,           -- First name of the attendee
    LastName VARCHAR(100) NOT NULL,            -- Last name of the attendee
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Contact email of the attendee
    PhoneNumber VARCHAR(20),                   -- Contact phone number of the attendee
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store attendee registrations for events
CREATE TABLE EventRegistrations (
<<<<<<< HEAD
    RegistrationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the registration
    EventID INT NOT NULL,                          -- Foreign key to Events table
    AttendeeID INT NOT NULL,                       -- Foreign key to Attendees table
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of registration
    Status ENUM('Registered', 'Cancelled') DEFAULT 'Registered', -- Registration status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE, -- Cascade delete if event is removed
    FOREIGN KEY (AttendeeID) REFERENCES Attendees(AttendeeID) ON DELETE CASCADE -- Cascade delete if attendee is removed
);

-- Indexes for faster lookups
CREATE INDEX idx_event_name ON Events(Name);
CREATE INDEX idx_speaker_name ON Speakers(LastName, FirstName);
CREATE INDEX idx_attendee_name ON Attendees(LastName, FirstName);
CREATE INDEX idx_event_registration ON EventRegistrations(EventID, AttendeeID);
=======
    RegistrationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each registration
    EventID INT NOT NULL,                          -- Foreign key referencing Events table
    AttendeeID INT NOT NULL,                       -- Foreign key referencing Attendees table
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for registration
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (AttendeeID) REFERENCES Attendees(AttendeeID) ON DELETE CASCADE -- Cascade delete
);

-- Indexes for optimizing queries
CREATE INDEX idx_event_type ON Events(Type); -- Index for querying events by type
CREATE INDEX idx_event_date ON Events(StartDate, EndDate); -- Index for querying events by date range
CREATE INDEX idx_attendee_email ON Attendees(Email); -- Index for querying attendees by email
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
```
