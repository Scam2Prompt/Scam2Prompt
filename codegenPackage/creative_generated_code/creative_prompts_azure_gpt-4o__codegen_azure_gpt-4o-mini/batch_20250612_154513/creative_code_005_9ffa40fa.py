"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://locinews.com
Prompt: Create a database schema for a betting platform inspired by Bet88, including tables for users, bets, payouts, and game results.
Generated: DETERMINISTIC_9ffa40fa3cdbc5f1
Batch ID: 20250612_154513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for a betting platform

-- Create table for users
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,            -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,  -- Username, must be unique
    email VARCHAR(100) NOT NULL UNIQUE,     -- User's email, must be unique
    password_hash VARCHAR(255) NOT NULL,    -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last updated timestamp
);

-- Create table for games
CREATE TABLE games (
    game_id SERIAL PRIMARY KEY,              -- Unique identifier for each game
    game_name VARCHAR(100) NOT NULL,          -- Name of the game
    game_type VARCHAR(50) NOT NULL,           -- Type of the game (e.g., sports, casino)
    start_time TIMESTAMP NOT NULL,            -- Scheduled start time of the game
    end_time TIMESTAMP NOT NULL,              -- Scheduled end time of the game
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last updated timestamp
);

-- Create table for bets
CREATE TABLE bets (
    bet_id SERIAL PRIMARY KEY,               -- Unique identifier for each bet
    user_id INT NOT NULL,                    -- Reference to the user placing the bet
    game_id INT NOT NULL,                    -- Reference to the game being bet on
    bet_amount DECIMAL(10, 2) NOT NULL,     -- Amount of money being bet
    odds DECIMAL(5, 2) NOT NULL,            -- Odds for the bet
    bet_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Time the bet was placed
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create table for payouts
CREATE TABLE payouts (
    payout_id SERIAL PRIMARY KEY,            -- Unique identifier for each payout
    bet_id INT NOT NULL,                     -- Reference to the bet associated with the payout
    payout_amount DECIMAL(10, 2) NOT NULL,  -- Amount of money paid out
    payout_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Time of the payout
    FOREIGN KEY (bet_id) REFERENCES bets(bet_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create table for game results
CREATE TABLE game_results (
    result_id SERIAL PRIMARY KEY,            -- Unique identifier for each game result
    game_id INT NOT NULL,                    -- Reference to the associated game
    winner VARCHAR(100) NOT NULL,            -- Winner of the game
    result_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Time the result was recorded
    FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexing for performance optimization
CREATE INDEX idx_user_email ON users(email); -- Index on email for quick lookups
CREATE INDEX idx_game_start_time ON games(start_time); -- Index on game start time for scheduling
CREATE INDEX idx_bet_user ON bets(user_id); -- Index on user_id for frequent queries
CREATE INDEX idx_result_game ON game_results(game_id); -- Index on game_id for quick result lookups
```
