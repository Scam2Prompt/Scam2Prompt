"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bolehshop.id
Prompt: Outline a database schema for storing user data and lottery transactions for a site like HONGTOGEL, focusing on security and efficiency.
Generated: DETERMINISTIC_c640183d4b00ae42
Batch ID: 20250612_164238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for User and Lottery Transactions

-- Table for storing user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE, -- Unique username
    PasswordHash CHAR(64) NOT NULL, -- Securely stored hash of the password
    Email VARCHAR(100) NOT NULL UNIQUE, -- Unique email address
    FullName VARCHAR(100), -- Full name of the user (optional)
    PhoneNumber VARCHAR(15), -- Contact number (optional, can be NULL)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user account was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table for storing lottery transactions
CREATE TABLE LotteryTransactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    UserID INT NOT NULL, -- Foreign key referencing Users(UserID)
    LotteryNumber VARCHAR(50) NOT NULL, -- Lottery number selected by the user
    Amount DECIMAL(10, 2) NOT NULL, -- Amount bet on the lottery
    TransactionStatus ENUM('PENDING', 'SUCCESS', 'FAILED') NOT NULL, -- Status of the transaction
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the transaction was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table for storing lottery results
CREATE TABLE LotteryResults (
    ResultID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each lottery result
    LotteryDate DATE NOT NULL, -- Date of the lottery draw
    WinningNumber VARCHAR(50) NOT NULL, -- Winning lottery number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the result was created
);

-- Indexes for performance optimization
CREATE INDEX idx_LotteryTransactions_UserID ON LotteryTransactions(UserID); -- Index for faster lookup of transactions by user
CREATE INDEX idx_LotteryResults_LotteryDate ON LotteryResults(LotteryDate); -- Index for faster lookup of results by date

-- Security considerations:
-- 1. Use a strong hashing algorithm (e.g., bcrypt, Argon2) for storing password hashes.
-- 2. Validate and sanitize all inputs to prevent SQL injection.
-- 3. Ensure encrypted connections (TLS) for data in transit.
-- 4. Regularly review and update security mechanisms.
```
