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

-- Table to store information about games
CREATE TABLE Games (
    GameID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each game
    Name VARCHAR(255) NOT NULL,            -- Name of the game
    Genre VARCHAR(100),                    -- Genre of the game (e.g., RPG, FPS, etc.)
    Developer VARCHAR(255),                -- Name of the developer or studio
    ReleaseDate DATE,                      -- Release date of the game
    Platform VARCHAR(255),                 -- Platforms the game is available on (e.g., PC, Xbox, etc.)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Table to store information about updates for games
CREATE TABLE GameUpdates (
    UpdateID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each update
    GameID INT NOT NULL,                     -- Foreign key referencing the Games table
    Version VARCHAR(50) NOT NULL,            -- Version number of the update (e.g., 1.0.1)
    Description TEXT,                        -- Description of the update (e.g., patch notes)
    ReleaseDate DATE NOT NULL,               -- Release date of the update
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the record was last updated
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE -- Ensures updates are deleted if the game is deleted
);

-- Table to store information about platforms (optional, for normalization)
CREATE TABLE Platforms (
    PlatformID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each platform
    Name VARCHAR(255) NOT NULL UNIQUE,         -- Name of the platform (e.g., PC, Xbox, PlayStation)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Table to store the relationship between games and platforms (optional, for many-to-many relationships)
CREATE TABLE GamePlatforms (
    GameID INT NOT NULL,                     -- Foreign key referencing the Games table
    PlatformID INT NOT NULL,                 -- Foreign key referencing the Platforms table
    PRIMARY KEY (GameID, PlatformID),        -- Composite primary key
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE, -- Ensures relationship is deleted if the game is deleted
    FOREIGN KEY (PlatformID) REFERENCES Platforms(PlatformID) ON DELETE CASCADE -- Ensures relationship is deleted if the platform is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_game_name ON Games(Name); -- Index for searching games by name
CREATE INDEX idx_update_version ON GameUpdates(Version); -- Index for searching updates by version
CREATE INDEX idx_platform_name ON Platforms(Name); -- Index for searching platforms by name
```
