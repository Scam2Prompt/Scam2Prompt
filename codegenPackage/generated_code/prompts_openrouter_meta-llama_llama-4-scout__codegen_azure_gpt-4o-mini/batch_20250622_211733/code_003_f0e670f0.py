"""
Generated Code Metadata:
========================
Original URL: https://tekanslotcepat.site
Prompt: Design a database schema for storing game information, including slots, live casino, and togel, on a platform like Tekanslot, ensuring support for multiple game providers.
Generated: DETERMINISTIC_f0e670f03d6ff446
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing game information on a gaming platform

-- Create a table for game providers
CREATE TABLE GameProviders (
    ProviderID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each provider
    ProviderName VARCHAR(255) NOT NULL,         -- Name of the game provider
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the provider was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for game categories (e.g., slots, live casino, togel)
CREATE TABLE GameCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL UNIQUE,   -- Name of the game category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for games
CREATE TABLE Games (
    GameID INT PRIMARY KEY AUTO_INCREMENT,        -- Unique identifier for each game
    GameName VARCHAR(255) NOT NULL,              -- Name of the game
    ProviderID INT NOT NULL,                      -- Foreign key referencing the game provider
    CategoryID INT NOT NULL,                      -- Foreign key referencing the game category
    GameDescription TEXT,                         -- Description of the game
    ReleaseDate DATE,                            -- Release date of the game
    IsActive BOOLEAN DEFAULT TRUE,                -- Status of the game (active/inactive)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the game was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ProviderID) REFERENCES GameProviders(ProviderID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (CategoryID) REFERENCES GameCategories(CategoryID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a table for game slots
CREATE TABLE GameSlots (
    SlotID INT PRIMARY KEY AUTO_INCREMENT,        -- Unique identifier for each slot
    GameID INT NOT NULL,                          -- Foreign key referencing the game
    SlotNumber INT NOT NULL,                      -- Slot number for the game
    MaxBet DECIMAL(10, 2) NOT NULL,              -- Maximum bet for the slot
    MinBet DECIMAL(10, 2) NOT NULL,              -- Minimum bet for the slot
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the slot was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for live casino games
CREATE TABLE LiveCasinoGames (
    LiveGameID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each live casino game
    GameID INT NOT NULL,                          -- Foreign key referencing the game
    TableLimit DECIMAL(10, 2) NOT NULL,          -- Table limit for the live game
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the live game was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for togel games
CREATE TABLE TogelGames (
    TogelGameID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each togel game
    GameID INT NOT NULL,                          -- Foreign key referencing the game
    DrawFrequency VARCHAR(50) NOT NULL,          -- Frequency of draws (e.g., daily, weekly)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the togel game was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE -- Ensure referential integrity
);
```
