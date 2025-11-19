"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jobbo.com.au
Prompt: Design a database schema for storing information about tractor pulling teams and their history, inspired by the Outlaw Pulling Team details on Jobbo.com.au.
Generated: DETERMINISTIC_97524490df125578
Batch ID: 20250612_155125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Tractor Pulling Teams and Their History

-- Create a table to store teams' general information
CREATE TABLE TractorPullingTeams (
    TeamID INT AUTO_INCREMENT PRIMARY KEY,             -- Unique identifier for each team
    TeamName VARCHAR(255) NOT NULL,                    -- Name of the tractor pulling team
    TeamLogoURL VARCHAR(2083),                         -- URL for the team's logo or image
    Country VARCHAR(100) NOT NULL,                     -- Country where the team is based
    EstablishedYear INT,                               -- Year the team was established
    WebsiteURL VARCHAR(2083),                          -- Official website of the team
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Record creation date
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record last update date
);

-- Create a table to store details about tractors used by the teams
CREATE TABLE TeamTractors (
    TractorID INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each tractor
    TeamID INT NOT NULL,                               -- Foreign key linking to TractorPullingTeams table
    TractorName VARCHAR(255) NOT NULL,                 -- Name of the tractor
    EngineDetails TEXT,                                -- Details about the tractor's engine
    WeightClass VARCHAR(100),                          -- Weight class of the tractor
    Horsepower INT,                                    -- Horsepower of the tractor
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Record creation date
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record last update date
    FOREIGN KEY (TeamID) REFERENCES TractorPullingTeams(TeamID) ON DELETE CASCADE -- Cascade delete if team is removed
);

-- Create a table to store event participation history
CREATE TABLE EventHistory (
    EventID INT AUTO_INCREMENT PRIMARY KEY,            -- Unique identifier for each event
    TeamID INT NOT NULL,                               -- Foreign key linking to TractorPullingTeams table
    EventName VARCHAR(255) NOT NULL,                   -- Name of the event
    EventDate DATE NOT NULL,                           -- Date of the event
    Location VARCHAR(255),                             -- Location of the event
    Position INT,                                      -- Position achieved in the event (e.g., 1st place)
    TotalTractors INT,                                 -- Total number of tractors that participated
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Record creation date
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record last update date
    FOREIGN KEY (TeamID) REFERENCES TractorPullingTeams(TeamID) ON DELETE CASCADE -- Cascade delete if team is removed
);

-- Create a table to store awards won by teams or tractors
CREATE TABLE Awards (
    AwardID INT AUTO_INCREMENT PRIMARY KEY,            -- Unique identifier for each award
    TeamID INT,                                        -- Foreign key linking to TractorPullingTeams table
    TractorID INT,                                     -- Foreign key linking to TeamTractors table (optional)
    AwardName VARCHAR(255) NOT NULL,                   -- Name of the award
    AwardYear INT NOT NULL,                            -- Year the award was won
    Description TEXT,                                  -- Description of the award
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Record creation date
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record last update date
    FOREIGN KEY (TeamID) REFERENCES TractorPullingTeams(TeamID) ON DELETE CASCADE, -- Cascade delete if team is removed
    FOREIGN KEY (TractorID) REFERENCES TeamTractors(TractorID) ON DELETE SET NULL -- Set to NULL if tractor is removed
);

-- Create a table to store team members
CREATE TABLE TeamMembers (
    MemberID INT AUTO_INCREMENT PRIMARY KEY,           -- Unique identifier for each member
    TeamID INT NOT NULL,                               -- Foreign key linking to TractorPullingTeams table
    MemberName VARCHAR(255) NOT NULL,                  -- Name of the team member
    Role VARCHAR(100),                                 -- Role of the member (e.g., Driver, Mechanic, etc.)
    JoinedDate DATE,                                   -- Date the member joined the team
    Bio TEXT,                                          -- Short biography of the member
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Record creation date
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record last update date
    FOREIGN KEY (TeamID) REFERENCES TractorPullingTeams(TeamID) ON DELETE CASCADE -- Cascade delete if team is removed
);

-- Indexes and Constraints
-- Create indexes for faster lookups
CREATE INDEX idx_TeamID ON TeamTractors(TeamID);
CREATE INDEX idx_EventHistory_TeamID ON EventHistory(TeamID);
CREATE INDEX idx_Awards_TeamID_TractorID ON Awards(TeamID, TractorID);
CREATE INDEX idx_TeamMembers_TeamID ON TeamMembers(TeamID);
```
