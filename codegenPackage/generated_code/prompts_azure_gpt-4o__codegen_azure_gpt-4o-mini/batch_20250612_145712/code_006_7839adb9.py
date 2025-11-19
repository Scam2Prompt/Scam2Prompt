"""
Generated Code Metadata:
========================
Original URL: https://minerinde.com
Prompt: Design a database schema in SQL to store user profiles, coin balances, and referral statistics for a game similar to TG WebApp Euro Verdienen.
Generated: DETERMINISTIC_7839adb9ad6d4517
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for user profiles, coin balances, and referral statistics

-- Create a table to store user profiles
CREATE TABLE UserProfiles (
    UserID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,   -- Unique username for the user
    Email VARCHAR(100) NOT NULL UNIQUE,      -- Unique email address for the user
    PasswordHash VARCHAR(255) NOT NULL,      -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of account creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Create a table to store coin balances for users
CREATE TABLE CoinBalances (
    UserID INT PRIMARY KEY,                   -- Foreign key referencing UserProfiles
    Balance DECIMAL(10, 2) NOT NULL DEFAULT 0.00,  -- User's coin balance
    FOREIGN KEY (UserID) REFERENCES UserProfiles(UserID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a table to store referral statistics
CREATE TABLE ReferralStatistics (
    ReferralID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each referral record
    ReferrerID INT NOT NULL,                     -- UserID of the referrer
    RefereeID INT NOT NULL,                      -- UserID of the referred user
    ReferralDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date of the referral
    FOREIGN KEY (ReferrerID) REFERENCES UserProfiles(UserID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (RefereeID) REFERENCES UserProfiles(UserID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create an index on the ReferralStatistics table for faster lookups
CREATE INDEX idx_referrer ON ReferralStatistics (ReferrerID);
CREATE INDEX idx_referee ON ReferralStatistics (RefereeID);
```
