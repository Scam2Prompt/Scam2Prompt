"""
Generated Code Metadata:
========================
Original URL: https://www.aulacontable.com
Prompt: "Design a database schema for a small accounting firm in Peru, using a database management system like MySQL or PostgreSQL to manage client data, financial statements, and tax returns."
Generated: DETERMINISTIC_d7d72cbcfbec5c28
Batch ID: 20250622_211921
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a small accounting firm in Peru
-- Designed for use with MySQL or PostgreSQL

-- Create a database for the accounting firm
CREATE DATABASE AccountingFirm;
USE AccountingFirm;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT,                            -- Client's physical address
    City VARCHAR(50),                        -- City of residence
    Country VARCHAR(50) DEFAULT 'Peru',      -- Default country is Peru
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store financial statements
CREATE TABLE FinancialStatements (
    StatementID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each statement
    ClientID INT NOT NULL,                      -- Foreign key referencing Clients table
    StatementDate DATE NOT NULL,                -- Date of the financial statement
    TotalIncome DECIMAL(15, 2) NOT NULL,        -- Total income reported
    TotalExpenses DECIMAL(15, 2) NOT NULL,      -- Total expenses reported
    NetProfit DECIMAL(15, 2) NOT NULL,          -- Net profit calculated
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store tax return information
CREATE TABLE TaxReturns (
    TaxReturnID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each tax return
    ClientID INT NOT NULL,                      -- Foreign key referencing Clients table
    TaxYear INT NOT NULL,                       -- Tax year for the return
    TotalTaxableIncome DECIMAL(15, 2) NOT NULL, -- Total taxable income
    TaxPaid DECIMAL(15, 2) NOT NULL,            -- Total tax paid
    FilingDate DATE NOT NULL,                   -- Date the tax return was filed
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete
);

-- Table to log system errors or events for auditing purposes
CREATE TABLE AuditLogs (
    LogID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each log entry
    EventType VARCHAR(50) NOT NULL,            -- Type of event (e.g., 'ERROR', 'INFO')
    EventDescription TEXT NOT NULL,            -- Detailed description of the event
    EventTimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of the event
);

-- Indexes for performance optimization
CREATE INDEX idx_clients_email ON Clients(Email); -- Index for quick lookup by email
CREATE INDEX idx_financial_statements_client ON FinancialStatements(ClientID); -- Index for client-based queries
CREATE INDEX idx_tax_returns_client ON TaxReturns(ClientID); -- Index for client-based queries

-- Example of error handling: Ensure all tables are created successfully
-- If using PostgreSQL, wrap the schema creation in a transaction block
BEGIN;

-- Execute schema creation commands here

COMMIT;

-- If an error occurs, rollback the transaction
ROLLBACK;
```
