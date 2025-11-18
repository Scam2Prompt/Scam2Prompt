"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jadobet.org
Prompt: Suggest a database schema for managing thousands of casino games, including slots and table games, with metadata for bonuses and payout ratios, as offered by BaxBet.
Generated: DETERMINISTIC_89582203e74498e9
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing thousands of casino games, including metadata for bonuses and payout ratios

-- Table to store general information about games
CREATE TABLE casino_games (
    game_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each game
    name VARCHAR(255) NOT NULL,             -- Name of the game
    type ENUM('slot', 'table') NOT NULL,    -- Type of game ('slot' or 'table')
    description TEXT,                       -- Optional description of the game
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the game was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store payout ratios for games
CREATE TABLE payout_ratios (
    payout_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each payout record
    game_id INT NOT NULL,                     -- Foreign key linking to casino_games table
    payout_ratio DECIMAL(5, 2) NOT NULL,      -- Payout ratio (e.g., 95.50 for 95.5%)
    FOREIGN KEY (game_id) REFERENCES casino_games(game_id) ON DELETE CASCADE -- Cascade delete to clean up related records
);

-- Table to store bonus information for games
CREATE TABLE game_bonuses (
    bonus_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each bonus record
    game_id INT NOT NULL,                    -- Foreign key linking to casino_games table
    bonus_name VARCHAR(255) NOT NULL,        -- Name of the bonus (e.g., "Free Spins")
    bonus_description TEXT,                  -- Detailed description of the bonus
    FOREIGN KEY (game_id) REFERENCES casino_games(game_id) ON DELETE CASCADE -- Cascade delete to clean up related records
);

-- Table to store tags for games (e.g., "High Stakes", "Popular")
CREATE TABLE game_tags (
    tag_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each tag
    game_id INT NOT NULL,                  -- Foreign key linking to casino_games table
    tag_name VARCHAR(255) NOT NULL,        -- Name of the tag
    FOREIGN KEY (game_id) REFERENCES casino_games(game_id) ON DELETE CASCADE -- Cascade delete to clean up related records
);

-- Table to store audit logs for tracking changes made to games
CREATE TABLE audit_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each log entry
    game_id INT,                              -- Optional foreign key linking to casino_games table
    action VARCHAR(255) NOT NULL,             -- Description of the action performed
    performed_by VARCHAR(255) NOT NULL,       -- Name or ID of the user who performed the action
    performed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the action was performed
    FOREIGN KEY (game_id) REFERENCES casino_games(game_id) ON DELETE SET NULL -- Set game_id to NULL if the game is deleted
);

-- Indexes to optimize queries
CREATE INDEX idx_game_type ON casino_games (type); -- Index for querying by game type
CREATE INDEX idx_payout_game_id ON payout_ratios (game_id); -- Index for querying payout ratios by game_id
CREATE INDEX idx_bonus_game_id ON game_bonuses (game_id); -- Index for querying bonuses by game_id
CREATE INDEX idx_tag_game_id ON game_tags (game_id); -- Index for querying tags by game_id
```
