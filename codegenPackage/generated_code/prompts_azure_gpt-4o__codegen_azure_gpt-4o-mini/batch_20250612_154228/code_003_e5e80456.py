"""
Generated Code Metadata:
========================
Original URL: https://betbax.net
Prompt: Create a database schema for managing live dealer games, including tables for tracking player bets and dealer interactions, inspired by BaxBet's live casino offerings.
Generated: DETERMINISTIC_e5e804568628ab76
Batch ID: 20250612_154228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing live dealer games

-- Create a database for the live casino
CREATE DATABASE LiveCasino;

-- Use the created database
USE LiveCasino;

-- Table to store information about players
CREATE TABLE Players (
    player_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each player
    username VARCHAR(50) NOT NULL UNIQUE,      -- Unique username for the player
    email VARCHAR(100) NOT NULL UNIQUE,         -- Unique email for the player
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of player registration
    last_login TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Last login time
);

-- Table to store information about live dealer games
CREATE TABLE Games (
    game_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each game
    game_type VARCHAR(50) NOT NULL,             -- Type of game (e.g., Blackjack, Roulette)
    dealer_id INT NOT NULL,                      -- Foreign key referencing the dealer
    start_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Start time of the game
    end_time TIMESTAMP,                          -- End time of the game
    FOREIGN KEY (dealer_id) REFERENCES Dealers(dealer_id)  -- Reference to the Dealers table
);

-- Table to store information about dealers
CREATE TABLE Dealers (
    dealer_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each dealer
    name VARCHAR(100) NOT NULL,                  -- Name of the dealer
    experience_years INT NOT NULL,               -- Years of experience
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp of dealer registration
);

-- Table to track player bets
CREATE TABLE Bets (
    bet_id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each bet
    player_id INT NOT NULL,                       -- Foreign key referencing the player
    game_id INT NOT NULL,                         -- Foreign key referencing the game
    bet_amount DECIMAL(10, 2) NOT NULL,          -- Amount of the bet
    bet_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the bet was placed
    outcome ENUM('WIN', 'LOSE', 'PENDING') NOT NULL, -- Outcome of the bet
    FOREIGN KEY (player_id) REFERENCES Players(player_id),  -- Reference to the Players table
    FOREIGN KEY (game_id) REFERENCES Games(game_id)  -- Reference to the Games table
);

-- Table to track dealer interactions with players
CREATE TABLE DealerInteractions (
    interaction_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each interaction
    dealer_id INT NOT NULL,                         -- Foreign key referencing the dealer
    player_id INT NOT NULL,                         -- Foreign key referencing the player
    interaction_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the interaction
    interaction_type VARCHAR(100) NOT NULL,        -- Type of interaction (e.g., chat, assistance)
    notes TEXT,                                     -- Additional notes about the interaction
    FOREIGN KEY (dealer_id) REFERENCES Dealers(dealer_id),  -- Reference to the Dealers table
    FOREIGN KEY (player_id) REFERENCES Players(player_id)   -- Reference to the Players table
);

-- Ensure all tables are created successfully
SELECT 'Database schema for Live Casino created successfully!' AS Message;
```
