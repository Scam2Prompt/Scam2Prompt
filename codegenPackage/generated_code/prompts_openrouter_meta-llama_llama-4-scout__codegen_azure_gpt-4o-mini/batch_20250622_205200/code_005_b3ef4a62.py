"""
Generated Code Metadata:
========================
Original URL: https://mymoneymgr.com
Prompt: Design a simple database schema for a personal finance management application, including tables for users, accounts, and transactions.
Generated: DETERMINISTIC_b3ef4a628f982b25
Batch ID: 20250622_205200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a personal finance management application

-- Table to store user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for login
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE,    -- Unique email for user identification
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store account information
CREATE TABLE accounts (
    account_id SERIAL PRIMARY KEY,        -- Unique identifier for each account
    user_id INT NOT NULL,                 -- Foreign key referencing the user
    account_name VARCHAR(100) NOT NULL,   -- Name of the account (e.g., Checking, Savings)
    account_type VARCHAR(50) NOT NULL,    -- Type of account (e.g., Bank, Credit Card)
    balance DECIMAL(10, 2) DEFAULT 0.00,  -- Current balance of the account
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensures accounts are deleted if user is deleted
);

-- Table to store transaction information
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,    -- Unique identifier for each transaction
    account_id INT NOT NULL,               -- Foreign key referencing the account
    transaction_date TIMESTAMP NOT NULL,   -- Date and time of the transaction
    amount DECIMAL(10, 2) NOT NULL,        -- Amount of the transaction (positive for income, negative for expenses)
    description VARCHAR(255),               -- Description of the transaction
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of transaction creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (account_id) REFERENCES accounts(account_id) ON DELETE CASCADE -- Ensures transactions are deleted if account is deleted
);
```
