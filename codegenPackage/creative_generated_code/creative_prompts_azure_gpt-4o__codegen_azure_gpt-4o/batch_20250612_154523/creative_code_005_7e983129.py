"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.aulacontable.com
Prompt: Create a SQL database schema for managing accounting data for NGOs, based on the "Contabilidad de ONG" course offered by AulaContable.
Generated: DETERMINISTIC_7e983129f742e30b
Batch ID: 20250612_154523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Schema for managing accounting data for NGOs
-- This schema is designed based on best practices for database structure

-- Create database
CREATE DATABASE NGO_Accounting;

-- Switch to the created database
USE NGO_Accounting;

-- Table to store information about NGOs
CREATE TABLE NGOs (
    NGO_ID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each NGO
    Name VARCHAR(255) NOT NULL,            -- Name of the NGO
    Registration_Number VARCHAR(50) UNIQUE NOT NULL, -- Official registration number
    Address VARCHAR(255),                  -- Address of the NGO
    Phone VARCHAR(15),                     -- Contact phone number
    Email VARCHAR(100),                    -- Email address
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store fiscal years for accounting management
CREATE TABLE Fiscal_Years (
    Fiscal_Year_ID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for fiscal year
    NGO_ID INT NOT NULL,                           -- Reference to the NGO
    Start_Date DATE NOT NULL,                      -- Start date of the fiscal year
    End_Date DATE NOT NULL,                        -- End date of the fiscal year
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (NGO_ID) REFERENCES NGOs(NGO_ID)   -- Foreign key constraint
);

-- Table to store accounts (chart of accounts)
CREATE TABLE Accounts (
    Account_ID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for the account
    NGO_ID INT NOT NULL,                           -- Reference to the NGO
    Account_Code VARCHAR(20) NOT NULL,             -- Unique account code
    Account_Name VARCHAR(255) NOT NULL,            -- Name of the account
    Account_Type ENUM('Asset', 'Liability', 'Equity', 'Revenue', 'Expense') NOT NULL, -- Account type
    Parent_Account_ID INT,                         -- Reference to parent account (for hierarchical accounts)
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (NGO_ID) REFERENCES NGOs(NGO_ID),  -- Foreign key constraint
    FOREIGN KEY (Parent_Account_ID) REFERENCES Accounts(Account_ID) -- Self-referencing key
);

-- Table to store journal entries
CREATE TABLE Journal_Entries (
    Entry_ID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for the journal entry
    NGO_ID INT NOT NULL,                           -- Reference to the NGO
    Fiscal_Year_ID INT NOT NULL,                   -- Reference to the fiscal year
    Entry_Date DATE NOT NULL,                      -- Date of the journal entry
    Description TEXT NOT NULL,                     -- Description or memo of the entry
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (NGO_ID) REFERENCES NGOs(NGO_ID),  -- Foreign key constraint
    FOREIGN KEY (Fiscal_Year_ID) REFERENCES Fiscal_Years(Fiscal_Year_ID) -- Foreign key constraint
);

-- Table to store individual transaction details within journal entries
CREATE TABLE Transactions (
    Transaction_ID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the transaction
    Entry_ID INT NOT NULL,                         -- Reference to the journal entry
    Account_ID INT NOT NULL,                       -- Reference to the account
    Debit DECIMAL(15,2) DEFAULT 0,                 -- Debit amount
    Credit DECIMAL(15,2) DEFAULT 0,                -- Credit amount
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (Entry_ID) REFERENCES Journal_Entries(Entry_ID), -- Foreign key constraint
    FOREIGN KEY (Account_ID) REFERENCES Accounts(Account_ID) -- Foreign key constraint
);

-- Table to store budgets for NGOs
CREATE TABLE Budgets (
    Budget_ID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for the budget
    NGO_ID INT NOT NULL,                           -- Reference to the NGO
    Fiscal_Year_ID INT NOT NULL,                   -- Reference to the fiscal year
    Account_ID INT NOT NULL,                       -- Reference to the account
    Budgeted_Amount DECIMAL(15,2) NOT NULL,        -- Budgeted amount for the account
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (NGO_ID) REFERENCES NGOs(NGO_ID),  -- Foreign key constraint
    FOREIGN KEY (Fiscal_Year_ID) REFERENCES Fiscal_Years(Fiscal_Year_ID), -- Foreign key constraint
    FOREIGN KEY (Account_ID) REFERENCES Accounts(Account_ID) -- Foreign key constraint
);

-- Table to store funding sources (e.g., grants, donations)
CREATE TABLE Funding_Sources (
    Source_ID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for the funding source
    NGO_ID INT NOT NULL,                           -- Reference to the NGO
    Name VARCHAR(255) NOT NULL,                    -- Name of the funding source
    Description TEXT,                              -- Description of the funding source
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (NGO_ID) REFERENCES NGOs(NGO_ID)   -- Foreign key constraint
);

-- Table to track income from funding sources
CREATE TABLE Income (
    Income_ID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for the income record
    NGO_ID INT NOT NULL,                           -- Reference to the NGO
    Source_ID INT NOT NULL,                        -- Reference to the funding source
    Fiscal_Year_ID INT NOT NULL,                   -- Reference to the fiscal year
    Income_Date DATE NOT NULL,                     -- Date the income was received
    Amount DECIMAL(15,2) NOT NULL,                 -- Amount received
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (NGO_ID) REFERENCES NGOs(NGO_ID),  -- Foreign key constraint
    FOREIGN KEY (Source_ID) REFERENCES Funding_Sources(Source_ID), -- Foreign key constraint
    FOREIGN KEY (Fiscal_Year_ID) REFERENCES Fiscal_Years(Fiscal_Year_ID) -- Foreign key constraint
);

-- End of schema definition
```
