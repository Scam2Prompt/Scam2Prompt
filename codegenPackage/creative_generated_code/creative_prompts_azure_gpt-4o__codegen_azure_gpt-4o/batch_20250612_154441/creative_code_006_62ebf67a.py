"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethopt.io
Prompt: Create a database schema for managing diverse casino games, user accounts, and transaction histories for a platform like 2QCOM.
Generated: DETERMINISTIC_62ebf67a6f62fdc9
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Casino management database schema for user accounts, games, and transaction histories

-- Table to store user accounts
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Unique username for the user
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for authentication
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Unique email address
    FullName VARCHAR(100) NOT NULL,        -- Full name of the user
    Balance DECIMAL(10, 2) DEFAULT 0.00,   -- Current balance in the user's account
    IsActive BOOLEAN DEFAULT TRUE,         -- Status indicating if the account is active
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the account was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Date and time of last account update
);

-- Table to store casino games
CREATE TABLE Games (
    GameID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each game
    GameName VARCHAR(100) NOT NULL UNIQUE, -- Name of the game
    GameType VARCHAR(50) NOT NULL,         -- Type/category of the game (e.g., "Slot", "Poker", etc.)
    MinBet DECIMAL(10, 2) DEFAULT 0.00,    -- Minimum bet amount for the game
    MaxBet DECIMAL(10, 2),                 -- Maximum bet amount for the game
    IsActive BOOLEAN DEFAULT TRUE,         -- Status indicating if the game is currently active
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the game was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Date and time of last game update
);

-- Table to store transaction history
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    UserID INT NOT NULL,                          -- Foreign key referencing Users(UserID)
    GameID INT,                                   -- Foreign key referencing Games(GameID), nullable for non-game transactions
    TransactionType ENUM('Deposit', 'Withdraw', 'Bet', 'Win') NOT NULL, -- Type of transaction
    Amount DECIMAL(10, 2) NOT NULL,               -- Transaction amount
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the transaction
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is removed
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE SET NULL -- Set GameID to NULL if game is removed
);

-- Table to track game sessions (optional for advanced features)
CREATE TABLE GameSessions (
    SessionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each game session
    UserID INT NOT NULL,                      -- Foreign key referencing Users(UserID)
    GameID INT NOT NULL,                      -- Foreign key referencing Games(GameID)
    StartTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Start time of the gaming session
    EndTime TIMESTAMP NULL,                   -- End time of the gaming session
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is removed
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE -- Cascade delete if game is removed
);

-- Indexes for performance optimization
CREATE INDEX IDX_UserBalance ON Users (Balance);
CREATE INDEX IDX_TransactionDate ON Transactions (TransactionDate);
CREATE INDEX IDX_GameType ON Games (GameType);

-- End of schema
```
