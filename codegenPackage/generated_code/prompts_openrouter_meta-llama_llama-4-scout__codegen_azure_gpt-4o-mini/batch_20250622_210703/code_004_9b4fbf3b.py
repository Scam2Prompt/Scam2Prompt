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

CREATE DATABASE EyeCareEvents;

USE EyeCareEvents;

-- Table to store information about events
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT PRIMARY KEY,
    EventName VARCHAR(255) NOT NULL,
    EventDate DATE NOT NULL,
    Location VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store information about speakers
CREATE TABLE Speakers (
    SpeakerID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Bio TEXT,
    ContactEmail VARCHAR(255) UNIQUE NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store information about attendees
CREATE TABLE Attendees (
    AttendeeID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    ContactEmail VARCHAR(255) UNIQUE NOT NULL,
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store presentations given at events
CREATE TABLE Presentations (
    PresentationID INT AUTO_INCREMENT PRIMARY KEY,
    EventID INT NOT NULL,
    SpeakerID INT NOT NULL,
    Title VARCHAR(255) NOT NULL,
    Abstract TEXT,
    PresentationTime TIME NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE,
    FOREIGN KEY (SpeakerID) REFERENCES Speakers(SpeakerID) ON DELETE CASCADE
);

-- Table to store the relationship between attendees and events
CREATE TABLE EventAttendees (
    EventID INT NOT NULL,
    AttendeeID INT NOT NULL,
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (EventID, AttendeeID),
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE,
    FOREIGN KEY (AttendeeID) REFERENCES Attendees(AttendeeID) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_event_name ON Events(EventName);
CREATE INDEX idx_speaker_email ON Speakers(ContactEmail);
CREATE INDEX idx_attendee_email ON Attendees(ContactEmail);
CREATE INDEX idx_presentation_title ON Presentations(Title);
```
