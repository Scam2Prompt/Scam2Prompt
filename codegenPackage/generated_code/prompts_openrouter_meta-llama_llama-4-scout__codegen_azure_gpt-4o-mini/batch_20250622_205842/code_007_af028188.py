"""
Generated Code Metadata:
========================
Original URL: https://online-game.online
Prompt: "Design a database schema for storing information about online games and their updates."
Generated: DETERMINISTIC_af02818873a77d47
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about online games and their updates

-- Create a table to store information about games
CREATE TABLE Games (
    GameID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each game
    Title VARCHAR(255) NOT NULL,            -- Title of the game
    Genre VARCHAR(100),                      -- Genre of the game (e.g., Action, RPG)
    ReleaseDate DATE,                        -- Release date of the game
    Developer VARCHAR(255),                  -- Developer of the game
    Publisher VARCHAR(255),                  -- Publisher of the game
    Description TEXT,                        -- Brief description of the game
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the game was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Create a table to store updates for each game
CREATE TABLE GameUpdates (
    UpdateID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each update
    GameID INT NOT NULL,                      -- Foreign key referencing the Games table
    UpdateVersion VARCHAR(50) NOT NULL,      -- Version of the update
    UpdateDate DATE NOT NULL,                 -- Date of the update
    UpdateNotes TEXT,                         -- Notes about what the update includes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the update was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of the last update
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create a table to store user reviews for each game
CREATE TABLE GameReviews (
    ReviewID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each review
    GameID INT NOT NULL,                       -- Foreign key referencing the Games table
    UserID INT NOT NULL,                       -- Identifier for the user who wrote the review
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating given by the user (1 to 5)
    ReviewText TEXT,                           -- Text of the review
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the review was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of the last update
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create a table to store users
CREATE TABLE Users (
    UserID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,      -- Unique username for the user
    Email VARCHAR(255) NOT NULL UNIQUE,        -- Unique email address for the user
    PasswordHash VARCHAR(255) NOT NULL,        -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);
```
