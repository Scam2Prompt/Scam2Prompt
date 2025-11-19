"""
Generated Code Metadata:
========================
Original URL: https://mctsummit.org
Prompt: "Design a database schema for managing attendees, speakers, and sponsors for the MCT Summit 2025, including tables for contact information and session assignments."
Generated: DETERMINISTIC_cfea3ce1ae5db680
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing attendees, speakers, sponsors, contact information, and session assignments for MCT Summit 2025

-- Table to store general contact information
CREATE TABLE ContactInfo (
    ContactID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for contact
    FirstName VARCHAR(50) NOT NULL,           -- First name of the contact
    LastName VARCHAR(50) NOT NULL,            -- Last name of the contact
    Email VARCHAR(100) NOT NULL UNIQUE,       -- Email address (must be unique)
    PhoneNumber VARCHAR(15),                  -- Phone number (optional)
    Address VARCHAR(255),                     -- Address (optional)
    City VARCHAR(50),                         -- City (optional)
    State VARCHAR(50),                        -- State (optional)
    Country VARCHAR(50),                      -- Country (optional)
    ZipCode VARCHAR(10),                      -- Zip code (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store attendees
CREATE TABLE Attendees (
    AttendeeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for attendee
    ContactID INT NOT NULL,                    -- Foreign key to ContactInfo table
    RegistrationDate DATE NOT NULL,            -- Date of registration
    TicketType ENUM('Standard', 'VIP', 'Student') NOT NULL, -- Type of ticket purchased
    FOREIGN KEY (ContactID) REFERENCES ContactInfo(ContactID) ON DELETE CASCADE
);

-- Table to store speakers
CREATE TABLE Speakers (
    SpeakerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for speaker
    ContactID INT NOT NULL,                   -- Foreign key to ContactInfo table
    Bio TEXT,                                 -- Short biography of the speaker
    Expertise VARCHAR(255),                   -- Area of expertise
    FOREIGN KEY (ContactID) REFERENCES ContactInfo(ContactID) ON DELETE CASCADE
);

-- Table to store sponsors
CREATE TABLE Sponsors (
    SponsorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for sponsor
    ContactID INT NOT NULL,                   -- Foreign key to ContactInfo table
    CompanyName VARCHAR(100) NOT NULL,        -- Name of the sponsoring company
    SponsorshipLevel ENUM('Gold', 'Silver', 'Bronze') NOT NULL, -- Level of sponsorship
    FOREIGN KEY (ContactID) REFERENCES ContactInfo(ContactID) ON DELETE CASCADE
);

-- Table to store sessions
CREATE TABLE Sessions (
    SessionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for session
    Title VARCHAR(255) NOT NULL,              -- Title of the session
    Description TEXT,                         -- Description of the session
    StartTime DATETIME NOT NULL,              -- Start time of the session
    EndTime DATETIME NOT NULL,                -- End time of the session
    Room VARCHAR(50),                         -- Room where the session will be held
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to assign speakers to sessions
CREATE TABLE SessionSpeakers (
    SessionSpeakerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for session-speaker assignment
    SessionID INT NOT NULL,                          -- Foreign key to Sessions table
    SpeakerID INT NOT NULL,                          -- Foreign key to Speakers table
    FOREIGN KEY (SessionID) REFERENCES Sessions(SessionID) ON DELETE CASCADE,
    FOREIGN KEY (SpeakerID) REFERENCES Speakers(SpeakerID) ON DELETE CASCADE
);

-- Table to assign attendees to sessions
CREATE TABLE SessionAttendees (
    SessionAttendeeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for session-attendee assignment
    SessionID INT NOT NULL,                           -- Foreign key to Sessions table
    AttendeeID INT NOT NULL,                          -- Foreign key to Attendees table
    FOREIGN KEY (SessionID) REFERENCES Sessions(SessionID) ON DELETE CASCADE,
    FOREIGN KEY (AttendeeID) REFERENCES Attendees(AttendeeID) ON DELETE CASCADE
);

-- Table to assign sponsors to sessions (if applicable)
CREATE TABLE SessionSponsors (
    SessionSponsorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for session-sponsor assignment
    SessionID INT NOT NULL,                          -- Foreign key to Sessions table
    SponsorID INT NOT NULL,                          -- Foreign key to Sponsors table
    FOREIGN KEY (SessionID) REFERENCES Sessions(SessionID) ON DELETE CASCADE,
    FOREIGN KEY (SponsorID) REFERENCES Sponsors(SponsorID) ON DELETE CASCADE
);
```
