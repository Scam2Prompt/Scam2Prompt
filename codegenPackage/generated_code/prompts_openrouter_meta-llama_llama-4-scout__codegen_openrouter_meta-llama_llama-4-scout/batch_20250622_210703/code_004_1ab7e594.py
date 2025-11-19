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
-- Create database for EASKF leagues
CREATE DATABASE easkf_leagues;

-- Use the database
USE easkf_leagues;

-- Create table for teams
CREATE TABLE teams (
    team_id INT AUTO_INCREMENT,
    team_name VARCHAR(255) NOT NULL,
    team_short_name VARCHAR(10) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (team_id)
);

-- Create table for players
CREATE TABLE players (
    player_id INT AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (player_id)
);

-- Create table for team players
CREATE TABLE team_players (
    team_id INT NOT NULL,
    player_id INT NOT NULL,
    jersey_number INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (team_id, player_id),
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE,
    FOREIGN KEY (player_id) REFERENCES players(player_id) ON DELETE CASCADE
);

-- Create table for matches
CREATE TABLE matches (
    match_id INT AUTO_INCREMENT,
    home_team_id INT NOT NULL,
    away_team_id INT NOT NULL,
    match_date DATE NOT NULL,
    home_score INT,
    away_score INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (match_id),
    FOREIGN KEY (home_team_id) REFERENCES teams(team_id) ON DELETE CASCADE,
    FOREIGN KEY (away_team_id) REFERENCES teams(team_id) ON DELETE CASCADE,
    CHECK (home_team_id <> away_team_id)
);

-- Create table for match results
CREATE TABLE match_results (
    match_id INT NOT NULL,
    player_id INT NOT NULL,
    goals_scored INT DEFAULT 0,
    yellow_cards INT DEFAULT 0,
    red_card BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (match_id, player_id),
    FOREIGN KEY (match_id) REFERENCES matches(match_id) ON DELETE CASCADE,
    FOREIGN KEY (player_id) REFERENCES players(player_id) ON DELETE CASCADE
);

-- Create table for league standings
CREATE TABLE league_standings (
    season INT NOT NULL,
    team_id INT NOT NULL,
    played_matches INT DEFAULT 0,
    won_matches INT DEFAULT 0,
    drawn_matches INT DEFAULT 0,
    lost_matches INT DEFAULT 0,
    goals_scored INT DEFAULT 0,
    goals_conceded INT DEFAULT 0,
    points INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (season, team_id),
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE
);
```
