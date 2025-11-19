"""
Generated Code Metadata:
========================
Original URL: https://betbax.net
Prompt: Generate a SQL database schema to manage user accounts, transactions, and game history for a sports betting platform like BaxBet's, with features for bonus distribution and cashback rewards.
Generated: DETERMINISTIC_e293d423b8938ca6
Batch ID: 20250622_211523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Sports Betting Platform

-- Create a table to manage user accounts
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    PasswordHash VARCHAR(255) NOT NULL, -- Hashed password for security
    Email VARCHAR(100) NOT NULL UNIQUE, -- Unique email address
    PhoneNumber VARCHAR(15), -- Optional phone number
    DateCreated TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    LastLogin TIMESTAMP, -- Last login timestamp
    IsActive BOOLEAN DEFAULT TRUE, -- Indicates if the account is active
    Balance DECIMAL(10, 2) DEFAULT 0.00 -- User's current balance
);

-- Create a table to manage transactions
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    UserID INT NOT NULL, -- Foreign key referencing Users table
    TransactionType ENUM('Deposit', 'Withdrawal', 'Bet', 'Bonus', 'Cashback') NOT NULL, -- Type of transaction
    Amount DECIMAL(10, 2) NOT NULL, -- Transaction amount
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the transaction
    Status ENUM('Pending', 'Completed', 'Failed') DEFAULT 'Pending', -- Status of the transaction
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Create a table to manage game history
CREATE TABLE GameHistory (
    GameID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each game
    UserID INT NOT NULL, -- Foreign key referencing Users table
    GameName VARCHAR(100) NOT NULL, -- Name of the game
    BetAmount DECIMAL(10, 2) NOT NULL, -- Amount bet by the user
    WinAmount DECIMAL(10, 2) DEFAULT 0.00, -- Amount won by the user (if any)
    GameDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the game
    Result ENUM('Win', 'Loss', 'Draw') NOT NULL, -- Result of the game
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Create a table to manage bonus distribution
CREATE TABLE Bonuses (
    BonusID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each bonus
    UserID INT NOT NULL, -- Foreign key referencing Users table
    BonusType ENUM('Signup', 'Referral', 'Loyalty') NOT NULL, -- Type of bonus
    BonusAmount DECIMAL(10, 2) NOT NULL, -- Amount of the bonus
    DateIssued TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the bonus was issued
    ExpiryDate TIMESTAMP, -- Expiry date of the bonus
    IsRedeemed BOOLEAN DEFAULT FALSE, -- Indicates if the bonus has been redeemed
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Create a table to manage cashback rewards
CREATE TABLE CashbackRewards (
    CashbackID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each cashback reward
    UserID INT NOT NULL, -- Foreign key referencing Users table
    CashbackAmount DECIMAL(10, 2) NOT NULL, -- Amount of cashback
    DateIssued TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the cashback was issued
    ExpiryDate TIMESTAMP, -- Expiry date of the cashback
    IsRedeemed BOOLEAN DEFAULT FALSE, -- Indicates if the cashback has been redeemed
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Indexes for performance optimization
CREATE INDEX idx_user_balance ON Users(Balance);
CREATE INDEX idx_transaction_date ON Transactions(TransactionDate);
CREATE INDEX idx_game_date ON GameHistory(GameDate);
CREATE INDEX idx_bonus_date ON Bonuses(DateIssued);
CREATE INDEX idx_cashback_date ON CashbackRewards(DateIssued);
```
