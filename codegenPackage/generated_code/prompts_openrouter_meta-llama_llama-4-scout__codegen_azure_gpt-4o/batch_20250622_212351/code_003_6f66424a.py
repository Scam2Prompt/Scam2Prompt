"""
Generated Code Metadata:
========================
Original URL: https://optionroom.finance
Prompt: "Design a basic database schema for managing user accounts, games, and transactions for an online betting platform like HUBET."
Generated: DETERMINISTIC_6f66424a58ed13f0
Batch ID: 20250622_212351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an online betting platform

-- Table to store user accounts
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Unique username for the user
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Unique email address
    Balance DECIMAL(10, 2) DEFAULT 0.00,   -- User's account balance
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to store games available for betting
CREATE TABLE Games (
    GameID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each game
    GameName VARCHAR(100) NOT NULL,        -- Name of the game
    GameDate DATETIME NOT NULL,            -- Date and time of the game
    Status ENUM('Scheduled', 'Ongoing', 'Completed') DEFAULT 'Scheduled', -- Game status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Game creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to store transactions (bets placed by users)
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    UserID INT NOT NULL,                          -- Foreign key referencing Users table
    GameID INT NOT NULL,                          -- Foreign key referencing Games table
    BetAmount DECIMAL(10, 2) NOT NULL,            -- Amount bet by the user
    BetType VARCHAR(50) NOT NULL,                 -- Type of bet (e.g., "Win", "Lose", "Draw")
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the transaction
    Status ENUM('Pending', 'Won', 'Lost') DEFAULT 'Pending', -- Status of the bet
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is removed
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE  -- Cascade delete if game is removed
);

-- Table to store audit logs for tracking changes and activities
CREATE TABLE AuditLogs (
    LogID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each log entry
    UserID INT,                           -- Foreign key referencing Users table (nullable for system logs)
    Action VARCHAR(255) NOT NULL,         -- Description of the action performed
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the action
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE SET NULL -- Set NULL if user is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_UserID ON Transactions(UserID);
CREATE INDEX idx_GameID ON Transactions(GameID);
CREATE INDEX idx_GameStatus ON Games(Status);
CREATE INDEX idx_TransactionStatus ON Transactions(Status);
```
