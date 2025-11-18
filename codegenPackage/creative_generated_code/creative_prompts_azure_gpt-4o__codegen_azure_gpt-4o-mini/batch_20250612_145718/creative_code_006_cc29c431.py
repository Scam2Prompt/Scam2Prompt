"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamsbat.com
Prompt: Create a database schema for tracking daily rewards and LVL ratings as outlined in the Hamster Kombat referral system roadmap for April 2024.
Generated: DETERMINISTIC_cc29c43137eaeb41
Batch ID: 20250612_145718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for tracking daily rewards and LVL ratings in Hamster Kombat referral system

-- Create a table for Users
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- User's chosen username
    email VARCHAR(100) NOT NULL UNIQUE,   -- User's email address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table for Rewards
CREATE TABLE Rewards (
    reward_id SERIAL PRIMARY KEY,        -- Unique identifier for each reward
    user_id INT NOT NULL,                -- Reference to the user receiving the reward
    reward_date DATE NOT NULL,           -- Date when the reward was granted
    reward_type VARCHAR(50) NOT NULL,    -- Type of reward (e.g., points, items)
    amount INT NOT NULL CHECK (amount >= 0), -- Amount of the reward (should be non-negative)
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensures integrity of user-reward relationship
);

-- Create a table for LVL ratings
CREATE TABLE LevelRatings (
    level_id SERIAL PRIMARY KEY,         -- Unique identifier for each level rating
    user_id INT NOT NULL,                -- Reference to the user with the rating
    level INT NOT NULL CHECK (level >= 0), -- Current level of the user (should be non-negative)
    rating_date DATE NOT NULL,           -- Date when the rating was recorded
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensures integrity of user-level relationship
);

-- Create a table for tracking referral actions
CREATE TABLE Referrals (
    referral_id SERIAL PRIMARY KEY,       -- Unique identifier for each referral
    referrer_id INT NOT NULL,            -- User who referred another user
    referred_id INT NOT NULL,             -- User who was referred
    referral_date DATE NOT NULL,          -- Date of the referral
    FOREIGN KEY (referrer_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Ensures integrity of referrer relationship
    FOREIGN KEY (referred_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensures integrity of referred relationship
);

-- Create an index for quick lookup of user rewards by date
CREATE INDEX idx_user_rewards ON Rewards(user_id, reward_date);

-- Create an index for quick lookup of user level ratings by date
CREATE INDEX idx_user_levels ON LevelRatings(user_id, rating_date);
```
