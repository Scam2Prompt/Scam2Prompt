"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tekanslotcepat.site
Prompt: Generate a database schema to manage user accounts, game preferences, and transaction history for a platform similar to Tekanslot.
Generated: DETERMINISTIC_bd33a64d04787461
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing user accounts, game preferences, and transaction history

-- Table to store user accounts
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,    -- Username (must be unique)
    Email VARCHAR(100) NOT NULL UNIQUE,      -- Email address (must be unique)
    PasswordHash VARCHAR(255) NOT NULL,      -- Hashed password for secure storage
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user account creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last account update
);

-- Table to store game preferences for each user
CREATE TABLE GamePreferences (
    PreferenceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each preference entry
    UserID INT NOT NULL,                         -- Foreign key referencing Users table
    GameName VARCHAR(100) NOT NULL,              -- Name of the game
    PreferenceData JSON,                         -- JSON data to store game-specific preferences
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of preference entry creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last preference update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete when user is deleted
);

-- Table to store transaction history
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    UserID INT NOT NULL,                          -- Foreign key referencing Users table
    Amount DECIMAL(10, 2) NOT NULL,               -- Transaction amount
    TransactionType ENUM('Deposit', 'Withdrawal', 'Purchase') NOT NULL, -- Transaction type
    Status ENUM('Pending', 'Completed', 'Failed') NOT NULL,            -- Status of the transaction
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of transaction creation
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete when user is deleted
);

-- Index for faster searching by email in Users table
CREATE INDEX idx_email ON Users (Email);

-- Index for faster searching by UserID in GamePreferences table
CREATE INDEX idx_userid_gamepreferences ON GamePreferences (UserID);

-- Index for faster searching by UserID in Transactions table
CREATE INDEX idx_userid_transactions ON Transactions (UserID);
```
