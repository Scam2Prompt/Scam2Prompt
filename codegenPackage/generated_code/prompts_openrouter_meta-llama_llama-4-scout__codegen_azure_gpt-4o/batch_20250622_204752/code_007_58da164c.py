"""
Generated Code Metadata:
========================
Original URL: https://hub-steth.org
Prompt: Design a simple database schema for storing personal finance data, including savings, checking, and investment accounts.
Generated: DETERMINISTIC_58da164caf0d0f5d
Batch ID: 20250622_204752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Personal Finance Data

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FirstName VARCHAR(50) NOT NULL,        -- User's first name
    LastName VARCHAR(50) NOT NULL,         -- User's last name
    Email VARCHAR(100) UNIQUE NOT NULL,    -- User's email address (must be unique)
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for account creation
);

-- Table to store account types (e.g., Savings, Checking, Investment)
CREATE TABLE AccountTypes (
    AccountTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for account type
    TypeName VARCHAR(50) NOT NULL UNIQUE,         -- Name of the account type (e.g., Savings)
    Description TEXT                              -- Optional description of the account type
);

-- Table to store user accounts
CREATE TABLE Accounts (
    AccountID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each account
    UserID INT NOT NULL,                      -- Foreign key referencing Users table
    AccountTypeID INT NOT NULL,               -- Foreign key referencing AccountTypes table
    AccountName VARCHAR(100) NOT NULL,        -- User-defined name for the account
    Balance DECIMAL(15, 2) DEFAULT 0.00,      -- Current balance in the account
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for account creation
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is deleted
    FOREIGN KEY (AccountTypeID) REFERENCES AccountTypes(AccountTypeID) ON DELETE RESTRICT -- Restrict deletion of account type
);

-- Table to store transactions for each account
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    AccountID INT NOT NULL,                       -- Foreign key referencing Accounts table
    TransactionType ENUM('Deposit', 'Withdrawal', 'Transfer') NOT NULL, -- Type of transaction
    Amount DECIMAL(15, 2) NOT NULL,               -- Amount involved in the transaction
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for the transaction
    Description TEXT,                             -- Optional description of the transaction
    FOREIGN KEY (AccountID) REFERENCES Accounts(AccountID) ON DELETE CASCADE -- Cascade delete if account is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_user_email ON Users(Email); -- Index for quick lookup by email
CREATE INDEX idx_account_user ON Accounts(UserID); -- Index for quick lookup of accounts by user
CREATE INDEX idx_transaction_account ON Transactions(AccountID); -- Index for quick lookup of transactions by account
```
