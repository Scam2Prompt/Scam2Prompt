"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coineehub.com
Prompt: Create a database schema in SQL for storing CoineeHub's investment plans, user transactions, and account balances, ensuring scalability and security.
Generated: DETERMINISTIC_7a60a8f3539d9526
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema for CoineeHub

-- Drop existing tables if they exist for re-creation
DROP TABLE IF EXISTS investment_plans CASCADE;
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS transactions CASCADE;
DROP TABLE IF EXISTS account_balances CASCADE;

-- Table for storing user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,            -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for each user
    email VARCHAR(100) NOT NULL UNIQUE,    -- Unique email for each user
    password_hash VARCHAR(255) NOT NULL,   -- Hashed password for secure storage
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table for storing investment plans
CREATE TABLE investment_plans (
    plan_id SERIAL PRIMARY KEY,              -- Unique identifier for each investment plan
    plan_name VARCHAR(100) NOT NULL,         -- Name of the investment plan
    min_investment DECIMAL(15, 2) NOT NULL,  -- Minimum investment amount
    max_investment DECIMAL(15, 2) NOT NULL,  -- Maximum investment amount
    interest_rate DECIMAL(5, 2) NOT NULL,     -- Interest rate for the plan
    duration_days INT NOT NULL,                -- Duration of the investment plan in days
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table for storing user transactions
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,       -- Unique identifier for each transaction
    user_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE, -- Foreign key referencing users
    plan_id INT NOT NULL REFERENCES investment_plans(plan_id) ON DELETE SET NULL, -- Foreign key referencing investment plans
    transaction_type VARCHAR(10) NOT NULL CHECK (transaction_type IN ('deposit', 'withdrawal')), -- Type of transaction
    amount DECIMAL(15, 2) NOT NULL CHECK (amount > 0), -- Amount involved in the transaction
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the transaction
    status VARCHAR(20) NOT NULL DEFAULT 'pending', -- Status of the transaction
    CONSTRAINT unique_user_transaction UNIQUE (user_id, transaction_date) -- Ensure a user can't repeat the same transaction on the same date
);

-- Table for storing user account balances
CREATE TABLE account_balances (
    user_id INT PRIMARY KEY REFERENCES users(user_id) ON DELETE CASCADE, -- Foreign key referencing users
    balance DECIMAL(15, 2) NOT NULL DEFAULT 0.00, -- Current balance of the user account
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Last update timestamp for balance
    CHECK (balance >= 0) -- Ensure balance cannot be negative
);

-- Indexes for performance improvement
CREATE INDEX idx_username ON users(username);
CREATE INDEX idx_email ON users(email);
CREATE INDEX idx_user_transactions ON transactions(user_id);
CREATE INDEX idx_plan_transactions ON transactions(plan_id);
```
