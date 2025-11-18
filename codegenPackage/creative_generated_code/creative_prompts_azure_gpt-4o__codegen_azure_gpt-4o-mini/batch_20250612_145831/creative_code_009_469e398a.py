"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smarts-invests.net
Prompt: Create a database schema for managing investment plans, user accounts, and transaction history, inspired by Smarts-invests' platform structure.
Generated: DETERMINISTIC_469e398aba181773
Batch ID: 20250612_145831
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing investment plans, user accounts, and transaction history

-- Drop existing tables if they exist for refresh purposes
DROP TABLE IF EXISTS transactions CASCADE;
DROP TABLE IF EXISTS investment_plans CASCADE;
DROP TABLE IF EXISTS users CASCADE;

-- Table for user accounts
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,                -- Unique identifier for each user
    username VARCHAR(50) UNIQUE NOT NULL,     -- Unique username for the user
    password_hash VARCHAR(255) NOT NULL,      -- Securely stored password hash
    email VARCHAR(100) UNIQUE NOT NULL,       -- Unique email address for communication
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last updated timestamp
    is_active BOOLEAN DEFAULT TRUE             -- Status of the user account
);

-- Table for investment plans
CREATE TABLE investment_plans (
    plan_id SERIAL PRIMARY KEY,                 -- Unique identifier for each investment plan
    plan_name VARCHAR(100) NOT NULL,           -- Name of the investment plan
    description TEXT,                           -- Description of the investment plan
    min_investment DECIMAL(10, 2) NOT NULL,    -- Minimum investment required for the plan
    max_investment DECIMAL(10, 2) NOT NULL,    -- Maximum investment allowed for the plan
    interest_rate DECIMAL(5, 2) NOT NULL,      -- Annual interest rate for the investment plan
    duration_months INT NOT NULL,               -- Duration of the investment in months
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Plan creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Last updated timestamp
);

-- Table for transaction history
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,          -- Unique identifier for each transaction
    user_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE, -- Reference to the user
    investment_plan_id INT NOT NULL REFERENCES investment_plans(plan_id) ON DELETE CASCADE, -- Reference to the investment plan
    transaction_type VARCHAR(10) NOT NULL CHECK (transaction_type IN ('deposit', 'withdrawal')), -- Type of transaction
    amount DECIMAL(10, 2) NOT NULL,             -- Amount involved in the transaction
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the transaction
    status VARCHAR(20) DEFAULT 'completed' CHECK (status IN ('completed', 'pending', 'failed')) -- Status of the transaction
);

-- Optional: Create indexes for improved performance
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_transactions_user ON transactions(user_id);
CREATE INDEX idx_transactions_plan ON transactions(investment_plan_id);
```
