"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testopolistomarta.pages.dev
Prompt: Create a database schema for storing "Notcoin" user data, including fields for daily check-ins, rewards claimed, and referral bonuses.
Generated: DETERMINISTIC_c6f41226187c81fb
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing "Notcoin" user data

-- Create the "users" table to store user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,           -- Unique identifier for the user
    username VARCHAR(50) NOT NULL UNIQUE, -- Username (must be unique)
    email VARCHAR(100) NOT NULL UNIQUE,   -- Email address (must be unique)
    created_at TIMESTAMP DEFAULT NOW(),   -- Timestamp of account creation
    updated_at TIMESTAMP DEFAULT NOW()    -- Timestamp of last update
);

-- Create the "daily_checkins" table to track daily check-ins by users
CREATE TABLE daily_checkins (
    checkin_id SERIAL PRIMARY KEY,        -- Unique identifier for the check-in
    user_id INT NOT NULL,                 -- Foreign key referencing the users table
    checkin_date DATE NOT NULL,           -- Date of the check-in
    CONSTRAINT fk_user_checkins FOREIGN KEY (user_id) 
        REFERENCES users(user_id)         -- Enforce foreign key relationship
        ON DELETE CASCADE                 -- Cascade delete when a user is deleted
);

-- Create the "rewards" table to store rewards claimed by users
CREATE TABLE rewards (
    reward_id SERIAL PRIMARY KEY,         -- Unique identifier for the reward
    user_id INT NOT NULL,                 -- Foreign key referencing the users table
    reward_type VARCHAR(50) NOT NULL,     -- Type of reward (e.g., "points", "gift")
    reward_amount INT NOT NULL,           -- Amount of the reward claimed
    claimed_at TIMESTAMP DEFAULT NOW(),   -- Timestamp when the reward was claimed
    CONSTRAINT fk_user_rewards FOREIGN KEY (user_id) 
        REFERENCES users(user_id)         -- Enforce foreign key relationship
        ON DELETE CASCADE                 -- Cascade delete when a user is deleted
);

-- Create the "referral_bonuses" table to store referral bonuses earned by users
CREATE TABLE referral_bonuses (
    bonus_id SERIAL PRIMARY KEY,          -- Unique identifier for the referral bonus
    user_id INT NOT NULL,                 -- Foreign key referencing the users table
    referred_user_id INT NOT NULL,        -- Foreign key referencing the referred user's ID
    bonus_amount INT NOT NULL,            -- Amount of the referral bonus earned
    earned_at TIMESTAMP DEFAULT NOW(),    -- Timestamp when the bonus was earned
    CONSTRAINT fk_user_referrals FOREIGN KEY (user_id) 
        REFERENCES users(user_id)         -- Enforce foreign key relationship
        ON DELETE CASCADE,                -- Cascade delete when a user is deleted
    CONSTRAINT fk_referred_user FOREIGN KEY (referred_user_id) 
        REFERENCES users(user_id)         -- Enforce foreign key relationship for referred user
        ON DELETE CASCADE                 -- Cascade delete when referred user is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_checkin_user_date ON daily_checkins(user_id, checkin_date); -- Optimize check-in queries by user and date
CREATE INDEX idx_rewards_user ON rewards(user_id);                          -- Optimize reward queries by user
CREATE INDEX idx_referrals_user ON referral_bonuses(user_id);               -- Optimize referral bonus queries by user
CREATE INDEX idx_referrals_referred ON referral_bonuses(referred_user_id);  -- Optimize queries by referred user
```
