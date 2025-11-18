"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonanzavc.com
Prompt: Suggest a database schema for storing user information, membership levels, referral codes, and earnings percentages for a platform similar to BonanzaVC.
Generated: DETERMINISTIC_da72e4829e4cd029
Batch ID: 20250612_154058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for a platform storing user information, membership levels, referral codes, 
-- and earnings percentages

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FullName VARCHAR(255) NOT NULL,        -- Full name of the user
    Email VARCHAR(320) NOT NULL UNIQUE,    -- Email address of the user (must be unique)
    PasswordHash VARCHAR(255) NOT NULL,   -- Hashed password for secure storage
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the user was last modified
);

-- Table to store membership levels available in the platform
CREATE TABLE MembershipLevels (
    LevelID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each membership level
    LevelName VARCHAR(100) NOT NULL UNIQUE, -- Name of the membership level (e.g., "Basic", "Premium")
    EarningsPercentage DECIMAL(5, 2) NOT NULL, -- Earnings percentage associated with the membership level
    Description TEXT,                        -- Optional description of the membership level
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the membership level was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when last modified
);

-- Table to store referral codes associated with users
CREATE TABLE ReferralCodes (
    CodeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each referral code
    UserID INT NOT NULL,                   -- User who owns this referral code
    ReferralCode VARCHAR(50) NOT NULL UNIQUE, -- Unique referral code
    IsActive BOOLEAN DEFAULT TRUE,         -- Status of the referral code (active or inactive)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the referral code was created
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Foreign key pointing to Users
);

-- Table to store earnings history for users based on referrals or other factors
CREATE TABLE Earnings (
    EarningID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each earning record
    UserID INT NOT NULL,                       -- User who earned the amount
    AmountEarned DECIMAL(10, 2) NOT NULL,      -- Amount earned
    Source VARCHAR(255),                       -- Source of the earning (e.g., "Referral")
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the earning was recorded
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Foreign key pointing to Users
);

-- Ensure proper indexing for performance optimization
CREATE INDEX idx_Users_Email ON Users(Email);
CREATE INDEX idx_ReferralCodes_UserID ON ReferralCodes(UserID);
CREATE INDEX idx_Earnings_UserID ON Earnings(UserID);
```
