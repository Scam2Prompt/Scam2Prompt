"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalarbitrageinv.com
Prompt: Create a database schema using SQL to manage user accounts, investment plans, referral data, and transaction history for a platform like Global Arbitrage Investments.
Generated: DETERMINISTIC_9011662dbb0a8d45
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Schema for managing user accounts, investment plans, referral data, and transaction history

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS Transactions;
DROP TABLE IF EXISTS Referrals;
DROP TABLE IF EXISTS InvestmentPlans;
DROP TABLE IF EXISTS Users;

-- Create table for user accounts
CREATE TABLE Users (
    UserID SERIAL PRIMARY KEY,  -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Unique username for the user
    PasswordHash VARCHAR(255) NOT NULL,  -- Hashed password for security
    Email VARCHAR(100) NOT NULL UNIQUE,  -- Unique email for communication
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Registration date and time
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Last update date and time
);

-- Create table for investment plans
CREATE TABLE InvestmentPlans (
    PlanID SERIAL PRIMARY KEY,  -- Unique identifier for each investment plan
    PlanName VARCHAR(100) NOT NULL,  -- Name of the investment plan
    MinInvestment DECIMAL(10, 2) NOT NULL,  -- Minimum investment amount
    MaxInvestment DECIMAL(10, 2) NOT NULL,  -- Maximum investment amount
    InterestRate DECIMAL(5, 2) NOT NULL,  -- Interest rate associated with the plan
    DurationMonths INT NOT NULL,  -- Duration of the investment in months
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Creation date and time
);

-- Create table for referral data
CREATE TABLE Referrals (
    ReferralID SERIAL PRIMARY KEY,  -- Unique identifier for each referral
    ReferrerID INT NOT NULL,  -- UserID of the user who referred
    ReferredID INT NOT NULL,  -- UserID of the referred user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date and time of referral
    FOREIGN KEY (ReferrerID) REFERENCES Users(UserID) ON DELETE CASCADE,  -- Define foreign key relationship
    FOREIGN KEY (ReferredID) REFERENCES Users(UserID) ON DELETE CASCADE  -- Define foreign key relationship
);

-- Create table for transaction history
CREATE TABLE Transactions (
    TransactionID SERIAL PRIMARY KEY,  -- Unique identifier for each transaction
    UserID INT NOT NULL,  -- UserID of the user making the transaction
    PlanID INT NOT NULL,  -- Investment plan associated with the transaction
    Amount DECIMAL(10, 2) NOT NULL,  -- Amount of money involved in the transaction
    TransactionType VARCHAR(10) NOT NULL CHECK (TransactionType IN ('Deposit', 'Withdrawal')),  -- Type of transaction
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date and time of the transaction
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,  -- Define foreign key relationship
    FOREIGN KEY (PlanID) REFERENCES InvestmentPlans(PlanID) ON DELETE CASCADE  -- Define foreign key relationship
);

-- Create indexes for better performance
CREATE INDEX idx_username ON Users(Username);
CREATE INDEX idx_email ON Users(Email);
CREATE INDEX idx_referrer ON Referrals(ReferrerID);
CREATE INDEX idx_user_transactions ON Transactions(UserID);
CREATE INDEX idx_plan_transactions ON Transactions(PlanID);
```
