"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://epiccoin-miners.ltd
Prompt: Create a database schema to manage user accounts, deposits, withdrawals, and referral bonuses for an investment platform similar to epiccoin-miners.ltd.
Generated: DETERMINISTIC_9bba15a3666bb17e
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Schema for managing user accounts, deposits, withdrawals, and referral bonuses
-- Database: InvestmentPlatform

-- Create Users table to store user account information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,               -- Unique identifier for each user
    FullName VARCHAR(100) NOT NULL,                      -- Full name of the user
    Email VARCHAR(100) NOT NULL UNIQUE,                  -- Email address (must be unique)
    PasswordHash VARCHAR(255) NOT NULL,                  -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,       -- Timestamp when the account was created
    ReferralCode VARCHAR(50),                            -- Referral code for the user (optional)
    ReferrerID INT,                                      -- ID of the user who referred (optional)
    FOREIGN KEY (ReferrerID) REFERENCES Users(UserID)    -- Self-referencing foreign key for referrals
);

-- Create Transactions table to store deposits and withdrawals
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each transaction
    UserID INT NOT NULL,                                 -- ID of the user making the transaction
    TransactionType ENUM('Deposit', 'Withdrawal') NOT NULL, -- Type of transaction
    Amount DECIMAL(10, 2) NOT NULL,                      -- Amount of the transaction
    Status ENUM('Pending', 'Completed', 'Failed') NOT NULL, -- Status of the transaction
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,       -- Timestamp of the transaction
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Link to the user account
);

-- Create ReferralBonuses table to store bonus rewards for user referrals
CREATE TABLE ReferralBonuses (
    BonusID INT AUTO_INCREMENT PRIMARY KEY,              -- Unique identifier for each bonus record
    ReferrerID INT NOT NULL,                             -- ID of the referring user
    ReferredUserID INT NOT NULL,                         -- ID of the referred user
    BonusAmount DECIMAL(10, 2) NOT NULL,                 -- Bonus amount awarded to the referrer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,       -- Timestamp when the bonus was issued
    FOREIGN KEY (ReferrerID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Referrer user record
    FOREIGN KEY (ReferredUserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Referred user record
);

-- Create Indexes for faster lookup
CREATE INDEX IDX_UserEmail ON Users(Email);              -- Index on the Email column for quick lookup
CREATE INDEX IDX_TransactionUserID ON Transactions(UserID); -- Index on UserID in Transactions
CREATE INDEX IDX_ReferralReferrerID ON ReferralBonuses(ReferrerID); -- Index on ReferrerID in ReferralBonuses

-- Error handling and constraints
-- Ensure positive amounts for transactions and bonuses
ALTER TABLE Transactions
ADD CONSTRAINT CHK_PositiveAmount CHECK (Amount > 0);

ALTER TABLE ReferralBonuses
ADD CONSTRAINT CHK_PositiveBonus CHECK (BonusAmount > 0);
```
