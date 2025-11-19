"""
Generated Code Metadata:
========================
Original URL: https://genteparaservir.org
Prompt: Design a simple database schema for storing information about members, events, and donations for an organization similar to Gente Para Servir.
Generated: DETERMINISTIC_99607b28290f6f44
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about members, events, and donations

-- Table to store member information
CREATE TABLE Members (
    MemberID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each member
    FirstName VARCHAR(50) NOT NULL,          -- Member's first name
    LastName VARCHAR(50) NOT NULL,           -- Member's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Member's email address
    PhoneNumber VARCHAR(15),                 -- Member's phone number
    Address TEXT,                            -- Member's address
    JoinDate DATE NOT NULL,                  -- Date the member joined the organization
    IsActive BOOLEAN DEFAULT TRUE            -- Indicates if the member is currently active
);

-- Table to store event information
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each event
    EventName VARCHAR(100) NOT NULL,         -- Name of the event
    EventDate DATE NOT NULL,                 -- Date of the event
    Location VARCHAR(100),                   -- Location of the event
    Description TEXT,                        -- Description of the event
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the event was created
);

-- Table to store donation information
CREATE TABLE Donations (
    DonationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each donation
    MemberID INT NOT NULL,                     -- Foreign key referencing Members table
    DonationDate DATE NOT NULL,                -- Date the donation was made
    Amount DECIMAL(10, 2) NOT NULL,            -- Amount of the donation
    PaymentMethod VARCHAR(50),                 -- Payment method used for the donation
    Notes TEXT,                                -- Additional notes about the donation
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID) -- Enforce relationship with Members table
);

-- Table to store event participation information
CREATE TABLE EventParticipation (
    ParticipationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each participation record
    MemberID INT NOT NULL,                          -- Foreign key referencing Members table
    EventID INT NOT NULL,                           -- Foreign key referencing Events table
    ParticipationDate DATE NOT NULL,                -- Date of participation
    Role VARCHAR(50),                               -- Role of the member in the event (e.g., volunteer, attendee)
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID), -- Enforce relationship with Members table
    FOREIGN KEY (EventID) REFERENCES Events(EventID)     -- Enforce relationship with Events table
);

-- Indexes for optimizing queries
CREATE INDEX idx_member_email ON Members(Email); -- Index for quick lookup by email
CREATE INDEX idx_event_date ON Events(EventDate); -- Index for quick lookup by event date
CREATE INDEX idx_donation_date ON Donations(DonationDate); -- Index for quick lookup by donation date
CREATE INDEX idx_participation_date ON EventParticipation(ParticipationDate); -- Index for quick lookup by participation date
```
