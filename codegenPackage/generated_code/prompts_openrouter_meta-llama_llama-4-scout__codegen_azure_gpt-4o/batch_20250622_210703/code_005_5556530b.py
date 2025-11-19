"""
Generated Code Metadata:
========================
Original URL: https://pshp.com.pk
Prompt: Design a database schema to store information about PSHP members, events, and achievements.
Generated: DETERMINISTIC_5556530b9a6f1960
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for PSHP members, events, and achievements

-- Table to store member information
CREATE TABLE Members (
    MemberID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each member
    FirstName VARCHAR(50) NOT NULL,          -- Member's first name
    LastName VARCHAR(50) NOT NULL,           -- Member's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Member's email address (must be unique)
    PhoneNumber VARCHAR(15),                 -- Member's phone number
    JoinDate DATE NOT NULL,                  -- Date the member joined PSHP
    IsActive BOOLEAN DEFAULT TRUE            -- Indicates if the member is currently active
);

-- Table to store event information
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each event
    EventName VARCHAR(100) NOT NULL,         -- Name of the event
    EventDate DATE NOT NULL,                 -- Date the event takes place
    Location VARCHAR(100),                   -- Location of the event
    Description TEXT,                        -- Detailed description of the event
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the event was created
);

-- Table to store achievements information
CREATE TABLE Achievements (
    AchievementID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each achievement
    AchievementName VARCHAR(100) NOT NULL,        -- Name of the achievement
    Description TEXT,                             -- Detailed description of the achievement
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the achievement was created
);

-- Table to store the relationship between members and events (attendance)
CREATE TABLE MemberEvents (
    MemberEventID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the relationship
    MemberID INT NOT NULL,                        -- Foreign key referencing Members table
    EventID INT NOT NULL,                         -- Foreign key referencing Events table
    Attended BOOLEAN DEFAULT FALSE,               -- Indicates if the member attended the event
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID) ON DELETE CASCADE,
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE
);

-- Table to store the relationship between members and achievements
CREATE TABLE MemberAchievements (
    MemberAchievementID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the relationship
    MemberID INT NOT NULL,                              -- Foreign key referencing Members table
    AchievementID INT NOT NULL,                         -- Foreign key referencing Achievements table
    AwardedDate DATE NOT NULL,                          -- Date the achievement was awarded
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID) ON DELETE CASCADE,
    FOREIGN KEY (AchievementID) REFERENCES Achievements(AchievementID) ON DELETE CASCADE
);

-- Indexes for optimization
CREATE INDEX idx_member_email ON Members(Email); -- Index for quick lookup by email
CREATE INDEX idx_event_date ON Events(EventDate); -- Index for quick lookup by event date
CREATE INDEX idx_achievement_name ON Achievements(AchievementName); -- Index for quick lookup by achievement name
```
