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
-- Database schema for storing information about tractor pulling teams and their history

-- Create a database named 'tractor_pulling'
CREATE DATABASE tractor_pulling;

USE tractor_pulling;

-- Table to store information about tractor pulling teams
CREATE TABLE teams (
    team_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each team
    team_name VARCHAR(100) NOT NULL,         -- Name of the team
    owner_name VARCHAR(100) NOT NULL,        -- Name of the team owner
    contact_email VARCHAR(100),               -- Contact email address for the team
    creation_date DATE NOT NULL DEFAULT CURRENT_DATE,  -- Date the team was formed
    location VARCHAR(100)                     -- Location of the team
);

-- Table to store information about tractors used by the teams
CREATE TABLE tractors (
    tractor_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each tractor
    team_id INT NOT NULL,                        -- Foreign key referencing teams
    tractor_name VARCHAR(100) NOT NULL,         -- Name of the tractor
    model VARCHAR(100),                          -- Model of the tractor
    weight_class VARCHAR(50),                    -- Weight class of the tractor
    engine_power INT,                            -- Engine power in horsepower
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE -- Ensure integrity
);

-- Table to store pulling event history for each team
CREATE TABLE pulling_events (
    event_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each event
    team_id INT NOT NULL,                          -- Foreign key referencing teams
    event_date DATE NOT NULL,                      -- Date of the pulling event
    event_location VARCHAR(100) NOT NULL,         -- Location of the pulling event
    distance_achieved DECIMAL(5, 2),              -- Distance achieved by the tractor
    position INT,                                  -- Position in the event
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE -- Ensure integrity
);

-- Table to store performance statistics for each pulling event
CREATE TABLE performance_stats (
    stat_id INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each statistic
    event_id INT NOT NULL,                         -- Foreign key referencing pulling events
    tractor_id INT NOT NULL,                       -- Foreign key referencing tractors
    distance_achieved DECIMAL(5, 2),              -- Distance achieved in the event
    time_taken DECIMAL(5, 2),                     -- Time taken for the pull in seconds
    FOREIGN KEY (event_id) REFERENCES pulling_events(event_id) ON DELETE CASCADE, -- Ensure integrity
    FOREIGN KEY (tractor_id) REFERENCES tractors(tractor_id) ON DELETE CASCADE  -- Ensure integrity
);

-- Indexes for better performance
CREATE INDEX idx_team_name ON teams(team_name);
CREATE INDEX idx_event_date ON pulling_events(event_date);
CREATE INDEX idx_tractor_name ON tractors(tractor_name);
```
