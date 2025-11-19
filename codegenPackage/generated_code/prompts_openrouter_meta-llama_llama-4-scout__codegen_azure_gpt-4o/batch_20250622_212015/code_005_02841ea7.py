"""
Generated Code Metadata:
========================
Original URL: https://crypto4rex360.com
Prompt: "Create a SQL database schema to store user information, investment plans, and transaction records for Crypto 4Rex 360, and write a query to retrieve a user's account balance and investment history."
Generated: DETERMINISTIC_02841ea71d3f698e
Batch ID: 20250622_212015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Crypto 4Rex 360

-- Create a table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL,         -- Username of the user
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Email address of the user
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store investment plans
CREATE TABLE InvestmentPlans (
    PlanID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each investment plan
    PlanName VARCHAR(100) NOT NULL,        -- Name of the investment plan
    Description TEXT,                      -- Description of the investment plan
    MinInvestmentAmount DECIMAL(18, 2) NOT NULL, -- Minimum investment amount
    MaxInvestmentAmount DECIMAL(18, 2),   -- Maximum investment amount (nullable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of plan creation
);

-- Create a table to store transaction records
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    UserID INT NOT NULL,                          -- Foreign key referencing Users table
    PlanID INT,                                   -- Foreign key referencing InvestmentPlans table (nullable for non-investment transactions)
    TransactionType ENUM('Deposit', 'Withdrawal', 'Investment') NOT NULL, -- Type of transaction
    Amount DECIMAL(18, 2) NOT NULL,               -- Transaction amount
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the transaction
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is deleted
    FOREIGN KEY (PlanID) REFERENCES InvestmentPlans(PlanID) ON DELETE SET NULL -- Set PlanID to NULL if plan is deleted
);

-- Query to retrieve a user's account balance and investment history
SELECT 
    u.Username,
    u.Email,
    COALESCE(SUM(CASE WHEN t.TransactionType = 'Deposit' THEN t.Amount 
                      WHEN t.TransactionType = 'Withdrawal' THEN -t.Amount 
                      ELSE 0 END), 0) AS AccountBalance, -- Calculate account balance
    JSON_ARRAYAGG(JSON_OBJECT(
        'TransactionID', t.TransactionID,
        'PlanName', p.PlanName,
        'TransactionType', t.TransactionType,
        'Amount', t.Amount,
        'TransactionDate', t.TransactionDate
    )) AS InvestmentHistory -- Aggregate investment history as JSON
FROM 
    Users u
LEFT JOIN 
    Transactions t ON u.UserID = t.UserID
LEFT JOIN 
    InvestmentPlans p ON t.PlanID = p.PlanID
WHERE 
    u.UserID = ? -- Replace '?' with the specific UserID
GROUP BY 
    u.UserID, u.Username, u.Email;
```
