"""
Generated Code Metadata:
========================
Original URL: https://billionalr.com
Prompt: Design a database schema to store user information, deposit history, and bonus claims for a slot game platform offering a "Depo 25 Bonus 25" promotion.
Generated: DETERMINISTIC_d30a8331e5452456
Batch ID: 20250622_205440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a slot game platform offering "Depo 25 Bonus 25" promotion

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Unique username for the user
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Unique email address
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store deposit history
CREATE TABLE Deposits (
    DepositID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each deposit
    UserID INT NOT NULL,                      -- Foreign key referencing Users table
    Amount DECIMAL(10, 2) NOT NULL,           -- Deposit amount
    DepositDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the deposit
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Table to store bonus claims
CREATE TABLE BonusClaims (
    BonusClaimID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each bonus claim
    UserID INT NOT NULL,                         -- Foreign key referencing Users table
    DepositID INT NOT NULL,                      -- Foreign key referencing Deposits table
    BonusAmount DECIMAL(10, 2) NOT NULL,         -- Bonus amount claimed
    ClaimedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the bonus was claimed
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is deleted
    FOREIGN KEY (DepositID) REFERENCES Deposits(DepositID) ON DELETE CASCADE -- Cascade delete if deposit is deleted
);

-- Indexes for performance optimization
CREATE INDEX idx_user_deposit ON Deposits(UserID);
CREATE INDEX idx_user_bonus ON BonusClaims(UserID);
CREATE INDEX idx_deposit_bonus ON BonusClaims(DepositID);
```
