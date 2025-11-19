"""
Generated Code Metadata:
========================
Original URL: https://play.dee.casino
Prompt: "Design a basic database schema for storing user transactions, bets, and game outcomes for an online casino."
Generated: DETERMINISTIC_8991e26de0b3399a
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an online casino system

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Unique username for the user
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Unique email for the user
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    Balance DECIMAL(15, 2) DEFAULT 0.00,   -- User's account balance
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to store transactions (deposits, withdrawals, etc.)
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    UserID INT NOT NULL,                          -- Foreign key to Users table
    Amount DECIMAL(15, 2) NOT NULL,               -- Transaction amount (positive for deposits, negative for withdrawals)
    TransactionType ENUM('Deposit', 'Withdrawal') NOT NULL, -- Type of transaction
    Status ENUM('Pending', 'Completed', 'Failed') DEFAULT 'Pending', -- Transaction status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Transaction creation timestamp
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Table to store bets placed by users
CREATE TABLE Bets (
    BetID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each bet
    UserID INT NOT NULL,                  -- Foreign key to Users table
    GameID INT NOT NULL,                  -- Foreign key to Games table
    BetAmount DECIMAL(15, 2) NOT NULL,    -- Amount wagered by the user
    PayoutAmount DECIMAL(15, 2) DEFAULT 0.00, -- Amount won (if any)
    BetStatus ENUM('Pending', 'Won', 'Lost') DEFAULT 'Pending', -- Status of the bet
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Bet creation timestamp
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is deleted
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE -- Cascade delete if game is deleted
);

-- Table to store game outcomes
CREATE TABLE Games (
    GameID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each game
    GameName VARCHAR(100) NOT NULL,        -- Name of the game
    Outcome VARCHAR(50) DEFAULT NULL,      -- Outcome of the game (e.g., "Player Wins", "Dealer Wins")
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Game creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Indexes for performance optimization
CREATE INDEX idx_user_transactions ON Transactions(UserID);
CREATE INDEX idx_user_bets ON Bets(UserID);
CREATE INDEX idx_game_bets ON Bets(GameID);
```
