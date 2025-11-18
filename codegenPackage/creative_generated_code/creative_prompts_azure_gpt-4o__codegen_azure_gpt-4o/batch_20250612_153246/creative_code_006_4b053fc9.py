"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blogdotrabalhadordigital.com
Prompt: Create a database schema for managing user accounts, game statistics, and bonus claims for an online gaming platform similar to Pelangi189.
Generated: DETERMINISTIC_4b053fc91ad4d9d0
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing user accounts, game statistics, and bonus claims

-- Create the users table to store account information
CREATE TABLE users (
    user_id BIGINT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,       -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE,         -- Unique email for contact purposes
    password_hash VARCHAR(255) NOT NULL,        -- Hashed password for security
    date_joined TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the user joined
    last_login TIMESTAMP NULL,                  -- Timestamp of the last login
    is_active BOOLEAN DEFAULT TRUE              -- Flag to indicate if the user account is active
);

-- Create the game_statistics table to store users' game data
CREATE TABLE game_statistics (
    stat_id BIGINT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each statistic entry
    user_id BIGINT NOT NULL,                    -- Foreign key referencing the users table
    game_name VARCHAR(100) NOT NULL,            -- Name of the game played
    games_played INT DEFAULT 0,                 -- Number of games played by the user
    games_won INT DEFAULT 0,                    -- Number of games won by the user
    total_score INT DEFAULT 0,                  -- Total score accumulated by the user
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last update
    FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Create the bonus_claims table to manage user bonus claim records
CREATE TABLE bonus_claims (
    claim_id BIGINT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each bonus claim
    user_id BIGINT NOT NULL,                    -- Foreign key referencing the users table
    bonus_type VARCHAR(50) NOT NULL,            -- Type of bonus claimed (e.g., "welcome_bonus", "daily_bonus")
    claim_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the bonus was claimed
    amount DECIMAL(10, 2) NOT NULL,             -- Amount of the bonus
    is_redeemed BOOLEAN DEFAULT FALSE,          -- Flag to indicate if the bonus has been redeemed
    FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Create indexes for faster lookups
CREATE INDEX idx_username ON users (username);
CREATE INDEX idx_user_id ON game_statistics (user_id);
CREATE INDEX idx_bonus_user_id ON bonus_claims (user_id);

-- Add constraints for data integrity
ALTER TABLE game_statistics
ADD CONSTRAINT chk_games_played CHECK (games_played >= 0);
ALTER TABLE game_statistics
ADD CONSTRAINT chk_games_won CHECK (games_won >= 0 AND games_won <= games_played);
ALTER TABLE bonus_claims
ADD CONSTRAINT chk_amount CHECK (amount > 0);

-- End of schema
```
