"""
Generated Code Metadata:
========================
Original URL: https://dromhusab.se
Prompt: "Design a database schema for an online casino platform, including tables for users, games, transactions, and bonuses, inspired by sites like Vulkan Vegas."
Generated: DETERMINISTIC_8ae20917dc018840
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for online casino platform

CREATE DATABASE OnlineCasino;

USE OnlineCasino;

-- Table to store user information
CREATE TABLE Users (
    `UserID` BIGINT AUTO_INCREMENT,
    `Username` VARCHAR(50) NOT NULL,
    `Email` VARCHAR(100) NOT NULL,
    `PasswordHash` VARCHAR(255) NOT NULL,
    `Country` VARCHAR(50) NOT NULL,
    `Currency` VARCHAR(10) NOT NULL,
    `RegistrationDate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `LastLoginDate` TIMESTAMP NULL,
    `IsActive` BOOLEAN DEFAULT TRUE,
    `IsVerified` BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (`UserID`),
    UNIQUE KEY (`Username`),
    UNIQUE KEY (`Email`)
);

-- Table to store game information
CREATE TABLE Games (
    `GameID` INT AUTO_INCREMENT,
    `GameName` VARCHAR(100) NOT NULL,
    `GameType` ENUM('slot', 'table', 'live') NOT NULL,
    `Provider` VARCHAR(50) NOT NULL,
    `MinBet` DECIMAL(10, 2) NOT NULL,
    `MaxBet` DECIMAL(10, 2) NOT NULL,
    `IsActive` BOOLEAN DEFAULT TRUE,
    PRIMARY KEY (`GameID`)
);

-- Table to store user accounts and balances
CREATE TABLE Accounts (
    `AccountID` BIGINT AUTO_INCREMENT,
    `UserID` BIGINT NOT NULL,
    `Balance` DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    `PendingWithdrawal` DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    `CreatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`AccountID`),
    FOREIGN KEY (`UserID`) REFERENCES Users(`UserID`) ON DELETE CASCADE
);

-- Table to store transactions (deposits, withdrawals)
CREATE TABLE Transactions (
    `TransactionID` BIGINT AUTO_INCREMENT,
    `UserID` BIGINT NOT NULL,
    `AccountID` BIGINT NOT NULL,
    `TransactionType` ENUM('deposit', 'withdrawal') NOT NULL,
    `Amount` DECIMAL(10, 2) NOT NULL,
    `Status` ENUM('pending', 'success', 'failed') NOT NULL DEFAULT 'pending',
    `CreatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`TransactionID`),
    FOREIGN KEY (`UserID`) REFERENCES Users(`UserID`) ON DELETE CASCADE,
    FOREIGN KEY (`AccountID`) REFERENCES Accounts(`AccountID`) ON DELETE CASCADE
);

-- Table to store bonuses and promotions
CREATE TABLE Bonuses (
    `BonusID` INT AUTO_INCREMENT,
    `BonusType` ENUM('welcome', 'deposit', 'free_spin') NOT NULL,
    `Description` TEXT NOT NULL,
    `Terms` TEXT NOT NULL,
    `CreatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`BonusID`)
);

-- Table to store user bonuses and claims
CREATE TABLE UserBonuses (
    `UserBonusID` BIGINT AUTO_INCREMENT,
    `UserID` BIGINT NOT NULL,
    `BonusID` INT NOT NULL,
    `ClaimedAt` TIMESTAMP NULL,
    `ExpiredAt` TIMESTAMP NULL,
    PRIMARY KEY (`UserBonusID`),
    FOREIGN KEY (`UserID`) REFERENCES Users(`UserID`) ON DELETE CASCADE,
    FOREIGN KEY (`BonusID`) REFERENCES Bonuses(`BonusID`) ON DELETE CASCADE
);

-- Table to store game bets and results
CREATE TABLE Bets (
    `BetID` BIGINT AUTO_INCREMENT,
    `UserID` BIGINT NOT NULL,
    `GameID` INT NOT NULL,
    `BetAmount` DECIMAL(10, 2) NOT NULL,
    `BetDetails` JSON NOT NULL,
    `Result` JSON NULL,
    `CreatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`BetID`),
    FOREIGN KEY (`UserID`) REFERENCES Users(`UserID`) ON DELETE CASCADE,
    FOREIGN KEY (`GameID`) REFERENCES Games(`GameID`) ON DELETE CASCADE
);

-- Create indexes on frequently used columns
CREATE INDEX idx_Users_Username ON Users (Username);
CREATE INDEX idx_Users_Email ON Users (Email);
CREATE INDEX idx_Accounts_UserID ON Accounts (UserID);
CREATE INDEX idx_Transactions_UserID ON Transactions (UserID);
CREATE INDEX idx_Bonuses_BonusType ON Bonuses (BonusType);
CREATE INDEX idx_UserBonuses_UserID ON UserBonuses (UserID);
CREATE INDEX idx_Bets_UserID ON Bets (UserID);
CREATE INDEX idx_Bets_GameID ON Bets (GameID);
```

```sql
-- Example inserts for testing
INSERT INTO Users (Username, Email, PasswordHash, Country, Currency)
VALUES 
('testuser', 'test@example.com', 'password_hash', 'USA', 'USD'),
('testuser2', 'test2@example.com', 'password_hash2', 'Canada', 'CAD');

INSERT INTO Games (GameName, GameType, Provider, MinBet, MaxBet)
VALUES 
('Slot Game', 'slot', 'Provider1', 0.10, 100.00),
('Table Game', 'table', 'Provider2', 1.00, 1000.00);

INSERT INTO Accounts (UserID, Balance)
VALUES 
(1, 100.00),
(2, 50.00);

INSERT INTO Bonuses (BonusType, Description, Terms)
VALUES 
('welcome', 'Welcome bonus description', 'Welcome bonus terms');

INSERT INTO UserBonuses (UserID, BonusID)
VALUES 
(1, 1),
(2, 1);
```
