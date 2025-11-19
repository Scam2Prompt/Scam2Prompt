"""
Generated Code Metadata:
========================
Original URL: https://www.atletismomg.org.br
Prompt: Develop a simple database schema to store information about athletic clubs, teams, and athletes, inspired by the structures used on the FMA website.
Generated: DETERMINISTIC_cbf91aed6cbd9db5
Batch ID: 20250622_211748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about athletic clubs, teams, and athletes

-- Table to store information about athletic clubs
CREATE TABLE AthleticClubs (
    ClubID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each club
    ClubName VARCHAR(255) NOT NULL,        -- Name of the athletic club
    Location VARCHAR(255),                -- Location of the club
    FoundedYear INT,                      -- Year the club was founded
    ContactEmail VARCHAR(255),            -- Contact email for the club
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about teams within athletic clubs
CREATE TABLE Teams (
    TeamID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each team
    ClubID INT NOT NULL,                   -- Foreign key referencing AthleticClubs
    TeamName VARCHAR(255) NOT NULL,        -- Name of the team
    SportType VARCHAR(255),                -- Type of sport the team participates in
    CoachName VARCHAR(255),                -- Name of the team's coach
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ClubID) REFERENCES AthleticClubs(ClubID) ON DELETE CASCADE -- Cascade delete if club is removed
);

-- Table to store information about athletes
CREATE TABLE Athletes (
    AthleteID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each athlete
    TeamID INT NOT NULL,                      -- Foreign key referencing Teams
    FirstName VARCHAR(255) NOT NULL,          -- Athlete's first name
    LastName VARCHAR(255) NOT NULL,           -- Athlete's last name
    DateOfBirth DATE,                         -- Athlete's date of birth
    Gender ENUM('Male', 'Female', 'Other'),   -- Athlete's gender
    Position VARCHAR(255),                    -- Position or role in the team
    ContactEmail VARCHAR(255),                -- Contact email for the athlete
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (TeamID) REFERENCES Teams(TeamID) ON DELETE CASCADE -- Cascade delete if team is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_club_location ON AthleticClubs(Location); -- Index for club location
CREATE INDEX idx_team_sport ON Teams(SportType);           -- Index for sport type
CREATE INDEX idx_athlete_name ON Athletes(LastName);       -- Index for athlete's last name

-- Example of error handling: Ensure proper constraints
-- For example, ClubName and TeamName must be unique within their respective tables
ALTER TABLE AthleticClubs ADD CONSTRAINT unique_club_name UNIQUE (ClubName);
ALTER TABLE Teams ADD CONSTRAINT unique_team_name UNIQUE (TeamName, ClubID);
```
