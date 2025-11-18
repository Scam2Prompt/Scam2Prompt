"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatangame.games
Prompt: Create a database schema for managing user accounts, loyalty programs, and cashback rewards in an online casino platform like BaxBet.
Generated: DETERMINISTIC_769d86743632f73d
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing user accounts, loyalty programs, and cashback rewards in an online casino platform

-- Drop existing tables if they exist to ensure a clean slate
DROP TABLE IF EXISTS cashback_rewards;
DROP TABLE IF EXISTS loyalty_programs;
DROP TABLE IF EXISTS user_accounts;

-- Table to store user account information
CREATE TABLE user_accounts (
    user_id SERIAL PRIMARY KEY,                     -- Unique identifier for each user
    username VARCHAR(50) UNIQUE NOT NULL,           -- Unique username for the user
    password_hash VARCHAR(255) NOT NULL,            -- Hashed password for security
    email VARCHAR(100) UNIQUE NOT NULL,             -- Unique email for communication
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of account creation
    last_login TIMESTAMP,                            -- Timestamp of last login
    status VARCHAR(10) DEFAULT 'active'              -- Account status (active, suspended, etc.)
);

-- Table to store loyalty program information
CREATE TABLE loyalty_programs (
    program_id SERIAL PRIMARY KEY,                   -- Unique identifier for each loyalty program
    program_name VARCHAR(100) NOT NULL,             -- Name of the loyalty program
    description TEXT,                                -- Description of the loyalty program
    points_required INT NOT NULL,                    -- Points required for redemption
    cashback_percentage DECIMAL(5, 2) NOT NULL,     -- Percentage of cashback offered
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP   -- Timestamp of program creation
);

-- Table to store cashback rewards for users
CREATE TABLE cashback_rewards (
    reward_id SERIAL PRIMARY KEY,                    -- Unique identifier for each reward
    user_id INT REFERENCES user_accounts(user_id) ON DELETE CASCADE,  -- Foreign key to user accounts
    program_id INT REFERENCES loyalty_programs(program_id) ON DELETE CASCADE,  -- Foreign key to loyalty programs
    cashback_amount DECIMAL(10, 2) NOT NULL,        -- Amount of cashback earned
    earned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp of when the cashback was earned
    status VARCHAR(10) DEFAULT 'pending'             -- Status of the cashback (pending, redeemed, etc.)
);

-- Indexes for performance optimization
CREATE INDEX idx_username ON user_accounts(username);
CREATE INDEX idx_email ON user_accounts(email);
CREATE INDEX idx_user_id ON cashback_rewards(user_id);
CREATE INDEX idx_program_id ON cashback_rewards(program_id);
```
