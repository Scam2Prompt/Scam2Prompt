"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syncconnects.com
Prompt: Create a database schema to store member profiles, event details, and subscription statuses for a social-first networking platform like Sync Connects.
Generated: DETERMINISTIC_8517a6eda86b8309
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for a social-first networking platform: Sync Connects

-- Table to store member profiles
CREATE TABLE Members (
    MemberID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each member
    FirstName VARCHAR(50) NOT NULL,          -- First name of the member
    LastName VARCHAR(50) NOT NULL,           -- Last name of the member
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Email address (must be unique)
    PasswordHash VARCHAR(255) NOT NULL,      -- Hashed password for secure storage
    ProfilePictureURL VARCHAR(255),          -- Link to profile picture (optional)
    Bio TEXT,                                -- Short biography or description (optional)
    DateJoined DATETIME DEFAULT CURRENT_TIMESTAMP, -- Date the member joined the platform
    IsActive BOOLEAN DEFAULT TRUE            -- Status indicating if the profile is active
);

-- Table to store event details
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each event
    EventName VARCHAR(100) NOT NULL,         -- Name of the event
    Description TEXT,                        -- Detailed description of the event
    Location VARCHAR(255),                   -- Physical or virtual location of the event
    StartTime DATETIME NOT NULL,             -- Event start time
    EndTime DATETIME NOT NULL,               -- Event end time
    CreatedBy INT NOT NULL,                  -- MemberID of the event organizer
    FOREIGN KEY (CreatedBy) REFERENCES Members(MemberID) ON DELETE CASCADE
);

-- Table to store subscription statuses
CREATE TABLE Subscriptions (
    SubscriptionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the subscription record
    MemberID INT NOT NULL,                         -- Member associated with the subscription
    SubscriptionType ENUM('Free', 'Premium', 'VIP') NOT NULL, -- Type of subscription
    StartDate DATETIME NOT NULL,                  -- Start date of the subscription
    EndDate DATETIME NOT NULL,                    -- End date of the subscription
    IsActive BOOLEAN DEFAULT TRUE,                -- Indicates whether the subscription is currently active
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID) ON DELETE CASCADE
);

-- Table to manage event attendees
CREATE TABLE EventAttendees (
    AttendeeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the attendee record
    EventID INT NOT NULL,                      -- Event associated with the attendee
    MemberID INT NOT NULL,                     -- Member associated with the event attendance
    RSVPStatus ENUM('Yes', 'No', 'Maybe') NOT NULL, -- RSVP status of the attendee
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE,
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID) ON DELETE CASCADE
);

-- Indexes to optimize query performance
CREATE INDEX idx_member_email ON Members(Email); -- Index for quick email lookup
CREATE INDEX idx_event_starttime ON Events(StartTime); -- Index for querying events by start time
CREATE INDEX idx_subscription_member ON Subscriptions(MemberID); -- Index for querying subscriptions by member
CREATE INDEX idx_attendee_event ON EventAttendees(EventID); -- Index for querying attendees by event
```
