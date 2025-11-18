"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swanbay.dip.vn
Prompt: Create a database schema in MySQL to manage user accounts, deposits, and withdrawals for an online betting platform like VZ99.
Generated: DETERMINISTIC_2a2fb2a6306bce14
Batch ID: 20250612_154506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for an online betting platform

-- Create the database
CREATE DATABASE IF NOT EXISTS betting_platform;

-- Use the database
USE betting_platform;

-- Table to store user accounts
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each user
    username VARCHAR(50) NOT NULL UNIQUE,   -- Unique username
    email VARCHAR(100) NOT NULL UNIQUE,     -- Unique email address for each user
    password_hash VARCHAR(255) NOT NULL,    -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for account creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to track deposits
CREATE TABLE IF NOT EXISTS deposits (
    deposit_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each deposit
    user_id INT NOT NULL,                      -- Foreign key referencing users table
    amount DECIMAL(10,2) NOT NULL,             -- Amount deposited
    deposit_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of deposit
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensures data integrity
);

-- Table to track withdrawals
CREATE TABLE IF NOT EXISTS withdrawals (
    withdrawal_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each withdrawal
    user_id INT NOT NULL,                         -- Foreign key referencing users table
    amount DECIMAL(10,2) NOT NULL,                -- Amount withdrawn
    withdrawal_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of withdrawal
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensures data integrity
);

-- Indexes to improve query performance
CREATE INDEX idx_user_id_deposits ON deposits(user_id);
CREATE INDEX idx_user_id_withdrawals ON withdrawals(user_id);

-- Error handling: Ensure all operations are executed within transactions
-- Note: This is typically implemented in the application layer, not directly in SQL.
```
