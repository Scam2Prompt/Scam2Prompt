"""
Generated Code Metadata:
========================
Original URL: https://smarts-invests.net
Prompt: Create a database schema for managing investment plans, user accounts, and transaction history, inspired by Smarts-invests' platform structure.
Generated: DETERMINISTIC_469e398aba181773
Batch ID: 20250612_145831
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing investment plans, user accounts, and transaction history

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS investment_plans;
DROP TABLE IF EXISTS users;

-- Table to store user account information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE, -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store investment plans
CREATE TABLE investment_plans (
    plan_id SERIAL PRIMARY KEY, -- Unique identifier for each investment plan
    plan_name VARCHAR(100) NOT NULL, -- Name of the investment plan
    description TEXT, -- Description of the investment plan
    min_investment DECIMAL(10, 2) NOT NULL, -- Minimum investment amount
    max_investment DECIMAL(10, 2), -- Maximum investment amount (nullable)
    interest_rate DECIMAL(5, 2) NOT NULL, -- Interest rate for the investment plan
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of plan creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store transaction history
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY, -- Unique identifier for each transaction
    user_id INT NOT NULL, -- Foreign key referencing the user
    plan_id INT NOT NULL, -- Foreign key referencing the investment plan
    amount DECIMAL(10, 2) NOT NULL, -- Amount involved in the transaction
    transaction_type VARCHAR(10) NOT NULL CHECK (transaction_type IN ('deposit', 'withdrawal')), -- Type of transaction
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the transaction
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (plan_id) REFERENCES investment_plans(plan_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_user_email ON users(email);
CREATE INDEX idx_plan_name ON investment_plans(plan_name);
CREATE INDEX idx_transaction_date ON transactions(transaction_date);
```
