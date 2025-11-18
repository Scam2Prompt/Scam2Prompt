"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financeinvestmentslimited.org
Prompt: Create a database schema for managing recurring deposits and investments, inspired by the features of Finance Investment Limited.
Generated: DETERMINISTIC_9180f3c17bf55a59
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing recurring deposits and investments
-- Inspired by the features of Finance Investment Limited

-- Create a table to store information about users
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each user
    FullName VARCHAR(100) NOT NULL,          -- Full name of the user
    Email VARCHAR(100) NOT NULL UNIQUE,      -- Email of the user (must be unique)
    PhoneNumber VARCHAR(15),                 -- Contact number of the user
    PasswordHash VARCHAR(255) NOT NULL,      -- Hashed password for secure authentication
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for account creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for account updates
);

-- Create a table to store information about investment plans
CREATE TABLE InvestmentPlans (
    PlanID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each investment plan
    PlanName VARCHAR(100) NOT NULL,          -- Name of the investment plan
    InterestRate DECIMAL(5, 2) NOT NULL,     -- Interest rate for the plan (e.g., 5.50%)
    MinDepositAmount DECIMAL(10, 2) NOT NULL,-- Minimum deposit amount for the plan
    DurationMonths INT NOT NULL,             -- Duration of the plan in months
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for plan creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for plan updates
);

-- Create a table to store recurring deposits made by users
CREATE TABLE RecurringDeposits (
    DepositID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each deposit
    UserID INT NOT NULL,                             -- Foreign key referencing Users(UserID)
    PlanID INT NOT NULL,                             -- Foreign key referencing InvestmentPlans(PlanID)
    DepositAmount DECIMAL(10, 2) NOT NULL,           -- Amount deposited
    StartDate DATE NOT NULL,                         -- Date when the deposit starts
    NextDepositDueDate DATE NOT NULL,                -- Date for the next deposit
    Status ENUM('Active', 'Completed', 'Cancelled') NOT NULL DEFAULT 'Active', -- Status of the deposit
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp for deposit creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for deposit updates
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade on user deletion
    FOREIGN KEY (PlanID) REFERENCES InvestmentPlans(PlanID) ON DELETE CASCADE -- Cascade on plan deletion
);

-- Create a table to store transactions related to deposits and investments
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each transaction
    DepositID INT NOT NULL,                          -- Foreign key referencing RecurringDeposits(DepositID)
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the transaction
    Amount DECIMAL(10, 2) NOT NULL,                  -- Transaction amount
    TransactionType ENUM('Deposit', 'Interest', 'Withdrawal') NOT NULL, -- Type of transaction
    Status ENUM('Pending', 'Completed', 'Failed') NOT NULL DEFAULT 'Completed', -- Transaction status
    FOREIGN KEY (DepositID) REFERENCES RecurringDeposits(DepositID) ON DELETE CASCADE -- Cascade on deposit deletion
);

-- Create a table to store logs for audit and monitoring purposes
CREATE TABLE AuditLogs (
    LogID INT AUTO_INCREMENT PRIMARY KEY,            -- Unique identifier for each log
    UserID INT,                                      -- Foreign key referencing Users(UserID)
    Action VARCHAR(255) NOT NULL,                   -- Description of the action performed
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date and time of the action
    IPAddress VARCHAR(45),                          -- IP address of the user performing the action
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE SET NULL -- User reference, set NULL on user deletion
);

-- Best practices:
-- - Use proper indexing on frequently searched columns.
-- - Ensure all table relationships are defined with foreign keys.
-- - Validate input data at the application level before inserting into the database.
-- - Encrypt sensitive data (e.g., passwords) using secure algorithms.
-- - Periodically backup the database for disaster recovery.
```
