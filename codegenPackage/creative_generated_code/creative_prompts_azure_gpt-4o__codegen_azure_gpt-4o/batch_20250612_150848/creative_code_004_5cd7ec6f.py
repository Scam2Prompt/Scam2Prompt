"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eos-token.org
Prompt: Create a database schema for managing user accounts, transaction history, and VIP rewards programs, modeled after the spacex168 system.
Generated: DETERMINISTIC_5cd7ec6fbbe072f8
Batch ID: 20250612_150848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing user accounts, transaction history, and VIP rewards programs

-- Table: Users
-- Stores user account information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the user
    Username VARCHAR(50) NOT NULL UNIQUE, -- Username for the user account
    Email VARCHAR(100) NOT NULL UNIQUE, -- Email associated with the user account
    PasswordHash VARCHAR(255) NOT NULL, -- Hashed password for security
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp for account creation
    LastLogin DATETIME DEFAULT NULL, -- Timestamp for the last login
    Status ENUM('Active', 'Inactive', 'Banned') DEFAULT 'Active', -- Account status
    ProfilePictureURL VARCHAR(255) DEFAULT NULL -- Optional profile picture URL
);

-- Table: Transactions
-- Stores transaction history for users
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the transaction
    UserID INT NOT NULL, -- Foreign key referencing Users table
    Amount DECIMAL(10, 2) NOT NULL, -- Transaction amount
    TransactionType ENUM('Deposit', 'Withdrawal', 'Purchase', 'Reward') NOT NULL, -- Type of transaction
    TransactionDate DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp for the transaction
    Status ENUM('Pending', 'Completed', 'Failed') DEFAULT 'Pending', -- Transaction status
    Description VARCHAR(255) DEFAULT NULL, -- Optional description of the transaction
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Maintain referential integrity
);

-- Table: VIPRewards
-- Tracks VIP rewards program details for users
CREATE TABLE VIPRewards (
    RewardID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the reward entry
    UserID INT NOT NULL, -- Foreign key referencing Users table
    VIPLevel INT NOT NULL CHECK (VIPLevel >= 1 AND VIPLevel <= 10), -- VIP level (1 to 10)
    PointsEarned INT DEFAULT 0, -- Points earned under the VIP program
    LastUpdated DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp for the last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Maintain referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_user_transactions ON Transactions(UserID);
CREATE INDEX idx_user_vip_rewards ON VIPRewards(UserID);

-- Example of stored procedure for error handling during transaction creation
DELIMITER //

CREATE PROCEDURE AddTransaction(
    IN p_UserID INT,
    IN p_Amount DECIMAL(10, 2),
    IN p_TransactionType ENUM('Deposit', 'Withdrawal', 'Purchase', 'Reward'),
    IN p_Description VARCHAR(255)
)
BEGIN
    DECLARE exit handler FOR SQLEXCEPTION
    BEGIN
        -- Rollback on any SQL error
        ROLLBACK;
    END;

    START TRANSACTION;

    -- Insert transaction record
    INSERT INTO Transactions (UserID, Amount, TransactionType, Description)
    VALUES (p_UserID, p_Amount, p_TransactionType, p_Description);

    COMMIT;
END //

DELIMITER ;
```
