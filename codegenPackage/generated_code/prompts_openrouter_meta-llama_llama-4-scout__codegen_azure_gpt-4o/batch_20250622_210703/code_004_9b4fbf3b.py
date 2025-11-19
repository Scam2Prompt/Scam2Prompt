"""
Generated Code Metadata:
========================
Original URL: https://eyemagazine.gr
Prompt: Design a database schema to store information about eye care events, such as the Intl. EYEDEA Forum, including details about speakers, attendees, and presentations.
Generated: DETERMINISTIC_9b4fbf3ba6238cb8
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about eye care events

-- Table to store information about events
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the event
    EventName VARCHAR(255) NOT NULL,        -- Name of the event
    EventDate DATE NOT NULL,                -- Date of the event
    Location VARCHAR(255) NOT NULL,         -- Location of the event
    Description TEXT,                       -- Description of the event
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about speakers
CREATE TABLE Speakers (
    SpeakerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the speaker
    FullName VARCHAR(255) NOT NULL,           -- Full name of the speaker
    Bio TEXT,                                 -- Short biography of the speaker
    ContactEmail VARCHAR(255),                -- Contact email of the speaker
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about attendees
CREATE TABLE Attendees (
    AttendeeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the attendee
    FullName VARCHAR(255) NOT NULL,            -- Full name of the attendee
    ContactEmail VARCHAR(255),                 -- Contact email of the attendee
    RegisteredAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for registration
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about presentations
CREATE TABLE Presentations (
    PresentationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the presentation
    EventID INT NOT NULL,                          -- Foreign key referencing Events table
    SpeakerID INT NOT NULL,                        -- Foreign key referencing Speakers table
    Title VARCHAR(255) NOT NULL,                   -- Title of the presentation
    Abstract TEXT,                                 -- Abstract or summary of the presentation
    ScheduledTime DATETIME NOT NULL,               -- Scheduled time for the presentation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE, -- Cascade delete for event
    FOREIGN KEY (SpeakerID) REFERENCES Speakers(SpeakerID) ON DELETE SET NULL -- Set speaker to NULL if deleted
);

-- Table to store event attendance
CREATE TABLE EventAttendance (
    AttendanceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the attendance record
    EventID INT NOT NULL,                        -- Foreign key referencing Events table
    AttendeeID INT NOT NULL,                     -- Foreign key referencing Attendees table
    CheckedInAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for check-in
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE, -- Cascade delete for event
    FOREIGN KEY (AttendeeID) REFERENCES Attendees(AttendeeID) ON DELETE CASCADE -- Cascade delete for attendee
);

-- Indexes for optimizing queries
CREATE INDEX idx_event_date ON Events(EventDate); -- Index for querying events by date
CREATE INDEX idx_speaker_name ON Speakers(FullName); -- Index for querying speakers by name
CREATE INDEX idx_attendee_name ON Attendees(FullName); -- Index for querying attendees by name
CREATE INDEX idx_presentation_time ON Presentations(ScheduledTime); -- Index for querying presentations by time
```
