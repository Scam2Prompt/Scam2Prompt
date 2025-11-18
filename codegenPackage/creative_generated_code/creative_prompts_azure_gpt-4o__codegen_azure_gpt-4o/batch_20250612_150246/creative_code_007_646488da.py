"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elixinvestmentltd.info
Prompt: Develop a database schema in MySQL to store user deposits, withdrawals, and investment plan details for an online trading platform like RystonFX Trading.
Generated: DETERMINISTIC_646488da8160a177
Batch ID: 20250612_150246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a schema for an online trading platform to store user deposits, withdrawals, 
-- and investment plan details along with proper relationships and constraints.

-- Create a table for user details
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FullName VARCHAR(255) NOT NULL,        -- Full name of the user
    Email VARCHAR(255) NOT NULL UNIQUE,    -- Email address of the user (unique constraint)
    PasswordHash VARCHAR(255) NOT NULL,    -- Password hash for secure authentication
    PhoneNumber VARCHAR(15),               -- Optional phone number of the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the user was created
);

-- Create a table for user deposits
CREATE TABLE Deposits (
    DepositID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each deposit
    UserID INT NOT NULL,                      -- Reference to the user making the deposit
    Amount DECIMAL(10, 2) NOT NULL,           -- Deposit amount
    DepositDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the deposit
    Status ENUM('Pending', 'Completed', 'Failed') NOT NULL DEFAULT 'Pending', -- Status of the deposit
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for user withdrawals
CREATE TABLE Withdrawals (
    WithdrawalID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each withdrawal
    UserID INT NOT NULL,                         -- Reference to the user making the withdrawal
    Amount DECIMAL(10, 2) NOT NULL,              -- Withdrawal amount
    WithdrawalDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the withdrawal
    Status ENUM('Pending', 'Completed', 'Failed') NOT NULL DEFAULT 'Pending', -- Status of the withdrawal
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for investment plans
CREATE TABLE InvestmentPlans (
    PlanID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each investment plan
    PlanName VARCHAR(255) NOT NULL,        -- Name of the investment plan
    Description TEXT NULL,                 -- Optional description of the investment plan
    MinInvestment DECIMAL(10, 2) NOT NULL, -- Minimum investment amount required
    MaxInvestment DECIMAL(10, 2) NOT NULL, -- Maximum investment amount allowed
    ROI DECIMAL(5, 2) NOT NULL,            -- Return on investment percentage
    DurationDays INT NOT NULL              -- Duration of the investment plan in days
);

-- Create a table for user investments
CREATE TABLE UserInvestments (
    InvestmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each investment
    UserID INT NOT NULL,                         -- Reference to the user making the investment
    PlanID INT NOT NULL,                         -- Reference to the investment plan selected
    Amount DECIMAL(10, 2) NOT NULL,              -- Investment amount
    StartDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Start date of the investment
    EndDate TIMESTAMP,                           -- End date of the investment (calculated)
    Status ENUM('Active', 'Completed', 'Cancelled') NOT NULL DEFAULT 'Active', -- Status of the investment
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (PlanID) REFERENCES InvestmentPlans(PlanID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Add an index to speed up queries on frequently used columns
CREATE INDEX idx_user_deposits ON Deposits(UserID);
CREATE INDEX idx_user_withdrawals ON Withdrawals(UserID);
CREATE INDEX idx_user_investments ON UserInvestments(UserID);
CREATE INDEX idx_plan_investments ON UserInvestments(PlanID);
```
