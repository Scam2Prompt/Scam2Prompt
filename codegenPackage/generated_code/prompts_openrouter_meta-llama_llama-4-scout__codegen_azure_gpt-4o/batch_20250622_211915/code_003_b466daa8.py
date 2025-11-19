"""
Generated Code Metadata:
========================
Original URL: https://swanbay.dip.vn
Prompt: Design a database schema for storing user information, game data, and transaction records for a betting platform like VZ99.
Generated: DETERMINISTIC_b466daa8a6fbfde0
Batch ID: 20250622_211915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a betting platform

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Unique username
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Unique email address
    FullName VARCHAR(100),                 -- Full name of the user
    DateOfBirth DATE,                      -- Date of birth of the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to store game information
CREATE TABLE Games (
    GameID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each game
    GameName VARCHAR(100) NOT NULL,        -- Name of the game
    GameType VARCHAR(50) NOT NULL,         -- Type/category of the game (e.g., sports, casino)
    StartTime DATETIME NOT NULL,           -- Start time of the game
    EndTime DATETIME,                      -- End time of the game (nullable for ongoing games)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Game creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to store transaction records
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    UserID INT NOT NULL,                          -- Foreign key referencing Users table
    GameID INT NOT NULL,                          -- Foreign key referencing Games table
    Amount DECIMAL(10, 2) NOT NULL,               -- Transaction amount
    TransactionType ENUM('Bet', 'Win', 'Deposit', 'Withdrawal') NOT NULL, -- Type of transaction
    TransactionStatus ENUM('Pending', 'Completed', 'Failed') NOT NULL,    -- Status of the transaction
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Transaction creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete for user
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE -- Cascade delete for game
);

-- Table to store bets placed by users
CREATE TABLE Bets (
    BetID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each bet
    UserID INT NOT NULL,                  -- Foreign key referencing Users table
    GameID INT NOT NULL,                  -- Foreign key referencing Games table
    BetAmount DECIMAL(10, 2) NOT NULL,    -- Amount bet by the user
    BetOutcome VARCHAR(50),               -- Predicted outcome of the bet
    BetStatus ENUM('Pending', 'Won', 'Lost') NOT NULL, -- Status of the bet
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Bet creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete for user
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE -- Cascade delete for game
);

-- Indexes for optimizing queries
CREATE INDEX idx_user_transactions ON Transactions(UserID);
CREATE INDEX idx_game_transactions ON Transactions(GameID);
CREATE INDEX idx_user_bets ON Bets(UserID);
CREATE INDEX idx_game_bets ON Bets(GameID);
```
