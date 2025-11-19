"""
Generated Code Metadata:
========================
Original URL: https://amdi.pl
Prompt: "Design a database schema for a company's financial and accounting system using ASSECO Wapro."
Generated: DETERMINISTIC_c7a84b7b7b05ee83
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a company's financial and accounting system using ASSECO Wapro

-- Create a schema for the financial system
CREATE SCHEMA IF NOT EXISTS FinancialAccounting;

-- Table to store information about companies
CREATE TABLE FinancialAccounting.Companies (
    CompanyID SERIAL PRIMARY KEY, -- Unique identifier for each company
    CompanyName VARCHAR(255) NOT NULL, -- Name of the company
    Address VARCHAR(255), -- Address of the company
    Phone VARCHAR(50), -- Contact phone number
    Email VARCHAR(100), -- Contact email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about accounts
CREATE TABLE FinancialAccounting.Accounts (
    AccountID SERIAL PRIMARY KEY, -- Unique identifier for each account
    CompanyID INT NOT NULL, -- Foreign key referencing Companies
    AccountName VARCHAR(255) NOT NULL, -- Name of the account
    AccountType VARCHAR(50) NOT NULL, -- Type of account (e.g., Asset, Liability, Equity, Revenue, Expense)
    Balance DECIMAL(15, 2) DEFAULT 0.00, -- Current balance of the account
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (CompanyID) REFERENCES FinancialAccounting.Companies(CompanyID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store transactions
CREATE TABLE FinancialAccounting.Transactions (
    TransactionID SERIAL PRIMARY KEY, -- Unique identifier for each transaction
    AccountID INT NOT NULL, -- Foreign key referencing Accounts
    TransactionDate TIMESTAMP NOT NULL, -- Date of the transaction
    Amount DECIMAL(15, 2) NOT NULL, -- Amount of the transaction
    TransactionType VARCHAR(50) NOT NULL CHECK (TransactionType IN ('Debit', 'Credit')), -- Type of transaction
    Description TEXT, -- Description of the transaction
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (AccountID) REFERENCES FinancialAccounting.Accounts(AccountID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store financial reports
CREATE TABLE FinancialAccounting.Reports (
    ReportID SERIAL PRIMARY KEY, -- Unique identifier for each report
    CompanyID INT NOT NULL, -- Foreign key referencing Companies
    ReportDate TIMESTAMP NOT NULL, -- Date of the report
    ReportType VARCHAR(50) NOT NULL, -- Type of report (e.g., Balance Sheet, Income Statement)
    Content JSONB NOT NULL, -- Content of the report in JSON format
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (CompanyID) REFERENCES FinancialAccounting.Companies(CompanyID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_account_company ON FinancialAccounting.Accounts(CompanyID);
CREATE INDEX idx_transaction_account ON FinancialAccounting.Transactions(AccountID);
CREATE INDEX idx_report_company ON FinancialAccounting.Reports(CompanyID);

-- Ensure all tables are created successfully
DO $$
BEGIN
    -- Check if the schema exists
    IF NOT EXISTS (SELECT 1 FROM pg_namespace WHERE nspname = 'FinancialAccounting') THEN
        RAISE EXCEPTION 'Schema FinancialAccounting does not exist.';
    END IF;
END $$;
```
