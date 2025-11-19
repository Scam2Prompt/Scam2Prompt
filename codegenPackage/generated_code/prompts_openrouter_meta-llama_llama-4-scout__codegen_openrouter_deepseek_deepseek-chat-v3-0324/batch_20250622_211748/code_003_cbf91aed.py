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
-- Database schema for athletic clubs, teams, and athletes management
-- Inspired by FMA website structures

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create table for athletic clubs
CREATE TABLE clubs (
    club_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    founded_date DATE,
    location TEXT,
    website_url TEXT,
    email TEXT CHECK (email LIKE '%@%.%'),
    phone_number TEXT,
    logo_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (name, location)
);

-- Create table for teams
CREATE TABLE teams (
    team_id INTEGER PRIMARY KEY AUTOINCREMENT,
    club_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    sport_type TEXT NOT NULL,
    age_category TEXT,
    gender_category TEXT CHECK (gender_category IN ('Male', 'Female', 'Mixed', 'Other')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (club_id) REFERENCES clubs(club_id) ON DELETE CASCADE,
    UNIQUE (club_id, name)
);

-- Create table for athletes
CREATE TABLE athletes (
    athlete_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    gender TEXT CHECK (gender IN ('Male', 'Female', 'Other')),
    nationality TEXT,
    profile_picture_url TEXT,
    email TEXT CHECK (email LIKE '%@%.%'),
    phone_number TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create junction table for athlete-team relationships
CREATE TABLE athlete_team_memberships (
    membership_id INTEGER PRIMARY KEY AUTOINCREMENT,
    athlete_id INTEGER NOT NULL,
    team_id INTEGER NOT NULL,
    join_date DATE DEFAULT CURRENT_DATE,
    leave_date DATE,
    position TEXT,
    jersey_number INTEGER,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (athlete_id) REFERENCES athletes(athlete_id) ON DELETE CASCADE,
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE,
    UNIQUE (athlete_id, team_id) ON CONFLICT REPLACE,
    CHECK (leave_date IS NULL OR leave_date > join_date)
);

-- Create table for competitions
CREATE TABLE competitions (
    competition_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    location TEXT,
    organizer TEXT,
    competition_level TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (end_date IS NULL OR end_date >= start_date)
);

-- Create junction table for team participation in competitions
CREATE TABLE team_participations (
    participation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    team_id INTEGER NOT NULL,
    competition_id INTEGER NOT NULL,
    standing TEXT,
    awards TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE,
    FOREIGN KEY (competition_id) REFERENCES competitions(competition_id) ON DELETE CASCADE,
    UNIQUE (team_id, competition_id)
);

-- Create indexes for performance optimization
CREATE INDEX idx_athlete_names ON athletes(last_name, first_name);
CREATE INDEX idx_team_club ON teams(club_id);
CREATE INDEX idx_membership_athlete ON athlete_team_memberships(athlete_id);
CREATE INDEX idx_membership_team ON athlete_team_memberships(team_id);
CREATE INDEX idx_participation_team ON team_participations(team_id);
CREATE INDEX idx_participation_competition ON team_participations(competition_id);
```
