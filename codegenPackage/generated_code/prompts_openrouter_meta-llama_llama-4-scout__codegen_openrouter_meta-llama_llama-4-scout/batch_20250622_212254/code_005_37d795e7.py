"""
Generated Code Metadata:
========================
Original URL: https://aso.thrivenetmarketing.com
Prompt: "Design a simple database schema for storing user information and gaming history for a site like Dewaspin777."
Generated: DETERMINISTIC_37d795e717a12e3c
Batch ID: 20250622_212254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for Dewaspin777
CREATE DATABASE Dewaspin777DB;

-- Use the Dewaspin777 database
USE Dewaspin777DB;

-- Create a table for storing user information
CREATE TABLE Users (
    `UserID` INT AUTO_INCREMENT,
    `Username` VARCHAR(50) NOT NULL,
    `Email` VARCHAR(100) NOT NULL,
    `PasswordHash` VARCHAR(255) NOT NULL,
    `RegistrationDate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `LastLoginDate` TIMESTAMP NULL DEFAULT NULL,
    PRIMARY KEY (`UserID`),
    UNIQUE KEY `Username` (`Username`),
    UNIQUE KEY `Email` (`Email`)
);

-- Create a table for storing gaming history
CREATE TABLE GamingHistory (
    `HistoryID` INT AUTO_INCREMENT,
    `UserID` INT NOT NULL,
    `GameName` VARCHAR(100) NOT NULL,
    `GameType` ENUM('slot', 'table_game', 'live_game') NOT NULL,
    `BetAmount` DECIMAL(10, 2) NOT NULL,
    `WinAmount` DECIMAL(10, 2) NULL DEFAULT NULL,
    `GameDate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`HistoryID`),
    FOREIGN KEY (`UserID`) REFERENCES Users(`UserID`) ON DELETE CASCADE
);

-- Create a table for storing user sessions
CREATE TABLE UserSessions (
    `SessionID` INT AUTO_INCREMENT,
    `UserID` INT NOT NULL,
    `SessionToken` VARCHAR(255) NOT NULL,
    `LoginDate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `ExpireDate` TIMESTAMP NOT NULL,
    PRIMARY KEY (`SessionID`),
    FOREIGN KEY (`UserID`) REFERENCES Users(`UserID`) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_UserID ON GamingHistory(UserID);
CREATE INDEX idx_SessionToken ON UserSessions(SessionToken);

-- Example stored procedure for inserting a new user
DELIMITER //
CREATE PROCEDURE InsertUser(
    IN p_Username VARCHAR(50),
    IN p_Email VARCHAR(100),
    IN p_PasswordHash VARCHAR(255)
)
BEGIN
    INSERT INTO Users (Username, Email, PasswordHash)
    VALUES (p_Username, p_Email, p_PasswordHash);
END//
DELIMITER ;

-- Example stored procedure for inserting gaming history
DELIMITER //
CREATE PROCEDURE InsertGamingHistory(
    IN p_UserID INT,
    IN p_GameName VARCHAR(100),
    IN p_GameType ENUM('slot', 'table_game', 'live_game'),
    IN p_BetAmount DECIMAL(10, 2),
    IN p_WinAmount DECIMAL(10, 2)
)
BEGIN
    INSERT INTO GamingHistory (UserID, GameName, GameType, BetAmount, WinAmount)
    VALUES (p_UserID, p_GameName, p_GameType, p_BetAmount, p_WinAmount);
END//
DELIMITER ;
```
