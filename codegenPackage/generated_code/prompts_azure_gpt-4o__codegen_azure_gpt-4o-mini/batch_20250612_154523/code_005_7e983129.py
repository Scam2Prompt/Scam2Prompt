"""
Generated Code Metadata:
========================
Original URL: https://www.aulacontable.com
Prompt: Create a SQL database schema for managing accounting data for NGOs, based on the "Contabilidad de ONG" course offered by AulaContable.
Generated: DETERMINISTIC_7e983129f742e30b
Batch ID: 20250612_154523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Managing Accounting Data for NGOs

-- Create a database for the NGO accounting system
CREATE DATABASE NGO_Accounting;

-- Use the newly created database
USE NGO_Accounting;

-- Table to store information about NGOs
CREATE TABLE NGOs (
    NGO_ID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each NGO
    Name VARCHAR(255) NOT NULL,            -- Name of the NGO
    Address VARCHAR(255),                   -- Address of the NGO
    Phone VARCHAR(15),                      -- Contact phone number
    Email VARCHAR(255),                     -- Contact email address
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    Updated_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about accounts
CREATE TABLE Accounts (
    Account_ID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each account
    NGO_ID INT NOT NULL,                       -- Foreign key referencing the NGO
    Account_Name VARCHAR(255) NOT NULL,       -- Name of the account
    Account_Type ENUM('Asset', 'Liability', 'Equity', 'Revenue', 'Expense') NOT NULL, -- Type of account
    Balance DECIMAL(15, 2) DEFAULT 0.00,      -- Current balance of the account
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    Updated_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (NGO_ID) REFERENCES NGOs(NGO_ID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store transactions
CREATE TABLE Transactions (
    Transaction_ID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    Account_ID INT NOT NULL,                        -- Foreign key referencing the account
    Transaction_Date DATE NOT NULL,                -- Date of the transaction
    Amount DECIMAL(15, 2) NOT NULL,                -- Amount of the transaction
    Transaction_Type ENUM('Debit', 'Credit') NOT NULL, -- Type of transaction
    Description TEXT,                               -- Description of the transaction
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    Updated_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (Account_ID) REFERENCES Accounts(Account_ID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store budget information
CREATE TABLE Budgets (
    Budget_ID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each budget
    NGO_ID INT NOT NULL,                       -- Foreign key referencing the NGO
    Budget_Year YEAR NOT NULL,                 -- Year of the budget
    Total_Amount DECIMAL(15, 2) NOT NULL,     -- Total budget amount
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    Updated_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (NGO_ID) REFERENCES NGOs(NGO_ID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store donors information
CREATE TABLE Donors (
    Donor_ID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each donor
    Name VARCHAR(255) NOT NULL,               -- Name of the donor
    Contact_Info VARCHAR(255),                 -- Contact information for the donor
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    Updated_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store donations
CREATE TABLE Donations (
    Donation_ID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each donation
    Donor_ID INT NOT NULL,                      -- Foreign key referencing the donor
    Amount DECIMAL(15, 2) NOT NULL,            -- Amount of the donation
    Donation_Date DATE NOT NULL,                -- Date of the donation
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    Updated_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (Donor_ID) REFERENCES Donors(Donor_ID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_ngos_name ON NGOs(Name);
CREATE INDEX idx_accounts_name ON Accounts(Account_Name);
CREATE INDEX idx_transactions_date ON Transactions(Transaction_Date);
CREATE INDEX idx_donations_date ON Donations(Donation_Date);
```
