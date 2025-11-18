"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://futurespaceinvestment.com
Prompt: Create a database schema in SQL to store user data, investment plans, daily profits, and referral commissions for a platform like FutureSpaceInvestments.
Generated: DETERMINISTIC_f5c0d2d91362c8c3
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for FutureSpaceInvestments

-- Drop existing tables if they exist to avoid conflicts during development
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS investment_plans;
DROP TABLE IF EXISTS daily_profits;
DROP TABLE IF EXISTS referral_commissions;

-- Table to store user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,                   -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,        -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE,          -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL,         -- Hashed password for user authentication
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the user was created
);

-- Table to store investment plans
CREATE TABLE investment_plans (
    plan_id SERIAL PRIMARY KEY,                   -- Unique identifier for each investment plan
    plan_name VARCHAR(100) NOT NULL,             -- Name of the investment plan
    min_investment DECIMAL(10, 2) NOT NULL,      -- Minimum investment amount for the plan
    max_investment DECIMAL(10, 2) NOT NULL,      -- Maximum investment amount for the plan
    daily_profit_rate DECIMAL(5, 4) NOT NULL,    -- Daily profit rate (as a percentage)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the plan was created
);

-- Table to store daily profits for users
CREATE TABLE daily_profits (
    profit_id SERIAL PRIMARY KEY,                 -- Unique identifier for each profit record
    user_id INT NOT NULL,                         -- Foreign key referencing the user
    plan_id INT NOT NULL,                         -- Foreign key referencing the investment plan
    date DATE NOT NULL,                           -- Date of the profit record
    profit_amount DECIMAL(10, 2) NOT NULL,       -- Amount of profit earned on that day
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (plan_id) REFERENCES investment_plans(plan_id) ON DELETE CASCADE, -- Foreign key constraint
    UNIQUE (user_id, plan_id, date)              -- Ensure one profit record per user, plan, and day
);

-- Table to store referral commissions for users
CREATE TABLE referral_commissions (
    commission_id SERIAL PRIMARY KEY,             -- Unique identifier for each commission record
    referrer_id INT NOT NULL,                     -- Foreign key referencing the referrer (user)
    referred_user_id INT NOT NULL,                -- Foreign key referencing the referred user
    commission_amount DECIMAL(10, 2) NOT NULL,   -- Amount of commission earned
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the commission was created
    FOREIGN KEY (referrer_id) REFERENCES users(user_id) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (referred_user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Comments on table relationships:
-- 1. The `users` table acts as the central hub for user information.
-- 2. The `investment_plans` table allows the platform to define different investment options.
-- 3. The `daily_profits` table tracks daily earnings for each user based on their chosen investment plan.
-- 4. The `referral_commissions` table records commissions earned by users who refer others to the platform.
```
