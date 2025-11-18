"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memekombatioclaim.pages.dev
Prompt: Design a database schema for tracking user participation in Meme Kombat battles, including fields for user ID, staked tokens, bets placed, and rewards earned.
Generated: DETERMINISTIC_99acc1a947b16696
Batch ID: 20250612_150622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema: Meme Kombat User Participation Tracking

-- Table: Users
-- Stores user information
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each user
    username VARCHAR(100) NOT NULL,         -- Username of the user
    email VARCHAR(255) UNIQUE NOT NULL,     -- Email address of the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the user record was created
);

-- Table: Battles
-- Stores information about Meme Kombat battles
CREATE TABLE Battles (
    battle_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each battle
    battle_name VARCHAR(255) NOT NULL,        -- Name or description of the battle
    start_time TIMESTAMP NOT NULL,            -- Start time of the battle
    end_time TIMESTAMP,                       -- End time of the battle (nullable for ongoing battles)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the battle record was created
);

-- Table: Participation
-- Tracks user participation in Meme Kombat battles
CREATE TABLE Participation (
    participation_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each participation entry
    user_id INT NOT NULL,                            -- Foreign key referencing Users(user_id)
    battle_id INT NOT NULL,                          -- Foreign key referencing Battles(battle_id)
    staked_tokens DECIMAL(18, 8) NOT NULL,           -- The number of tokens staked by the user
    bet_placed VARCHAR(255) NOT NULL,               -- Description of the bet placed by the user
    reward_earned DECIMAL(18, 8) DEFAULT 0,         -- Rewards earned by the user (default is 0)
    participation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Time of participation
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (battle_id) REFERENCES Battles(battle_id) ON DELETE CASCADE,
    INDEX (user_id),
    INDEX (battle_id)
);

-- Additional Notes:
-- Ensure proper indexing for performance optimization on user_id and battle_id fields.
-- Use appropriate permissions and encryption mechanisms to secure sensitive user data.
-- Regularly monitor and backup the database for reliability and data integrity.
```
