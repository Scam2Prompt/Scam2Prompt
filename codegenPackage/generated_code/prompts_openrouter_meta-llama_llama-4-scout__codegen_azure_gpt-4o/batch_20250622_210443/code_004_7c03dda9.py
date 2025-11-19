"""
Generated Code Metadata:
========================
Original URL: https://cdjuangrande.es
Prompt: Design a database schema for storing information about a football team like cdjuangrande, including tables for team history, players, sponsors, and contact details.
Generated: DETERMINISTIC_7c03dda9c7dbba56
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about a football team

-- Table: Teams
-- Stores basic information about the football team
CREATE TABLE Teams (
    TeamID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the team
    TeamName VARCHAR(100) NOT NULL,        -- Name of the team
    FoundedYear INT,                       -- Year the team was founded
    StadiumName VARCHAR(100),              -- Name of the team's stadium
    WebsiteURL VARCHAR(255),               -- Official website URL
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table: TeamHistory
-- Stores historical information about the team
CREATE TABLE TeamHistory (
    HistoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the history record
    TeamID INT NOT NULL,                      -- Foreign key referencing Teams table
    Year INT NOT NULL,                        -- Year of the historical event
    Achievement TEXT,                         -- Description of the achievement or event
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (TeamID) REFERENCES Teams(TeamID) ON DELETE CASCADE -- Cascade delete if team is removed
);

-- Table: Players
-- Stores information about players in the team
CREATE TABLE Players (
    PlayerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the player
    TeamID INT NOT NULL,                     -- Foreign key referencing Teams table
    FirstName VARCHAR(50) NOT NULL,          -- Player's first name
    LastName VARCHAR(50) NOT NULL,           -- Player's last name
    Position VARCHAR(30),                    -- Player's position (e.g., Forward, Midfielder)
    JerseyNumber INT,                        -- Player's jersey number
    DateOfBirth DATE,                        -- Player's date of birth
    Nationality VARCHAR(50),                 -- Player's nationality
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (TeamID) REFERENCES Teams(TeamID) ON DELETE CASCADE -- Cascade delete if team is removed
);

-- Table: Sponsors
-- Stores information about sponsors associated with the team
CREATE TABLE Sponsors (
    SponsorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the sponsor
    TeamID INT NOT NULL,                      -- Foreign key referencing Teams table
    SponsorName VARCHAR(100) NOT NULL,        -- Name of the sponsor
    SponsorshipAmount DECIMAL(10, 2),         -- Amount sponsored
    ContactEmail VARCHAR(100),                -- Contact email for the sponsor
    ContactPhone VARCHAR(15),                 -- Contact phone number for the sponsor
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (TeamID) REFERENCES Teams(TeamID) ON DELETE CASCADE -- Cascade delete if team is removed
);

-- Table: ContactDetails
-- Stores contact information for the team
CREATE TABLE ContactDetails (
    ContactID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the contact record
    TeamID INT NOT NULL,                      -- Foreign key referencing Teams table
    ContactName VARCHAR(100) NOT NULL,        -- Name of the contact person
    ContactEmail VARCHAR(100) NOT NULL,       -- Email address of the contact person
    ContactPhone VARCHAR(15) NOT NULL,        -- Phone number of the contact person
    Address TEXT,                             -- Physical address of the contact person
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (TeamID) REFERENCES Teams(TeamID) ON DELETE CASCADE -- Cascade delete if team is removed
);

-- Ensure proper indexing for faster queries
CREATE INDEX idx_team_name ON Teams(TeamName);
CREATE INDEX idx_player_name ON Players(LastName, FirstName);
CREATE INDEX idx_sponsor_name ON Sponsors(SponsorName);
CREATE INDEX idx_contact_email ON ContactDetails(ContactEmail);
```
