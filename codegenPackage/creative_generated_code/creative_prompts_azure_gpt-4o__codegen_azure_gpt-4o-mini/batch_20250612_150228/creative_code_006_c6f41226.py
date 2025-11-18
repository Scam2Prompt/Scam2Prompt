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

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,        -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username of the user
    email VARCHAR(100) NOT NULL UNIQUE,   -- Unique email address of the user
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for user authentication
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the user was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

CREATE TABLE daily_check_ins (
    check_in_id SERIAL PRIMARY KEY,    -- Unique identifier for each check-in
    user_id INT NOT NULL,               -- Identifier for the user who checked in
    check_in_date DATE NOT NULL,        -- Date of the check-in
    reward_points INT DEFAULT 0,        -- Reward points earned for the check-in
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

CREATE TABLE rewards_claimed (
    reward_id SERIAL PRIMARY KEY,       -- Unique identifier for each claimed reward
    user_id INT NOT NULL,               -- Identifier for the user who claimed the reward
    reward_type VARCHAR(50) NOT NULL,   -- Type of reward claimed
    claimed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the reward was claimed
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

CREATE TABLE referral_bonuses (
    bonus_id SERIAL PRIMARY KEY,         -- Unique identifier for each referral bonus
    referrer_id INT NOT NULL,           -- Identifier for the user who referred someone
    referred_user_id INT NOT NULL,      -- Identifier for the referred user
    bonus_amount DECIMAL(10, 2) NOT NULL, -- Bonus amount earned for the referral
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the referral bonus was created
    FOREIGN KEY (referrer_id) REFERENCES users(user_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (referred_user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);
```
