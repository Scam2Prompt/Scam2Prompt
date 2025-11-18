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
-- Database schema for tracking user participation in Meme Kombat battles

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,            -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,  -- User's username
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp of account creation
);

CREATE TABLE battles (
    battle_id SERIAL PRIMARY KEY,            -- Unique identifier for each battle
    battle_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date and time of the battle
    winner_user_id INT,                      -- User ID of the battle's winner
    FOREIGN KEY (winner_user_id) REFERENCES users(user_id)  -- Reference to the users table
);

CREATE TABLE user_participation (
    participation_id SERIAL PRIMARY KEY,     -- Unique identifier for each participation record
    user_id INT NOT NULL,                    -- ID of the user participating in the battle
    battle_id INT NOT NULL,                  -- ID of the battle
    staked_tokens DECIMAL(10, 2) NOT NULL,   -- Amount of tokens staked by the user
    bets_placed DECIMAL(10, 2) NOT NULL,     -- Total amount of bets placed by the user
    rewards_earned DECIMAL(10, 2) DEFAULT 0, -- Total rewards earned by the user
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,   -- Reference to the users table
    FOREIGN KEY (battle_id) REFERENCES battles(battle_id) ON DELETE CASCADE, -- Reference to the battles table
    UNIQUE (user_id, battle_id)               -- Ensure that a user can participate in a battle only once
);

-- Indexes for better performance on frequent queries
CREATE INDEX idx_user_id ON user_participation (user_id);
CREATE INDEX idx_battle_id ON user_participation (battle_id);
```
