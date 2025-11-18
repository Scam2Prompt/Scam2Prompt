"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reward-nyanheroes.pages.dev
Prompt: Create a database schema to store user activity, mission completion data, and referral tracking for a blockchain-based platform like Nyan Heroes.
Generated: DETERMINISTIC_23e5d2d376798a2f
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Database Schema
-- This schema is designed to store user activity, mission completion data,
-- and referral tracking for a blockchain-based platform.

-- Users table: Stores information about the users
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,            -- Unique identifier for each user
    wallet_address VARCHAR(255) NOT NULL, -- Blockchain wallet address
    username VARCHAR(50) NOT NULL,        -- Unique username
    email VARCHAR(100),                   -- Optional email for the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date the account was created
);

-- Activity Logs table: Records user actions/activity on the platform
CREATE TABLE ActivityLogs (
    log_id SERIAL PRIMARY KEY,            -- Unique identifier for each activity log
    user_id INT REFERENCES Users(user_id) ON DELETE CASCADE, -- Relates activity log to a user
    activity_type VARCHAR(50) NOT NULL,   -- Type of activity (e.g., login, transaction)
    activity_details TEXT,                -- Additional data/details about the activity
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- When the activity occurred
);

-- Missions table: Stores the missions available on the platform
CREATE TABLE Missions (
    mission_id SERIAL PRIMARY KEY,        -- Unique identifier for each mission
    mission_name VARCHAR(100) NOT NULL,  -- Name of the mission
    description TEXT,                     -- Detailed description of the mission
    reward_amount NUMERIC(18, 8) NOT NULL,-- Reward for mission completion (e.g., cryptocurrency)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date the mission was added
);

-- Mission Completion table: Tracks which users have completed which missions
CREATE TABLE MissionCompletion (
    completion_id SERIAL PRIMARY KEY,     -- Unique identifier for each mission completion record
    user_id INT REFERENCES Users(user_id) ON DELETE CASCADE, -- Relates completion record to a user
    mission_id INT REFERENCES Missions(mission_id) ON DELETE CASCADE, -- Relates completion record to a mission
    completion_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- When the mission was completed
    reward_claimed BOOLEAN DEFAULT FALSE -- Indicates if the reward has been claimed
);

-- Referrals table: Tracks referrals made by users
CREATE TABLE Referrals (
    referral_id SERIAL PRIMARY KEY,       -- Unique identifier for each referral record
    referrer_id INT REFERENCES Users(user_id) ON DELETE CASCADE, -- User who referred another user
    referred_id INT REFERENCES Users(user_id) ON DELETE CASCADE, -- User who was referred
    referral_bonus_claimed BOOLEAN DEFAULT FALSE, -- Indicates if the referral bonus has been claimed
    referred_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date the referral was made
);

-- Indexes for performance optimization
CREATE INDEX idx_users_wallet_address ON Users(wallet_address); -- Index for quick lookup by wallet address
CREATE INDEX idx_activitylogs_user_id ON ActivityLogs(user_id); -- Index for user-specific activity queries
CREATE INDEX idx_missioncompletion_user_id ON MissionCompletion(user_id); -- Index for mission completion by user
CREATE INDEX idx_referrals_referrer_id ON Referrals(referrer_id); -- Index for referrer-specific referral queries

-- This schema ensures data integrity through foreign key constraints,
-- uses indexes for performance optimization, and includes fields to track timestamps.
```
