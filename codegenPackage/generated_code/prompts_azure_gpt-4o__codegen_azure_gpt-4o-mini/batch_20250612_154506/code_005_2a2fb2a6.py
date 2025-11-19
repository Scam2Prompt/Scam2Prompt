"""
Generated Code Metadata:
========================
Original URL: https://swanbay.dip.vn
Prompt: Create a database schema in MySQL to manage user accounts, deposits, and withdrawals for an online betting platform like VZ99.
Generated: DETERMINISTIC_2a2fb2a6306bce14
Batch ID: 20250612_154506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- MySQL Database Schema for Online Betting Platform

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS transactions;

-- Create a table to store user information
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,    -- Unique username for the user
    password_hash VARCHAR(255) NOT NULL,     -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE,       -- Unique email address for the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of account creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Create a table to manage user accounts
CREATE TABLE accounts (
    account_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each account
    user_id INT NOT NULL,                       -- Foreign key referencing the user
    balance DECIMAL(10, 2) DEFAULT 0.00,       -- Current balance of the account
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of account creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a table to log transactions (deposits and withdrawals)
CREATE TABLE transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each transaction
    account_id INT NOT NULL,                         -- Foreign key referencing the account
    transaction_type ENUM('deposit', 'withdrawal') NOT NULL,  -- Type of transaction
    amount DECIMAL(10, 2) NOT NULL,                 -- Amount of the transaction
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of the transaction
    FOREIGN KEY (account_id) REFERENCES accounts(account_id) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_user_email ON users(email);
CREATE INDEX idx_account_user ON accounts(user_id);
CREATE INDEX idx_transaction_account ON transactions(account_id);
```
