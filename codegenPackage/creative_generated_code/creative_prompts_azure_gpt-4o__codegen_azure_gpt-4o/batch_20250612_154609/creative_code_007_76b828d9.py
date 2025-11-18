"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welforcevestcapital.com
Prompt: Generate SQL queries to track user activity on Welforcevest Capital, including deposits, withdrawals, referrals, and ranking upgrades, for reporting and analytics purposes.
Generated: DETERMINISTIC_76b828d9cbfc9148
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a table to store user activity logs
CREATE TABLE UserActivityLogs (
    LogID INT AUTO_INCREMENT PRIMARY KEY,              -- Unique identifier for the log
    UserID INT NOT NULL,                               -- Reference to the user performing the activity
    ActivityType ENUM('Deposit', 'Withdrawal', 'Referral', 'RankingUpgrade') NOT NULL, -- Type of activity
    Amount DECIMAL(18, 2),                            -- Amount involved in the activity (if applicable)
    ReferralUserID INT NULL,                          -- Reference to the user referred (for referrals)
    OldRank VARCHAR(50),                              -- Old ranking (for ranking upgrades)
    NewRank VARCHAR(50),                              -- New ranking (for ranking upgrades)
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,     -- Time of the activity
    Remarks VARCHAR(255)                              -- Additional details or metadata about the activity
);

-- Query to log a deposit activity
INSERT INTO UserActivityLogs (UserID, ActivityType, Amount, Remarks)
VALUES (123, 'Deposit', 500.00, 'Deposit made via bank transfer.');

-- Query to log a withdrawal activity
INSERT INTO UserActivityLogs (UserID, ActivityType, Amount, Remarks)
VALUES (123, 'Withdrawal', 200.00, 'Withdrawal to PayPal.');

-- Query to log a referral activity
INSERT INTO UserActivityLogs (UserID, ActivityType, ReferralUserID, Remarks)
VALUES (123, 'Referral', 456, 'User referred successfully.');

-- Query to log a ranking upgrade activity
INSERT INTO UserActivityLogs (UserID, ActivityType, OldRank, NewRank, Remarks)
VALUES (123, 'RankingUpgrade', 'Silver', 'Gold', 'User upgraded ranking due to performance.');

-- Query to retrieve all user activities for analytics
SELECT 
    UserID,
    ActivityType,
    Amount,
    ReferralUserID,
    OldRank,
    NewRank,
    Timestamp,
    Remarks
FROM UserActivityLogs
ORDER BY Timestamp DESC;

-- Query to get the total deposits made by each user
SELECT 
    UserID,
    SUM(Amount) AS TotalDeposits
FROM UserActivityLogs
WHERE ActivityType = 'Deposit'
GROUP BY UserID;

-- Query to get the total withdrawals made by each user
SELECT 
    UserID,
    SUM(Amount) AS TotalWithdrawals
FROM UserActivityLogs
WHERE ActivityType = 'Withdrawal'
GROUP BY UserID;

-- Query to count the number of referrals each user has made
SELECT 
    UserID,
    COUNT(ReferralUserID) AS TotalReferrals
FROM UserActivityLogs
WHERE ActivityType = 'Referral'
GROUP BY UserID;

-- Query to retrieve ranking upgrade history for each user
SELECT 
    UserID,
    OldRank,
    NewRank,
    Timestamp,
    Remarks
FROM UserActivityLogs
WHERE ActivityType = 'RankingUpgrade'
ORDER BY Timestamp DESC;

-- Error handling suggestion:
-- Ensure constraints and foreign keys are applied for UserID and ReferralUserID fields to maintain data integrity.
-- For production usage, index the UserID and ActivityType columns to optimize query performance.
```
