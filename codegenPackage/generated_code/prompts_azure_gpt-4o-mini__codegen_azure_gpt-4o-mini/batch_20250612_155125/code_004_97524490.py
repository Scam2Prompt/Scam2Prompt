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

CREATE DATABASE TractorPulling;

USE TractorPulling;

-- Table to store information about tractor pulling teams
CREATE TABLE Teams (
    TeamID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each team
    TeamName VARCHAR(100) NOT NULL,        -- Name of the team
    OwnerName VARCHAR(100) NOT NULL,       -- Name of the team owner
    Location VARCHAR(100),                  -- Location of the team
    EstablishedYear INT,                    -- Year the team was established
    ContactEmail VARCHAR(100),              -- Contact email for the team
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about tractors used by teams
CREATE TABLE Tractors (
    TractorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each tractor
    TeamID INT NOT NULL,                       -- Foreign key referencing Teams
    TractorName VARCHAR(100) NOT NULL,        -- Name of the tractor
    EngineType VARCHAR(100),                   -- Type of engine used
    Horsepower INT,                            -- Horsepower of the tractor
    WeightClass VARCHAR(50),                   -- Weight class of the tractor
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (TeamID) REFERENCES Teams(TeamID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store pulling events
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each event
    EventName VARCHAR(100) NOT NULL,        -- Name of the event
    EventDate DATE NOT NULL,                 -- Date of the event
    Location VARCHAR(100),                   -- Location of the event
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store results of each event for each team
CREATE TABLE Results (
    ResultID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each result
    EventID INT NOT NULL,                     -- Foreign key referencing Events
    TeamID INT NOT NULL,                      -- Foreign key referencing Teams
    Position INT NOT NULL,                    -- Position achieved by the team
    Distance DECIMAL(10, 2) NOT NULL,        -- Distance pulled by the tractor
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (TeamID) REFERENCES Teams(TeamID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_team_name ON Teams(TeamName);
CREATE INDEX idx_event_date ON Events(EventDate);
CREATE INDEX idx_team_event ON Results(TeamID, EventID);
```
