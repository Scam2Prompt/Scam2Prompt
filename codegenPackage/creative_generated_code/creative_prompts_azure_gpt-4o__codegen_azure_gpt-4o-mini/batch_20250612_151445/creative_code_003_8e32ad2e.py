"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.shibaswaap.us.com
Prompt: Create a database schema for managing user accounts, game statistics, and transaction histories for a multi-platform gaming ecosystem like 789Club.
Generated: DETERMINISTIC_8e32ad2e89fb5cb8
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing user accounts, game statistics, and transaction histories 
-- for a multi-platform gaming ecosystem

CREATE DATABASE IF NOT EXISTS GamingEcosystem;

USE GamingEcosystem;

-- Table to store user account information
CREATE TABLE IF NOT EXISTS Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    Username VARCHAR(50) NOT NULL UNIQUE,
    Email VARCHAR(100) NOT NULL UNIQUE,
    PasswordHash VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    IsActive BOOLEAN DEFAULT TRUE
);

-- Table to store game statistics for each user
CREATE TABLE IF NOT EXISTS GameStatistics (
    StatID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT NOT NULL,
    GameID INT NOT NULL,
    Score INT NOT NULL,
    LevelReached INT NOT NULL,
    Playtime INT NOT NULL, -- Playtime in minutes
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE
);

-- Table to manage games available in the ecosystem
CREATE TABLE IF NOT EXISTS Games (
    GameID INT AUTO_INCREMENT PRIMARY KEY,
    GameName VARCHAR(100) NOT NULL,
    Platform VARCHAR(50) NOT NULL,
    ReleaseDate DATE,
    IsActive BOOLEAN DEFAULT TRUE
);

-- Table to store transaction histories for user purchases or in-game transactions
CREATE TABLE IF NOT EXISTS Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL, -- Amount in the currency used
    TransactionType ENUM('Deposit', 'Withdrawal', 'Purchase') NOT NULL,
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

-- Indexes for better query performance
CREATE INDEX idx_username ON Users (Username);
CREATE INDEX idx_email ON Users (Email);
CREATE INDEX idx_userid ON GameStatistics (UserID);
CREATE INDEX idx_transaction_user ON Transactions (UserID);

-- Sample trigger to prevent transactions exceeding user balance (assuming a balance field exists)
DELIMITER //
CREATE TRIGGER PreventOverspending
BEFORE INSERT ON Transactions
FOR EACH ROW
BEGIN
    DECLARE user_balance DECIMAL(10, 2);
    
    SELECT Balance INTO user_balance FROM UserBalances WHERE UserID = NEW.UserID; -- Assume UserBalances table exists

    IF NEW.TransactionType = 'Withdrawal' AND user_balance < NEW.Amount THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Insufficient balance for the transaction';
    END IF;
END;
//
DELIMITER ;

-- Sample view to summarize user statistics
CREATE VIEW UserSummary AS
SELECT 
    u.UserID,
    u.Username,
    COUNT(gs.StatID) AS TotalGamesPlayed,
    SUM(gs.Score) AS TotalScore,
    SUM(t.Amount) AS TotalSpent
FROM Users u
LEFT JOIN GameStatistics gs ON u.UserID = gs.UserID
LEFT JOIN Transactions t ON u.UserID = t.UserID
GROUP BY u.UserID, u.Username;

-- End of schema
```
