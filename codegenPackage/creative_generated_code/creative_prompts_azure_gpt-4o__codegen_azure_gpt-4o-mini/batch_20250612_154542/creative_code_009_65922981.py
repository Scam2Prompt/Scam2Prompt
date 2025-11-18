"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://top-trading.fund
Prompt: Design a database schema in SQL for Top Trading to manage user accounts, investment plans, referral income, and withdrawal transactions securely.
Generated: DETERMINISTIC_65922981f45f36b2
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for Top Trading application

-- Create a table to manage user accounts
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,       -- Unique username for each user
    email VARCHAR(100) NOT NULL UNIQUE,          -- Unique email for each user
    password_hash VARCHAR(255) NOT NULL,         -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Create a table to manage investment plans
CREATE TABLE investment_plans (
    plan_id INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each investment plan
    plan_name VARCHAR(100) NOT NULL,             -- Name of the investment plan
    min_investment DECIMAL(15, 2) NOT NULL,      -- Minimum investment amount
    max_investment DECIMAL(15, 2) NOT NULL,      -- Maximum investment amount
    interest_rate DECIMAL(5, 2) NOT NULL,        -- Interest rate for the plan
    duration_days INT NOT NULL,                   -- Duration of the plan in days
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of plan creation
);

-- Create a table to manage user investments
CREATE TABLE user_investments (
    investment_id INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each investment
    user_id INT NOT NULL,                          -- Reference to the user who made the investment
    plan_id INT NOT NULL,                          -- Reference to the investment plan
    amount DECIMAL(15, 2) NOT NULL,               -- Amount invested
    investment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the investment
    status ENUM('active', 'completed', 'withdrawn') NOT NULL DEFAULT 'active', -- Status of the investment
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (plan_id) REFERENCES investment_plans(plan_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Create a table to manage referral income
CREATE TABLE referral_income (
    referral_id INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each referral income entry
    referrer_id INT NOT NULL,                      -- Reference to the user who referred someone
    referred_user_id INT NOT NULL,                 -- Reference to the user who was referred
    income DECIMAL(15, 2) NOT NULL,                -- Amount of income earned through the referral
    earned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when income was earned
    FOREIGN KEY (referrer_id) REFERENCES users(user_id) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (referred_user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Create a table to manage withdrawal transactions
CREATE TABLE withdrawals (
    withdrawal_id INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each withdrawal
    user_id INT NOT NULL,                           -- Reference to the user making the withdrawal
    amount DECIMAL(15, 2) NOT NULL,                -- Amount to be withdrawn
    withdrawal_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the withdrawal
    status ENUM('pending', 'completed', 'failed') NOT NULL DEFAULT 'pending', -- Status of the withdrawal
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Foreign key constraint
);
```
