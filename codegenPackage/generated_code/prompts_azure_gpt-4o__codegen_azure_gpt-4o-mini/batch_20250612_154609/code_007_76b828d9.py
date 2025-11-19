"""
Generated Code Metadata:
========================
Original URL: https://welforcevestcapital.com
Prompt: Generate SQL queries to track user activity on Welforcevest Capital, including deposits, withdrawals, referrals, and ranking upgrades, for reporting and analytics purposes.
Generated: DETERMINISTIC_76b828d9cbfc9148
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to track user activity on Welforcevest Capital

-- Create a table to log user activities
CREATE TABLE UserActivityLog (
    ActivityID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each activity
    UserID INT NOT NULL,                         -- ID of the user performing the activity
    ActivityType ENUM('Deposit', 'Withdrawal', 'Referral', 'Ranking Upgrade') NOT NULL,  -- Type of activity
    ActivityAmount DECIMAL(10, 2),              -- Amount involved in the activity (for deposits/withdrawals)
    ReferralID INT,                              -- ID of the referred user (if applicable)
    ActivityDate DATETIME DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of the activity
    FOREIGN KEY (UserID) REFERENCES Users(UserID),  -- Foreign key to Users table
    FOREIGN KEY (ReferralID) REFERENCES Users(UserID)  -- Foreign key to Users table for referrals
);

-- Insert a new deposit activity
INSERT INTO UserActivityLog (UserID, ActivityType, ActivityAmount)
VALUES (?, 'Deposit', ?);

-- Insert a new withdrawal activity
INSERT INTO UserActivityLog (UserID, ActivityType, ActivityAmount)
VALUES (?, 'Withdrawal', ?);

-- Insert a new referral activity
INSERT INTO UserActivityLog (UserID, ActivityType, ReferralID)
VALUES (?, 'Referral', ?);

-- Insert a new ranking upgrade activity
INSERT INTO UserActivityLog (UserID, ActivityType)
VALUES (?, 'Ranking Upgrade');

-- Query to retrieve user activity report
SELECT 
    UserID,
    ActivityType,
    SUM(ActivityAmount) AS TotalAmount,
    COUNT(*) AS ActivityCount,
    MIN(ActivityDate) AS FirstActivityDate,
    MAX(ActivityDate) AS LastActivityDate
FROM 
    UserActivityLog
GROUP BY 
    UserID, ActivityType
ORDER BY 
    UserID, ActivityType;

-- Error handling for insert operations
DELIMITER //

CREATE PROCEDURE LogUserActivity(
    IN p_UserID INT,
    IN p_ActivityType ENUM('Deposit', 'Withdrawal', 'Referral', 'Ranking Upgrade'),
    IN p_ActivityAmount DECIMAL(10, 2) DEFAULT NULL,
    IN p_ReferralID INT DEFAULT NULL
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Handle the error (e.g., log it, rethrow it, etc.)
        ROLLBACK;
        SELECT 'Error occurred while logging user activity' AS ErrorMessage;
    END;

    START TRANSACTION;

    INSERT INTO UserActivityLog (UserID, ActivityType, ActivityAmount, ReferralID)
    VALUES (p_UserID, p_ActivityType, p_ActivityAmount, p_ReferralID);

    COMMIT;
END //

DELIMITER ;
```
