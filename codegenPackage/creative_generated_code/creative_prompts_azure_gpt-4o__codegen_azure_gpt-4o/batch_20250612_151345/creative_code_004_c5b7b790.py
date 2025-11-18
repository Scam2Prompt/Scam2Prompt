"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://foodandwine.one
Prompt: Write a SQL schema for a database to manage game categories, user bets, and transaction records for a gambling platform similar to Hi88.
Generated: DETERMINISTIC_c5b7b7902b8df56d
Batch ID: 20250612_151345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Schema for a Gambling Platform Database

-- Table to manage game categories
CREATE TABLE GameCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,         -- Unique identifier for the game category
    Name VARCHAR(255) NOT NULL,                        -- Name of the game category
    Description TEXT,                                  -- Optional description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the latest update
);

-- Table to manage users
CREATE TABLE Users (
    UserID INT PRIMARY KEY AUTO_INCREMENT,             -- Unique identifier for the user
    Username VARCHAR(255) NOT NULL UNIQUE,             -- Unique username for the user
    Email VARCHAR(255) NOT NULL UNIQUE,                -- Unique email for the user
    PasswordHash VARCHAR(255) NOT NULL,                -- Hashed password for secure storage
    Balance DECIMAL(10, 2) DEFAULT 0.00,               -- User's account balance
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Timestamp for when the user was registered
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the latest update
);

-- Table to manage user bets
CREATE TABLE Bets (
    BetID INT PRIMARY KEY AUTO_INCREMENT,              -- Unique identifier for the bet
    UserID INT NOT NULL,                               -- Reference to the user placing the bet
    CategoryID INT NOT NULL,                           -- Reference to the game category for the bet
    Amount DECIMAL(10, 2) NOT NULL,                    -- Amount bet by the user
    Outcome ENUM('WIN', 'LOSS', 'PENDING') DEFAULT 'PENDING', -- Outcome of the bet
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Timestamp for when the bet was placed
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Foreign key to Users table
    FOREIGN KEY (CategoryID) REFERENCES GameCategories(CategoryID) ON DELETE CASCADE -- Foreign key to GameCategories table
);

-- Table to manage transaction records
CREATE TABLE Transactions (
    TransactionID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for the transaction
    UserID INT NOT NULL,                               -- Reference to the user involved in the transaction
    BetID INT,                                         -- Reference to the bet (if applicable)
    Type ENUM('DEPOSIT', 'WITHDRAWAL', 'BET_PLACEMENT', 'BET_SETTLEMENT') NOT NULL, -- Type of transaction
    Amount DECIMAL(10, 2) NOT NULL,                    -- Amount involved in the transaction
    Status ENUM('SUCCESS', 'FAILED', 'PENDING') DEFAULT 'PENDING', -- Status of the transaction
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Timestamp for when the transaction occurred
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Foreign key to Users table
    FOREIGN KEY (BetID) REFERENCES Bets(BetID) ON DELETE SET NULL -- Foreign key to Bets table
);

-- Indexes for optimization
CREATE INDEX idx_UserID ON Users(UserID);
CREATE INDEX idx_CategoryID ON GameCategories(CategoryID);
CREATE INDEX idx_BetUser ON Bets(UserID);
CREATE INDEX idx_TransactionUser ON Transactions(UserID);
```
