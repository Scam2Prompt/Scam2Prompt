"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tetherusdt.shop
Prompt: Develop a database schema for managing slot game providers like Pragmatic Play, Joker123, Slot88, and Habanero, including game metadata and user statistics.
Generated: DETERMINISTIC_de252559a43e5d25
Batch ID: 20250612_154455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing slot game providers and related metadata

-- Table for game providers
CREATE TABLE game_providers (
    provider_id SERIAL PRIMARY KEY,          -- Unique identifier for the provider
    provider_name VARCHAR(100) NOT NULL,    -- Name of the provider (e.g., Pragmatic Play, Joker123)
    website_url VARCHAR(255),               -- URL to the provider's website
    created_at TIMESTAMP DEFAULT NOW(),     -- Timestamp when the provider was added
    updated_at TIMESTAMP DEFAULT NOW()      -- Timestamp when the provider details were last updated
);

-- Table for slot games
CREATE TABLE slot_games (
    game_id SERIAL PRIMARY KEY,             -- Unique identifier for the slot game
    provider_id INT NOT NULL,               -- Foreign key linking the game to its provider
    game_name VARCHAR(150) NOT NULL,        -- Name of the slot game
    theme VARCHAR(100),                     -- Theme of the slot game (e.g., Adventure, Fantasy)
    volatility_level VARCHAR(50),           -- Volatility level (e.g., Low, Medium, High)
    RTP DECIMAL(5, 2),                      -- Return-to-Player percentage (e.g., 96.50%)
    created_at TIMESTAMP DEFAULT NOW(),     -- Timestamp when the game was added
    updated_at TIMESTAMP DEFAULT NOW(),     -- Timestamp when the game details were last updated
    FOREIGN KEY (provider_id) REFERENCES game_providers(provider_id) ON DELETE CASCADE
);

-- Table for user statistics
CREATE TABLE user_statistics (
    user_id INT NOT NULL,                   -- Unique identifier for the user
    game_id INT NOT NULL,                   -- Foreign key linking the statistics to the game
    total_spins INT DEFAULT 0,              -- Total number of spins the user has made
    total_wagered DECIMAL(10, 2) DEFAULT 0, -- Total amount wagered by the user
    total_won DECIMAL(10, 2) DEFAULT 0,     -- Total amount won by the user
    created_at TIMESTAMP DEFAULT NOW(),     -- Timestamp when the statistics entry was created
    updated_at TIMESTAMP DEFAULT NOW(),     -- Timestamp when the statistics entry was last updated
    PRIMARY KEY (user_id, game_id),         -- Composite key ensuring uniqueness per user-game combination
    FOREIGN KEY (game_id) REFERENCES slot_games(game_id) ON DELETE CASCADE
);

-- Indexes to improve query performance
CREATE INDEX idx_provider_name ON game_providers(provider_name); -- Index for provider name searches
CREATE INDEX idx_game_name ON slot_games(game_name);             -- Index for slot game name searches
CREATE INDEX idx_user_id ON user_statistics(user_id);            -- Index for user statistics by user

-- Example error handling:
-- Ensure all decimal values (RTP, total_wagered, total_won) are non-negative using constraints.
ALTER TABLE slot_games ADD CONSTRAINT chk_rtp_non_negative CHECK (RTP >= 0);
ALTER TABLE user_statistics ADD CONSTRAINT chk_total_wagered_non_negative CHECK (total_wagered >= 0);
ALTER TABLE user_statistics ADD CONSTRAINT chk_total_won_non_negative CHECK (total_won >= 0);
```
