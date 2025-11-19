"""
Generated Code Metadata:
========================
Original URL: https://top-trading.fund
Prompt: Design a database schema in SQL for Top Trading to manage user accounts, investment plans, referral income, and withdrawal transactions securely.
Generated: DETERMINISTIC_65922981f45f36b2
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Top Trading

-- Create a table to store user accounts
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for each user
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE, -- Unique email for each user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store investment plans
CREATE TABLE investment_plans (
    plan_id SERIAL PRIMARY KEY, -- Unique identifier for each investment plan
    plan_name VARCHAR(100) NOT NULL, -- Name of the investment plan
    min_investment DECIMAL(10, 2) NOT NULL, -- Minimum investment amount
    max_investment DECIMAL(10, 2) NOT NULL, -- Maximum investment amount
    interest_rate DECIMAL(5, 2) NOT NULL, -- Interest rate for the plan
    duration_months INT NOT NULL, -- Duration of the investment in months
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of plan creation
);

-- Create a table to store referral income
CREATE TABLE referral_income (
    referral_id SERIAL PRIMARY KEY, -- Unique identifier for each referral record
    referrer_id INT NOT NULL, -- User ID of the referrer
    referred_user_id INT NOT NULL, -- User ID of the referred user
    income DECIMAL(10, 2) NOT NULL, -- Amount of income earned from the referral
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of income record
    FOREIGN KEY (referrer_id) REFERENCES users(user_id) ON DELETE CASCADE, -- Foreign key to users table
    FOREIGN KEY (referred_user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Foreign key to users table
);

-- Create a table to store withdrawal transactions
CREATE TABLE withdrawals (
    withdrawal_id SERIAL PRIMARY KEY, -- Unique identifier for each withdrawal
    user_id INT NOT NULL, -- User ID of the account making the withdrawal
    amount DECIMAL(10, 2) NOT NULL, -- Amount to be withdrawn
    status VARCHAR(20) NOT NULL CHECK (status IN ('pending', 'completed', 'failed')), -- Status of the withdrawal
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of withdrawal request
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Foreign key to users table
);

-- Create an index on the username and email for faster lookups
CREATE INDEX idx_username ON users(username);
CREATE INDEX idx_email ON users(email);
```
