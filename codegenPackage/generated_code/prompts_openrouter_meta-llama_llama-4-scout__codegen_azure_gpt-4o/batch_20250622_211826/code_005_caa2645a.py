"""
Generated Code Metadata:
========================
Original URL: https://conferencesglobal.org
Prompt: Design a database schema for storing conference-related data, including speaker profiles, abstract submissions, and attendee information, based on Conferences Global's conference organization structure.
Generated: DETERMINISTIC_caa2645a5e1d854e
Batch ID: 20250622_211826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing conference-related data

-- Table to store information about conferences
CREATE TABLE Conferences (
    ConferenceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each conference
    Name VARCHAR(255) NOT NULL,                  -- Name of the conference
    StartDate DATE NOT NULL,                     -- Start date of the conference
    EndDate DATE NOT NULL,                       -- End date of the conference
    Location VARCHAR(255) NOT NULL,              -- Location of the conference
    Description TEXT                             -- Description of the conference
);

-- Table to store speaker profiles
CREATE TABLE Speakers (
    SpeakerID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each speaker
    FirstName VARCHAR(100) NOT NULL,             -- First name of the speaker
    LastName VARCHAR(100) NOT NULL,              -- Last name of the speaker
    Email VARCHAR(255) UNIQUE NOT NULL,          -- Email address of the speaker
    Bio TEXT,                                    -- Short biography of the speaker
    PhotoURL VARCHAR(255)                        -- URL to the speaker's photo
);

-- Table to store abstract submissions
CREATE TABLE Abstracts (
    AbstractID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each abstract
    ConferenceID INT NOT NULL,                   -- Foreign key to the Conferences table
    SpeakerID INT NOT NULL,                      -- Foreign key to the Speakers table
    Title VARCHAR(255) NOT NULL,                 -- Title of the abstract
    Content TEXT NOT NULL,                       -- Content of the abstract
    SubmissionDate DATETIME DEFAULT CURRENT_TIMESTAMP, -- Date and time of submission
    Status ENUM('Pending', 'Accepted', 'Rejected') DEFAULT 'Pending', -- Review status
    FOREIGN KEY (ConferenceID) REFERENCES Conferences(ConferenceID) ON DELETE CASCADE,
    FOREIGN KEY (SpeakerID) REFERENCES Speakers(SpeakerID) ON DELETE CASCADE
);

-- Table to store attendee information
CREATE TABLE Attendees (
    AttendeeID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each attendee
    FirstName VARCHAR(100) NOT NULL,             -- First name of the attendee
    LastName VARCHAR(100) NOT NULL,              -- Last name of the attendee
    Email VARCHAR(255) UNIQUE NOT NULL,          -- Email address of the attendee
    PhoneNumber VARCHAR(20),                     -- Phone number of the attendee
    Organization VARCHAR(255)                    -- Organization the attendee belongs to
);

-- Table to store conference registrations
CREATE TABLE Registrations (
    RegistrationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each registration
    ConferenceID INT NOT NULL,                     -- Foreign key to the Conferences table
    AttendeeID INT NOT NULL,                       -- Foreign key to the Attendees table
    RegistrationDate DATETIME DEFAULT CURRENT_TIMESTAMP, -- Date and time of registration
    FOREIGN KEY (ConferenceID) REFERENCES Conferences(ConferenceID) ON DELETE CASCADE,
    FOREIGN KEY (AttendeeID) REFERENCES Attendees(AttendeeID) ON DELETE CASCADE
);

-- Table to store the schedule of events within a conference
CREATE TABLE Schedule (
    ScheduleID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each schedule entry
    ConferenceID INT NOT NULL,                   -- Foreign key to the Conferences table
    Title VARCHAR(255) NOT NULL,                 -- Title of the event
    Description TEXT,                            -- Description of the event
    StartTime DATETIME NOT NULL,                 -- Start time of the event
    EndTime DATETIME NOT NULL,                   -- End time of the event
    Location VARCHAR(255),                       -- Location of the event
    FOREIGN KEY (ConferenceID) REFERENCES Conferences(ConferenceID) ON DELETE CASCADE
);

-- Table to store feedback from attendees
CREATE TABLE Feedback (
    FeedbackID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each feedback entry
    ConferenceID INT NOT NULL,                   -- Foreign key to the Conferences table
    AttendeeID INT NOT NULL,                     -- Foreign key to the Attendees table
    Rating INT CHECK (Rating BETWEEN 1 AND 5),   -- Rating given by the attendee (1-5)
    Comments TEXT,                               -- Additional comments from the attendee
    SubmissionDate DATETIME DEFAULT CURRENT_TIMESTAMP, -- Date and time of feedback submission
    FOREIGN KEY (ConferenceID) REFERENCES Conferences(ConferenceID) ON DELETE CASCADE,
    FOREIGN KEY (AttendeeID) REFERENCES Attendees(AttendeeID) ON DELETE CASCADE
);
```
