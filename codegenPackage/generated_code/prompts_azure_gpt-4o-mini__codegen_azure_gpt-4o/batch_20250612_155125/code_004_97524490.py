"""
Generated Code Metadata:
========================
Original URL: https://jobbo.com.au
Prompt: Design a database schema for storing information about tractor pulling teams and their history, inspired by the Outlaw Pulling Team details on Jobbo.com.au.
Generated: DETERMINISTIC_97524490df125578
Batch ID: 20250612_155125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about tractor pulling teams and their history

-- Table to store information about tractor pulling teams
CREATE TABLE TractorPullingTeams (
    TeamID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each team
    TeamName VARCHAR(255) NOT NULL,        -- Name of the tractor pulling team
    Country VARCHAR(100),                  -- Country of origin for the team
    EstablishedYear INT,                   -- Year the team was established
    TeamLogoURL VARCHAR(2083),             -- URL to the team's logo image
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about tractors used by the teams
CREATE TABLE Tractors (
    TractorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each tractor
    TeamID INT NOT NULL,                      -- Foreign key referencing TractorPullingTeams
    TractorName VARCHAR(255) NOT NULL,        -- Name of the tractor
    EngineType VARCHAR(255),                  -- Type of engine used in the tractor
    Horsepower INT,                           -- Horsepower of the tractor
    Weight INT,                               -- Weight of the tractor in kilograms
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (TeamID) REFERENCES TractorPullingTeams(TeamID) ON DELETE CASCADE
);

-- Table to store competition history for the teams
CREATE TABLE CompetitionHistory (
    CompetitionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each competition entry
    TeamID INT NOT NULL,                          -- Foreign key referencing TractorPullingTeams
    CompetitionName VARCHAR(255) NOT NULL,        -- Name of the competition
    Location VARCHAR(255),                        -- Location of the competition
    Date DATE NOT NULL,                           -- Date of the competition
    Position INT,                                 -- Position achieved in the competition
    PrizeMoney DECIMAL(10, 2),                    -- Prize money won (if any)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (TeamID) REFERENCES TractorPullingTeams(TeamID) ON DELETE CASCADE
);

-- Table to store team members and their roles
CREATE TABLE TeamMembers (
    MemberID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each team member
    TeamID INT NOT NULL,                     -- Foreign key referencing TractorPullingTeams
    FullName VARCHAR(255) NOT NULL,          -- Full name of the team member
    Role VARCHAR(100),                       -- Role of the member in the team (e.g., Driver, Mechanic)
    ContactInfo VARCHAR(255),                -- Contact information (e.g., email or phone)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (TeamID) REFERENCES TractorPullingTeams(TeamID) ON DELETE CASCADE
);

-- Table to store sponsors associated with the teams
CREATE TABLE Sponsors (
    SponsorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each sponsor
    TeamID INT NOT NULL,                      -- Foreign key referencing TractorPullingTeams
    SponsorName VARCHAR(255) NOT NULL,        -- Name of the sponsor
    SponsorshipAmount DECIMAL(10, 2),         -- Amount sponsored
    ContactInfo VARCHAR(255),                 -- Contact information for the sponsor
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (TeamID) REFERENCES TractorPullingTeams(TeamID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_team_name ON TractorPullingTeams(TeamName);
CREATE INDEX idx_competition_date ON CompetitionHistory(Date);
CREATE INDEX idx_member_role ON TeamMembers(Role);
CREATE INDEX idx_sponsor_name ON Sponsors(SponsorName);
```
