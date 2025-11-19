"""
Generated Code Metadata:
========================
Original URL: https://republik.pages.dev
Prompt: Design a database schema to store information about slot games, including game metadata, RTP rates, and user gameplay history, for a platform like ANGKA805.
Generated: DETERMINISTIC_6ac61a818273b502
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about slot games, RTP rates, and user gameplay history

-- Create a table to store game metadata
CREATE TABLE slot_games (
    game_id SERIAL PRIMARY KEY, -- Unique identifier for each game
    game_name VARCHAR(255) NOT NULL, -- Name of the slot game
    provider VARCHAR(255) NOT NULL, -- Game provider or developer
    release_date DATE NOT NULL, -- Release date of the game
    description TEXT, -- Description of the game
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the game was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Create a table to store RTP (Return to Player) rates for each game
CREATE TABLE rtp_rates (
    rtp_id SERIAL PRIMARY KEY, -- Unique identifier for each RTP entry
    game_id INT NOT NULL, -- Foreign key referencing the slot_games table
    rtp_rate DECIMAL(5, 2) NOT NULL CHECK (rtp_rate >= 0 AND rtp_rate <= 100), -- RTP rate as a percentage
    effective_date DATE NOT NULL, -- Date when the RTP rate becomes effective
    FOREIGN KEY (game_id) REFERENCES slot_games(game_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to store user gameplay history
CREATE TABLE user_gameplay_history (
    history_id SERIAL PRIMARY KEY, -- Unique identifier for each gameplay record
    user_id INT NOT NULL, -- Identifier for the user (assumed to be managed in a separate users table)
    game_id INT NOT NULL, -- Foreign key referencing the slot_games table
    bet_amount DECIMAL(10, 2) NOT NULL, -- Amount bet by the user
    win_amount DECIMAL(10, 2) NOT NULL, -- Amount won by the user
    gameplay_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the gameplay
    FOREIGN KEY (game_id) REFERENCES slot_games(game_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create an index on the user_gameplay_history table for faster queries by user_id
CREATE INDEX idx_user_gameplay ON user_gameplay_history(user_id);

-- Create an index on the rtp_rates table for faster queries by game_id
CREATE INDEX idx_rtp_game ON rtp_rates(game_id);
```
