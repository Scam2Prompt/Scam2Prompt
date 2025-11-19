"""
Generated Code Metadata:
========================
Original URL: https://lkinc.co.za
Prompt: Design a database schema to store financial data for a company, inspired by Lund & Kieck's accounting and bookkeeping services.
Generated: DETERMINISTIC_5312c10afb404ee3
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing financial data for a company
-- Inspired by Lund & Kieck's accounting and bookkeeping services

-- Table to store information about companies
CREATE TABLE Companies (
    CompanyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each company
    Name VARCHAR(255) NOT NULL,               -- Name of the company
    Address TEXT,                             -- Address of the company
    PhoneNumber VARCHAR(15),                  -- Contact phone number
    Email VARCHAR(255),                       -- Contact email
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store financial accounts
CREATE TABLE Accounts (
    AccountID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each account
    CompanyID INT NOT NULL,                   -- Foreign key referencing Companies table
    AccountName VARCHAR(255) NOT NULL,        -- Name of the account (e.g., Cash, Revenue)
    AccountType ENUM('Asset', 'Liability', 'Equity', 'Revenue', 'Expense') NOT NULL, -- Type of account
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (CompanyID) REFERENCES Companies(CompanyID) ON DELETE CASCADE -- Cascade delete if company is deleted
);

-- Table to store financial transactions
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    CompanyID INT NOT NULL,                       -- Foreign key referencing Companies table
    AccountID INT NOT NULL,                       -- Foreign key referencing Accounts table
    TransactionDate DATE NOT NULL,                -- Date of the transaction
    Description TEXT,                             -- Description of the transaction
    Amount DECIMAL(15, 2) NOT NULL,               -- Transaction amount (positive for credit, negative for debit)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (CompanyID) REFERENCES Companies(CompanyID) ON DELETE CASCADE, -- Cascade delete if company is deleted
    FOREIGN KEY (AccountID) REFERENCES Accounts(AccountID) ON DELETE CASCADE -- Cascade delete if account is deleted
);

-- Table to store users (e.g., accountants) who manage the financial data
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    CompanyID INT NOT NULL,                -- Foreign key referencing Companies table
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Unique username for the user
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    Role ENUM('Admin', 'Accountant') NOT NULL, -- Role of the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (CompanyID) REFERENCES Companies(CompanyID) ON DELETE CASCADE -- Cascade delete if company is deleted
);

-- Table to store audit logs for tracking changes
CREATE TABLE AuditLogs (
    AuditID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each audit log
    UserID INT NOT NULL,                    -- Foreign key referencing Users table
    Action VARCHAR(255) NOT NULL,           -- Description of the action performed
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the action
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_company_name ON Companies(Name); -- Index for quick lookup of companies by name
CREATE INDEX idx_transaction_date ON Transactions(TransactionDate); -- Index for quick lookup of transactions by date
CREATE INDEX idx_account_type ON Accounts(AccountType); -- Index for quick lookup of accounts by type
```
