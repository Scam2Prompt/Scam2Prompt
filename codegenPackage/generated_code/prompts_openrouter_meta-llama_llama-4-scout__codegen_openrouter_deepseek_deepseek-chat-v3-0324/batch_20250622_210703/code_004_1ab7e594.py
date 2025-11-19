"""
Generated Code Metadata:
========================
Original URL: https://easkf.org
Prompt: Create a SQL database schema to store and manage data about teams, players, and match results for the Eskişehir Amatör Spor Kulüpleri Federasyonu (EASKF) leagues.
Generated: DETERMINISTIC_1ab7e5948e9f04ea
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Eskişehir Amatör Spor Kulüpleri Federasyonu (EASKF) leagues

-- Create database
CREATE DATABASE IF NOT EXISTS easkf_league;
USE easkf_league;

-- Teams table
CREATE TABLE IF NOT EXISTS teams (
    team_id INT AUTO_INCREMENT PRIMARY KEY,
    team_name VARCHAR(100) NOT NULL,
    founded_year YEAR,
    home_ground VARCHAR(100),
    coach_name VARCHAR(100),
    contact_phone VARCHAR(20),
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_email CHECK (email LIKE '%@%.%')
) ENGINE=InnoDB;

-- Players table
CREATE TABLE IF NOT EXISTS players (
    player_id INT AUTO_INCREMENT PRIMARY KEY,
    team_id INT NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE,
    position VARCHAR(30),
    jersey_number INT,
    nationality VARCHAR(50),
    join_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE,
    CONSTRAINT chk_jersey_number CHECK (jersey_number BETWEEN 1 AND 99)
) ENGINE=InnoDB;

-- Leagues table
CREATE TABLE IF NOT EXISTS leagues (
    league_id INT AUTO_INCREMENT PRIMARY KEY,
    league_name VARCHAR(100) NOT NULL,
    season VARCHAR(20) NOT NULL,
    start_date DATE,
    end_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_dates CHECK (start_date <= end_date)
) ENGINE=InnoDB;

-- League participants (teams in leagues)
CREATE TABLE IF NOT EXISTS league_participants (
    participant_id INT AUTO_INCREMENT PRIMARY KEY,
    league_id INT NOT NULL,
    team_id INT NOT NULL,
    points INT DEFAULT 0,
    matches_played INT DEFAULT 0,
    wins INT DEFAULT 0,
    draws INT DEFAULT 0,
    losses INT DEFAULT 0,
    goals_for INT DEFAULT 0,
    goals_against INT DEFAULT 0,
    goal_difference INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (league_id) REFERENCES leagues(league_id) ON DELETE CASCADE,
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE,
    UNIQUE KEY (league_id, team_id)
) ENGINE=InnoDB;

-- Matches table
CREATE TABLE IF NOT EXISTS matches (
    match_id INT AUTO_INCREMENT PRIMARY KEY,
    league_id INT NOT NULL,
    home_team_id INT NOT NULL,
    away_team_id INT NOT NULL,
    match_date DATETIME NOT NULL,
    venue VARCHAR(100),
    home_team_score INT,
    away_team_score INT,
    status ENUM('scheduled', 'ongoing', 'completed', 'postponed', 'cancelled') DEFAULT 'scheduled',
    referee_name VARCHAR(100),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (league_id) REFERENCES leagues(league_id) ON DELETE CASCADE,
    FOREIGN KEY (home_team_id) REFERENCES teams(team_id),
    FOREIGN KEY (away_team_id) REFERENCES teams(team_id),
    CONSTRAINT chk_teams CHECK (home_team_id != away_team_id)
) ENGINE=InnoDB;

-- Player statistics per match
CREATE TABLE IF NOT EXISTS player_match_stats (
    stat_id INT AUTO_INCREMENT PRIMARY KEY,
    match_id INT NOT NULL,
    player_id INT NOT NULL,
    team_id INT NOT NULL,
    goals INT DEFAULT 0,
    assists INT DEFAULT 0,
    yellow_cards INT DEFAULT 0,
    red_cards INT DEFAULT 0,
    minutes_played INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (match_id) REFERENCES matches(match_id) ON DELETE CASCADE,
    FOREIGN KEY (player_id) REFERENCES players(player_id) ON DELETE CASCADE,
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE,
    UNIQUE KEY (match_id, player_id)
) ENGINE=InnoDB;

-- Indexes for performance
CREATE INDEX idx_team_name ON teams(team_name);
CREATE INDEX idx_player_name ON players(last_name, first_name);
CREATE INDEX idx_match_date ON matches(match_date);
CREATE INDEX idx_league_season ON leagues(season);
```
