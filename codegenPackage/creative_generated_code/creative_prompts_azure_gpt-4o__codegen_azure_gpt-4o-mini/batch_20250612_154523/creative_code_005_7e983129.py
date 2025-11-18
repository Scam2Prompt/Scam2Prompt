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
-- SQL script to create a database schema for managing accounting data for NGOs

-- Drop the database if it exists (for development purposes)
DROP DATABASE IF EXISTS ngo_accounting;

-- Create a new database for NGO accounting
CREATE DATABASE ngo_accounting;

-- Use the newly created database
USE ngo_accounting;

-- Table to store information about NGOs
CREATE TABLE ngos (
    ngo_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each NGO
    name VARCHAR(255) NOT NULL,            -- Name of the NGO
    registration_number VARCHAR(100) UNIQUE NOT NULL, -- Registration number
    address VARCHAR(255),                   -- Address of the NGO
    contact_email VARCHAR(100),             -- Contact email
    phone_number VARCHAR(20),               -- Contact phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Creation date
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update date
);

-- Table to store accounts for each NGO
CREATE TABLE accounts (
    account_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each account
    ngo_id INT NOT NULL,                        -- Foreign key to the NGOs table
    account_name VARCHAR(255) NOT NULL,        -- Name of the account
    account_type ENUM('asset', 'liability', 'equity', 'income', 'expense') NOT NULL, -- Type of account
    balance DECIMAL(15, 2) DEFAULT 0.00,       -- Current balance of the account
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Creation date
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update date
    FOREIGN KEY (ngo_id) REFERENCES ngos(ngo_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to store transactions for each account
CREATE TABLE transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    account_id INT NOT NULL,                       -- Foreign key to the accounts table
    transaction_date DATE NOT NULL,                -- Date of the transaction
    amount DECIMAL(15, 2) NOT NULL,               -- Amount of the transaction
    transaction_type ENUM('debit', 'credit') NOT NULL, -- Type of transaction
    description VARCHAR(255),                      -- Description of the transaction
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Creation date
    FOREIGN KEY (account_id) REFERENCES accounts(account_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to store budget information for each NGO
CREATE TABLE budgets (
    budget_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each budget
    ngo_id INT NOT NULL,                       -- Foreign key to the NGOs table
    budget_year YEAR NOT NULL,                 -- Year of the budget
    total_budget DECIMAL(15, 2) NOT NULL,     -- Total budget amount
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Creation date
    FOREIGN KEY (ngo_id) REFERENCES ngos(ngo_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to store budget allocations for each NGO
CREATE TABLE budget_allocations (
    allocation_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each allocation
    budget_id INT NOT NULL,                       -- Foreign key to the budgets table
    account_id INT NOT NULL,                      -- Foreign key to the accounts table
    allocated_amount DECIMAL(15, 2) NOT NULL,    -- Amount allocated
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Creation date
    FOREIGN KEY (budget_id) REFERENCES budgets(budget_id) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (account_id) REFERENCES accounts(account_id) ON DELETE CASCADE -- Foreign key constraint
);
```
