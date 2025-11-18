"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bolehshop.id
Prompt: Create a database schema in SQL for managing lottery game results, user accounts, and payment transactions, inspired by the HONGTOGEL platform.
Generated: DETERMINISTIC_078d2b3a960e1199
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing lottery game results, user accounts, and payment transactions

-- Table for storing user account information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE, -- Unique username
    PasswordHash VARCHAR(255) NOT NULL, -- Hashed password for security
    Email VARCHAR(100) NOT NULL UNIQUE, -- Unique email address
    FullName VARCHAR(100), -- Full name of the user
    PhoneNumber VARCHAR(15), -- Optional phone number
    Balance DECIMAL(10, 2) DEFAULT 0.00, -- User's account balance
    IsActive BOOLEAN DEFAULT TRUE, -- Status of the account
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table for storing lottery game information
CREATE TABLE LotteryGames (
    GameID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each game
    GameName VARCHAR(100) NOT NULL, -- Name of the lottery game
    DrawDate DATE NOT NULL, -- Date of the lottery draw
    WinningNumbers VARCHAR(255) NOT NULL, -- Winning numbers for the game
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table for storing user bets on lottery games
CREATE TABLE UserBets (
    BetID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each bet
    UserID INT NOT NULL, -- Reference to the user who placed the bet
    GameID INT NOT NULL, -- Reference to the lottery game
    BetNumbers VARCHAR(255) NOT NULL, -- Numbers chosen by the user
    BetAmount DECIMAL(10, 2) NOT NULL, -- Amount bet by the user
    IsWinningBet BOOLEAN DEFAULT FALSE, -- Whether the bet was a winning bet
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Bet creation timestamp
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Foreign key to Users table
    FOREIGN KEY (GameID) REFERENCES LotteryGames(GameID) ON DELETE CASCADE -- Foreign key to LotteryGames table
);

-- Table for storing payment transactions
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    UserID INT NOT NULL, -- Reference to the user
    TransactionType ENUM('Deposit', 'Withdrawal', 'Bet') NOT NULL, -- Type of transaction
    Amount DECIMAL(10, 2) NOT NULL, -- Transaction amount
    Status ENUM('Pending', 'Completed', 'Failed') DEFAULT 'Pending', -- Status of the transaction
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Transaction creation timestamp
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Foreign key to Users table
);

-- Create indexes for faster queries
CREATE INDEX idx_UserID ON UserBets(UserID);
CREATE INDEX idx_GameID ON UserBets(GameID);
CREATE INDEX idx_TransactionUserID ON Transactions(UserID);
```
