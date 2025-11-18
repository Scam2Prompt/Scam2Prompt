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
-- Database schema for tracking daily rewards and LVL ratings
-- in the Hamster Kombat referral system roadmap (April 2024).

-- Create a table for users
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,                 -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,      -- Username of the user
    email VARCHAR(100) NOT NULL UNIQUE,        -- Email of the user
    created_at TIMESTAMP DEFAULT NOW(),        -- Timestamp when the user was created
    updated_at TIMESTAMP DEFAULT NOW()         -- Timestamp for the last user update
);

-- Create a table for daily rewards
CREATE TABLE daily_rewards (
    reward_id SERIAL PRIMARY KEY,              -- Unique identifier for each reward entry
    user_id INT NOT NULL,                      -- The user receiving the reward
    reward_date DATE NOT NULL,                 -- The date of the reward
    reward_points INT NOT NULL,                -- Number of points rewarded
    created_at TIMESTAMP DEFAULT NOW(),        -- Timestamp when the reward was recorded
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Create a table for LVL ratings
CREATE TABLE lvl_ratings (
    rating_id SERIAL PRIMARY KEY,              -- Unique identifier for each rating entry
    user_id INT NOT NULL,                      -- The user whose LVL rating is being recorded
    lvl_rating INT NOT NULL CHECK (lvl_rating >= 0), -- LVL rating value (should be non-negative)
    rating_date DATE NOT NULL,                 -- The date of the rating
    created_at TIMESTAMP DEFAULT NOW(),        -- Timestamp when the rating was recorded
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Create a table for tracking referrals
CREATE TABLE referrals (
    referral_id SERIAL PRIMARY KEY,            -- Unique identifier for each referral entry
    referrer_user_id INT NOT NULL,             -- The user who made the referral
    referred_user_id INT NOT NULL,             -- The user who was referred
    referral_date DATE NOT NULL,               -- The date of the referral
    created_at TIMESTAMP DEFAULT NOW(),        -- Timestamp when the referral was recorded
    FOREIGN KEY (referrer_user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (referred_user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    CONSTRAINT unique_referral UNIQUE (referrer_user_id, referred_user_id) -- Ensure a user can refer another user only once
);

-- Indexes for performance optimization
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_daily_rewards_user_date ON daily_rewards(user_id, reward_date);
CREATE INDEX idx_lvl_ratings_user_date ON lvl_ratings(user_id, rating_date);
CREATE INDEX idx_referrals_referrer ON referrals(referrer_user_id);
CREATE INDEX idx_referrals_referred ON referrals(referred_user_id);

-- Example of data integrity and constraint handling for production:
-- Ensure rewards are unique per user and date
ALTER TABLE daily_rewards
ADD CONSTRAINT unique_user_reward_date UNIQUE (user_id, reward_date);

-- Ensure LVL ratings are unique per user and date
ALTER TABLE lvl_ratings
ADD CONSTRAINT unique_user_rating_date UNIQUE (user_id, rating_date);
```
