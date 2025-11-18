"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betbax.net
Prompt: Create a database schema for managing live dealer games, including tables for tracking player bets and dealer interactions, inspired by BaxBet's live casino offerings.
Generated: DETERMINISTIC_e5e804568628ab76
Batch ID: 20250612_154228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing live dealer games

-- Create a table for storing player information
CREATE TABLE Players (
    PlayerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each player
    Username VARCHAR(50) NOT NULL UNIQUE,     -- Unique username for the player
    Email VARCHAR(100) NOT NULL UNIQUE,        -- Unique email for communication
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    LastLogin TIMESTAMP                        -- Last login timestamp
);

-- Create a table for storing dealer information
CREATE TABLE Dealers (
    DealerID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each dealer
    Name VARCHAR(50) NOT NULL,                 -- Dealer's name
    ShiftStart TIME NOT NULL,                  -- Start time of the dealer's shift
    ShiftEnd TIME NOT NULL,                    -- End time of the dealer's shift
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Create a table for storing games
CREATE TABLE Games (
    GameID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each game
    GameType VARCHAR(50) NOT NULL,             -- Type of game (e.g., Blackjack, Roulette)
    DealerID INT NOT NULL,                      -- Foreign key referencing Dealers
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (DealerID) REFERENCES Dealers(DealerID) ON DELETE CASCADE -- Enforce referential integrity
);

-- Create a table for tracking player bets
CREATE TABLE Bets (
    BetID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each bet
    PlayerID INT NOT NULL,                      -- Foreign key referencing Players
    GameID INT NOT NULL,                        -- Foreign key referencing Games
    Amount DECIMAL(10, 2) NOT NULL,            -- Amount of the bet
    BetTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Time when the bet was placed
    Status ENUM('Pending', 'Won', 'Lost') NOT NULL, -- Status of the bet
    FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID) ON DELETE CASCADE, -- Enforce referential integrity
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE -- Enforce referential integrity
);

-- Create a table for tracking dealer interactions
CREATE TABLE DealerInteractions (
    InteractionID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each interaction
    DealerID INT NOT NULL,                         -- Foreign key referencing Dealers
    GameID INT NOT NULL,                           -- Foreign key referencing Games
    InteractionTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Time of interaction
    Action VARCHAR(100) NOT NULL,                 -- Description of the interaction
    FOREIGN KEY (DealerID) REFERENCES Dealers(DealerID) ON DELETE CASCADE, -- Enforce referential integrity
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE -- Enforce referential integrity
);

-- Create indexes for optimizing query performance
CREATE INDEX idx_player ON Bets(PlayerID);
CREATE INDEX idx_game ON Bets(GameID);
CREATE INDEX idx_dealer ON DealerInteractions(DealerID);
CREATE INDEX idx_game_interaction ON DealerInteractions(GameID);
```
