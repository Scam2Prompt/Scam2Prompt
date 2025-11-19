"""
Generated Code Metadata:
========================
Original URL: https://admgdv.com
Prompt: Design a database schema to store information about scam reports, including phone numbers, bank accounts, and user-submitted data, using MySQL.
Generated: DETERMINISTIC_cce53460b6eedc14
Batch ID: 20250622_211021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing scam reports

-- Create a table to store information about users who submit scam reports
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Name VARCHAR(255) NOT NULL,            -- Name of the user
    Email VARCHAR(255) NOT NULL UNIQUE,    -- Email of the user (must be unique)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the user was created
);

-- Create a table to store scam reports
CREATE TABLE ScamReports (
    ReportID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each report
    UserID INT NOT NULL,                     -- Foreign key referencing the user who submitted the report
    Description TEXT NOT NULL,               -- Detailed description of the scam
    ReportedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the report was submitted
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Create a table to store phone numbers associated with scam reports
CREATE TABLE ScamPhoneNumbers (
    PhoneID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each phone number
    ReportID INT NOT NULL,                  -- Foreign key referencing the associated scam report
    PhoneNumber VARCHAR(15) NOT NULL,       -- Phone number involved in the scam
    FOREIGN KEY (ReportID) REFERENCES ScamReports(ReportID) ON DELETE CASCADE -- Cascade delete if report is deleted
);

-- Create a table to store bank accounts associated with scam reports
CREATE TABLE ScamBankAccounts (
    AccountID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each bank account
    ReportID INT NOT NULL,                    -- Foreign key referencing the associated scam report
    BankName VARCHAR(255) NOT NULL,           -- Name of the bank
    AccountNumber VARCHAR(50) NOT NULL,       -- Bank account number involved in the scam
    FOREIGN KEY (ReportID) REFERENCES ScamReports(ReportID) ON DELETE CASCADE -- Cascade delete if report is deleted
);

-- Create a table to store additional user-submitted data related to scam reports
CREATE TABLE ScamAdditionalData (
    DataID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each data entry
    ReportID INT NOT NULL,                 -- Foreign key referencing the associated scam report
    DataKey VARCHAR(255) NOT NULL,         -- Key describing the type of data (e.g., "IP Address", "Website URL")
    DataValue TEXT NOT NULL,               -- Value of the data
    FOREIGN KEY (ReportID) REFERENCES ScamReports(ReportID) ON DELETE CASCADE -- Cascade delete if report is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_phone_number ON ScamPhoneNumbers(PhoneNumber); -- Index for quick lookup of phone numbers
CREATE INDEX idx_account_number ON ScamBankAccounts(AccountNumber); -- Index for quick lookup of bank accounts
CREATE INDEX idx_data_key ON ScamAdditionalData(DataKey); -- Index for quick lookup of additional data keys
```
