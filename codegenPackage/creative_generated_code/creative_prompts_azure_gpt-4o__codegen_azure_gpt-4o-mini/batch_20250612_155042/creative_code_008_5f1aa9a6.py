"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simemes.vercel.app
Prompt: Develop a database schema in SQL for storing SIMemes player data, including resources like poop, chests, and tokens, as well as player interactions.
Generated: DETERMINISTIC_5f1aa9a67fb15aae
Batch ID: 20250612_155042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- ==========================================
-- Database Schema for SIMemes Player Data
-- ==========================================

-- Drop existing tables if they exist (for clean slate during development)
DROP TABLE IF EXISTS PlayerInteractions;
DROP TABLE IF EXISTS Players;
DROP TABLE IF EXISTS Resources;

-- ==========================================
-- Players Table
-- ==========================================
CREATE TABLE Players (
    player_id SERIAL PRIMARY KEY,          -- Unique identifier for each player
    username VARCHAR(50) NOT NULL UNIQUE,  -- Player's username, must be unique
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the player was created
    last_login TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of the last login
);

-- ==========================================
-- Resources Table
-- ==========================================
CREATE TABLE Resources (
    resource_id SERIAL PRIMARY KEY,        -- Unique identifier for each resource entry
    player_id INT NOT NULL,                -- Foreign key linking to the Players table
    poop INT DEFAULT 0,                    -- Amount of poop resources the player has
    chests INT DEFAULT 0,                  -- Amount of chests the player has
    tokens INT DEFAULT 0,                  -- Amount of tokens the player has
    FOREIGN KEY (player_id) REFERENCES Players(player_id) ON DELETE CASCADE
);

-- ==========================================
-- Player Interactions Table
-- ==========================================
CREATE TABLE PlayerInteractions (
    interaction_id SERIAL PRIMARY KEY,     -- Unique identifier for each interaction
    player_id INT NOT NULL,                -- Foreign key linking to the Players table
    interacted_with INT NOT NULL,          -- ID of the player interacted with
    interaction_type VARCHAR(50) NOT NULL, -- Type of interaction (e.g., "trade", "battle")
    interaction_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- When the interaction occurred
    FOREIGN KEY (player_id) REFERENCES Players(player_id) ON DELETE CASCADE,
    FOREIGN KEY (interacted_with) REFERENCES Players(player_id) ON DELETE CASCADE
);

-- ==========================================
-- Indexes for Performance Optimization
-- ==========================================
CREATE INDEX idx_username ON Players(username);
CREATE INDEX idx_player_id ON Resources(player_id);
CREATE INDEX idx_interaction_time ON PlayerInteractions(interaction_time);
```
