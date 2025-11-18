"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metlifeinvests.com
Prompt: Suggest a database schema to manage investment plans, user accounts, and referral commissions for a platform like MET LIFE INVESTS.
Generated: DETERMINISTIC_00488c5324e14645
Batch ID: 20250612_151506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Investment Management Platform

-- Table: Users
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FullName VARCHAR(255) NOT NULL,        -- Full name of the user
    Email VARCHAR(255) UNIQUE NOT NULL,   -- Email address (must be unique)
    PasswordHash VARCHAR(255) NOT NULL,   -- Hashed password for user authentication
    PhoneNumber VARCHAR(20),              -- Phone number of the user
    ReferralCode VARCHAR(50) UNIQUE,      -- Unique referral code generated for each user
    ReferredBy INT,                       -- UserID of the referrer (foreign key to Users)
    AccountCreated TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of account creation
);

-- Table: InvestmentPlans
CREATE TABLE InvestmentPlans (
    PlanID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each investment plan
    PlanName VARCHAR(255) NOT NULL,        -- Name of the investment plan
    Description TEXT,                      -- Description of the plan
    MinimumInvestment DECIMAL(15, 2) NOT NULL, -- Minimum investment amount
    MaximumInvestment DECIMAL(15, 2),          -- Maximum investment amount (NULL for no limit)
    InterestRate DECIMAL(5, 2) NOT NULL,  -- Interest rate for the plan (e.g., 5.00 for 5%)
    DurationInMonths INT NOT NULL         -- Duration of the plan in months
);

-- Table: UserInvestments
CREATE TABLE UserInvestments (
    InvestmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each investment
    UserID INT NOT NULL,                         -- Foreign key to Users table
    PlanID INT NOT NULL,                         -- Foreign key to InvestmentPlans table
    InvestmentAmount DECIMAL(15, 2) NOT NULL,    -- Amount invested by the user
    InvestmentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of investment
    MaturityDate TIMESTAMP NOT NULL,             -- Date when the investment matures
    Status ENUM('Active', 'Completed', 'Cancelled') DEFAULT 'Active', -- Investment status
    FOREIGN KEY (UserID) REFERENCES Users(UserID), -- Relationship with Users table
    FOREIGN KEY (PlanID) REFERENCES InvestmentPlans(PlanID) -- Relationship with InvestmentPlans table
);

-- Table: ReferralCommissions
CREATE TABLE ReferralCommissions (
    CommissionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each commission record
    ReferrerID INT NOT NULL,                     -- UserID of the referrer
    ReferredID INT NOT NULL,                     -- UserID of the referred user
    InvestmentID INT NOT NULL,                   -- Foreign key to UserInvestments table
    CommissionAmount DECIMAL(15, 2) NOT NULL,    -- Commission amount earned
    CommissionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of commission payment
    FOREIGN KEY (ReferrerID) REFERENCES Users(UserID),  -- Relationship with Users table (referrer)
    FOREIGN KEY (ReferredID) REFERENCES Users(UserID),  -- Relationship with Users table (referred)
    FOREIGN KEY (InvestmentID) REFERENCES UserInvestments(InvestmentID) -- Relationship with UserInvestments table
);

-- Table: Transactions
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    UserID INT NOT NULL,                          -- Foreign key to Users table
    TransactionType ENUM('Deposit', 'Withdrawal', 'Commission') NOT NULL, -- Type of transaction
    Amount DECIMAL(15, 2) NOT NULL,              -- Transaction amount
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of transaction
    FOREIGN KEY (UserID) REFERENCES Users(UserID) -- Relationship with Users table
);

-- Indexes for performance optimization
CREATE INDEX idx_users_email ON Users(Email);             -- Index for quick lookup by email
CREATE INDEX idx_investments_user ON UserInvestments(UserID); -- Index for investments by user
CREATE INDEX idx_commissions_referrer ON ReferralCommissions(ReferrerID); -- Index for commissions by referrer
CREATE INDEX idx_transactions_user ON Transactions(UserID); -- Index for transactions by user
```
