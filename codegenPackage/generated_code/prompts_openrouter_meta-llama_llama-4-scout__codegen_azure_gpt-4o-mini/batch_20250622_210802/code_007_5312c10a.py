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

-- Create a database for the financial data
CREATE DATABASE FinancialData;

-- Use the created database
USE FinancialData;

-- Table to store information about companies
CREATE TABLE Companies (
    CompanyID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each company
    CompanyName VARCHAR(255) NOT NULL,         -- Name of the company
    Address VARCHAR(255),                       -- Address of the company
    PhoneNumber VARCHAR(15),                    -- Contact number
    Email VARCHAR(255),                         -- Contact email
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about accounts
CREATE TABLE Accounts (
    AccountID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each account
    CompanyID INT NOT NULL,                     -- Foreign key referencing Companies
    AccountName VARCHAR(255) NOT NULL,         -- Name of the account
    AccountType ENUM('Asset', 'Liability', 'Equity', 'Revenue', 'Expense') NOT NULL, -- Type of account
    Balance DECIMAL(15, 2) DEFAULT 0.00,       -- Current balance of the account
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (CompanyID) REFERENCES Companies(CompanyID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store transactions
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    AccountID INT NOT NULL,                       -- Foreign key referencing Accounts
    TransactionDate DATE NOT NULL,                -- Date of the transaction
    Amount DECIMAL(15, 2) NOT NULL,              -- Amount of the transaction
    TransactionType ENUM('Debit', 'Credit') NOT NULL, -- Type of transaction
    Description VARCHAR(255),                     -- Description of the transaction
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (AccountID) REFERENCES Accounts(AccountID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store financial reports
CREATE TABLE FinancialReports (
    ReportID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each report
    CompanyID INT NOT NULL,                       -- Foreign key referencing Companies
    ReportType ENUM('Balance Sheet', 'Income Statement', 'Cash Flow Statement') NOT NULL, -- Type of report
    ReportDate DATE NOT NULL,                     -- Date of the report
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (CompanyID) REFERENCES Companies(CompanyID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_company_name ON Companies(CompanyName);
CREATE INDEX idx_account_name ON Accounts(AccountName);
CREATE INDEX idx_transaction_date ON Transactions(TransactionDate);
CREATE INDEX idx_report_date ON FinancialReports(ReportDate);
```
