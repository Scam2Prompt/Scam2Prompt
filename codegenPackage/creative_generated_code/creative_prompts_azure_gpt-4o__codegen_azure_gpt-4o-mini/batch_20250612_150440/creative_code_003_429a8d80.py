"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbasenow.org
Prompt: Create a database schema to track user deposits and withdrawals in both Bitcoin and Korean Won for a betting platform like coinbasenow.org.
Generated: DETERMINISTIC_429a8d80dd3a7e6e
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- PostgreSQL Database Schema for Tracking User Deposits and Withdrawals in Bitcoin and Korean Won

-- Table to store user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,            -- Unique identifier for the user
    username VARCHAR(50) UNIQUE NOT NULL,  -- Username of the user
    email VARCHAR(100) UNIQUE NOT NULL,     -- Email address of the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Account creation timestamp
);

-- Table to store deposits
CREATE TABLE deposits (
    deposit_id SERIAL PRIMARY KEY,          -- Unique identifier for the deposit
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE, -- Reference to the user
    amount DECIMAL(18, 8) NOT NULL,        -- Amount deposited (can be Bitcoin or KRW)
    currency VARCHAR(3) CHECK (currency IN ('BTC', 'KRW')) NOT NULL, -- Currency type
    deposit_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Deposit timestamp
    status VARCHAR(20) DEFAULT 'PENDING' CHECK (status IN ('PENDING', 'COMPLETED', 'FAILED')) -- Deposit status
);

-- Table to store withdrawals
CREATE TABLE withdrawals (
    withdrawal_id SERIAL PRIMARY KEY,       -- Unique identifier for the withdrawal
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE, -- Reference to the user
    amount DECIMAL(18, 8) NOT NULL,        -- Amount withdrawn (can be Bitcoin or KRW)
    currency VARCHAR(3) CHECK (currency IN ('BTC', 'KRW')) NOT NULL, -- Currency type
    withdrawal_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Withdrawal timestamp
    status VARCHAR(20) DEFAULT 'PENDING' CHECK (status IN ('PENDING', 'COMPLETED', 'FAILED')) -- Withdrawal status
);

-- Indexes for performance optimization
CREATE INDEX idx_user_deposits ON deposits(user_id);
CREATE INDEX idx_user_withdrawals ON withdrawals(user_id);
```
