"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aspjj.com
Prompt: "Create a database schema for managing slot game data, including game titles, RTP rates, and user bets, as described on สล็อตเว็บตรง."
Generated: DETERMINISTIC_8b148c6dfd89e436
Batch ID: 20250612_145526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Slot Game Management Database Schema
-- This schema is designed to manage data for slot games, including game titles, RTP (Return to Player) rates, and user bets.

-- Table to store slot games information
CREATE TABLE SlotGames (
    GameID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each slot game
    GameTitle VARCHAR(255) NOT NULL,              -- Title of the slot game
    RTPRate DECIMAL(5, 2) NOT NULL CHECK (RTPRate BETWEEN 0 AND 100), -- Return to Player percentage (0-100)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the game was added
);

-- Table to store user bet information
CREATE TABLE UserBets (
    BetID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each bet
    UserID INT NOT NULL,                          -- Identifier for the user placing the bet (Foreign Key to Users table, if exists)
    GameID INT NOT NULL,                          -- Identifier of the slot game (Foreign Key to SlotGames table)
    BetAmount DECIMAL(10, 2) NOT NULL CHECK (BetAmount > 0), -- Amount of money the user bet
    WinAmount DECIMAL(10, 2) DEFAULT 0,           -- Amount of money the user won (0 if no win)
    BetPlacedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the bet was placed
    FOREIGN KEY (GameID) REFERENCES SlotGames(GameID) ON DELETE CASCADE
);

-- Indexes for better performance
CREATE INDEX idx_game_title ON SlotGames(GameTitle); -- Index for quick search on game titles
CREATE INDEX idx_user_game ON UserBets(UserID, GameID); -- Composite index for user and game relationships

-- Example usage scenarios:
-- 1. Add new slot games to the SlotGames table.
-- 2. Track user bets and winnings in the UserBets table.
-- 3. Query RTP rates and game titles for analytics purposes.
-- 4. Enforce data integrity through foreign keys and constraints.
```
