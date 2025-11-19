"""
Generated Code Metadata:
========================
Original URL: https://republik.pages.dev
Prompt: Design a database schema to store information about slot games, including game metadata, RTP rates, and user gameplay history, for a platform like ANGKA805.
Generated: DETERMINISTIC_6ac61a818273b502
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for slot games
CREATE DATABASE SlotGameDB;

-- Use the database
USE SlotGameDB;

-- Create table for game metadata
CREATE TABLE Games (
    `GameID` INT AUTO_INCREMENT,
    `GameName` VARCHAR(255) NOT NULL,
    `GameDescription` TEXT,
    `GameType` ENUM('SLOT', 'TABLE_GAME') NOT NULL,
    `CreatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `UpdatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`GameID`)
);

-- Create table for RTP rates
CREATE TABLE RTP_Rates (
    `RTPID` INT AUTO_INCREMENT,
    `GameID` INT NOT NULL,
    `RTP` DECIMAL(5,2) NOT NULL,
    `CreatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `UpdatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`RTPID`),
    FOREIGN KEY (`GameID`) REFERENCES Games(`GameID`) ON DELETE CASCADE
);

-- Create table for user gameplay history
CREATE TABLE User_Gameplay_History (
    `HistoryID` BIGINT AUTO_INCREMENT,
    `UserID` INT NOT NULL,
    `GameID` INT NOT NULL,
    `BetAmount` DECIMAL(10,2) NOT NULL,
    `WinAmount` DECIMAL(10,2) NOT NULL,
    `GameplayDate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`HistoryID`),
    FOREIGN KEY (`GameID`) REFERENCES Games(`GameID`) ON DELETE CASCADE
);

-- Create table for users
CREATE TABLE Users (
    `UserID` INT AUTO_INCREMENT,
    `Username` VARCHAR(255) NOT NULL UNIQUE,
    `Email` VARCHAR(255) NOT NULL UNIQUE,
    `PasswordHash` VARCHAR(255) NOT NULL,
    `CreatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `UpdatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`UserID`)
);

-- Create index on GameID and UserID for faster queries
CREATE INDEX idx_GameID ON User_Gameplay_History (GameID);
CREATE INDEX idx_UserID ON User_Gameplay_History (UserID);

-- Procedure to insert gameplay history
DELIMITER //
CREATE PROCEDURE InsertGameplayHistory(
    IN p_UserID INT,
    IN p_GameID INT,
    IN p_BetAmount DECIMAL(10,2),
    IN p_WinAmount DECIMAL(10,2)
)
BEGIN
    INSERT INTO User_Gameplay_History (UserID, GameID, BetAmount, WinAmount)
    VALUES (p_UserID, p_GameID, p_BetAmount, p_WinAmount);
END//
DELIMITER ;

-- Procedure to get user gameplay history
DELIMITER //
CREATE PROCEDURE GetUserGameplayHistory(
    IN p_UserID INT
)
BEGIN
    SELECT * FROM User_Gameplay_History
    WHERE UserID = p_UserID
    ORDER BY GameplayDate DESC;
END//
DELIMITER ;

-- Example usage
INSERT INTO Games (GameName, GameDescription, GameType)
VALUES ('Slot Game 1', 'This is a slot game', 'SLOT');

INSERT INTO RTP_Rates (GameID, RTP)
VALUES (1, 95.00);

INSERT INTO Users (Username, Email, PasswordHash)
VALUES ('user1', 'user1@example.com', 'password_hash');

CALL InsertGameplayHistory(1, 1, 10.00, 50.00);

CALL GetUserGameplayHistory(1);
```
