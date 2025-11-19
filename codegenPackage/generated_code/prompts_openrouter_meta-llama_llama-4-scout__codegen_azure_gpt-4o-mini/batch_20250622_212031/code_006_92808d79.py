"""
Generated Code Metadata:
========================
Original URL: https://financeimpactpro.com
Prompt: Design a database schema to store user information, investment plans, and transactions for the Finance Impact Pro platform, ensuring data security and integrity.
Generated: DETERMINISTIC_92808d79a7825ca0
Batch ID: 20250622_212031
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Finance Impact Pro platform

-- Create a table to store user information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for login
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE, -- Unique email address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    is_active BOOLEAN DEFAULT TRUE -- Status of the user account
);

-- Create a table to store investment plans
CREATE TABLE InvestmentPlans (
    plan_id SERIAL PRIMARY KEY, -- Unique identifier for each investment plan
    plan_name VARCHAR(100) NOT NULL, -- Name of the investment plan
    description TEXT, -- Description of the investment plan
    min_investment DECIMAL(10, 2) NOT NULL, -- Minimum investment amount
    max_investment DECIMAL(10, 2), -- Maximum investment amount (nullable)
    interest_rate DECIMAL(5, 2) NOT NULL, -- Interest rate for the investment plan
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of plan creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store transactions
CREATE TABLE Transactions (
    transaction_id SERIAL PRIMARY KEY, -- Unique identifier for each transaction
    user_id INT NOT NULL, -- Foreign key referencing Users table
    plan_id INT NOT NULL, -- Foreign key referencing InvestmentPlans table
    amount DECIMAL(10, 2) NOT NULL, -- Amount of the transaction
    transaction_type VARCHAR(10) CHECK (transaction_type IN ('deposit', 'withdrawal')), -- Type of transaction
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the transaction
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (plan_id) REFERENCES InvestmentPlans(plan_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create an index on the Transactions table for faster queries
CREATE INDEX idx_user_transactions ON Transactions(user_id);
CREATE INDEX idx_plan_transactions ON Transactions(plan_id);
```
