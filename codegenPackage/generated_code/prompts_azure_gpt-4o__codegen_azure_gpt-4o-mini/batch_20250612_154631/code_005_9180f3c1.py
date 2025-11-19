"""
Generated Code Metadata:
========================
Original URL: https://financeinvestmentslimited.org
Prompt: Create a database schema for managing recurring deposits and investments, inspired by the features of Finance Investment Limited.
Generated: DETERMINISTIC_9180f3c17bf55a59
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing recurring deposits and investments

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Accounts;
DROP TABLE IF EXISTS RecurringDeposits;
DROP TABLE IF EXISTS Investments;

-- Table to store user information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for login
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE, -- Unique email for notifications
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store account information for users
CREATE TABLE Accounts (
    account_id SERIAL PRIMARY KEY, -- Unique identifier for each account
    user_id INT NOT NULL, -- Foreign key referencing Users
    account_type VARCHAR(50) NOT NULL, -- Type of account (e.g., Savings, Investment)
    balance DECIMAL(15, 2) NOT NULL DEFAULT 0.00, -- Current balance in the account
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensures data integrity
);

-- Table to manage recurring deposits
CREATE TABLE RecurringDeposits (
    deposit_id SERIAL PRIMARY KEY, -- Unique identifier for each deposit
    account_id INT NOT NULL, -- Foreign key referencing Accounts
    amount DECIMAL(10, 2) NOT NULL, -- Amount to be deposited
    frequency VARCHAR(20) NOT NULL, -- Frequency of deposits (e.g., Monthly, Quarterly)
    start_date DATE NOT NULL, -- Start date of the recurring deposit
    end_date DATE, -- Optional end date for the recurring deposit
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of deposit creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (account_id) REFERENCES Accounts(account_id) ON DELETE CASCADE -- Ensures data integrity
);

-- Table to manage investments
CREATE TABLE Investments (
    investment_id SERIAL PRIMARY KEY, -- Unique identifier for each investment
    account_id INT NOT NULL, -- Foreign key referencing Accounts
    investment_type VARCHAR(50) NOT NULL, -- Type of investment (e.g., Stocks, Bonds)
    amount DECIMAL(10, 2) NOT NULL, -- Amount invested
    investment_date DATE NOT NULL, -- Date of investment
    maturity_date DATE, -- Optional maturity date for the investment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of investment creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (account_id) REFERENCES Accounts(account_id) ON DELETE CASCADE -- Ensures data integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_user_email ON Users(email);
CREATE INDEX idx_account_user ON Accounts(user_id);
CREATE INDEX idx_deposit_account ON RecurringDeposits(account_id);
CREATE INDEX idx_investment_account ON Investments(account_id);
```
