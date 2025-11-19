"""
Generated Code Metadata:
========================
Original URL: https://hbpufeng.com
Prompt: Design a database schema for storing game-related data, inspired by the types of games and user information managed by 盛煌娱乐.
Generated: DETERMINISTIC_7f36204ec3b93947
Batch ID: 20250622_212039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing game-related data

-- Create a database for the gaming application
CREATE DATABASE GameDatabase;

-- Use the created database
USE GameDatabase;

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,    -- Unique username for the user
    PasswordHash VARCHAR(255) NOT NULL,      -- Hashed password for security
    Email VARCHAR(100) NOT NULL UNIQUE,      -- Unique email address for the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of user creation
    LastLogin TIMESTAMP NULL,                 -- Timestamp of last login
    IsActive BOOLEAN DEFAULT TRUE              -- Status of the user account
);

-- Table to store game information
CREATE TABLE Games (
    GameID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each game
    Title VARCHAR(100) NOT NULL,              -- Title of the game
    Genre VARCHAR(50) NOT NULL,               -- Genre of the game (e.g., Action, RPG)
    ReleaseDate DATE NOT NULL,                 -- Release date of the game
    Developer VARCHAR(100) NOT NULL,          -- Developer of the game
    Description TEXT,                          -- Description of the game
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp of game entry creation
);

-- Table to store user game statistics
CREATE TABLE UserGameStats (
    StatID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each stat entry
    UserID INT NOT NULL,                       -- Foreign key referencing Users
    GameID INT NOT NULL,                       -- Foreign key referencing Games
    Score INT DEFAULT 0,                       -- User's score in the game
    PlayTime INT DEFAULT 0,                    -- Total playtime in minutes
    Achievements JSON DEFAULT NULL,            -- JSON field to store achievements
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of stat entry creation
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE   -- Ensure referential integrity
);

-- Table to store user reviews for games
CREATE TABLE GameReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each review
    UserID INT NOT NULL,                       -- Foreign key referencing Users
    GameID INT NOT NULL,                       -- Foreign key referencing Games
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating given by the user (1 to 5)
    ReviewText TEXT,                           -- Text of the review
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of review creation
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE   -- Ensure referential integrity
);

-- Table to store game sessions
CREATE TABLE GameSessions (
    SessionID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each session
    UserID INT NOT NULL,                        -- Foreign key referencing Users
    GameID INT NOT NULL,                        -- Foreign key referencing Games
    SessionStart TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Start time of the session
    SessionEnd TIMESTAMP NULL,                  -- End time of the session
    Duration INT DEFAULT 0,                     -- Duration of the session in minutes
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE   -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_username ON Users(Username);
CREATE INDEX idx_game_title ON Games(Title);
CREATE INDEX idx_user_game ON UserGameStats(UserID, GameID);
CREATE INDEX idx_game_review ON GameReviews(GameID);
```
