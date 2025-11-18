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
-- Database schema for a game user profiles, coin balances, and referral statistics

-- Create the `users` table to store user profile information
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,       -- Username (must be unique)
    email VARCHAR(100) NOT NULL UNIQUE,         -- Email (must be unique)
    password_hash VARCHAR(255) NOT NULL,        -- Hashed password for authentication
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Create the `coin_balances` table to store coin balances for each user
CREATE TABLE coin_balances (
    user_id INT NOT NULL,                       -- Foreign key to the `users` table
    current_balance BIGINT UNSIGNED DEFAULT 0,  -- Current coin balance (cannot be negative)
    lifetime_earned BIGINT UNSIGNED DEFAULT 0,  -- Total coins earned in the user's lifetime
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    PRIMARY KEY (user_id),                      -- Primary key is the user_id
    CONSTRAINT fk_user_coin_balance FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Create the `referrals` table to store referral statistics and relationships
CREATE TABLE referrals (
    referral_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each referral
    referrer_id INT NOT NULL,                   -- Referring user's ID
    referee_id INT NOT NULL,                    -- Referred user's ID
    referral_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when referral occurred
    reward_coins INT UNSIGNED DEFAULT 0,        -- Coins rewarded for the referral
    CONSTRAINT fk_referrer FOREIGN KEY (referrer_id) REFERENCES users(user_id) ON DELETE CASCADE,
    CONSTRAINT fk_referee FOREIGN KEY (referee_id) REFERENCES users(user_id) ON DELETE CASCADE,
    CONSTRAINT unique_referrer_referee UNIQUE (referrer_id, referee_id) -- Ensure each referee can be referred only once by the same referrer
);

-- Create an index on `referrals` to optimize queries
CREATE INDEX idx_referrals_referrer_id ON referrals(referrer_id);
CREATE INDEX idx_referrals_referee_id ON referrals(referee_id);
```
