"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerinde.com
Prompt: Design a database schema in SQL to store user profiles, coin balances, and referral statistics for a game similar to TG WebApp Euro Verdienen.
Generated: DETERMINISTIC_7839adb9ad6d4517
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for user profiles, coin balances, and referral statistics

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS referral_stats;
DROP TABLE IF EXISTS coin_balances;
DROP TABLE IF EXISTS user_profiles;

-- Create a table to store user profiles
CREATE TABLE user_profiles (
    user_id SERIAL PRIMARY KEY,           -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE,   -- User's email address
    password_hash VARCHAR(255) NOT NULL,   -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user profile was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store coin balances for each user
CREATE TABLE coin_balances (
    balance_id SERIAL PRIMARY KEY,          -- Unique identifier for the balance entry
    user_id INT NOT NULL,                   -- Foreign key to link to user_profiles
    coins INT DEFAULT 0,                    -- Current coin balance for the user
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for last balance update
    FOREIGN KEY (user_id) REFERENCES user_profiles(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store referral statistics
CREATE TABLE referral_stats (
    referral_id SERIAL PRIMARY KEY,         -- Unique identifier for each referral entry
    referrer_id INT NOT NULL,               -- The user who made the referral
    referred_id INT NOT NULL,                -- The user who was referred
    referral_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the referral was made
    FOREIGN KEY (referrer_id) REFERENCES user_profiles(user_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (referred_id) REFERENCES user_profiles(user_id) ON DELETE CASCADE, -- Ensure referential integrity
    UNIQUE (referrer_id, referred_id)       -- Ensure one referral per user pair
);

-- Indexes can be added for optimization purposes
CREATE INDEX idx_username ON user_profiles(username);
CREATE INDEX idx_email ON user_profiles(email);
CREATE INDEX idx_user_id ON coin_balances(user_id);
CREATE INDEX idx_referrer ON referral_stats(referrer_id);
CREATE INDEX idx_referred ON referral_stats(referred_id);

-- End of SQL script
```
