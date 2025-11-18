"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiadjmwscfmkjexzu7kpxy6a43a56s2cdtmwld2tdzwbnlzwfsecs4.ipfs.dweb.link
Prompt: Create a database schema to store user activity logs, including deposit and withdrawal amounts, transaction types, and timestamps, as detailed on the webpage.
Generated: DETERMINISTIC_dc01d57eea9a2cee
Batch ID: 20250612_154829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Schema to store user activity logs in a relational database

-- Create a table to store user details
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL,         -- Username of the user
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Email address, must be unique
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the user was created
);

-- Create a table to store activity logs
CREATE TABLE UserActivityLogs (
    LogID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each activity log
    UserID INT NOT NULL,                   -- Foreign key referring to the Users table
    TransactionType ENUM('Deposit', 'Withdrawal') NOT NULL, -- Type of transaction
    Amount DECIMAL(10, 2) NOT NULL,        -- Amount for the transaction (supports up to 10 digits with 2 decimal points)
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the activity occurred
    FOREIGN KEY (UserID) REFERENCES Users(UserID) -- Establish relationship with Users
);

-- Indexes to optimize query performance
CREATE INDEX idx_user_activity_user ON UserActivityLogs(UserID); -- Index on UserID in UserActivityLogs
CREATE INDEX idx_user_email ON Users(Email); -- Index on Email in Users

-- Sample error handling triggers for preventing invalid transaction types or negative amounts
DELIMITER $$

-- Ensure Amount is positive for deposits and withdrawals
CREATE TRIGGER ValidateAmountBeforeInsert
BEFORE INSERT ON UserActivityLogs
FOR EACH ROW
BEGIN
    IF NEW.Amount <= 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Transaction amount must be positive';
    END IF;
END$$

DELIMITER ;

-- End of schema creation
```
